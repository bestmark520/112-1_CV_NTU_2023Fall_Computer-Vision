import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

output_directory = 'results'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# (a) a binary image (threshold at 128)
def image_bin(image_to_process, value):
    row = image_to_process.shape[0]  # image 高度
    col = image_to_process.shape[1]  # image 寬度
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image_to_process[i, j, k] >= value:
                    image_to_process[i, j, k] = 255  # 設成白色
                else:
                    image_to_process[i, j, k] = 0  # 設成黑色
    return image_to_process

# (b) a histogram
def hist(image_to_process):
    hist_data = [0] * 256
    row = image_to_process.shape[0]  # image 高度
    col = image_to_process.shape[1]  # image 寬度
    for i in range(row):
        for j in range(col):
            hist_data[image_to_process[i, j, 0]] += 1
    plt.bar(range(0, 256), hist_data, color='black')
    plt.savefig(os.path.join(output_directory, 'HW2_part(b)_histogram_binary.jpg'))
    plt.show()

# (c) connected components use (a) result
def draw_rectangle(id):
    down = 0
    right = 0
    top = AAA
    left = AAA
    cen_i = []
    cen_j = []
    for i in range(AAA):
        for j in range(AAA):
            if (label_id[i, j] == id):
                cen_i.append(i)
                cen_j.append(j)
                if (i < top):
                    top = i
                elif (i > down):
                    down = i
                if (j < left):
                    left = j
                elif (j > right):
                    right = j
    cv.rectangle(aaa3, (left, top), (right, down), (0, 255, 0), 2)  # draw rectangle
    center_i = sum(cen_i) / len(cen_i)
    center_j = sum(cen_j) / len(cen_j)
    center_i = int(center_i)
    center_j = int(center_j)
    cv.line(aaa3, (center_j - 8, center_i), (center_j + 8, center_i), (0, 255, 0), 2)  # horizontal line
    cv.line(aaa3, (center_j, center_i - 8), (center_j, center_i + 8), (0, 255, 0), 2)  # vertical line

# Show original image
aaa = cv.imread('lena.bmp')
cv.imshow('original image', aaa)
cv.waitKey(0)

# (a) a binary image (threshold at 128)
aaa1 = cv.imread('lena.bmp')
binary_image = image_bin(aaa1, 128)
cv.imwrite(os.path.join(output_directory, 'HW2_part(a)_image_binary.jpg'), binary_image)
cv.imshow('image_binary', binary_image)
cv.waitKey(0)

# (b) a histogram
aaa2 = cv.imread('lena.bmp')
hist(aaa2)

# (c) connected components use (a) result
aaa3 = binary_image
AAA = aaa3.shape[0]  # image 高度
BBB = aaa3.shape[1]  # image 寬度

label_id = np.zeros((AAA, BBB), dtype=int)  # 紀錄label id
label_cnt = 1
for i in range(AAA):
    for j in range(BBB):
        if aaa3[i, j, 0] != 0:
            if (i == 0 and j == 0):  # origin
                label_id[i, j] = label_cnt
                label_cnt += 1
            elif (i == 0 and j != 0):  # first row
                if (label_id[i, j - 1]) != 0:
                    label_id[i, j] = label_id[i, j - 1]
                else:
                    label_id[i, j] = label_cnt
                    label_cnt += 1
            elif (i != 0 and j == 0):  # first column
                if (label_id[i - 1, j]) != 0:
                    label_id[i, j] = label_id[i - 1, j]
                else:
                    label_id[i, j] = label_cnt
                    label_cnt += 1
            else:  # other points
                if (label_id[i - 1, j] == 0 and label_id[i, j - 1] != 0):  # left is not zero
                    label_id[i, j] = label_id[i, j - 1]
                elif (label_id[i - 1, j] != 0 and label_id[i, j - 1] == 0):  # above is not zero
                    label_id[i, j] = label_id[i - 1, j]
                elif (label_id[i - 1, j] != 0 and label_id[i, j - 1] != 0):  # above and left are not zero
                    if (label_id[i - 1, j] == label_id[i, j - 1]):  # above and left are the same
                        label_id[i, j] = label_id[i, j - 1]
                    else:  # above and left are different
                        color_left = label_id[i, j - 1]
                        color_up = label_id[i - 1, j]
                        label_id[i, j] = color_left
                        for a in range(AAA):
                            for b in range(BBB):
                                if (label_id[a, b] == color_up):
                                    label_id[a, b] = color_left
                else:  # above and left are both zero
                    label_id[i, j] = label_cnt
                    label_cnt += 1

threshold = 500
area_cnt = np.zeros(AAA * BBB, dtype=int)
for i in range(AAA):
    for j in range(BBB):
        area_cnt[label_id[i, j]] += 1
area = []
for i in range(1, AAA * BBB):
    if (area_cnt[i] > 500):
        area.append(i)

for i in area:
    draw_rectangle(i)

cv.imwrite(os.path.join(output_directory, 'HW2_part(c)_image_connected components(regions with + at centroid, bounding box).jpg'), aaa3)
cv.imshow('connected components', aaa3)
cv.waitKey(0)