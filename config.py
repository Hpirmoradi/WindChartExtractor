# ==========================
# config.py
# تنظیمات برنامه
# ==========================

from pathlib import Path

# پوشه PDFها
INPUT_FOLDER = Path(r"C:\Users\M\Downloads\New folder")

# پوشه خروجی
OUTPUT_FOLDER = Path("output")

# کیفیت خروجی
DPI = 300

# فرمت خروجی
IMAGE_FORMAT = "PNG"

# کلیدواژه‌های تشخیص نمودار
KEYWORDS = [
    "WS 10",
    "WG 10",
    "WS 50",
    "WG 50"
]

# مختصات اولیه برش
# بعداً با نمونه PDF دقیق تنظیم می‌کنیم
CROP = {

    "left": 300,

    "top": 500,

    "right_margin": 300,

    "bottom": 2600

}
