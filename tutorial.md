Berikut adalah contoh sederhana **CKAN Extension (ckanext)** untuk menambahkan aksi API baru yang mengembalikan pesan sederhana. Ekstensi ini menunjukkan bagaimana Anda bisa membuat dan mengintegrasikan fungsionalitas baru ke dalam CKAN.

---

### **Fungsi Ekstensi**
Ekstensi ini akan menambahkan API baru bernama `hello_world`. Ketika API dipanggil, ia akan mengembalikan pesan seperti `"Hello, World!"` atau pesan khusus jika parameter `name` disertakan.

---

### **Langkah-Langkah Membuat CKAN Extension**

#### 1. **Buat Direktori Ekstensi**
Gunakan perintah berikut untuk membuat kerangka dasar ekstensi:
```bash
ckan generate extension my_hello_world
```

Struktur direktori akan terlihat seperti ini:
```plaintext
ckanext-my_hello_world/
├── ckanext/
│   └── my_hello_world/
│       ├── __init__.py
│       ├── plugin.py       # Tempat implementasi plugin
│       └── tests/          # Tempat untuk unit test
├── setup.py                # Konfigurasi instalasi Python
├── README.md               # Dokumentasi ekstensi
└── requirements.txt        # Daftar dependensi (jika ada)
```

#### 2. **Tambahkan Plugin API Baru**
Edit file `plugin.py` untuk mendefinisikan plugin dan aksi API baru:

```python
from ckan.plugins import SingletonPlugin, implements
from ckan.plugins import toolkit

class HelloWorldPlugin(SingletonPlugin):
    """
    Plugin sederhana untuk menambahkan API baru bernama 'hello_world'
    """
    implements(toolkit.IActions)

    def get_actions(self):
        # Tambahkan aksi API baru bernama 'hello_world'
        return {
            'hello_world': hello_world
        }

def hello_world(context, data_dict):
    """
    Aksi API sederhana yang mengembalikan pesan
    """
    # Ambil parameter 'name' jika ada
    name = data_dict.get('name', 'World')
    return {'message': f'Hello, {name}!'}
```

#### 3. **Daftarkan Plugin**
Tambahkan nama plugin (`my_hello_world`) ke file `ckan.ini` di bagian `ckan.plugins`:
```ini
ckan.plugins = my_hello_world
```

---

### **Cara Menggunakan Ekstensi**

1. **Instal Ekstensi:**
   Jalankan perintah berikut di direktori utama ekstensi untuk menginstalnya:
   ```bash
   pip install -e .
   ```

2. **Restart CKAN:**
   Restart instance CKAN untuk memuat ekstensi baru:
   ```bash
   supervisorctl restart ckan
   ```

3. **Coba Aksi API Baru:**
   Gunakan API `hello_world` yang baru dibuat.

   #### Contoh Request:
   - **Tanpa Parameter:**
     ```bash
     curl -X GET "http://localhost/api/3/action/hello_world"
     ```
   - **Dengan Parameter:**
     ```bash
     curl -X GET "http://localhost/api/3/action/hello_world" \
       -d '{"name": "CKAN"}' \
       -H "Content-Type: application/json"
     ```

   #### Contoh Respons:
   - **Tanpa Parameter:**
     ```json
     {
       "help": "http://localhost/api/3/action/help_show?name=hello_world",
       "success": true,
       "result": {
         "message": "Hello, World!"
       }
     }
     ```

   - **Dengan Parameter:**
     ```json
     {
       "help": "http://localhost/api/3/action/help_show?name=hello_world",
       "success": true,
       "result": {
         "message": "Hello, CKAN!"
       }
     }
     ```

---

### **Kegunaan Ekstensi**
Ekstensi ini memiliki fungsi sederhana sebagai contoh bagaimana:
1. Menambahkan aksi API baru di CKAN.
2. Memahami struktur dasar ekstensi CKAN.
3. Mengembangkan CKAN agar sesuai dengan kebutuhan spesifik, seperti API khusus untuk integrasi eksternal.

---

### **Pengembangan Lanjutan**
- Anda bisa memodifikasi ekstensi ini untuk:
  - Mengakses dan memanipulasi data CKAN (dataset, resource, dll.).
  - Mengintegrasikan sistem eksternal.
  - Menambahkan validasi input parameter.

---

Objek `Session` dalam CKAN berasal dari SQLAlchemy dan berfungsi sebagai antarmuka untuk berinteraksi dengan database. `Session` memungkinkan Anda menjalankan berbagai operasi database seperti query, insert, update, dan delete. Berikut adalah daftar operasi umum yang dapat dilakukan dengan `Session`:

---

### **1. Query Data**
#### **Mengambil Semua Baris**
```python
from ckan.model.meta import Session
from ckan.model import Package

packages = Session.query(Package).all()
```

#### **Mengambil Data dengan Filter**
```python
# Mengambil dataset yang privat
packages = Session.query(Package).filter(Package.private == True).all()
```

#### **Mengambil Satu Baris**
```python
# Mengambil dataset dengan ID tertentu
package = Session.query(Package).filter(Package.id == '123456').first()
```

#### **Menghitung Jumlah Baris**
```python
# Menghitung total dataset
count = Session.query(Package).count()
```

#### **Mengurutkan Data**
```python
# Mengurutkan dataset berdasarkan nama
packages = Session.query(Package).order_by(Package.name).all()
```

#### **Paginasi Data**
```python
# Mengambil 10 dataset pertama (paginasi)
packages = Session.query(Package).limit(10).offset(0).all()
```

---

### **2. Insert Data**
#### **Menambahkan Data Baru**
Untuk menambahkan data ke database:
```python
from ckan.model import Package
from ckan.model.meta import Session

# Membuat objek baru
new_package = Package(
    id="new_id",
    name="new_dataset",
    title="New Dataset",
    private=False
)

# Menambahkan ke sesi
Session.add(new_package)
Session.commit()  # Simpan perubahan ke database
```

---

### **3. Update Data**
#### **Mengupdate Data yang Ada**
Untuk memperbarui data yang sudah ada:
```python
# Mengambil dataset
package = Session.query(Package).filter(Package.id == '123456').first()

# Mengupdate atribut
if package:
    package.title = "Updated Dataset Title"
    Session.commit()  # Simpan perubahan
```

---

### **4. Delete Data**
#### **Menghapus Baris**
Untuk menghapus baris dari database:
```python
# Mengambil dataset
package = Session.query(Package).filter(Package.id == '123456').first()

# Menghapus dataset
if package:
    Session.delete(package)
    Session.commit()  # Simpan perubahan
```

---

### **5. Raw SQL Query**
#### **Menjalankan Query Kustom**
Anda dapat menjalankan SQL langsung menggunakan `Session.execute`:
```python
from sqlalchemy import text
from ckan.model.meta import Session

# Menjalankan SQL mentah
result = Session.execute(text("SELECT id, name FROM package WHERE private = false"))

# Iterasi hasil
for row in result:
    print(row.id, row.name)
```

---

### **6. Transaction Management**
#### **Rollback Perubahan**
Jika terjadi kesalahan, Anda dapat membatalkan perubahan:
```python
try:
    package = Session.query(Package).filter(Package.id == '123456').first()
    if package:
        package.title = "Temporary Update"
        Session.commit()  # Simpan perubahan
except Exception as e:
    Session.rollback()  # Batalkan perubahan jika ada error
    raise e
```

---

### **7. Menutup Session**
Pastikan untuk menutup sesi jika selesai digunakan:
```python
Session.close()
```

---

### **Kombinasi Operasi**
Anda dapat menggabungkan operasi seperti filter, order_by, dan limit:
```python
packages = (
    Session.query(Package)
    .filter(Package.private == False)
    .order_by(Package.title.desc())
    .limit(5)
    .all()
)
```

---

### **Daftar Operasi SQLAlchemy yang Dapat Digunakan**
Berikut adalah beberapa metode lain yang bisa Anda gunakan dengan `Session`:
- **`add()`**: Menambahkan objek baru ke sesi.
- **`add_all([obj1, obj2])`**: Menambahkan banyak objek.
- **`merge()`**: Menggabungkan perubahan ke dalam sesi.
- **`flush()`**: Menulis perubahan ke dalam database tanpa commit.
- **`commit()`**: Menyimpan semua perubahan.
- **`rollback()`**: Membatalkan semua perubahan dalam sesi.
- **`execute()`**: Menjalankan SQL mentah.
- **`query()`**: Membuat query.
- **`delete()`**: Menghapus objek dari sesi.

---

Jika Anda memiliki kasus penggunaan tertentu, beri tahu saya, dan saya bisa membantu membuatkan query atau operasi yang sesuai! 😊
