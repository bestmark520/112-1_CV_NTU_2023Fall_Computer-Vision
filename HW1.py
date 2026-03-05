import cv2 as cv
import os

output_directory = 'results'
if not os.path.exists(output_directory): os.makedirs(output_directory)

#part 1.(a) image upside down
def image_upside_down(image):
    row = image.shape[0] #image 高度
    col = image.shape[1] #image 寬度
    # image.shape -> (height, width, channels) # channels, 0 → 藍色通道, 1 → 綠色通道, 2 → 紅色通道
    half = row // 2
    for i in range(half):
        for j in range(col):
            for k in range(3): image[i,j,k], image[row - i -1, j, k] = image[row - i -1, j, k], image[i,j,k]
    return image

#part 1.(b) image right-side-left
def image_right_side_left(image):
    row = image.shape[0]
    col = image.shape[1]
    half = col // 2
    for i in range(row):
        for j in range(half):
            for k in range(3): image[i,j,k], image[i,col - 1 - j,k] = image[i,col - 1 - j,k], image[i,j,k]
    return image

#part 1.(c) diagonally flip
def image_diagonally_flip(image):
    #do right-side-left first and than upside down the image
    row = image.shape[0] #image 高度
    col = image.shape[1] #image 寬度
    half = row // 2
    for i in range(row):
        for j in range(half):
            for k in range(3): image[i,j,k], image[i,col - 1 - j,k] = image[i,col - 1 - j,k], image[i,j,k]
    for i in range(half):
        for j in range(col):
            for k in range(3): image[i,j,k], image[row - i -1, j, k] = image[row - i -1, j, k], image[i,j,k]
    return image

# show oringinal image
image = cv.imread('lena.bmp')
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(0)_image_original.jpg'), image)
cv.imshow('origianl image', image)
cv.waitKey(0)

# part 1.(a)
image_upside_down = image_upside_down(image)
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(a)_image_upside_down.jpg'), image_upside_down)
cv.imshow('HW1_part1.(a)_image_upside_down', image_upside_down)
cv.waitKey(0)

# part 1.(b)
image_right_side_left = image_right_side_left(image)
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(b)_image_right_side_left.jpg'), image_right_side_left)
cv.imshow('HW1_part1.(b)_image_right_side_left', image_right_side_left)
cv.waitKey(0)

# part 1.(c)
image_diagonally_flip = image_diagonally_flip(image)
cv.imwrite(os.path.join(output_directory, 'HW1_part1.(c)_image_diagonally_flip.jpg'), image_diagonally_flip)
cv.imshow('HW1_part1.(c)_image_diagonally_flip', image_diagonally_flip)
cv.waitKey(0)

# part 2.(d) rotate lena.bmp 45 degrees clockwise
row = image.shape[0]
col = image.shape[1]
center = (row / 2, col / 2)
matrix = cv.getRotationMatrix2D(center, 45, 1) #函式 cv.getRotationMatrix2D
image_rotated = cv.warpAffine(image, matrix, (row, col))
cv.imwrite(os.path.join(output_directory, 'HW1_part2.(d)_image_rotated.jpg'), image_rotated)
cv.imshow('HW1_part2.(d)_rotate lena.bmp 45 degrees clockwise', image_rotated)
cv.waitKey(0)

# part 2.(e) shrink lena.bmp in half
image_shrink = cv.resize(image, (row // 2, col // 2)) #函式 cv.resize
cv.imwrite(os.path.join(output_directory, 'HW1_part2.(e)_image_shrink.jpg'), image_shrink)
cv.imshow('HW1_part2.(e)_shrink lena.bmp in half', image_shrink)
cv.waitKey(0)

# part 2.(f) binarize lena.bmp at 128 to get a binary image
retVal, image_binarize = cv.threshold(image, 127, 255, cv.THRESH_BINARY) #函式 cv.threshold
cv.imwrite(os.path.join(output_directory, 'HW1_part2.(f)_image_binarize.jpg'), image_binarize)
cv.imshow('HW1_part2.(f)_binarize lena.bmp at 128 to get a binary image', image_binarize)
cv.waitKey(0)
