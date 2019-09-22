try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2

# Simple image to string
test = pytesseract.image_to_string(Image.open('duh.jpeg'))
print(test)
print(pytesseract.image_to_data(Image.open('processed.jpg')))

