import sys
import os
import cv2 as cv
import skimage
import numpy
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} image.jpg'.format(sys.argv[0]))
        sys.exit(1)
    input_img = sys.argv[1]
    
    img = cv.imread(input_img)
    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    ret,th = cv.threshold(img,0,255,cv.THRESH_BINARY_INV +cv.THRESH_OTSU)
    plt.imshow(th, cmap='gray')
    plt.show()

#    blur = cv.blur(th,(2,2))
#    blur = cv.medianBlur(th, 3)
#    plt.imshow(blur, cmap='gray')
#    plt.show()

#    cv.imwrite('blackwhite_test.jpg', blur)

    """

    kernel = np.ones((1,1),np.uint8)
    closing = cv.morphologyEx(th2, cv.MORPH_OPEN, kernel)
    plt.imshow(closing, cmap='gray')
    plt.show()


    
    edges = cv.Canny(th2, ret, ret2)
    plt.imshow(edges, cmap='gray')
    plt.show()


    lines = cv.HoughLines(edges,1,numpy.pi/180,43)
    # Draw lines on the image
    for line in lines:
        rho,theta = line[0]
        a = numpy.cos(theta)
        b = numpy.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    # Show result
    plt.imshow(img)
    plt.show()
    sys.exit()
    """
