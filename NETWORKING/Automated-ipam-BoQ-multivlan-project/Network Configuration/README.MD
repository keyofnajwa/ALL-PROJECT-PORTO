# 🛠️ Konfigurasi Infrastruktur & Live Simulation (Cisco Packet Tracer)

Repositori ini berisi seluruh file implementasi teknis dan dokumentasi konfigurasi CLI (*Command Line Interface*) untuk memenuhi kebutuhan proyek infrastruktur jaringan klien. Seluruh konfigurasi di bawah ini dirancang untuk memastikan performa optimal, otomasi distribusi IP, serta pengamanan berlapis pada Layer 2 dan akses perangkat.

---

## 🔑 Dokumen Autentikasi Pengujian (Lab Credentials)
Untuk kebutuhan audit dan pengujian konfigurasi live pada file `.pkt` di Cisco Packet Tracer, seluruh lini pengamanan di-standarisasikan menggunakan kredensial berikut:
* **Enable Password / Secret:** `cisco`
* **Console Password:** `cisco`
* **VTY / Remote Lines Password:** `cisco`

---

## 📐 1. Arsitektur Logis & Topologi Jaringan
Sesuai dengan permintaan klien untuk membagi jaringan berdasarkan divisi guna mengoptimalkan *broadcast domain*, jaringan ini dibagi menjadi 5 segmen fungsional:

#### Diagram Topologi Jaringan
<br><br>
<img width="1302" height="537" alt="WROKSPACE TOPOLOGY" src="https://github.com/user-attachments/assets/f60f1ce2-0096-40f9-be8c-bdec4fcb0570" />
<br><br>
<img width="1095" height="742" alt="PHYSICALL-VIEW" src="https://github.com/user-attachments/assets/6034dbe5-b31b-4a66-9bf0-c5dca0d72b92" />


* **Segmentasi VLAN:**
    * **VLAN 10:** CS (Customer Service)
    * **VLAN 20:** Receptionist
    * **VLAN 30:** Finance (Zona Khusus & Sensitif)
    * **VLAN 40:** Manager
    * **VLAN 50:** IT Engineer

---

## 🚀 2. Implementasi Konfigurasi Core & Access Layer

### A. Inter-VLAN Routing & DHCP Deployment
Memastikan mobilitas data antar-VLAN berjalan lancar dan seluruh 33+ perangkat endpoint mendapatkan parameter IP Address secara otomatis tanpa konfigurasi manual.
* **Router-on-a-Stick (Dot1Q):** Subinterfaces dikonfigurasikan pada core router untuk bertindak sebagai *default gateway* bagi masing-masing VLAN.
    <br><br>
<img width="651" height="232" alt="ip interface router" src="https://github.com/user-attachments/assets/73a8cab8-1439-4041-856d-6eab6c416995" />

* **DHCP Pools Server:** Alokasi scope IP Address dinamis yang diisolasi per zona VLAN.
    <br><br>
    <img width="307" height="302" alt="all dhcp" src="https://github.com/user-attachments/assets/fc8c0127-b2e8-4bca-b67c-7767577c96fb" />


* **Verifikasi Lease IP:** Pembuktian bahwa perangkat klien berhasil menyewa IP Address dari pool yang sesuai.
    
    <img width="1002" height="332" alt="pc1 dapat vlan 10 succes" src="https://github.com/user-attachments/assets/c42d6ae2-a53c-486d-8019-fd4143a1118b" />
    <br><br>
    <img width="929" height="485" alt="ip vlan 40 sucess" src="https://github.com/user-attachments/assets/09ca0755-83f7-44b0-96c9-690d07b69c3a" />

### B. Pengerasan Keamanan Perangkat (Device Hardening)
Memenuhi *request* keamanan ketat dari klien untuk melindungi hak akses kontrol Switch dan Router dari modifikasi ilegal:
* **Autentikasi Akses Berlapis:** Penguncian total pada seluruh jalur masuk administrasi (`Line Console`, Privilege EXEC Mode via `Enable`, dan remote akses via `Line VTY 0-4`).
* **Enkripsi Password Menyeluruh:** Mengaktifkan fitur `service password-encryption`. Seluruh password di dalam sistem (`running-config`) otomatis terenkripsi penuh sehingga tidak bertipe *plain-text* yang rawan di-intip.
* **Peringatan Akses Resmi (Banner MOTD):** Implementasi pesan peringatan terminal sebagai perimeter hukum bagi pihak yang mencoba masuk tanpa izin.
    
    <img width="772" height="170" alt="banner pass active switch f-cs-rt" src="https://github.com/user-attachments/assets/6b46f6ab-35b3-43d3-9fab-9324a002d780" />
    <br><br>
    <img width="667" height="197" alt="banner pass active switch ITMA" src="https://github.com/user-attachments/assets/75f3ca2c-c73e-42d3-ade7-a8f380c86801" />


### C. Port Security Spesifik (VLAN 30 - Finance)
Divisi **VLAN 30 (Finance)** menyimpan data keuangan krusial milik klien. Untuk mengantisipasi adanya penyusupan fisik (perangkat asing yang dicolok sembarangan ke port switch Finance), fitur **Active Port Security** diterapkan secara ketat:
* **Batasan MAC Address:** Port switch hanya mendengarkan dan mengizinkan perangkat terdaftar milik tim Finance.
* **Violation Mode - Shutdown:** Jika mendeteksi adanya MAC Address asing yang tidak sah, port switch akan otomatis mati (*Shutdown*) secara instan untuk mengisolasi ancaman.
    
  <img width="576" height="225" alt="port securtyy secure finance" src="https://github.com/user-attachments/assets/48ed6862-6e45-4c13-abfd-9b95270cb371" />

    
### D. Verifikasi Konektivitas (End-to-End Ping)
* Pengujian interkoneksi dilakukan menyeluruh menggunakan ICMP echo (Ping) lintas departemen untuk memastikan stabilitas jaringan 100% *connected*.
    
    <img width="962" height="492" alt="ping connectivuty" src="https://github.com/user-attachments/assets/c9cbd38a-85fb-4ee1-b97f-44a7446520d4" />


---

## 🔍 🛠️ Studi Kasus Troubleshooting: Bug "Trunk Allowed None"

Proses penyerahan proyek ke klien menyertakan laporan audit *troubleshooting* riil saat proses *deployment* di lapangan.

### 1. Isolasi Masalah Menggunakan Komparasi `show run`
Saat pengujian awal, endpoint pada **VLAN 40 dan VLAN 50 gagal mendapatkan IP DHCP**. Untuk melacak *bug*, saya melakukan komparasi konfigurasi menggunakan perintah `show running-config` antara Switch **F-CS** (Floor-1) yang berjalan normal dengan Switch **IT-MA** (Floor-2) yang bermasalah.

* **Akar Masalah:** Ditemukan kesalahan penulisan sintaks pada jalur trunk Switch F-CS. Terdapat ketidaksengajaan penggunaan tanda titik `.` sebagai pemisah, alih-alih menggunakan tanda koma `,` saat mendaftarkan list VLAN (terbaca: `40.50.99`).
* **Dampak Teknis:** Cisco IOS menolak string tersebut, menyebabkan status enkapsulasi trunk yang diizinkan (*allowed*) jatuh ke status **`none`** (memblokir seluruh jalur VLAN 40 & 50 di Layer 2).

<img width="993" height="591" alt="dhcp failed" src="https://github.com/user-attachments/assets/eb9c74d9-8482-4109-a37d-c24149363274" />
<br><br>
<img width="313" height="166" alt="vlan allowed none" src="https://github.com/user-attachments/assets/9e6a425d-6b78-4974-8669-b68bf7acc88f" />


### 2. Resolusi & Validasi Akhir
* **Solusi:** Sintaks yang salah dihapus, kemudian dimasukkan kembali perintah dengan pemisah tanda koma `,` yang benar untuk membuka izin lintas data data VLAN.
* **Verifikasi Perbaikan:** Di-audit kembali menggunakan perintah `show interfaces trunk` untuk memastikan seluruh *interface* yang aktif ke mode trunk sudah berjalan normal.

<img width="319" height="135" alt="vvlan allow4d bnr dari show run" src="https://github.com/user-attachments/assets/be353443-43ff-4112-bd40-a86c1b64eb21" />


* **Hasil:** Endpoint langsung mendapatkan parameter IP Address dari DHCP server secara instan dan konektivitas inter-VLAN sukses total.

---

## 📂 Cara Menjalankan File Simulasi
1. Download file dengan ekstensi `.pkt` yang ada di dalam folder ini.
2. Buka aplikasi **Cisco Packet Tracer**.
3. Lakukan audit pada Switch atau Router menggunakan kredensial lab yang tertera di atas untuk melihat baris konfigurasi lengkapnya.
