
```markdown
# Online Shop - DRF

یک فروشگاه اینترنتی ساده پیاده‌سازی‌شده با استفاده از Django Rest Framework.

## ویژگی‌ها

- ثبت‌نام و احراز هویت کاربران
- مدیریت کاربران و نقش‌های مدیر
- پروفایل کاربران
- علاقه‌مندی‌های کاربران
- مدیریت و دسته‌بندی محصولات
- جستجو و فیلتر محصولات
- مدیریت سبد خرید
- مشاهده لیست سفارشات
- نظرات و بازخورد کاربران برای محصولات
- ثبت سفارش و پرداخت
- پیگیری سفارش

### پیش‌نیازها

- Python 3.10+
- pip
- virtualenv
- PostgreSQL

### مراحل نصب

1. کلون کردن مخزن:

```bash
git clone https://github.com/Iman-CodeHermit/online-shop-drf.git
cd online-shop-drf
```

2. ساخت محیط مجازی:

```bash
python -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
```

3. نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

4. انجام مهاجرت‌ها:

```bash
python manage.py migrate
```

5. ساخت ابرکاربر (اختیاری):

```bash
python manage.py createsuperuser
```

6. اجرای سرور توسعه:

```bash
python manage.py runserver
```
## مشارکت

در صورت علاقه‌مندی به همکاری، Pull Request ارسال کنید یا Issue ثبت نمایید.



---

**سازنده:** [Iman-CodeHermit](https://github.com/Iman-CodeHermit)
