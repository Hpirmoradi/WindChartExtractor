# ==========================
# cropper.py
# رندر PDF + برش + ذخیره PNG
# ==========================

import fitz
from PIL import Image
from pathlib import Path

from config import OUTPUT_FOLDER, DPI, CROP
from names import get_persian_name


def render_page(page):

    zoom = DPI / 72

    matrix = fitz.Matrix(zoom, zoom)

    pix = page.get_pixmap(matrix=matrix, alpha=False)

    img = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    return img


def crop_image(img):

    width, height = img.size

    left = CROP["left"]
    top = CROP["top"]
    right = width - CROP["right_margin"]
    bottom = min(CROP["bottom"], height)

    return img.crop((left, top, right, bottom))


def save_chart(pdf_path, page_number):

    doc = fitz.open(pdf_path)

    page = doc.load_page(page_number - 1)

    img = render_page(page)

    img = crop_image(img)

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    name = get_persian_name(
        pdf_path.name,
        page_number
    )

    outfile = OUTPUT_FOLDER / f"{name}.png"

    img.save(outfile)

    print("✓", outfile.name)

    doc.close()
