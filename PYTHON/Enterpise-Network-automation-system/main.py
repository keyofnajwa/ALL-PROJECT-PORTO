import sys
import time
from netmiko import ConnectHandler

# =====================================================================
# CONFIGURATION: DEVICE DATA (DICTIONARY)
# =====================================================================
# Silakan sesuaikan IP Address, Username, dan Password sesuai dengan 
# topologi perangkat MikroTik Anda di GNS3 / VMware.
target_router = {
    'device_type': 'mikrotik_routeros',
    'host': 'YOUR_MIKROTIK_IP',              # IP Management Router
    'username': 'admin',                 # Akun Administrator
    'password': 'YOUR_MIKROTIK_PASSWORD',  # Password Router
    'port': 22,                          # Port Layanan SSH
}

def display_menu():
    """Menampilkan Menu Antarmuka Utama yang Formal"""
    print("\n" + "="*50)
    print("     ENTERPRISE NETWORK AUTOMATION SYSTEM (ENAS)    ")
    print("==================================================")
    print(" Kategori Menu Konfigurasi:")
    print(" [1] Tambah VLAN Baru (Add VLAN)")
    print(" [2] Modifikasi VLAN Eksisting (Edit VLAN)")
    print(" [3] Hapus VLAN Eksisting (Delete VLAN)")
    print(" [4] Tampilkan Status Interface (Show Interfaces)")
    print(" [0] Keluar dari Sistem (Exit)")
    print("="*50)

def execute_automation():
    while True:
        display_menu()
        user_choice = input("Masukkan kode opsi aksi Anda (0-4): ")
        
        if user_choice == "0":
            print("\n[INFO] Menghentikan program. Terima kasih telah menggunakan ENAS.")
            sys.exit()
            
        elif user_choice in ["1", "2", "3", "4"]:
            try:
                print(f"\n[+] Menginisiasi koneksi SSH menuju {target_router['host']}...")
                # Membuka sesi koneksi remote via Netmiko
                session = ConnectHandler(**target_router)
                print("[STATUS] Koneksi berhasil didirikan. Router siap menerima instruksi.")
                
                # -------------------------------------------------------------
                # OPSI 1: TAMBAH VLAN (ADD VLAN)
                # -------------------------------------------------------------
                if user_choice == "1":
                    print("\n--- FORMULIR PENAMBAHAN VLAN BARU ---")
                    vlan_id = input("-> Masukkan VLAN ID (Contoh: 10): ")
                    vlan_name = input("-> Masukkan Nama VLAN (Contoh: VLAN_Admin): ")
                    vlan_int = input("-> Masukkan Interface Induk (Contoh: ether2): ")
                    
                    # Sintaks MikroTik RouterOS untuk membuat VLAN
                    command = f"/interface vlan add name={vlan_name} vlan-id={vlan_id} interface={vlan_int} disabled=no"
                    
                    print("[+] Mengirimkan parameter konfigurasi...")
                    response = session.send_command(command)
                    
                    if response:
                        print(f"[GAGAL] Respon Router: {response.strip()}")
                    else:
                        print(f"[SUKSES] VLAN ID {vlan_id} ({vlan_name}) berhasil ditambahkan pada {vlan_int}.")
                
                # -------------------------------------------------------------
                # OPSI 2: MODIFIKASI VLAN (EDIT VLAN)
                # -------------------------------------------------------------
                elif user_choice == "2":
                    print("\n--- FORMULIR MODIFIKASI VLAN EKSISTING ---")
                    current_name = input("-> Masukkan NAMA VLAN yang akan diubah: ")
                    new_name = input("-> Masukkan NAMA BARU (Tekan Enter jika tidak diubah): ")
                    new_int = input("-> Masukkan INTERFACE BARU (Tekan Enter jika tidak diubah): ")
                    
                    # Logika peracikan perintah modifikasi berdasarkan input pengguna
                    if new_name and new_int:
                        command = f"/interface vlan set [find name={current_name}] name={new_name} interface={new_int}"
                    elif new_name:
                        command = f"/interface vlan set [find name={current_name}] name={new_name}"
                    elif new_int:
                        command = f"/interface vlan set [find name={current_name}] interface={new_int}"
                    else:
                        print("[INFO] Tidak ada perubahan parameter yang dimasukkan.")
                        command = None
                        
                    if command:
                        print("[+] Memperbarui parameter perangkat...")
                        response = session.send_command(command)
                        if response:
                            print(f"[GAGAL] Respon Router: {response.strip()}")
                        else:
                            print(f"[SUKSES] Parameter VLAN '{current_name}' berhasil diperbarui.")
                
                # -------------------------------------------------------------
                # OPSI 3: HAPUS VLAN (DELETE VLAN)
                # -------------------------------------------------------------
                elif user_choice == "3":
                    print("\n--- FORMULIR PENGHAPUSAN VLAN ---")
                    vlan_name = input("-> Masukkan NAMA VLAN yang akan dihapus secara permanen: ")
                    
                    # Sintaks pencarian indeks berdasarkan properti nama untuk proses hapus
                    command = f"/interface vlan remove [find name={vlan_name}]"
                    
                    print("[+] Mengeksekusi proses penghapusan...")
                    response = session.send_command(command)
                    if response:
                        print(f"[GAGAL] Respon Router: {response.strip()}")
                    else:
                        print(f"[SUKSES] VLAN '{vlan_name}' telah berhasil dihapus dari sistem.")
                
                # -------------------------------------------------------------
                # OPSI 4: TAMPILKAN STATUS INTERFACE (SHOW INTERFACES)
                # -------------------------------------------------------------
                elif user_choice == "4":
                    print("\n" + "-"*60)
                    print("         LAPORAN STATUS INTERFACE PERANGKAT MIKROTIK        ")
                    print("-"*60)
                    # Mengambil data tabel interface dari MikroTik
                    device_output = session.send_command("/interface print")
                    print(device_output)
                    print("-"*60)
                
                # Menutup sesi SSH secara aman setelah proses selesai
                session.disconnect()
                print("[STATUS] Sesi SSH ditutup kembali secara aman.")
                time.sleep(1) # Jeda visual sebelum menu kembali muncul
                
            except Exception as error_exception:
                print(f"[ERROR] Kegagalan komunikasi sistem. Detail: {error_exception}")
        else:
            print("[PERINGATAN] Kode opsi tidak valid. Sila masukkan angka antara 0 hingga 4.")

if __name__ == "__main__":
    execute_automation()