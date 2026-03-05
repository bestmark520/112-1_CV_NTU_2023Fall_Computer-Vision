import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

output_directory = 'results'
if not os.path.exists(output_directory): os.makedirs(output_directory)

# (a) a binary image (threshold at 128)
def image_bin(image, threshold):
    row = image.shape[0]  # image 高度
    col = image.shape[1]  # image 寬度
    for i in range(row):
        for j in range(col):
            for k in range(3):
                if image[i, j, k] >= threshold: image[i, j, k] = 255  # 設成白色
                else: image[i, j, k] = 0  # 設成黑色
    return image

# (b) a histogram
def hist(image):
    hist_data = [0] * 256 # 圖的x軸是像素值範圍是 0 ~ 255 # y軸是出現的次數
    row = image.shape[0]  # image 高度
    col = image.shape[1]  # image 寬度
    for i in range(row):
        for j in range(col): hist_data[image[i, j, 0]] += 1
    plt.bar(range(0, 256), hist_data, color='black')
    plt.savefig(os.path.join(output_directory, 'HW2_part(b)_histogram_binary.jpg'))
    plt.show()

# (c) connected components use (a) result
def connected_components(image, min_area=500):
    """
    Find connected components in a binary image, draw bounding boxes and centroid (+).
    image: binary image (3 channels)
    min_area: minimum number of pixels to consider a component
    """
    height = image.shape[0]   # 圖像高度
    width = image.shape[1]    # 圖像寬度

    # 1. 建立 label 矩陣
    labels = np.zeros((height, width), dtype=int)
    current_label = 1

    for row in range(height):
        for col in range(width):
            if image[row, col, 0] != 0:  # 只看前景像素
                label_above = labels[row - 1, col] if row > 0 else 0
                label_left  = labels[row, col - 1] if col > 0 else 0

                if label_above == 0 and label_left == 0:
                    labels[row, col] = current_label
                    current_label += 1
                elif label_above != 0 and label_left == 0:
                    labels[row, col] = label_above
                elif label_above == 0 and label_left != 0:
                    labels[row, col] = label_left
                else:  # label_above != 0 and label_left != 0
                    if label_above == label_left:
                        labels[row, col] = label_above
                    else:
                        # 合併不同 label
                        label_to_keep = label_left
                        label_to_merge = label_above
                        labels[row, col] = label_to_keep
                        labels[labels == label_to_merge] = label_to_keep

    # 2. 計算每個 label 面積
    max_possible_labels = height * width
    area_count = np.zeros(max_possible_labels, dtype=int)
    for row in range(height):
        for col in range(width):
            area_count[labels[row, col]] += 1

    # 3. 畫 bounding box + centroid
    for component_id in range(1, max_possible_labels):
        if area_count[component_id] >= min_area:
            rows, cols = np.where(labels == component_id)
            top, bottom = rows.min(), rows.max()
            left, right = cols.min(), cols.max()

            # 畫 bounding box
            cv.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

            # 計算 centroid
            center_row = int(np.mean(rows))
            center_col = int(np.mean(cols))

            # 畫十字
            cv.line(image, (center_col - 8, center_row), (center_col + 8, center_row), (0, 255, 0), 2)
            cv.line(image, (center_col, center_row - 8), (center_col, center_row + 8), (0, 255, 0), 2)

    return image

# Show original image
image = cv.imread('lena.bmp')
cv.imshow('original image', image)
cv.waitKey(0)

# (a) a binary image (threshold at 128)
binary_image = image_bin(image, 128)
cv.imwrite(os.path.join(output_directory, 'HW2_part(a)_image_binary.jpg'), binary_image)
cv.imshow('image_binary', binary_image)
cv.waitKey(0)

# (b) a histogram
image = cv.imread('lena.bmp')
hist(image)

# (c) connected components use (a) result
image = connected_components(binary_image)
cv.imwrite(os.path.join(output_directory, 'HW2_part(c)_image_connected components(regions with + at centroid, bounding box).jpg'), image)
cv.imshow('connected components', image)
cv.waitKey(0)
