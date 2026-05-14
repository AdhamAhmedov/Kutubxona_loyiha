# Kutubxona Voqealar Boshqaruvi Tizimi (Event-Driven Architecture)

Ushbu loyiha **Komponentga asoslangan arxitektura (CBA)** va **Voqealarga asoslangan model (Event-Driven)** tamoyillarini namoyish etish uchun yaratilgan. Loyiha kutubxonada kitob olish jarayonini simulyatsiya qiladi.

##  Loyiha Imkoniyatlari
* **Event Bus:** Markazlashgan voqealar navbati.
* **Ko'p tarmoqli ishlov berish:** Voqealar fonda (daemon thread) qayta ishlanadi.
* **MongoDB Integratsiyasi:** Kitob olish tarixi ma'lumotlar bazasiga saqlanadi.
* **Konsol Bildirishnomalari:** Foydalanuvchiga real vaqtda xabar ko'rsatiladi.

## 🛠 Texnologiyalar
* **Python 3.x**
* **MongoDB** (Ma'lumotlarni saqlash uchun)
* **PyMongo** (MongoDB bilan aloqa uchun)
* **Unittest** (Tizimni sinash uchun)

##  Fayllar Tuzilishi
* `bus.py` - Voqealar navbatini va handlerlarni boshqaradi.
* `events.py` - Tizimdagi voqealar (BookBorrowedEvent) strukturasini belgilaydi.
* `handlers.py` - Voqealarga mantiqiy ishlov beruvchi komponentlar.
* `main.py` - Loyihani ishga tushirish nuqtasi.
* `test_system.py` - Tizimning ishlashini tekshiruvchi testlar.

##  O'rnatish va Ishga Tushirish

1. **Repozitoriyani yuklab oling:**
   ```bash
   git clone [https://github.com/AdhamAhmedov/Kutubxona_loyiha.git](https://github.com/AdhamAhmedov/Kutubxona_loyiha.git)
   cd Kutubxona_loyiha
