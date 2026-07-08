# ==========================
# names.py
# تبدیل نام فایل به فارسی
# ==========================

FILE_NAMES = {

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


def get_base_name(file_name):

    name = file_name.replace(".pdf", "")

    if "_20" in name:
        name = name[:name.index("_20")]

    return name


def get_persian_name(file_name, page_number):

    base = get_base_name(file_name)

    # مسیر عسلویه
    if base == "Route_Asaluyeh_Anchorage_Phase11":

        if page_number == 6:
            return "عسلویه"

        if page_number == 7:
            return "میانی عسلویه"

    # مسیر سلمان
    if base == "Route_Lavan_Salman":

        if page_number == 7:
            return "میانی سلمان"

        if page_number == 8:
            return "سلمان"

    return FILE_NAMES.get(base, base)
