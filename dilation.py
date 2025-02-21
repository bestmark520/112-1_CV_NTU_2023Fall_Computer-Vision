import numpy as np
from scipy.ndimage import binary_dilation

# 定義圖像A和元素B
image_A = np.array([[0, 0, 0],
                    [0, 1, 1],
                    [0, 0, 0]])

element_B = np.array([[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]])

# 使用二值膨脹操作
result = binary_dilation(image_A, structure=element_B).astype(int)

# 輸出結果
print("圖像A經過元素B膨脹後的結果：")
print(result)

import cv2

# 創建圖像A（5x5網格）
A = np.zeros((6, 5), dtype=np.uint8) # x, y顛倒，同圖片的定義
# 設置圖A中的黑點
A[1, 2] = 1
A[2, 2] = 1
A[3, 2] = 1
A[4, 2] = 1

# 創建kernel B（1x3網格）
B = np.array([[1, 0, 1]], dtype=np.uint8)

print("\n圖A:")
print(A)
print("\n圖B:")
print(B)

# 執行膨脹
A_dilated = cv2.dilate(A, B, iterations=1)

print("\n膨脹後的圖A:")
print(A_dilated)

