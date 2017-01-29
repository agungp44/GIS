<justify>Latar Belakang : <br>
1. Bagaimana cara menjalankan Map Server dan Map Proxy?
<br>

Isi : <br>
1. Untuk menjalankan data geospasial pertama download terlebih dahulu data geospasialnya di http://www.halaman.download/ kemudian pilih Producer dan Indonesia MapProxy. <br>
2. Jika sudah di download, selanjutnya ekstrak file yang telah di download ingat tempat anda mengekstrak file tersebut! <br>
3. Pada file indomap kemudian mapproxy, terdapat 3 buah file. <br>
4. Kemudian buka file agm.yaml dan edit beberapa baris sesuai dengan direktori tempat anda menyimpan file tersebut : <br>
- /usr/libexec/mapserver <br>
- /usr/lib/cgi-bin/mapserver <br>
- /var/mapdata/mapfile/indo.map <br>
- dan ubah baris working_dir: /var/mapdata/tmp <br>
Ubah baris tersebut sesuai dengan tempat anda menyimpan file hasil ekstrak tadi. <br>
5. Kemudian pada directory MapProxy di terminal ketikan perintah vi mapproxy.ini edit baris chdir = /var/mymapproxy/ menjadi sesuai dengan tempat file tersebut. <br>
6. Selanjutnya edit file config.py pada directory mapproxy application = make_wsgi_app(r'/var/mymapproxy/agm.yaml') menjadi sesuai dengan tempat file tersebut. <br>
7. Untuk menjalankan program gunakan perintah uwsgi mapproxy.ini <br>
8. Untuk mengecek apakah mapproxy sudah terinsall atau belum, buka browser kemudian ketik localhost:8080/demo <br>
9. Pada bagian WMTS Klik image format yaitu png. <br>


Penutup: <br>
Kesimpulan <br>
Pada pembahasan kali ini kita dapat mengetahui cara menjalankan map proxy dan map server <br>
Saran <br>
Lebih diperbanyak praktek jika ingin cepat menguasai. </justify>