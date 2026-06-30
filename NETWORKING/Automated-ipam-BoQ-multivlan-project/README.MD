# 🌐 Automated IPAM & BoQ Project: Implementing Multi-VLAN DHCP with Active Port Security

Selamat datang di repositori resmi proyek  - **Network Infrastructure & Data Automation Portfolio**.

Proyek ini merupakan dokumentasi lengkap dari visualisasi dashboard interaktif Microsoft Excel yang sebelumnya telah saya bagikan di **LinkedIn**. Di sini, saya tidak hanya menyajikan rancangan kalkulasi data, tetapi juga menyediakan pembuktian teknis berupa simulasi jaringan aktif berskala *Enterprise* (Multi-Floor Network) menggunakan **Cisco Packet Tracer**.

---

## 📂 Struktur Repositori (Project Directory)

Untuk mempermudah peninjauan dan audit dokumen, repositori ini telah dibagi menjadi beberapa folder terstruktur sesuai standar manajemen proyek:

*   **`01-Client-Brief-and-Documentation/`**
    *   Berisi latar belakang proyek fiktif (*Client Brief* berbasis email) untuk mensimulasikan kebutuhan riil di industri.
    *   Menyimpan dokumen master **`p.pdf`** yang berisi database administrasi jaringan serta rincian kalkulasi biaya.
*   **`02-Network-Configuration-and-Simulation/`**
    *   Berisi file lab simulasi live murni (**`.pkt`**) yang dapat dijalankan langsung di Cisco Packet Tracer.
    *   Dilengkapi dengan dokumentasi *Command Line Interface* (CLI) untuk pengerasan keamanan (*hardening*) perangkat dan studi kasus *troubleshooting*.

---

## 📊 Ringkasan Proyek (Project Highlights)

Proyek ini menjembatani peran seorang **Network Administrator** yang harus mampu menyajikan tata kelola data yang valid kepada manajemen, sekaligus peran **Technical Engineer** yang mengeksekusi konfigurasi di lapangan.

### 1. Data Automation & Financial Analytics (Excel)
*   **Otomasi IPAM Matrix:** Pelacakan otomatis dan manajemen *inventory* untuk 33+ perangkat endpoint lintas lantai menggunakan rumus logis (`VLOOKUP`, `COUNTIF`, `COUNTA`).
*   **CAPEX Analytics & BoQ:** Perhitungan otomatis pengadaan logistik perangkat keras jaringan dengan total anggaran **Rp 55.470.001** yang divisualisasikan melalui grafik interaktif *side-by-side*.

### 2. Core Configuration & Device Hardening (Cisco)
*   **Multi-VLAN & DHCP:** Pembagian 5 segmen zona departemen (CS, Receptionist, Finance, Manager, IT Engineer) dengan alokasi dynamic IP pool otomatis via *Router-on-a-Stick*.
*   **Infrastruktur Layer 2 Security:** Proteksi ketat menggunakan *Active Port Security* dengan tindakan tegas `Shutdown Violation` khusus pada **VLAN 30 (Finance)** untuk melindungi data keuangan krusial.
*   **Device Hardening:** Pengamanan menyeluruh pada seluruh jalur akses masuk administrasi (`Line Console`, `Enable Secret`, dan `Line VTY 0-4`) yang terenkripsi penuh menggunakan `service password-encryption` serta dilengkapi Banner MOTD.

### 🛠️ Studi Kasus Real Troubleshooting
Proyek ini juga mendokumentasikan analisis pemecahan masalah riil saat *deployment* di mana saya berhasil melacak bug *DHCP Lease Failure* pada VLAN 40 & 50 melalui komparasi `show running-config` akibat kesalahan penulisan sintaks tanda baca pada jalur trunking switch.

---

## 🚀 Cara Meninjau Proyek Ini

1.  **Melihat Hasil Interaktif (Excel):** Masuk ke folder `01-Client-Brief-and-Documentation/` untuk mengunduh master PDF/Spreadsheet dashboard finansial.
2.  **Menguji Konfigurasi Live (Cisco):** Masuk ke folder `02-Network-Configuration-and-Simulation/`, unduh file `.pkt`, dan jalankan di aplikasi Cisco Packet Tracer Anda.
3.  **Kredensial Pengujian (Lab Credentials):** Untuk kebutuhan masuk ke terminal switch/router, gunakan password standar pengujian: `cisco` (untuk Enable, Console, dan VTY).

---
*Kritik, saran, maupun masukan dari para praktisi, senior engineer, dan rekan-rekan sekalian sangat saya harapkan untuk bekal pengembangan kemampuan saya ke depan. Terima kasih!* 🙏✨

