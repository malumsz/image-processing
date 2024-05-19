from PIL import Image

def apply_median_filter(img):
    gray_img = img.convert("L")
    median_img = Image.new('L', img.size)

    for x in range(2, gray_img.width - 1):
        for y in range(2, gray_img.height - 1):
            gray = gray_img.getpixel((x, y))

            pixels = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixels.append(gray_img.getpixel((x + i, y + j)))
            pixels.sort()
            median_value = pixels[4]

            median_img.putpixel((x, y), median_value)

    return median_img
