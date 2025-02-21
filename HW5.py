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

def main1(image, d):
    row = image.shape[0]
    col = image.shape[1]
    new_image = c.zeros((row, col))

    for i in range(row):
        for j in range(col):
            max_v = 0
            for k in d:
                ki, kj = k
                if ki + i >= 0 and ki + i < row and kj + j >= 0 and kj + j < col:
                    max_v = max(max_v, image[ki + i, kj + j])
            new_image[i, j] = max_v
    return new_image

def main2(image, d):
    row = image.shape[0]
    col = image.shape[1]
    new_image = c.zeros((row, col))
    for i in range(row):
        for j in range(col):
            min_v = 255
            for k in d:
                ki, kj = k
                if ki + i >= 0 and ki + i < row and kj + j >= 0 and kj + j < col:
                    min_v = min(min_v, image[ki + i, kj + j])
            new_image[i, j] = min_v
    return new_image

def main3(image, d):
    return main1(main2(image, d), d)

def main4(image, d):
    return main2(main1(image, d), d)

a1 = a.imread('lena.bmp', a.IMREAD_GRAYSCALE)
a.imshow('image_original', a1)
a.waitKey(0)

a_dilation = main1(a1, d)
b.imshow(a_dilation, cmap='gray') #設定圖片
b.title('image_dilation')
b.savefig(os.path.join(output_directory, 'HW5_part(a)_image_dilation.jpg'))
b.show()

a_erosion = main2(a1, d)
b.imshow(a_erosion, cmap='gray')
b.title('image_erosion')
b.savefig(os.path.join(output_directory, 'HW5_part(b)_image_erosion.jpg'))
b.show()

a_open = main3(a1, d)
#a.imshow('image_open', a_open) #無法用cv imshow
b.imshow(a_open, cmap='gray')
b.title('image_opening')
b.savefig(os.path.join(output_directory, 'HW5_part(c)_image_opening.jpg'))
b.show()

a_close = main4(a1, d)
b.imshow(a_close, cmap='gray')
b.title('image_closing')
b.savefig(os.path.join(output_directory, 'HW5_part(d)_image_closing.jpg'))
b.show()