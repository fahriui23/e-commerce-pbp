# Tugas 2 PBP - Trias Fahri Naufal

Markdown ini dibuat untuk memenuhi Tugas 2 PBP dengan nama aplikasi "Wanda Beras". <br />
Link Deployment PWS : http://trias-fahri-wandaberas.pbp.cs.ui.ac.id

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

Client (User)<br />
    |<br />
    | 1. Sends Request<br />
    V<br />
+----------------------+<br />
|     Request URL      |<br />
+----------------------+<br />
           |<br />
           | 2. Maps to view<br />
           V<br />
+----------------------+<br />
|       urls.py        |<br />
+----------------------+<br />
           |<br />
           | 3. (Optional) Interacts with model<br />
           V<br />
+----------------------+<br />
|      views.py        |<br />
+----------------------+<br />
           |<br />
           | 4. Returns data to the view<br />
           V<br />
+----------------------+<br />
|      models.py       |<br />
+----------------------+<br />
           |<br />
           | 5. Render the response<br />
           V<br />
+----------------------+<br />
|   HTML Template      |<br />
+----------------------+<br />
           |<br />
           | 6. Sends response<br />
           V<br />
+----------------------+<br />
|   Client (Response)  |<br />
+----------------------+<br />


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

# Tugas 3 PBP - Trias Fahri Naufal

1. Mengapa kita membutuhkan Data Delivery? 

Data delivery diperlukan dalam suatu platform karena sebuah platform sering harus menyediakan informasi kepada user secara aman dan efisien.
Data Delivery menjadi penting karena kebutuhan pertukaran informasi, keamanan, dan juga efisiensi.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya pribadi JSON lebih readable bagi manusia.
Hal tersebut menjadi salah satu dari beberapa alasan yang menjadikan JSON lebih terkenal dari XML, beberapa alasan lainnya adalah karena JSON lebih mudah di-parsing, memiliki struktur data yang lebih sederhana, dan juga lebih ringan. 

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() berguna untuk memvalidasi data dan juga error handling. Method ini juga berfunsgi untuk menjadi filter bagi data yang masuk, dengan memastikan bahwa hanya data yang sudah bersih yang akan masuk ke database.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token memastikan bahwa form yang dikirimkan oleh pengguna merupakan benar-benar dari pengguna. Token ini unik untuk setiap sesi dan setiap request, sehingga kriminal siber tidak dapat menggunakan form yang sah untuk tindakan yang tidak intended oleh pengguna aslinya.

Tanpa csrf_token, platform akan rentan terhadap serangan csrf (Cross-Site Request Forgery), yaitu serangan dengan membuat end user execute suatu aksi yang tidak diinginkan secara paksa (seperti transaksi bank).

Penyerang dapat membuat page yang mengirimkan permintaan POST ke platform yang telah diautentikasi oleh user. Karena tidak ada csrf token untuk memverifikasi permintaan, platform akan menganggap permintaan itu sah.

## Step Pengerjaan
### Membuat Form Input Data
1. Membuat file forms.py di direktori main, dan mengisi dengan class Product, beserta field yang akan diminta pada form

```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"] #field yang akan diminta
```
2. Membuat view untuk handling form input pengguna dan menyimpan ke database
3. Buat template HTML untuk membuat form (ada di create_product.html)

### Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

1. Menambahkan method untuk setiap fungsi views yang akan dibuat. Fungsi tersebut disupport dengan pertama melakukan import terhadap HttpResponse dan serializers

```
#main/views.py
from django.http import HttpResponse
from django.core import serializers
...


def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```


2. Langkas diatas berupa fungsi pada views.py yang berguna untuk melihat objek dalam format XML dan JSON
3. Untuk melihat objek dalam format XML dan JSON by ID, kita dapat membuat method baru yang menerima parameter id juga

```
#main/views.py

...
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
...

```
Dengan menggunakan parameter id kita dapat meilihat per objek by idnya masing masing

### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
Pada file urls.py, tambahkan routing url untuk setiap method dalam views.py

```
    ...
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>', show_json_by_id, name='show_json_by_id'),
    ...
```
