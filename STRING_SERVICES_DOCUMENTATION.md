# String Services Documentation
## Overview

String Services merupakan modul yang menyediakan empat layanan pemrosesan teks dasar:

1. **char_count** - Menghitung jumlah karakter
2. **word_count** - Menghitung jumlah kata
3. **reverse** - Membalik urutan teks
4. **remove_vowels** - Menghapus semua vokal

Semua fungsi dirancang untuk diintegrasikan dengan TCP Server dan dapat dipanggil melalui protokol JSON Lines.

---

## Fungsi-Fungsi

### 1. char_count(text)

**Deskripsi:** Menghitung total jumlah karakter dalam sebuah teks.

**Parameter:**
- `text` (str): Teks yang akan dihitung

**Return:**
```python
{
    "status": "success" | "error",
    "result": int | None,
    "message": str
}
```

**Contoh Penggunaan:**
```python
from services.string_services import char_count

result = char_count("hello world")
# Output: {
#   "status": "success",
#   "result": 11,
#   "message": "Total 11 character(s) found"
# }
```

**Validasi:**
- Input harus berupa string
- Jika input bukan string atau None, return status "error"

**Catatan:**
- Menghitung semua karakter termasuk spasi, angka, dan simbol

---

### 2. word_count(text)

**Deskripsi:** Menghitung total jumlah kata dalam sebuah teks.

**Parameter:**
- `text` (str): Teks yang akan dihitung

**Return:**
```python
{
    "status": "success" | "error",
    "result": int | None,
    "message": str
}
```

**Contoh Penggunaan:**
```python
from services.string_services import word_count

result = word_count("hello world python")
# Output: {
#   "status": "success",
#   "result": 3,
#   "message": "Total 3 word(s) found"
# }
```

**Validasi:**
- Input harus berupa string
- Jika input bukan string atau None, return status "error"

**Catatan:**
- Kata didefinisikan sebagai urutan karakter yang dipisahkan oleh whitespace
- Fungsi menggunakan `.split()` Python yang otomatis menangani multiple spaces

---

### 3. reverse(text)

**Deskripsi:** Membalik urutan karakter dalam sebuah teks.

**Parameter:**
- `text` (str): Teks yang akan dibalik

**Return:**
```python
{
    "status": "success" | "error",
    "result": str | None,
    "message": str
}
```

**Contoh Penggunaan:**
```python
from services.string_services import reverse

result = reverse("hello")
# Output: {
#   "status": "success",
#   "result": "olleh",
#   "message": "String reversed: 'hello' -> 'olleh'"
# }
```

**Validasi:**
- Input harus berupa string
- Jika input bukan string atau None, return status "error"

**Catatan:**
- Menggunakan string slicing `[::-1]` untuk efisiensi
- Spasi dan karakter khusus tetap dipertahankan

---

### 4. remove_vowels(text)

**Deskripsi:** Menghapus semua huruf vokal dari sebuah teks.

**Parameter:**
- `text` (str): Teks yang akan dihapus vokalnya

**Return:**
```python
{
    "status": "success" | "error",
    "result": str | None,
    "message": str
}
```

**Contoh Penggunaan:**
```python
from services.string_services import remove_vowels

result = remove_vowels("hello world")
# Output: {
#   "status": "success",
#   "result": "hll wrld",
#   "message": "Removed 3 vowel(s): 'hello world' -> 'hll wrld'"
# }
```

**Validasi:**
- Input harus berupa string
- Jika input bukan string atau None, return status "error"

**Catatan:**
- Menghapus vokal lowercase: a, e, i, o, u
- Menghapus vokal uppercase: A, E, I, O, U
- Spasi, angka, dan simbol tetap dipertahankan

---

## Response Format

Semua fungsi mengembalikan dictionary dengan struktur konsisten:

| Field | Tipe | Deskripsi |
|-------|------|-----------|
| `status` | str | "success" atau "error" |
| `result` | varies | Hasil operasi (int/str) atau None jika error |
| `message` | str | Pesan deskriptif |

### Success Response
```json
{
  "status": "success",
  "result": 5,
  "message": "Total 5 character(s) found"
}
```

### Error Response
```json
{
  "status": "error",
  "result": null,
  "message": "Input must be a string, got int"
}
```

---

## Unit Tests

Semua fungsi memiliki unit test komprehensif di `tests/test_string.py`.

**Total Test Cases:** 33 tests

### Test Coverage per Fungsi:
- **char_count:** 7 test cases
- **word_count:** 8 test cases
- **reverse:** 8 test cases
- **remove_vowels:** 10 test cases

### Menjalankan Tests:

```bash
# Run semua tests
python -m pytest tests/test_string.py -v

# Atau dengan unittest
python -m unittest tests.test_string -v

# Run test spesifik
python -m unittest tests.test_string.TestCharCount -v
```

### Contoh Output:
```
test_char_count_empty_string ... ok
test_char_count_invalid_input_int ... ok
test_char_count_invalid_input_list ... ok
test_char_count_invalid_input_none ... ok
test_char_count_simple_string ... ok
test_char_count_with_numbers_and_special ... ok
test_char_count_with_spaces ... ok
test_remove_vowels_all_vowels ... ok
test_remove_vowels_empty_string ... ok
...

Ran 33 tests in 0.012s

OK
```

---

## Integration dengan TCP Server

Fungsi-fungsi ini akan diintegrasikan dengan TCP Server melalui protokol JSON Lines.

### Expected Protocol Format:

**Request:**
```json
{
  "service": "char_count",
  "params": {
    "text": "hello world"
  }
}
```

**Response:**
```json
{
  "status": "success",
  "result": 11,
  "message": "Total 11 character(s) found"
}
```