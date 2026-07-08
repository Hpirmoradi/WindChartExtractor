"""
==========================================
Wind Chart Extractor
Detector Module
==========================================
"""

import fitz

from config import (
    KEYWORDS,
    FIXED_PAGE,
    MULTI_PAGE,
    VERBOSE
)


# ----------------------------------------------------------
# بررسی وجود متن های نمودار
# ----------------------------------------------------------

def page_contains_chart(page):

    text = page.get_text("text").upper()

    score = 0

    for word in KEYWORDS:

        if word in text:

            score += 1

    return score >= 4


# ----------------------------------------------------------
# جستجوی کل فایل
# ----------------------------------------------------------

def scan_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    pages = []

    for i in range(doc.page_count):

        page = doc.load_page(i)

        if page_contains_chart(page):

            pages.append(i + 1)

    doc.close()

    return pages


# ----------------------------------------------------------
# تعیین صفحات خروجی
# ----------------------------------------------------------

def get_output_pages(pdf_path):

    base = pdf_path.stem

    if "_20" in base:

        base = base.split("_20")[0]

    # -------------------------
    # فایل های مسیر
    # -------------------------

    if base in MULTI_PAGE:

        return list(MULTI_PAGE[base].keys())

    # -------------------------
    # فایل های با صفحه ثابت
    # -------------------------

    if base in FIXED_PAGE:

        return [FIXED_PAGE[base]]

    # -------------------------
    # در غیر اینصورت اسکن کن
    # -------------------------

    pages = scan_pdf(pdf_path)

    return pages


# ----------------------------------------------------------
# چاپ نتیجه
# ----------------------------------------------------------

def print_result(pdf_path, pages):

    if not VERBOSE:

        return

    print()

    print("-" * 50)

    print(pdf_path.name)

    if len(pages) == 0:

        print("✗ نمودار پیدا نشد")

        return

    for p in pages:

        print(f"✓ صفحه {p}")


# ----------------------------------------------------------
# تابع اصلی
# ----------------------------------------------------------

def detect(pdf_path):

    pages = get_output_pages(pdf_path)

    print_result(pdf_path, pages)

    return pages


# ----------------------------------------------------------
# تست
# ----------------------------------------------------------

if __name__ == "__main__":

    from pathlib import Path

    from config import INPUT_FOLDER

    pdfs = sorted(INPUT_FOLDER.glob("*.pdf"))

    print()

    print("=" * 60)

    print("Testing detector")

    print("=" * 60)

    for pdf in pdfs:

        detect(pdf)
