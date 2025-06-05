# Load and Resize Image

from PIL import Image

def load_image(image_path, new_width=100):

    # Open the Image
    img = Image.open(image_path)

    # Calculate Aspect Ratio
    aspect_ratio = img.height / img.width

    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, new_height))
    return img

# mapping pixels to ASCII characters

# First we need to convert the image to grayscale
# for that 

def convert_to_grayscale(img):
    return img.convert("L")

# next we have to map pixels 
def map_pixels_to_ASCII(img):
    ascii_chars = "@%#*+=-:."
    pixels = img.getdata()
    num_chars = len(ascii_chars)
    ascii_str = "".join([ascii_chars[pixel * (num_chars - 1) // 255] for pixel in pixels])
    return ascii_str


# Generating final ASCII Art
def generate_ascii_art(image_path, new_width=100):

    # Load and resize image 
    img = load_image(image_path, new_width)

    # Convert to Grayscale
    gray_image = convert_to_grayscale(img)

    # Map Pixels to ASCII
    ascii_str = map_pixels_to_ASCII(gray_image)

    # Format ASCII String into Rows
    ascii_art = "\n".join([ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width)])

    return ascii_art

def save_ascii_art(ascii_art, output_path):
    with open(output_path, "w") as file:
        file.write(ascii_art)

ascii_art = generate_ascii_art("indrajith1.JPG",50)
save_ascii_art(ascii_art, "final.txt")