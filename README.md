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

# Screenshot
<img width="1512" alt="Screenshot 2024-09-17 at 00 02 48" src="https://github.com/user-attachments/assets/2aa254d3-33f5-4f2f-80e2-a5f0a236fe23">
<img width="1512" alt="Screenshot 2024-09-17 at 00 03 01" src="https://github.com/user-attachments/assets/e894e872-5d01-40cf-ae60-edc025e7c32d">
<img width="1512" alt="Screenshot 2024-09-17 at 00 03 15" src="https://github.com/user-attachments/assets/e8d04f1c-d5d2-4518-b064-0f1ac73e8ab1">
<img width="1512" alt="Screenshot 2024-09-17 at 00 03 21" src="https://github.com/user-attachments/assets/425f2065-3dd0-42ce-adae-21314b894957">

# Tugas 4 PBP - Trias Fahri Naufal
1. Perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect() adalah class bawaan Django yang mengembalikan respons untuk pengalihan halaman secara manual. 
redirect() adalah shortcut yang lebih mudah digunakan karena menerima argumen seperti URL atau nama view.

2. Cara Kerja Penghubungan Model Product dengan User

Penghubungan dilakukan menggunakan ForeignKey, yang menghubungkan entitas produk dengan pemiliknya (pengguna). Django akan secara otomatis mengelola hubungan ini.

3. Perbedaan antara Autentikasi dan Otorisasi

Autentikasi adalah proses memverifikasi identitas pengguna (misalnya, saat login).
Sedangkan otorisasi adalah proses menentukan hak akses pengguna setelah terautentikasi.
Django mengelola autentikasi dengan sistem pengguna bawaan, dan otorisasi diatur dengan group dan permission.

4. Bagaimana Django Mengingat Pengguna yang Telah Login

Django menggunakan sesi (session) yang disimpan dalam cookie untuk mengingat pengguna yang telah login. Cookies bisa digunakan untuk menyimpan data kecil seperti preferensi pengguna.

## Step Pengerjaan
1. Registrasi:
Buat form registrasi menggunakan UserCreationForm bawaan Django.
Implementasikan view untuk registrasi pengguna dan hubungkan ke URL yang sesuai di urls.py.

Berikut kode yang diimplementasikan di file views.py

```
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

```
lalu import register ke urls.py dan hubungkan melalui urlpatterns

```
from main.views import register

urlpatterns = [
    ...
    path('register/', register, name='register'),
    ...
]
```

Setelah itu kita harus membuat file register.html yang berfungsi sebagai tempat dilakukannya registrasi



2. login

Membuat Form Login dengan menggunakan import login

```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login    
```

kode diatas merupakan fungsi bawaan dari Django untuk melakukan login dan juga autentikasi apa bila login berhasil

lalu membuat fungsi login_user yang berguna untuk menghandle login dari user
```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

login(request, user) berguna untuk melakukan login terlebih dahulu. Apabila berhasil, fungsi ini akan membuat session untuk user tersebut dan juga mengarahkan user ke show_main seperti yang dapat di lihat pada line selanjutnya yaitu redirecting ke main.

lalu hubungkan melalui urls.py dengan menambahkan kode berikut

```
from main.views import login_user

app_name = 'main'

urlpatterns = [
    ...
    path('login/', login_user, name='login'),
    ...
]
```

3. logout

Membuat Form logout dengan menggunakan import logout

```
from django.contrib.auth import logout
```

kode diatas merupakan fungsi bawaan dari Django untuk menghandle logout.

lalu membuat fungsi logout_user yang berguna untuk menghandle logout dari user
```
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

logout(request) berguna untuk melakukan logout dan menghapus sesi pengguna yang saat ini.
Lalu diredirect kembali ke main -> login

lalu hubungkan melalui urls.py dengan menambahkan kode berikut

```
from main.views import logout_user

app_name = 'main'

urlpatterns = [
    ...
    path('logout/', logout_user, name='logout'),
    ...
]
```

lalu tambahkan hyperlink tag berikut pada main.html

```
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...

```

3. Menghubungkan model Product dan User

Pada models.py, tambahkan import berikut:
```
from django.contrib.auth.models import User
```

lalu pada class Product tambahkan kode berikut:
```
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

kode diatas menghubungkan suatu product dengan user melalui suatu relationship, hal ini memastikan bahwa sebuah product pasti terhubung kepada seorang user

selanjutnya pada views.py, ubah kode untuk membuat product dengan berikut:
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

```

kode bagian commit=False memastikan bahwa Django tidak langsung menyimpan objek yang sudah dibuat langsung ke database, hal ini menyebabkan kita dapat meng-alter dahulu objek yang akan di simpan.
Pada konteks ini kita akan mengisi field user dengan user yang sedang login sekarang.

Lalu pada show_main, ubah context field user menjadi user yang sedang login sekarang dengan mengubah kode menjadi seperti ini:
```
context = {
         'name': request.user.username,
         ...
    }
```

jangan lupa juga bahwa kita harus melakukan filter terhadap product yang dimunculkan hanyalah product milik user tersebut secara eksklusif. Pada show_main ubah kode menjadi berikut:
```
def show_main(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)
    ...
```
# Tugas 5 PBP - Trias Fahri Naufal

1. Berikut ini urutan prioritasnya, nomor 1 yang memiliki prioritas paling tinggi, yaitu :

    1. Inline style
    2. External dan internal style sheets
    3. Browser default

2. Responsiveness menjadi salah satu aspek penting dalam design web dan aplikasi dengan alasan aksesibilitas. Sebuah web apabila tidak responsive maka tidak akan mudah, bahkan belum tentu dapat digunakan pada beberapa device yang berbeda, terutama pada platform mobile. Salah satu contoh web yang sudah responsive yaitu SIAKNG Universitas Indonesia. Di lain sisi, kebanyakan web adalah web yang responsive, namun terdapat suatu web yang diciptakan dengan sengaja non-responsive untuk contoh saja, yaitu: https://dequeuniversity.com/library/responsive/1-non-responsive.

3. 
    Padding adalah jarak antara konten suatu elemen dengan bordernya.
    Border merupakan garis pembatas dari suatu elemen, berada diantara elemen dan margin.
    Margin adalah ruang di luar border elemen dengan fungsi untuk memberikan jarak antar elemen.

    contoh:
    