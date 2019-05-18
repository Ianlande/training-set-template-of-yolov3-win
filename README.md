# training-set-template-of-yolov3-win
Darknet_windows的训练集模板以及使用方式

------

## 文件说明
`backup` : 训练得到的自动保存的权重文件
`cfg` : 一些配置文件
`data` : 训练集、测试集等各种数据
`Image_origin` : 原始训练集
`script` : 脚本文件，用于处理数据

------

## 使用方法
### 1. 将采集到的所有原始数据放到`Image_origin`文件夹中  
### 2. 使用`script`文件夹下的`rename_img.py`将所有图片重命名，重命名后的图片会被放入`data\Images`文件夹中
### 3. 使用`labelimg`对图片打标签，并将所有`xml`文件放入`data\labels`中


## 补充
> * 你可能需要修改`script`中的脚本文件以便满足你的需要
