import cv2
import numpy as np
from PIL import Image
import io

def preprocess_image(image_bytes):
    """Preprocess image for better OCR results"""
    image = Image.open(io.BytesIO(image_bytes)).convert("L")  # Convert to grayscale
    image = np.array(image)

    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Adaptive Thresholding
    threshold = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Dilation (Expands text edges)
    kernel = np.ones((2, 2), np.uint8)
    dilated = cv2.dilate(threshold, kernel, iterations=1)

    return Image.fromarray(dilated)  # Convert back to PIL Image

if __name__ == "__main__":
    print("Preprocessing module is working!")
