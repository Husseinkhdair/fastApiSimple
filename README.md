# مشروع FastAPI بسيط مع CRUD باستخدام Local Dictionary

مشروع FastAPI متكامل يحتوي على أمثلة عملية لجميع العمليات الأساسية (**GET**, **POST**, **PUT**, **DELETE**) مع التعامل مع البيانات المخزنة محلياً في قاموس (`dict`).

---

## 📁 محتويات المشروع

- [`main.py`](file:///c:/fastApi/main.py): يحتوي على كود التطبيق ونقاط النهاية (Endpoints) والـ Schemas.
- [`requirements.txt`](file:///c:/fastApi/requirements.txt): يحتوي على المكتبات المطلوبة (`fastapi`, `uvicorn`, `pydantic`).

---

## 🚀 طريقة التشغيل

### 1️⃣ إنشاء وتفعيل بيئة افتراضية (Virtual Environment)
```bash
python -m venv venv
```
- **على Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate
  ```
- **على Linux / macOS:**
  ```bash
  source venv/bin/activate
  ```

### 2️⃣ تثبيت المكتبات المطلوبة
```bash
pip install -r requirements.txt
```

### 3️⃣ تشغيل خادم Uvicorn
```bash
uvicorn main:app --reload
```

---

## 📌 نقاط النهاية (Endpoints) المتاحة

| العملية | المسار (Endpoint) | الوصف |
| :--- | :--- | :--- |
| **GET** | `/` | الصفحة الرئيسية |
| **GET** | `/items` | جلب جميع العناصر |
| **GET** | `/items/{item_id}` | جلب عنصر محدد عن طريق الـ ID |
| **POST** | `/items` | إضافة عنصر جديد |
| **PUT** | `/items/{item_id}` | تعديل بيانات عنصر موجود |
| **DELETE** | `/items/{item_id}` | حذف عنصر محدد |

---

## 🌐 تجربة الـ API تفاعلياً (Swagger UI)

بعد تشغيل الخادم، افتح المتصفح وانتقل إلى:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
