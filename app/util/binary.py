from PIL import Image

def convert_to_grayscale(image):
    if image.mode != 'L':
        image = image.convert('L')
    return image

def convert_to_binary(image, threshold=128):
    if image.mode != 'L':
        image = convert_to_grayscale(image)
    
    width, height = image.size
    bin_image = Image.new('1', (width, height))
    
    for x in range(width):
        for y in range(height):
            gray_value = image.getpixel((x, y))
            bin_value = 1 if gray_value >= threshold else 0
            bin_image.putpixel((x, y), bin_value)
    
    return bin_image
