# type: ignore
import colorgram, os

def extract_colors(image) -> tuple: 
    """
    Extract the most dominant colors from the given image, and returns a tuple
    Args:
        image (str): The path to the image file.
    """
    colors = colorgram.extract(image, 20)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

image_path = os.path.join(os.path.dirname(__file__), "image.jpg")

print(extract_colors(image_path))