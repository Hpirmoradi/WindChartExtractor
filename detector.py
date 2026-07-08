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
    MULTI_PAGE
)


# -----------------------------------------
# بررسی وجود کلمات نمودار
# -----------------------------------------

def page_has_chart(page):

    text = page.get_text("text").upper()

    score = 0

    for word in KEYWORDS:

        if word in text:

            score += 1

    return score >= 4


# -----------------------------------------
# پیدا کردن صفحات نمودار
# -----------------------------------------

def detect(pdf_path):

    doc = fitz.open(pdf_path)

    base = pdf_path.stem

    if "_20" in base:

        base = base.split("_20")[0]

    pages = []

    # ----------------------------------
    # فایل‌های چندصفحه‌ای
    # ----------------------------------

    if base in MULTI_PAGE:

        pages = sorted(MULTI_PAGE[base].keys())

        doc.close()

        return pages

    # ----------------------------------
    # فایل‌های صفحه ثابت
    # ----------------------------------

    if base in FIXED_PAGE:

        pages.append(FIXED_PAGE[base])

        doc.close()

        return pages

    # ----------------------------------
    # جستجوی خودکار
    # ----------------------------------

    for i in range(doc.page_count):

        page = doc.load_page(i)

        if page_has_chart(page):

            pages.append(i + 1)

    doc.close()

    return pages


# -----------------------------------------
# تست
# -----------------------------------------

if __name__ == "__main__":

    from pathlib import Path

    from config import INPUT_FOLDER

    pdfs = sorted(INPUT_FOLDER.glob("*.pdf"))

    print("=" * 50)

    print("Detector Test")

    print("=" * 50)

    for pdf in pdfs:

        pages = detect(pdf)

        print()

        print(pdf.name)

        if pages:

            print("صفحات :", pages)

        else:

            print("نمودار پیدا نشد")
