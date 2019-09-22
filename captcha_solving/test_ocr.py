try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2

# Simple image to string
image = cv2.imread('captcha_test.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imwrite('test.jpg', gray)

test = pytesseract.image_to_string(Image.open('test.jpg'))
print(test)
