"""
==========================================
Wind Chart Extractor
Cropper Module
==========================================
"""

import cv2
import fitz
import numpy as np

from PIL import Image

from config import (
    OUTPUT_FOLDER,
    DPI,
    ZOOM,
    AUTO_CROP,
    LEFT,
    TOP,
    RIGHT,
    BOTTOM,
    SAVE_FULL_PAGE,
    FULLPAGE_FOLDER
)

from names import get_persian_name


# ----------------------------------------------------------
# رندر صفحه PDF
# ----------------------------------------------------------

def render_page(page):

    mat = fitz.Matrix(ZOOM, ZOOM)

    pix = page.get_pixmap(
        matrix=mat,
        alpha=False
    )

    img = Image.frombytes(
        "RGB",
        (pix.width, pix.height),
        pix.samples
    )

    return img


# ----------------------------------------------------------
# تبدیل PIL به OpenCV
# ----------------------------------------------------------

def pil_to_cv(img):

    return cv2.cvtColor(
        np.array(img),
        cv2.COLOR_RGB2BGR
    )


# ----------------------------------------------------------
# پیدا کردن محدوده نمودار
# ----------------------------------------------------------

def auto_crop(img):

    cv = pil_to_cv(img)

    gray = cv2.cvtColor(
        cv,
        cv2.COLOR_BGR2GRAY
    )

    _, th = cv2.threshold(
        gray,
        230,
        255,
        cv2.THRESH_BINARY_INV
    )

    contours, _ = cv2.findContours(
        th,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:

        return img

    best = None
    best_area = 0

    h, w = gray.shape

    for cnt in contours:

        x, y, ww, hh = cv2.boundingRect(cnt)

        area = ww * hh

        if area < 150000:
            continue

        if ww < w * 0.55:
            continue

        if hh < h * 0.25:
            continue

        if area > best_area:

            best_area = area
            best = (x, y, ww, hh)

    if best is None:

        return img

    x, y, ww, hh = best

    pad = 25

    x = max(0, x - pad)
    y = max(0, y - pad)

    ww = min(img.width - x, ww + pad * 2)
    hh = min(img.height - y, hh + pad * 2)

    return img.crop(
        (
            x,
            y,
            x + ww,
            y + hh
        )
    )


# ----------------------------------------------------------
# برش دستی
# ----------------------------------------------------------

def manual_crop(img):

    w, h = img.size

    return img.crop(

        (

            LEFT,

            TOP,

            w - RIGHT,

            min(BOTTOM, h)

        )

    )


# ----------------------------------------------------------
# ذخیره صفحه
# ----------------------------------------------------------

def save_chart(pdf_path, page_number):

    doc = fitz.open(pdf_path)

    page = doc.load_page(page_number - 1)

    img = render_page(page)

    if SAVE_FULL_PAGE:

        full = FULLPAGE_FOLDER / (

            pdf_path.stem +

            "_page" +

            str(page_number) +

            ".png"

        )

        img.save(full)

    if AUTO_CROP:

        img = auto_crop(img)

    else:

        img = manual_crop(img)

    name = get_persian_name(

        pdf_path.name,

        page_number

    )

    out = OUTPUT_FOLDER / (

        name + ".png"

    )

    img.save(out)

    print("✓", out.name)

    doc.close()
