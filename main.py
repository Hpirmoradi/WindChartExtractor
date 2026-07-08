"""
==========================================
Wind Chart Extractor
Main Program
Version 1.0
==========================================
"""

import time

from config import (
    INPUT_FOLDER,
    OUTPUT_FOLDER,
    SHOW_TIME
)

from detector import detect

from cropper import save_chart


# ---------------------------------------------------
# برنامه اصلی
# ---------------------------------------------------

def main():

    start = time.time()

    pdfs = sorted(INPUT_FOLDER.glob("*.pdf"))

    print("=" * 60)
    print("      Wind Chart Extractor")
    print("=" * 60)
    print()

    print("تعداد فایل ها :", len(pdfs))
    print()

    success = 0
    failed = []

    # ----------------------------------------------

    for pdf in pdfs:

        print("-" * 60)
        print(pdf.name)

        pages = detect(pdf)

        if not pages:

            print("✗ نمودار پیدا نشد")
            failed.append(pdf.name)
            print()
            continue

        print("صفحات :", pages)

        for page in pages:

            try:

                save_chart(pdf, page)

                success += 1

            except Exception as e:

                print("خطا :", e)

        print()

    # ----------------------------------------------

    print("=" * 60)

    print("پایان پردازش")

    print()

    print("تعداد تصاویر استخراج شده :", success)

    print()

    print("محل ذخیره :")

    print(OUTPUT_FOLDER.resolve())

    if failed:

        print()

        print("فایل های ناموفق")

        for f in failed:

            print("-", f)

    if SHOW_TIME:

        print()

        print(
            "زمان اجرا : %.2f ثانیه"
            % (time.time() - start)
        )

    print("=" * 60)


# ---------------------------------------------------

if __name__ == "__main__":

    main()
