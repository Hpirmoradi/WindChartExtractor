"""
==========================================
Wind Chart Extractor
Names Module
==========================================
"""

from pathlib import Path
from config import MULTI_PAGE

# --------------------------------------------------
# نام‌های فارسی
# --------------------------------------------------

PERSIAN_NAMES = {

    "Shafagh": "شفق",

    "Balal_Gas_Field": "بلال",

    "Nasr2": "نصر",

    "Southpars": "پارس جنوبی",

    "Qeshm": "قشم",

    "Froozan": "فروزان",

    "Siri": "سیری",

    "Reshadat": "رشادت",

    "Lavan": "لاوان",

    "Kish": "کیش",

    "Khark": "خارگ",

    "Bahregan": "بهرگان",

    "Aboozar": "ابوذر",

    "Bushehr": "بوشهر",

    "Roudsar": "رودسر"

}

# --------------------------------------------------
# حذف تاریخ از نام فایل
# --------------------------------------------------

def get_base_name(file_name: str):

    name = Path(file_name).stem

    if "_20" in name:

        name = name.split("_20")[0]

    return name


# --------------------------------------------------
# آیا فایل مسیر است؟
# --------------------------------------------------

def is_route_file(base_name):

    return base_name in MULTI_PAGE


# --------------------------------------------------
# نام فارسی فایل‌های معمولی
# --------------------------------------------------

def get_normal_name(base_name):

    if base_name in PERSIAN_NAMES:

        return PERSIAN_NAMES[base_name]

    return base_name


# --------------------------------------------------
# نام فارسی فایل‌های مسیر
# --------------------------------------------------

def get_route_name(base_name, page_number):

    if base_name not in MULTI_PAGE:

        return None

    pages = MULTI_PAGE[base_name]

    if page_number in pages:

        return pages[page_number]

    return None


# --------------------------------------------------
# تابع اصلی
# --------------------------------------------------

def get_persian_name(file_name, page_number):

    base = get_base_name(file_name)

    route_name = get_route_name(base, page_number)

    if route_name:

        return route_name

    return get_normal_name(base)


# --------------------------------------------------
# تست
# --------------------------------------------------

if __name__ == "__main__":

    tests = [

        ("Shafagh_2026070804.pdf", 5),

        ("Nasr2_2026070804.pdf", 4),

        ("Balal_Gas_Field_2026070804.pdf", 5),

        ("Route_Asaluyeh_Anchorage_Phase11_2026070804.pdf", 6),

        ("Route_Asaluyeh_Anchorage_Phase11_2026070804.pdf", 7),

        ("Route_Lavan_Salman_2026070801.pdf", 7),

        ("Route_Lavan_Salman_2026070801.pdf", 8),

    ]

    print()

    print("=" * 40)

    for file_name, page in tests:

        print(

            file_name,

            " ---> ",

            get_persian_name(file_name, page)

        )

    print("=" * 40)
