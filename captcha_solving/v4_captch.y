import sys
import os
import cv2 as cv
import skimage
import numpy
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt


def remove_composite_color(img, threshold=50, color0=0, color1=1):
    channel0 = img[:, :, color0]
    channel1 = img[:, :, color1]

    new_channel0 = []
    new_channel1 = []
    for i, row0 in enumerate(channel0):
        new_row1 = []
        new_row0 = []
        row1 = channel1[i]
        for j, px0 in enumerate(row0):
            px1 = row1[j]
            new_px = -1
            if px0 > px1:
                diff = px0 - px1
            else:
                diff = px1 - px0
            if diff < threshold:
                new_px = 0
            if new_px == 0:
                new_row0.append(new_px) 
                new_row1.append(new_px) 
            else:
                new_row0.append(px0)
                new_row1.append(px1)
        new_channel0.append(numpy.array(new_row0))
        new_channel1.append(numpy.array(new_row1))
    new_np_channel0 = numpy.array(new_channel0)
    new_np_channel1 = numpy.array(new_channel1)
    img[:, :, color0] = new_np_channel0
    img[:, :, color0] = new_np_channel1
    return img

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} image.jpg'.format(sys.argv[0]))
        sys.exit(1)
    input_img = sys.argv[1]
    
    img = cv.imread(input_img)

    img = cv.GaussianBlur(img, (3, 3), 0)
    plt.imshow(img, cmap='gray')
    plt.show()

    """
    img = cv.medianBlur(img, 3)
    plt.imshow(blur, cmap='gray')
    plt.show()
    """

    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    plt.imshow(img, cmap='gray')
    plt.show()
    ddepth = cv.CV_8U


    img = cv.Laplacian(img, ddepth, ksize=3)

    ret,th = cv.threshold(img,0,255,cv.THRESH_BINARY_INV +cv.THRESH_OTSU)
    plt.imshow(th, cmap='gray')
    plt.show()

#    blur = cv.blur(th,(2,2))

    cv.imwrite('blackwhite_test.jpg', blur)

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
