import cv2 as cv
import numpy as np
import os

output_directory = 'results'
if not os.path.exists(output_directory): os.makedirs(output_directory)

d = [[-2, -1], [-2, 0], [-2, 1],
     [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
     [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
     [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
     [2, -1], [2, 0], [2, 1]]

def binarize(image, threshold):
    row = image.shape[0]
    col = image.shape[1]
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image[i, j, k] >= threshold:
                    image[i, j, k] = 255
                else:
                    image[i, j, k] = 0
    return image

def dilation(image, d):
    row = image.shape[0]
    col = image.shape[1]
    new_image = np.zeros((row, col, 3))

    for i in range(row):
        for j in range(col):
            if image[i, j, 0] == 255:
                for k in d:
                    ki, kj = k
                    if ki + i >= 0 and ki + i < row and kj + j >= 0 and kj + j < col:
                        for m in range(3):
                            new_image[ki + i, kj + j, m] = 255
    return new_image

def erosion(image, d, target):
    row = image.shape[0]
    col = image.shape[1]
    new_image = np.zeros((row, col, 3))
    if target == 0:
        for i in range(row):
            for j in range(col):
                for k in range(3):
                    new_image[i, j, k] = 255
    for i in range(row):
        for j in range(col):
            if image[i, j, 0] == target:
                for k in d:
                    ki, kj = k
                    flag = 1
                    if ki + i < 0 or ki + i >= row or kj + j < 0 or kj + j >= col or image[ki + i, kj + j, 0] != target:
                        flag = 0
                        break
                if flag == 1:
                    for m in range(3):
                        new_image[ki + i, kj + j, m] = target
    return new_image

# 先侵蝕後膨脹
def opening(image, d): return dilation(erosion(image, d, 255), d)

# 先膨脹後侵蝕
def closing(image, d): return erosion(dilation(image, d), d, 255)

def hit_and_miss(image, kernel_j, kernel_k):
    row = image.shape[0]
    col = image.shape[1]
    image_c = np.zeros((row, col, 3))
    image_out = np.zeros((row, col, 3))
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image[i, j, k] == 255:
                    image_c[i, j, k] = 0
                else:
                    image_c[i, j, k] = 255

    image = erosion(image, kernel_j, 255)
    image_c = erosion(image_c, kernel_k, 0)
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image[i, j, k] and image_c[i, j, k]:
                    image_out[i, j, k] = 255

    return image_out

a1 = cv.imread('lena.bmp')
cv.imshow('image_original', a1)
cv.waitKey(0)
a_bin = binarize(a1, 128)

a_dilation = dilation(a_bin, d)
cv.imwrite(os.path.join(output_directory, 'HW4_part(a)_image_dilation.jpg'), a_dilation)
cv.imshow('image_dilation', a_dilation)
cv.waitKey(0)

a_erosion = erosion(a_bin, d, 255)
cv.imwrite(os.path.join(output_directory, 'HW4_part(b)_image_erosion.jpg'), a_erosion)
cv.imshow('image_erosion', a_erosion)
cv.waitKey(0)

a_open = opening(a_bin, d)
cv.imwrite(os.path.join(output_directory, 'HW4_part(c)_image_open.jpg'), a_open)
cv.imshow('image_opening', a_open)
cv.waitKey(0)

a_close = closing(a_bin, d)
cv.imwrite(os.path.join(output_directory, 'HW4_part(d)_image_close.jpg'), a_close)
cv.imshow('image_closing', a_close)
cv.waitKey(0)

kj = [[-1, 0], [0, 0], [0, -1]]
kk = [[0, 1], [1, 1], [1, 0]]
a_hitandmiss = hit_and_miss(a_bin, kj, kk)
cv.imwrite(os.path.join(output_directory, 'HW4_part(e)_image_hit and miss.jpg'), a_hitandmiss)
cv.imshow('image_hit and miss', a_hitandmiss)
cv.waitKey(0)
cv.destroyAllWindows()
