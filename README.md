# Tugas 2 PBP - Trias Fahri Naufal

Markdown ini dibuat untuk memenuhi Tugas 2 PBP dengan nama aplikasi "Wanda Beras". <br />
Link Deployment PWS : 

## Step pengerjaan proyek

dibawah merupakan step-by-step pengerjaan proyek

### Pembuatan Proyek Django

1. Buat direktori `e-commerce` sebagai direktori untuk proyek ini.
2. Pada direktori `e-commerce`, install virtual environment melalui terminal dengan command berikut:

   ```python
   python3 -m venv env
   ```
3. Setelah virtual environment terinstall, aktifkan dengn command:

   ```
   source env/bin/activate
   ```

4. Buat file `requirements.txt` pada directory e-commerce dengan isi sebagai berikut:

   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
5. Setelah itu, install dependencies pada `requirements.txt` dengan command:

   ```
   pip install -r requirements.tx
   ```
6. Lalu, lakukan inisiasi project django dengan nama `e_commerce` dengan command berikut:

   ```
   django-admin startproject e_commerce .
   ```

7. Setelah proyek terinisiasi, tambahkan `"localhost"` dan `"127.0.0.1"` pada list `ALLOWED_HOST` di file `settings.py`.

   ### Membuat aplikasi `main`
8. Buat aplikasi baru bernama `main` dengan command:

   ```
   python manage.py startapp main
   ```

   #### Membuat Template

9. Setelah aplikasi main terinstall, tambahkan `'main'` ke list `INSTALLED_APPS` pada file `settings.py` supaya menjadi tanda terdapatnya aplikasi `main` ini.

10. buat folder `templates` di dalam folder `main` untuk membuat template lalu tambahkan file `main.html` yang akan berfungsi sebagai templatenya.

11. Isi template tersebut dengan hal yang dibutuhkan.

    ### Membuat Models

12. Tambahkan sebuah model pada file `models.py` yaitu `Product` yang memiliki attribute `name` , `price`, dan `description`.

13. Untuk mengaplikasikan model, migrate dengan command di bawah ini:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

    ### Menghubungkan View dengan Template

14. Selanjutnya, isi file `views.py` dengan function bernama `show_main` yang akan menjembatani data ke template ketika ada  request dari template.

15. Data yang akan dikirim berupa atribut-atribut berupa atribut `name`,` price`, `description`, `name`, `npm`, dan `class`.

    ### Konfigurasi URL
16. Buat file `urls.py` di dalam `main` dan tambahkan kode di bawah untuk configure routing pada aplikasi:

    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```

17. konfigurasi file `urls.py` yang berada pada `e_commerce` untuk routing project keseluruhan dengan kode dibawah:

    ```
    ...
    from django.urls import path, include
    ...

    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
    ```

### Git dan PWS Deployment

20. Buat terlebih dahulu repository baru di github lalu menginisiasinya dan menghubungkan kepada repository yang ada di local
21. Setelah terhubung, lakukan `add`, `commit`, dan `push` ke remote repository github
22. Untuk melakukan deployment ke PWS, tambahkan URL repo github pada step 20 ke list `ALLOWED_HOST` pada `settings.py`.
23. Sambungkan repository dengan PWS, lalu push ke repository PWS untuk melakukan deployment.

## Request client ke web aplikasi berbasis Django

```mermaid
graph TD
    A[Client (User)] -->|1. Sends Request| B[Request URL]
    B -->|2. Maps to view| C[urls.py]
    C -->|3. (Optional) Interacts with model| D[views.py]
    D -->|4. Returns data to the view| E[models.py]
    E -->|5. Render the response| F[HTML Template]
    F -->|6. Sends response| G[Client (Response)]
```

## Fungsi `git` dalam pengembangan perangkat lunak

git memiliki beberapa fungsi utama, sepert Version Control, Collaborative Development, dan Branching.

Version Control berfungsi dengan melacak perubahan pada kode, berfungsi agar developer dapat melihat kembali kode pada versi sebelumnya untuk satu dan lain hal seperti evaluasi kode.

Collaborative Development disupport oleh git dengan memungkinkan beberapa developer untuk mengerjakan suatu proyek secara bersamaan yang menggunakan sistem yang akan dijelaskan pada poin selanjutnya.

Branching, dengan ini developer yang bekerja sama pada proyek dapat mengerjakan proyek tanpa menggangu progress satu sama lain.


## Mengapa Django?

Menurut saya karena beberapa hal, seperti bahwa Django menggunakan bahasa pemrograman yang kami sudah pelajari sebelumnya yaitu python. Django juga merupakan salah satu framework yang banyak digunakan di industri, yang menyebabkan Django memiliki community yang cukup besar untuk memudahkan mahasiswa troubleshooting saat terjadi error.

## Kenapa models pada Django disebut sebagai ORM?

Models pada Django disebut sebagai ORM karena (Object Relational Mapping) karena Models pada Django melakukan mapping yang diselimuti dengan abstraksi. Sehingga developer tidak harus berinteraksi dengan database dengan menulis SQL manual, melainkan menggunakan python. <br />

Sekian jawaban saya :) . <br />

Salam <br/>

Trias Fahri Naufal 