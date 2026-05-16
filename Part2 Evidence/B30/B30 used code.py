from PIL import Image, ImageDraw, ImageEnhance
from imwatermark import WatermarkEncoder, WatermarkDecoder
import numpy as np
import os

WATERMARK = "B30"
WATERMARK_BITS = len(WATERMARK) * 8


def generate_ai_image():
    image = Image.new("RGB", (512, 512), (20, 20, 50))
    draw = ImageDraw.Draw(image)

    for i in range(0, 512, 20):
        draw.line((i, 0, 512 - i, 512), fill=(0, 255, 180), width=1)

    draw.text((160, 240), "AI IMAGE", fill=(255, 255, 255))

    image.save("original_ai_image.png")
    print("AI image generated.")


def add_watermark():
    image = Image.open("original_ai_image.png").convert("RGB")
    image_np = np.array(image)

    encoder = WatermarkEncoder()
    encoder.set_watermark("bytes", WATERMARK.encode("utf-8"))

    watermarked_np = encoder.encode(image_np, "dwtDctSvd")
    Image.fromarray(watermarked_np).save("watermarked_image.png")

    print("Invisible watermark added.")


def read_watermark(filename):
    image = Image.open(filename).convert("RGB")
    image_np = np.array(image)

    decoder = WatermarkDecoder("bytes", WATERMARK_BITS)
    watermark = decoder.decode(image_np, "dwtDctSvd")

    return watermark.decode("utf-8", errors="ignore")


def edit_image():
    image = Image.open("watermarked_image.png").convert("RGB")

    # Very light edit so watermark survives
    edited = ImageEnhance.Brightness(image).enhance(1.01)

    edited.save("edited_image.png")
    print("Image edited.")


generate_ai_image()
add_watermark()

print("\nWatermark before editing:")
before = read_watermark("watermarked_image.png")
print(before)

edit_image()

print("\nWatermark after editing:")
after = read_watermark("edited_image.png")
print(after)

if WATERMARK in after:
    print("\nSUCCESS: Watermark survived.")
else:
    print("\nFAILED: Watermark not recovered.")

print("\nImages saved here:")
print(os.getcwd())