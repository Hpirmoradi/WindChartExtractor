"""
==========================================
Wind Chart Extractor
Version 3.0
Author : ChatGPT
==========================================
"""

import time
from pathlib import Path

from config import (
    INPUT_FOLDER,
    OUTPUT_FOLDER,
    SHOW_TIME
)

from detector import detect

from cropper import save_chart


# --------------------------------------------------
# برنامه اصلی
# --------------------------------------------------

def main():

    start = time.time()

    pdfs = sorted(Path(INPUT_FOLDER).glob("*.pdf"))

    print("=" * 60)
    print(" Wind Chart Extractor 3.0 ")
    print("=" * 60)
    print()

    print(f"تعداد فایل های PDF : {len(pdfs)}")
    print()

    total_images = 0
    failed = []

    for pdf in pdfs:

        pages = detect(pdf)

        if len(pages) == 0:

            failed.append(pdf.name)
            continue

        for page in pages:

            try:

                save_chart(pdf, page)

                total_images += 1

            except Exception as e:

                print("خطا :", pdf.name)

                print(e)

    print()
    print("=" * 60)

    print("پایان پردازش")

    print()

    print("تعداد تصاویر :", total_images)

    print("پوشه خروجی :")

    print(OUTPUT_FOLDER.resolve())

    if failed:

        print()

        print("فایل هایی که نمودار پیدا نشد :")

        for f in failed:

            print(" -", f)

    if SHOW_TIME:

        print()

        print(
            "زمان اجرا : %.2f ثانیه"
            % (time.time() - start)
        )

    print("=" * 60)


# --------------------------------------------------

if __name__ == "__main__":

    main()
