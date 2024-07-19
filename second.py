from os import listdir

from PIL import Image


def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    data = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            data.append(pixel[-1])
    binary_data = ''.join([str(bit) for bit in data])
    n = int(binary_data, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()


def is_image(image_path):
    try:
        Image.open(image_path)
        return True
    except:
        return False


def has_hidden_text(image_path):
    if not is_image(image_path):
        return False
    try:
        decode_image(image_path)
        return True
    except:
        return False


# from steganography import has_hidden_text

all, x = len(listdir("./gray/")), 0
for i in listdir("./gray/"):
    x += 1
    # print(f'{x}/{all}')
    if has_hidden_text(f'./gray/{i}'):
        print(f'{i} has in it !')
    else:
        pass
        # print('The image does not have hidden text in it.')

print("-----------------------")

all, x = len(listdir("./LSB/")), 0
for i in listdir("./LSB/"):
    x += 1
    # print(f'{x}/{all}')
    if has_hidden_text(f'./LSB/{i}'):
        print(f'{i} has in it !')
    else:
        pass
        # print('The image does not have hidden text in it.')