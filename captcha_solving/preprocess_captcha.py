import sys
import cv2 as cv
import skimage
import numpy
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

#    cv.imshow('image',img)
#    cv.waitKey(0)

#    imshow(img)
    def remove_peaks(img, threshold=50, filter_=None, nth_max=1, peak=True,\
                     colors=[0,1,2]):
        color = ('r','g','b')
#        for color in [0, 1, 2]:
        for color in colors:
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

            print(color, max_value, lower_bound, upper_bound)
            def filter_(val, max_value, threshold, peak):
                print(val, max_value, threshold, peak, lower_bound, upper_bound)
                if peak:
                    if val > lower_bound and val < upper_bound:
                        val = 0
                else:
                    if val < lower_bound or val > upper_bound:
                        val = 0
                print(val)
                return val

            channel = img[:, :, color]
            np_rows=[]
            for row in channel:
                new_row = []
                for px in row:
                    px = filter_(px, max_value, threshold, peak)
                    new_row.append(px)
                np_rows.append(numpy.array(new_row))
            new_blue  = numpy.array(np_rows)
            img[:, :, color] = new_blue
        return img


    img = remove_peaks(img, threshold=1, nth_max=1, peak=True, colors=[2])
    img = remove_peaks(img, threshold=50, nth_max=5, peak=False, colors=[0])
    img = remove_composite_color(img, color0=0, color1=1)
#    img[:,:,1]=0
#    img[:,:,2]=0
#    plt.imshow(img, cmap='gray')
#    plt.show()

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#    ret2,th2 = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV +cv.THRESH_OTSU)
    ret2,th2 = cv.threshold(gray,10,255,cv.THRESH_BINARY_INV)
    plt.imshow(th2, cmap='gray')
    plt.show()

#    for row in blue_channel:
#        print(px)

#    print(blue_channel)
#    print(stats.mode(blue_histr))
#    plt.plot(blue_histr, color = 'b')
#    plt.xlim([0,256])
    #for i,col in enumerate(color):
#    plt.show()

