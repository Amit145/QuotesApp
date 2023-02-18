import os
import textwrap
import random
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

inputFolder = "images/"
fontType = "fonts/Arial.ttf"
list1 = [1, 2, 3, 4, 5]


def create_image(quote):
    if len(quote) <= 50:
        current_h, pad = 225, 25
        para = textwrap.wrap(quote, width=25)
        # print(len(col))
    if 51 <= len(quote) <= 100:
        current_h, pad = 210, 25
        para = textwrap.wrap(quote, width=25)
        # print(len(col))
    if 101 <= len(quote) <= 150:
        current_h, pad = 175, 25
        para = textwrap.wrap(quote, width=30)
        # print(len(col))
    if 151 <= len(quote) <= 180:
        current_h, pad = 150, 25
        para = textwrap.wrap(quote, width=30)
        # print(len(col))
    if 181 <= len(quote) <= 200:
        current_h, pad = 125, 15
        para = textwrap.wrap(quote, width=30)
        # print(len(col))
    if 201 <= len(quote) <= 250:
        current_h, pad = 100, 15
        para = textwrap.wrap(quote, width=30)
        # print(len(col))

    img_count = random.choice(list1)
    img = Image.open(inputFolder + str(img_count) + ".jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontType, 30)

    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((600 - w) / 2, current_h), line, font=font)
        current_h += h + pad

    image_name = f'output_image/{time.time_ns()}.jpg'
    print(image_name)
    img.save(image_name)
    return os.path.abspath(image_name), image_name
