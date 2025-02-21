import cv2 as cv
import numpy as np
import os

output_directory = 'results'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

#part 1.(a) image upside down
def image_upside_down(image_to_process):
    row = image_to_process.shape[0] #image 高度
    col = image_to_process.shape[1] #image 寬度
    half = row // 2
    for i in range(half):
        for j in range(col):
            for k in range(3):
                image_to_process[i,j,k], image_to_process[row - i -1, j, k] = image_to_process[row - i -1, j, k], image_to_process[i,j,k]
    return image_to_process

#part 1.(b) image right-side-left
def image_right_side_left(image_to_process):
    row = image_to_process.shape[0] #image 高度
    col = image_to_process.shape[1] #image 寬度
    half = col // 2
    for i in range(row):
        for j in range(half):
            for k in range(3):
                image_to_process[i,j,k], image_to_process[i,col - 1 - j,k] = image_to_process[i,col - 1 - j,k], image_to_process[i,j,k]
    return image_to_process

#part 1.(c) diagonally flip
def image_diagonally_flip(image_to_process):
    #do right-side-left first and than upside down the image
    row = image_to_process.shape[0] #image 高度
    col = image_to_process.shape[1] #image 寬度
    half = row // 2
    for i in range(row):
        for j in range(half):
            for k in range(3):
                image_to_process[i,j,k], image_to_process[i,col - 1 - j,k] = image_to_process[i,col - 1 - j,k], image_to_process[i,j,k]
    for i in range(half):
        for j in range(col):
            for k in range(3):
                image_to_process[i,j,k], image_to_process[row - i -1, j, k] = image_to_process[row - i -1, j, k], image_to_process[i,j,k]
    return image_to_process

#show oringinal image
image = cv.imread('lena.bmp')
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(0)_image_original.jpg'), image)
cv.imshow('origianl image', image)

cv.waitKey(0)

#part 1.(a)
image1 = cv.imread('lena.bmp')
image_upside_down = image_upside_down(image1)
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(a)_image_upside_down.jpg'), image_upside_down)
cv.imshow('image upside down', image_upside_down)
cv.waitKey(0)

#part 1.(b)
image2 = cv.imread('lena.bmp')
image_right_side_left = image_right_side_left(image2)
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(b)_image_right_side_left.jpg'), image_right_side_left)
cv.imshow('image right-side-left', image_right_side_left)
cv.waitKey(0)

#part 1.(c)
image3 = cv.imread('lena.bmp')
image_diagonally_flip = image_diagonally_flip(image3)
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(c)_image_diagonally_flip.jpg'), image_diagonally_flip)
cv.imshow('image diagonally flip', image_diagonally_flip)
cv.waitKey(0)