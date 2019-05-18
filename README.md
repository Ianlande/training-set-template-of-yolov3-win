# training-set-template-of-yolov3-win
Darknet_windows的训练集模板以及使用方式，用于windows10系统

------

## 文件说明
`backup` : 训练得到的自动保存的权重文件  
`cfg` : 一些配置文件  
`data` : 训练集、验证集等各种数据  
`Image_origin` : 原始训练集  
`script` : 脚本文件，用于处理数据  

------

## 使用方法
##### 1. 将采集到的所有原始数据放到`Image_origin`文件夹中  
##### 2. 使用`script`文件夹下的`rename_img.py`将所有图片重命名，重命名后的图片会被放入`data\Images`文件夹中  
##### 3. 使用`labelimg`对图片打标签，并将所有`xml`文件放入`data\labels`中  
##### 4. 使用`script`文件夹下的`training_set_label.py`  
##### 5. 修改其它配置文件  

### `training_set_label.py`
其目的是为每一个图片的`xml`文件创建一个`txt`文件，并将其放入`data\Images`中，同时根据9:1的比例分配训练集与测试集

### 修改其它配置文件
##### `cfg`中的`training_set_template.cfg`
修改classes与filters，一共需要修改三处。如果检测A类物体，则classes=A，filters=(classess+5)*3=(A+5)*3

##### `cfg`中的`training_set_template_obj.data`
存放需要识别的类别数以及各种配置文件的路径

##### `data`中的`training_set_template_obj.names`
存放需要识别的类别种类，注意最后一行必须是一个回车键

## 补充
> * 你可能需要修改`script`中的脚本文件以便满足你的需要  
> * 这个包中并没有设置测试集，需要可以自行添加
> * 参考https://github.com/AlexeyAB/darknet
