# type: ignore
import colorgram

def extract_colors(image, num_of_colors: int) -> tuple: 
    """
    Extract the most dominant colors from the given image, and returns a tuple
    Args:
        image (str): The path to the image file.
    """
    colors = colorgram.extract(image, num_of_colors)
    return [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

