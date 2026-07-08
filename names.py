"""
==========================================
Wind Chart Extractor
Names Module
==========================================
"""

from pathlib import Path
from config import MULTI_PAGE

# ---------------------------------------
# نام‌های فارسی
# ---------------------------------------

PERSIAN_NAMES = {
    "Aboozar": "ابوذر",
    "Bahregan": "بهرگان",
    "Balal_Gas_Field": "بلال",
    "Bushehr": "بوشهر",
    "Froozan": "فروزان",
    "Khark": "خارگ",
    "Kish": "کیش",
    "Lavan": "لاوان",
    "Nasr2": "نصر",
    "Qeshm": "قشم",
    "Reshadat": "رشادت",
    "Roudsar": "رودسر",
    "Shafagh": "شفق",
    "Siri": "سیری",
    "Southpars": "پارس جنوبی"
}


def get_base_name(filename):
    """حذف تاریخ از انتهای نام فایل"""

    name = Path(filename).stem

    if "_20" in name:
        name = name.split("_20")[0]

    return name


def get_persian_name(filename, page):

    base = get_base_name(filename)

    # فایل‌های چندصفحه‌ای
    if base in MULTI_PAGE:

        pages = MULTI_PAGE[base]

        if page in pages:
            return pages[page]

    # فایل‌های معمولی
    if base in PERSIAN_NAMES:
        return PERSIAN_NAMES[base]

    return base


if __name__ == "__main__":

    tests = [
        ("Aboozar_2026070801.pdf", 4),
        ("Shafagh_2026070804.pdf", 5),
        ("Route_Asaluyeh_Anchorage_Phase11_2026070804.pdf", 6),
        ("Route_Asaluyeh_Anchorage_Phase11_2026070804.pdf", 7),
        ("Route_Lavan_Salman_2026070801.pdf", 7),
        ("Route_Lavan_Salman_2026070801.pdf", 8),
    ]

    print("=" * 40)

    for file, page in tests:
        print(file, "=>", get_persian_name(file, page))

    print("=" * 40)
