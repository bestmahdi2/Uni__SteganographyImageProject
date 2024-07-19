import random
from os import listdir

from PIL import Image


def hide_text_in_grayscale_image(image, text):
    """Hides text in a grayscale image using LSB Steganography.

    Args:
      image: A PIL Image object in grayscale.
      text: The text to hide in the image.

    Returns:
      A PIL Image object in grayscale with the text hidden in it.
    """

    # Convert the text to a byte array.
    text_bytes = bytearray(text, encoding='utf-8')

    # Get the dimensions of the image.
    width, height = image.size

    # Create a list to store the random pixel positions.
    random_pixel_positions = []
    for i in range(len(text_bytes)):
        # Generate a random pixel position.
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        # Add the random pixel position to the list.
        random_pixel_positions.append((x, y))

    # Iterate over the random pixel positions and hide the text in the image.
    for i in range(len(random_pixel_positions)):
        # Get the pixel value at the random pixel position.
        pixel = image.getpixel(random_pixel_positions[i])

        # Get the least significant bit of the pixel value.
        lsb = pixel & 1

        # Replace the least significant bit of the pixel value with the next bit of the text.
        pixel = (pixel & ~1) | (text_bytes[i] & 1)

        # Set the pixel value at the random pixel position.
        image.putpixel(random_pixel_positions[i], pixel)

    # Return the image with the text hidden in it.
    return image


def save_image(image, filename):
    """Saves an image to a file.

    Args:
      image: A PIL Image object.
      filename: The filename to save the image to.
    """

    image.save(filename)


if __name__ == '__main__':
    message = """In this era of digital revolution and continuous technological advancement, bots, otherwise known as web robots or Internet bots, have established a significant role across numerous domains. From digital marketing to entertainment, from customer service to cybersecurity, these artificial software agents know how to make their place indispensable.

Bots are basically software applications that run automated tasks over the Internet. They can perform these tasks at an infinitely higher speed than humans, making them incredibly efficient. Bots were initially designed to perform repetitive tasks, much like assembly line robots. However, today they are capable of much more.

There are several types of bots, each designed for a specified function or a range of functions. The most common examples include web crawlers, chatbots, malicious bots, trading bots, and social bots.

Web crawlers are also known as spider bots that travel through the World Wide Web, collecting and indexing information about websites."""

    all, x = len(listdir("./gray/")), 0
    for i in listdir("./gray/"):
        x += 1
        print(f'{x}/{all}')
        # Load the image.
        image = Image.open(f'./gray/{i}').convert('L')

        # Hide the text in the image.
        hidden_image = hide_text_in_grayscale_image(image, message)

        # Save the image with the text hidden in it.
        save_image(hidden_image, f'./LSB/{i}')
