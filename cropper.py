"""
==========================================
Wind Chart Extractor
Cropper (PyMuPDF + Pillow)
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


def save_chart(pdf_path, page_number):

    doc = fitz.open(pdf_path)

    page = doc.load_page(page_number - 1)

    mat = fitz.Matrix(ZOOM, ZOOM)

    pix = page.get_pixmap(matrix=mat, alpha=False)

    img = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    width, height = img.size

    left = LEFT
    top = TOP
    right = width - RIGHT
    bottom = min(BOTTOM, height)

    chart = img.crop((left, top, right, bottom))

    name = get_persian_name(
        pdf_path.name,
        page_number
    )

    outfile = OUTPUT_FOLDER / f"{name}.png"

    chart.save(outfile)

    print("✓", outfile.name)

    doc.close()
