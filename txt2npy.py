import numpy as np

# npy 输出地址
out_path = 'C:\\Users\\DELL\\Desktop\\smoke_detection\\smoke_image_test_data_output_file\\'

# 生成标签 npy 文件
res = []

# 添加元素
for i in range(135):
    res.append([1.0])

for i in range(135, 270):
    res.append([0.0])

# 转换为数组
res = np.array(res)

# 显示尺寸
print(res.shape)

# 数组存为 npy
np.save(out_path + "smoke_image_test_label.npy", res)