"""
==========================================
Wind Chart Extractor
Cropper Module
==========================================
"""

import fitz
from PIL import Image

from config import (
    OUTPUT_FOLDER,
    ZOOM,
    LEFT,
    TOP,
    RIGHT,
    BOTTOM
)

from names import get_persian_name


# -------------------------------------------------
# رندر صفحه PDF
# -------------------------------------------------

def render_page(page):

    matrix = fitz.Matrix(ZOOM, ZOOM)

    pix = page.get_pixmap(
        matrix=matrix,
        alpha=False
    )

    img = Image.frombytes(
        "RGB",
        (pix.width, pix.height),
        pix.samples
    )

    return img


# -------------------------------------------------
# برش تصویر
# -------------------------------------------------

def crop_image(img):

    width, height = img.size

    left = LEFT
    top = TOP

    right = width - RIGHT
    bottom = min(BOTTOM, height)

    return img.crop(
        (
            left,
            top,
            right,
            bottom
        )
    )


# -------------------------------------------------
# ذخیره تصویر
# -------------------------------------------------

def save_chart(pdf_path, page_number):

    doc = fitz.open(pdf_path)

    page = doc.load_page(page_number - 1)

    img = render_page(page)

    chart = crop_image(img)

    name = get_persian_name(
        pdf_path.name,
        page_number
    )

    outfile = OUTPUT_FOLDER / f"{name}.png"

    chart.save(
        outfile,
        format="PNG"
    )

    print("✓", outfile.name)

    doc.close()


# -------------------------------------------------
# تست
# -------------------------------------------------

if __name__ == "__main__":

    from pathlib import Path

    from config import INPUT_FOLDER

    pdf = sorted(
        INPUT_FOLDER.glob("*.pdf")
    )[0]

    print(pdf.name)

    save_chart(pdf,4)
