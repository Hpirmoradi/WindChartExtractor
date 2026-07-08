# ==========================
# detector.py
# پیدا کردن صفحات نمودار باد
# ==========================

import fitz
from config import KEYWORDS


def is_chart_page(page):

    """
    بررسی می‌کند آیا صفحه نمودار باد است یا خیر.
    """

    text = page.get_text().upper()

    return all(word in text for word in KEYWORDS)


def find_chart_pages(pdf_path):

    """
    همه صفحاتی که نمودار باد دارند را برمی‌گرداند.
    """

    doc = fitz.open(pdf_path)

    pages = []

    for page_no in range(doc.page_count):

        page = doc.load_page(page_no)

        if is_chart_page(page):

            pages.append(page_no + 1)

    doc.close()

    return pages


def find_pages_for_file(pdf_path):

    """
    منطق مخصوص فایل‌های خاص
    """

    pages = find_chart_pages(pdf_path)

    name = pdf_path.stem

    # -------------------------
    # مسیر عسلویه
    # -------------------------

    if name.startswith("Route_Asaluyeh_Anchorage_Phase11"):

        result = []

        if 6 in pages:
            result.append(6)

        if 7 in pages:
            result.append(7)

        return result

    # -------------------------
    # مسیر سلمان
    # -------------------------

    if name.startswith("Route_Lavan_Salman"):

        result = []

        if 7 in pages:
            result.append(7)

        if 8 in pages:
            result.append(8)

        return result

    # سایر فایل‌ها
    if pages:

        return [pages[0]]

    return []
