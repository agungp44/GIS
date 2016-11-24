<justify>Latar Belakang:<br>
1. Cara Membuat Shapefile?<br>
2. Cara Mengedit Shapefile?<br>
3. Cara Menghapus Shapefile?<br>
<br>
<br>
Isi:<br>
Kali ini saya akan sedikit memberikan tutorial bagaimana cara membuat data geospasial. pada pembuatan data geospasial ini saya menggunakan library pyshp.<br>
Berikut cara membuat data geospasial:<br>
1. Masuk Python<br>
2. Import Shapefile<br>
3. sf = shapefile.writer(shpetype=1)<br>
4. sf.point(10.10)<br>
5. sf.field('warung','C','40')<br>
6. sf.field('pemilik','C','80')<br>
7. sf.record('warteg','andi seep')<br>
8. sf.save('datawarteg.shp')<br>
<br>
Selanjutnya Mengedit Data Geospasial. Berikut cara mengedit data geospasial :<br>
1. Masuk Python<br>
2. Ganti sf = shapefile.writer(shpetype=1) dengan sf = shapefile.editor(datawarteg.shp)<br>
3. Langkah berikutnya sama dengan langkah pembuatan data geospasial<br>
<br>
Dan Terakhir adalah bagaimana cara menghapus/delete data geospasial. Berikut cara menghapus data geospasial:<br>
1. sf.delete(10)<br>
2. sf.shapes()[10].points[(10,10])<br>
3. sf.points[10,10]<br>
4. sf.record('warteg')<br>
5. sf.save('datawarteg.shp')<br>
<br>
<br>
Penutup:<br>
Kesimpulan<br>
Dalam pembahasan kali ini kita dapat mengetahui cara membuat, mengubah dan menghapus data geospasial.<br>
<br>
Saran<br>
Di perbanyak praktek akan memudahkan anda semakin cepat belajar dan bisa membuat data geospasial.<br></justify>