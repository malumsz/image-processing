from PIL import Image

def apply_mean_filter(img):
    gray_img = img.convert("L")
    mean_img = Image.new('L', img.size)

    for x in range(2, gray_img.width - 1):
        for y in range(2, gray_img.height - 1):
            gray = gray_img.getpixel((x, y))

            mean_value = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    mean_value += gray_img.getpixel((x + i, y + j))
            mean_value //= 9

            mean_img.putpixel((x, y), mean_value)

    return mean_img
