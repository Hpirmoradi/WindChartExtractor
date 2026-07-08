from pathlib import Path

# مسیر PDFها
INPUT_FOLDER = Path(r"C:\Users\M\Downloads\New folder")

# پوشه خروجی
OUTPUT_FOLDER = Path("output")
OUTPUT_FOLDER.mkdir(exist_ok=True)

# کیفیت تصویر
DPI = 300
ZOOM = DPI / 72

# تنظیمات برش
LEFT = 350
TOP = 420
RIGHT = 250
BOTTOM = 2200

# نمایش زمان اجرا
SHOW_TIME = True
