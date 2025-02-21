import cv2 as a
import matplotlib.pyplot as b
import numpy as c
import os

output_directory = 'results'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

d = [[-2, -1], [-2, 0], [-2, 1],
     [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
     [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
     [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
     [2, -1], [2, 0], [2, 1]]

def main1(image, threshold):
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

def main2(image, d):
    row = image.shape[0]
    col = image.shape[1]
    new_image = c.zeros((row, col, 3))

    for i in range(row):
        for j in range(col):
            if image[i, j, 0] == 255:
                for k in d:
                    ki, kj = k
                    if ki + i >= 0 and ki + i < row and kj + j >= 0 and kj + j < col:
                        for m in range(3):
                            new_image[ki + i, kj + j, m] = 255
    return new_image

def main3(image, d, target):
    row = image.shape[0]
    col = image.shape[1]
    new_image = c.zeros((row, col, 3))
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

def main4(image, d):
    return main2(main3(image, d, 255), d)

def main5(image, d):
    return main3(main2(image, d), d, 255)

def main6(image, kernel_j, kernel_k):
    row = image.shape[0]
    col = image.shape[1]
    image_c = c.zeros((row, col, 3))
    image_out = c.zeros((row, col, 3))
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image[i, j, k] == 255:
                    image_c[i, j, k] = 0
                else:
                    image_c[i, j, k] = 255

    image = main3(image, kernel_j, 255)
    image_c = main3(image_c, kernel_k, 0)
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image[i, j, k] and image_c[i, j, k]:
                    image_out[i, j, k] = 255

    return image_out

a1 = a.imread('lena.bmp')
a.imshow('image_original', a1)
a.waitKey(0)
a_bin = main1(a1, 128)

a_dilation = main2(a_bin, d)
a.imwrite(os.path.join(output_directory, 'HW4_part(a)_image_dilation.jpg'), a_dilation)
a.imshow('image_dilation', a_dilation)
a.waitKey(0)

a_erosion = main3(a_bin, d, 255)
a.imwrite(os.path.join(output_directory, 'HW4_part(b)_image_erosion.jpg'), a_erosion)
a.imshow('image_erosion', a_erosion)
a.waitKey(0)

a_open = main4(a_bin, d)
a.imwrite(os.path.join(output_directory, 'HW4_part(c)_image_open.jpg'), a_open)
a.imshow('image_opening', a_open)
a.waitKey(0)

a_close = main5(a_bin, d)
a.imwrite(os.path.join(output_directory, 'HW4_part(d)_image_close.jpg'), a_close)
a.imshow('image_closing', a_close)
a.waitKey(0)

kj = [[-1, 0], [0, 0], [0, -1]]
kk = [[0, 1], [1, 1], [1, 0]]
a_hitandmiss = main6(a_bin, kj, kk)
a.imwrite(os.path.join(output_directory, 'HW4_part(e)_image_hit and miss.jpg'), a_hitandmiss)
a.imshow('image_hit and miss', a_hitandmiss)
a.waitKey(0)
a.destroyAllWindows()