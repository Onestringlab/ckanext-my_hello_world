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

Jika Anda membutuhkan pengembangan atau fitur tambahan, beri tahu saya!