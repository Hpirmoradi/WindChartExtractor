# ==========================
# main.py
# برنامه اصلی
# ==========================

from pathlib import Path

from config import INPUT_FOLDER
from detector import find_pages_for_file
from cropper import save_chart


def main():

    pdfs = sorted(Path(INPUT_FOLDER).glob("*.pdf"))

    print("=" * 50)
    print(f"تعداد PDFها : {len(pdfs)}")
    print("=" * 50)

    total = 0

    for pdf in pdfs:

        print("\n" + "-" * 50)
        print(pdf.name)

        pages = find_pages_for_file(pdf)

        if not pages:

            print("✗ نمودار پیدا نشد")
            continue

        for page in pages:

            print(f"صفحه {page}")

            save_chart(
                pdf,
                page
            )

            total += 1

    print("\n" + "=" * 50)
    print(f"تعداد تصاویر ذخیره شده : {total}")
    print("=" * 50)


if __name__ == "__main__":
    main()
