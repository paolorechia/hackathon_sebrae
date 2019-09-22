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
    
    img = cv.imread(input_img)

#    cv.imshow('image',img)
#    cv.waitKey(0)

#    imshow(img)
    def remove_peaks(img, threshold=50, filter_=None, nth_max=1, sign=True):
        color = ('b','g','r')
        for color in [0, 1, 2]:
            histr = cv.calcHist([img],[color],None,[256],[0,256])
            flatten = histr.flatten()
            sorted_ = numpy.sort(flatten)
            most_freq = sorted_[-nth_max]
            print(most_freq)
            max_idx = numpy.where(histr == most_freq)
#            max_idx = numpy.where(histr == max(histr))
            max_value = max_idx[0][0]
            lower_bound = max_value - threshold
            upper_bound = max_value + threshold

            def filter_(val, max_value, threshold, sign):
                if sign:
                    if val < lower_bound:
                        val = 0
                    if val > upper_bound:
                        val = 0
                else:
                    if val > lower_bound:
                        val = 0
                    if val < upper_bound:
                        val = 0
                return val
               

            print(color, max_value, lower_bound, upper_bound)
            channel = img[:, :, color]
            np_rows=[]
            for row in channel:
                new_row = []
                for px in row:
                    px = filter_(px, max_value, threshold, sign)
                    new_row.append(px)
                np_rows.append(numpy.array(new_row))
            new_blue  = numpy.array(np_rows)
            img[:, :, color] = new_blue
        return img

    img = remove_peaks(img, threshold=50, nth_max=1, sign=True)
#    img = remove_peaks(img, threshold=100, nth_max=2, sign=False)
    plt.imshow(img, cmap='gray')
    plt.show()

#    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#    ret2,th2 = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV +cv.THRESH_OTSU)
#    gray = cv
#    plt.imshow(th2, cmap='gray')
#    plt.show()

#    for row in blue_channel:
#        print(px)

#    print(blue_channel)
#    print(stats.mode(blue_histr))
#    plt.plot(blue_histr, color = 'b')
#    plt.xlim([0,256])
    #for i,col in enumerate(color):
#    plt.show()

