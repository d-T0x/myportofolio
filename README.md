# **PORTFOLIO**
#### *website built on Django as part of CS assignment*
 
I'll update this repo periodically, that's all :D
<br><br>

## **Assignment 1 - Deadline: Monday, 7 Sep 2026**
> ### Pertanyaan Reflektif Tugas 1
1. Saya menggunakan semantik HTML5 berupa `<section>`, `<nav>`, dan `<article>` dengan rincian
    1. `<section>`: digunakan untuk memberikan batas segmen besar.
    2. `<nav>`: digunakan untuk menandai komponen dalam header situs.
    3. `<article>`: digunakan untuk menandai setiap proyek dalam segmen `Projects`.
2. Pembagian menjadi 2 pertanyaan:
    1. Tantangan tata letak terberat saya terdapat pada pemosisian *button* untuk mengisi kolom `PLATFORMS` di `meta-row`. Hal ini disebabkan perbedaan lebar kolom saat berada di desktop dan mobile.
    2. Mengatasi permasalahan pada poin 1, saya pertama mengevaluasi lebar *image* yang dipakai di desktop. Karena image terlalu lebar dan apabila saya *resize* hingga cukup di kolom mobile *image* akan menjadi terlalu kecil, saya memutuskan untuk mengganti *image* dengan *image* tampilan logo saja. Selain tantangan berat tersebut, terdapat juga tantangan sedang yakni mengubah jenis display daftar proyek dari desktop ke mobile. Di desktop saya ingin tampilan daftar proyek berada *side-to-side* supaya lebih mudah dilihat sedangkan di mobile saya ingin tampilan berupa susunan. Untuk mencapai tujuan tersebut, jenis style `display` dari section `Projects` di desktop saya set sebagai `flex` dan saat di mobile saya ubah menjadi `grid`.
    3. Sejauh fitur yang sudah diimplementasi, saya tidak merasakan adanya batasan pada fitur manapun dengan kondisi *static web*. Namun, ke depannya salah satu fitur yang saya ingin implementasi adalah pengeiriman komentar dari pengunjung *web* dan hal tersebut membutuhkan implementasi *dynamic web*.

> ### Features
1. `Projects` section with 2 contents.
2. Third meta row element `PLATFORMS` equipped with platform-based (mobile/desktop) button image change.

> ### AI Use
1. CSS image resize using AI overview from Google.
2. HTML and CSS adjustment for platform-based image change (mobile/desktop) using AI overview from Google.

> ### Learning Sources
1. Youtube tutorials.
2. W3 school website.
3. GeeksforGeeks website.
<br><br>



## **Assignment 2 - Deadline: Monday, 14 Sep 2026**
> ### Pertanyaan Reflektif Tugas 2
1. Saat masuk ke web melalui url, request akan dikirim menuju server dan views.py akan memfilter request tersebut. Karena request merupakan request masuk dengan `path=""`, maka views mengembalikan data pada model berdasarkan fungsi `show_main` yakni link template `index.html` dan context untuk template tersebut. Hal serupa terjadi untuk request menuju halaman Experience dan Project hanya saja saat fetch model dari `models.py`, context me-return context berupa list object Experience/Project (sesuai request) ke template `experience.html`/`project.html` (sesuai request). <br> Peran `urls.py` proyek dan `urls.py` aplikasi sebenarnya serupa. Perbedaan utamanya adalah file utama yang dirujuk oleh Django saat load web di awal adalah `urls.py` milik proyek. Oleh karena itu, supaya url pada aplikasi Main tetap dapat memberikan request ke server, kita perlu menambahkan kode `path("", include("main.urls"))` pada `urls.py` di proyek supaya url pada `urls.py` di aplikasi (dalam hal ini Main) dapat terbaca. <br><br>
2. Penjelasan paling intuitif menurut saya tentunya ada di domain perulangan. Hal ini mencakup hal-hal yang berkaitan dengan suatu daftar atau list. Apabila kita menulis suatu daftar langsung pada template (file html) tentunya akan sangat melelahkan dan repetitif; itu baru dari aspek pembuatannya. Melihat dari aspek pengembangan berkelanjutan, apabila suatu saat developer ingin mengubah styling dari list atau menambahkan class baru di list tersebut maka perlu pekerjaan yang, sekali lagi, melelahkan dan repetitif. Maka dari itu, melalui penerapan model dan template ini lah setiap daftar tidak perlu ditulis sebanyak daftar tersebut; hanya perlu ditulis sekali kemudian diiterasi sebanyak jumlah daftar pada model.<br><br>
3. Fungsi `makemigrations` membuat file .py baru yang berisi perubahan model pada suatu aplikasi Django sedangkan fungsi `migrate` adalah untuk berpindah (migrasi) dari model Django menuju model Django terbaru. Apabila hanya fungsi `makemigrations` saja yang dipanggil, maka object pada model yang diterapkan hanyalah versi terakhir dari model yang kita migrasi-ke (migrate to), bukan model terbaru. Maka dari itu perlu kedua fungsi yang dijalankan secara sekuensial (`makemigrations` kemudian `migrate`) supaya model terbaru dapat terimplementasi dengan baik.
<br><br>

> ### Features
1. `Project` page with 2 contents.
2. `project-card` mouse hover blur and brightness change; if on desktop, hover feature is available, if on desktop it's automatically in the hovered state since mobile doesn't have hover control.
3. `project-content` hover display
4. Adjusted font variation for the website.

> ### AI Use
1. #### Tools
    1. Claude Haiku 4.5 (VS Code chat session)
    2. Google AI Overview
2. #### Prompt Strategy
    1. Only use AI if I got SUPER stuck on something; when there's no specific guide on youtube nor website.
    2. When prompting, I utilize context and the clear goal that I want to achieve and also prioritizes "why" and "how" questions so the AI doesn't immediately change the code but rather explain what's wrong with my current implemenation
3. #### Prompting Log
    1. Context: Input a date field in project object without the hour specific information 
        - AI used : Claude Haiku 4.5 from VS Code Chat Session
        1. I'm frustrated. I want to have the "Created" column in the Project page to display a date. However, after trying to use models.DateTimeField(), apparently it asks for the hour, and I don't want that, hence I changed to models.DateField() AND YOU KNOW WHAT, it still included the hour, just "implicitly"--indicated by "midnight" displayed on the website and when I checked from the admin page it included the hour automatically with 00:00:00. Having had enough, I gave up with the date & time field stuff and tried to go with models.CharField() instead. After inputting the date of creation in the char field and saving from the admin page, refreshing the web, it displayed "None", visited the project's page in the admin again, and the date I inserted IS GONE, like, what??????? Tried to test is it because I haven't migrated or what not with changing the element of PROJECT_TYPE--changing 2d and 3d art to "web" and "app", but IT WORKS. I was like, WHAT'S WRONGGGG. Help me solve this please, I can't seem to find a source to address this specific problem
        2. Yes, just look at my models.py and admin.py
    2. Context: Passing image reference to template from models
        - AI used : Claude Haiku 4.5 from VS Code Chat Session
        1. Now I have a problem about images. I tried to follow a youtube tutorial on how to use object to pass image (as you can see by the field in models.py and the "{{ project.thumbnail.url }}" in project.html) and it didn't work. Another image part that doesn't work is the itch.io icon. How can I solve these image problems and what causes these problem to emerge?
        2. Tried to use your solution but it didn't work. Tried to follow a youtube tutorial and it also didn't work. Now what am I supposed to do? just go through my files and see what causes this error. Is it the CSS? Is it the MVT flow? Is it the HTML? Or is it anything else?
    3. Context: Adding CSS background to html template with Django model
        - AI used : AI Overview from Google search
        1. adding css background to html with django objects
    4. Context: Overriding parent styling
        - AI used: : Claude Haiku 4.5 from VS Code Chat Session
        1. How do I override the project-card background image styling of grayscale filter and make project-content colored? Tried to specify the class tag but it didn't work
        2. Didn't work. How do I make the card content colored and appear with grayscale background image while being hovered and 0 opacity content + colored background image while not being hovered?

> ### Learning Sources
These are sources that I managed to keep track of.
1. https://www.w3schools.com/django/django_admin_create_user.php
2. https://www.w3schools.com/django/django_admin_include_members.php
3. https://www.youtube.com/watch?v=GNsuF4xB80E
4. https://www.youtube.com/watch?v=jkCMl-N6sb8
5. https://www.w3schools.com/django/django_add_image.php/django_add_js_file.php
<br><br>



## **Assignment 3 - Deadline: Monday, 21 Sep 2026**
> ### Pertanyaan Reflektif Tugas 3
1. Sebagaimana dalam pembuatan website terdapat berbagai framework yang dapat membantu bagian tertentu, Django menyediakan `ModelForm` untuk mempermudah pembuatan form (penyediaan boilerplate dan lain-lain) dalam website alih-alih menggunakan HTML murni yang, jika dibandingkan dengan `ModelForm` dari Django, perlu banyak modifikasi untuk mencapai tingkat layak digunakan dalam produksi skala menengah-besar.<br><br> Mengenai `{% csrf_token %}`, ini merupakan fitur dari Django disediakan untuk menghidnari serangan CSRF. Simpelnya, supaya user yang unauthenticated di suatu website tidak dapat mengirim/mengubah data (`GET` atau `POST` request) dari website, maka diterapkanlah sistem token yang berlaku pada user session. 
<br><br>
2. Jawaban simpelnya, ya, karena ekosistem pemrograman modern secara umum lebih mendukung format JSON dibandingkan XML. Menilik lebih dalam, sebenarnya pemakaian umum JSON lebih unggul daripada XML. Ambil contoh dari penulisan kose JSON dan XML, JSON lebih minim boilerplate--tidak perlu menulis prolog, closing tag,  dan sebagainya seperti XML-- sehingga secara umum menyebabkan ukuran payload lebih kecil (lightweight) dibanding menggunakan XML. Di luar penulisan kode, JSON berkorelasi lebih baik terhadap data struktur sebagian besar bahasa pemrograman serta berintegrasi secara natural dengan JavaScript di sisi _frontend_.
<br><br>
3. Saat klik URL ke suatu page, ambil contoh page Experience, fungsi `show_experience` akan terpanggil sesuai path yang terdaftar dalam `urls.py`. Dalam fungsi show_experience, terdapat pemanggilan fungsi get_experiences_json sehingga terpanggilan fungsi tersebut dengan return value berupa data yang sudah di-_serialize_ dalam format JSON. Lalu, dalam fungsi `show_experience`, return value `get_experiences_json` akan di-_deserealize_ supaya dapat dibaca sebagai tipe data yang dikenali python dan selanjutnya dikirim lagi ke template `experience.html`. <br><br> _Serialization_ ke format JSON merupakan tahap yang harus dilakukan supaya nantinya server dapat return value fungsi sebagai `HTTPResponse` (protol standar interaksi antara _server_ dan _client_ web browser) ke client dan selanjutnya diolah lagi oleh client.
<br><br>

> ### Features
1. Experience object CRUD (Create, Read, Update, Delete) functionality.
2. Experience form date verification (start date must be less than end date).
3. Experience start and end date display.
4. Updated Experience model for start and end date to use DateField rather than DateTimeField

> ### AI Use
1. #### Tools
    1. None
2. #### Prompt Strategy
    1. Managed to not use any AI. Only used public internet resources, PBP tutorial codes, and my own endeavor (struggled but worth the joy :" )
3. #### Prompting Log
    1. None

> ### Learning Sources
These are the resources that I used:
1. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Box_alignment
2. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Aligning_items
3. https://stackoverflow.com/questions/75637882/django-form-start-date-end-date-validation
4. https://www.geeksforgeeks.org/python/update-view-function-based-views-django/
5. https://www.youtube.com/watch?v=_4Mp8nwPAmY
6. https://www.geeksforgeeks.org/python/csrf-token-in-django/
7. https://medium.com/@sridharsubbaiya1234/json-why-it-beats-plain-text-and-xml-most-of-the-time-6379791a1d6e
8. https://www.digitalapi.ai/blogs/json-vs-xml-for-web-apis-choosing-the-right-data-format
9. https://www.geeksforgeeks.org/python/csrf-token-in-django/
<br><br>

### **Creator Profile**
<hr>
Name : Hafizuddin Dzaki Azzam
<br>
NPM : 2506597220
<br>
Class : PBP C
 