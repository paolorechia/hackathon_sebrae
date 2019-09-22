import sys
import cv2 as cv
import skimage
import numpy
from scipy import stats
from matplotlib import pyplot as plt


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} image.jpg'.format(sys.argv[0]))
        sys.exit(1)
    input_img = sys.argv[1]
    
    bo, go, ro = (156, 238, 173)
    img = cv.imread(input_img)
#    plt.imshow(img)
#    plt.show()
    b = img[0][0][0]
    g = img[1][1][1]
    r = img[2][2][2]
    print(bo, go, ro)
    print(b, g, r)
    diff = (bo - b, go - g, ro - r)
    print(diff)
    test = (b + diff[0], g + diff[1], r + diff[2])
    img[:, :, 0] = img[:, :, 0] + diff[0]
    img[:, :, 1] = img[:, :, 1] + diff[1]
    img[:, :, 2] = img[:, :, 2] + diff[2]
    print(test)
#    plt.imshow(img)
#    plt.show()
    cv.imwrite('test_color_shift.jpg', img)

