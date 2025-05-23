
from PIL import Image
import numpy as np

def decode(input_file_path):
    # your solution here!
    img = Image.open(input_file_path).convert('RGB').rotate(-90)
    output_shape = (img.size[0] // 2, 1000)
    img = np.array(img)

    h, w = output_shape
    result = np.zeros((h, w, 3), dtype=np.uint8)

    # cx, cy = img.shape[1] // 2, img.shape[0] // 2
    cx, cy = 0 , 0

    for y in range(h):
        for x in range(w):
            r = y * (img.shape[0] // h)
            theta = 2 * np.pi * x / w  # full circle for each row
            sx = int(x + r * np.cos(theta))
            sy = int(0 + r * np.sin(theta))

            if 0 <= sx < img.shape[1] and 0 <= sy < img.shape[0]:
                result[y, x] = img[sy, sx]

    return Image.fromarray(result)

input_file_path = "woodgrain.jpg"
decode(input_file_path).save("output.jpg")

    
