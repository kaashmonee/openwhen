    
from PIL import Image
import numpy as np

# def decode(input_file_path):
#     # your solution here!
#     img = Image.open(input_file_path).convert('RGB')
#     output_shape = (img.size[0] // 2, 1000)
#     img = np.array(img)

#     h, w = output_shape
#     result = np.zeros((h, w, 3), dtype=np.uint8)

#     cx, cy = img.shape[1] // 2, img.shape[0] // 2
#     for y in range(h):
#         for x in range(w):
#             # r = y * (img.shape[0] / h)
#             # theta = 2 * np.pi * x / w  # full circle for each row
#             # sx = int(cx + r * np.cos(theta))
#             # sy = int(cy + r * np.sin(theta))

#             # if 0 <= sx < img.shape[1] and 0 <= sy < img.shape[0]:
#             #     result[y, x] = img[sy, sx]
#                         # Calculate r and theta
#             # r = x
#             # theta = 2 * np.pi * (y - cy) / h  # Map y to [-pi, pi]
            
#             # # Apply inverse transformation (only cosine)
#             # sy = int(cy + r * np.cos(theta))
            
#             # if 0 <= sy < h:
#             #     result[y, x] = img[sy, x]
#                         # Calculate the vertical shift based on cosine
#             shift = int(h/2 * np.cos(2 * np.pi * x / w))
            
#             # Calculate the source y-coordinate
#             sy = (y + shift) % h
            
#             result[y, x] = img[sy, x]

#     return Image.fromarray(result)

def decode(input_file_path):
    img = Image.open(input_file_path).convert('RGB')
    img = np.array(img)
    
    h, w = img.shape[:2]
    result = np.zeros_like(img)
    
    for y in range(h):
        for x in range(w):
            # Calculate the source y-coordinate using a cosine function
            sy = int( h/2+ (h/2) * np.cos(8 * np.pi * x / w))
            
            # Ensure sy is within bounds
            sy = max(0, min(sy, h-1))
            
            # Copy the pixel from the source to the result
            result[y, x] = img[sy, x]
    
    return Image.fromarray(result)
    
input_file_path = "woodgrain.jpg"
decode(input_file_path).save("output.jpg")
