Praktikum 13 – Membangun Aplikasi Multi Komponen (POS)
Mata Kuliah
Pemrograman Berorientasi Objek – Praktikum (INF2143)
________________________________________
Identitas Mahasiswa
•	Nama : Radit Andrea Alfarrizi
•	NIM : 2411102441167
•	Kelas : C
________________________________________
Deskripsi Proyek
Proyek ini merupakan simulasi aplikasi kasir sederhana (Point of Sale / POS) berbasis Command-Line Interface (CLI) yang dibangun menggunakan prinsip Object-Oriented Programming (OOP). Aplikasi ini mengintegrasikan beberapa komponen terpisah seperti Model, Repository, Service, dan Orchestrator menjadi satu kesatuan sistem yang fungsional.
________________________________________
Tujuan Praktikum
Tujuan dari praktikum ini adalah: 1. Memahami peran Orchestrator dalam arsitektur OOP modern. 2. Menerapkan Dependency Injection (DI) untuk menghubungkan komponen aplikasi. 3. Mengimplementasikan Repository sebagai lapisan data. 4. Membangun aplikasi CLI yang mengintegrasikan beberapa service. 5. Membuktikan penerapan OCP dan DIP melalui challenge metode pembayaran.
________________________________________
Arsitektur Aplikasi
Aplikasi disusun menggunakan Layered Architecture, yaitu:
1.	Model – Merepresentasikan struktur data produk.
2.	Repository – Menyediakan akses dan pengelolaan data produk.
3.	Service – Menangani logika bisnis seperti keranjang belanja dan pembayaran.
4.	Orchestrator (PosApp) – Mengatur alur aplikasi dan interaksi antar komponen.
________________________________________
Struktur Folder dan File
├── models.py
├── repositories.py
├── services.py
├── main_app.py
└── README.md
________________________________________
Penjelasan Komponen
1. Model (models.py)
Berisi class Product yang merepresentasikan data produk seperti ID, nama, dan harga.
2. Repository (repositories.py)
ProductRepository berfungsi sebagai lapisan data yang menyediakan akses produk tanpa melibatkan logika bisnis.
3. Service (services.py)
Berisi: - CartService untuk mengelola keranjang belanja. - IPaymentProcessor sebagai abstraksi metode pembayaran. - Implementasi pembayaran CashPayment dan DebitCardPayment.
4. Orchestrator (main_app.py)
PosApp bertugas mengoordinasikan alur aplikasi, mulai dari pemilihan produk, penghitungan total, hingga proses pembayaran.
________________________________________
Implementasi Dependency Injection
Dependency Injection diterapkan pada constructor PosApp, di mana objek repository, service, dan payment processor disuntikkan dari luar. Dengan pendekatan ini, pergantian metode pembayaran dapat dilakukan tanpa mengubah kode pada class PosApp.
________________________________________
Challenge OCP/DIP
Challenge dilakukan dengan menambahkan metode pembayaran baru DebitCardPayment yang mengimplementasikan interface IPaymentProcessor.
Perubahan dilakukan hanya pada titik masuk aplikasi (main_app.py) dengan mengganti objek payment processor, tanpa mengubah kode di dalam class PosApp.
Hal ini membuktikan bahwa sistem telah memenuhi prinsip Open/Closed Principle (OCP) dan Dependency Inversion Principle (DIP).
________________________________________
Hasil Eksekusi Program
Aplikasi berjalan melalui antarmuka CLI. Pengguna dapat memilih produk, menambahkan ke keranjang, dan melakukan pembayaran.
Hasil output:
 
________________________________________
Refleksi
Penerapan Dependency Injection pada class PosApp membuat sistem kasir lebih fleksibel dan mudah dikembangkan. Penambahan metode pembayaran baru dapat dilakukan tanpa memodifikasi logika utama aplikasi, sehingga mengurangi risiko error dan meningkatkan maintainability. Pendekatan ini sangat relevan untuk pengembangan Mini Project UAS yang berskala lebih besar.
________________________________________
Kesimpulan
Praktikum ini menunjukkan bahwa integrasi multi komponen dengan arsitektur berlapis dan Dependency Injection menghasilkan aplikasi yang rapi, modular, dan siap dikembangkan. Aplikasi POS sederhana ini berhasil menggabungkan konsep OOP, DI, serta prinsip SOLID dalam satu sistem nyata.
________________________________________
URL Repository GitHub: (https://github.com/elvandojhonny-source/praktikum-pbo-13)
