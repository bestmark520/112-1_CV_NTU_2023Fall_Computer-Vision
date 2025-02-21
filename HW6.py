import cv2 as a
import matplotlib.pyplot as b
import numpy as c

def main1(image_to_process, value):
    row = image_to_process.shape[0]
    col = image_to_process.shape[1]
    for i in range(row):
        for j in range(col):
            if image_to_process[i, j] >= value:
                image_to_process[i, j] = 255
            else:
                image_to_process[i, j] = 0
    return image_to_process

def main2(b, c, d, e):
    if b == c and (d != b or e != b):
        return 'q'
    if b == c and (d == b and e == b):
        return 'r'
    return 's'

def main3(image_to_process):
    dump_image = c.zeros((64, 64), dtype=int)
    row = dump_image.shape[0]
    col = dump_image.shape[1]
    for i in range(row):
        for j in range(col):
            dump_image[i, j] = image_to_process[8 * i, 8 * j]

    for i in range(row):
        for j in range(col):
            if dump_image[i, j] > 0:
                if i - 1 < 0 or j - 1 < 0:
                    x7 = 0
                else:
                    x7 = dump_image[i - 1, j - 1]
                if i - 1 < 0:
                    x2 = 0
                else:
                    x2 = dump_image[i - 1, j]
                if i - 1 < 0 or j + 1 >= col:
                    x6 = 0
                else:
                    x6 = dump_image[i - 1, j + 1]
                if j - 1 < 0:
                    x3 = 0
                else:
                    x3 = dump_image[i, j - 1]

                x0 = dump_image[i, j]

                if j + 1 >= col:
                    x1 = 0
                else:
                    x1 = dump_image[i, j + 1]
                if i + 1 >= row or j - 1 < 0:
                    x8 = 0
                else:
                    x8 = dump_image[i + 1, j - 1]
                if i + 1 >= row:
                    x4 = 0
                else:
                    x4 = dump_image[i + 1, j]
                if i + 1 >= row or j + 1 >= col:
                    x5 = 0
                else:
                    x5 = dump_image[i + 1, j + 1]

                a1 = main2(x0, x1, x6, x2)
                a2 = main2(x0, x2, x7, x3)
                a3 = main2(x0, x3, x8, x4)
                a4 = main2(x0, x4, x5, x1)

                if a1 == 'r' and a2 == 'r' and a3 == 'r' and a4 == 'r':
                    ans = 5
                    print(ans, end='')
                else:
                    ans = 0
                    for a in [a1, a2, a3, a4]:
                        if a == 'q':
                            ans += 1

                    if ans != 0:
                        print(ans, end='')
                    else:
                        print(' ', end='')

            else:
                print(' ', end='')

            if j == col - 1:
                print('')

image = a.imread('lena.bmp', a.IMREAD_GRAYSCALE)
image_bin = main1(image, 128)
result = main3(image_bin)
