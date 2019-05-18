"""
将xml装成txt
"""

import xml.etree.ElementTree as ET
import pickle
import os
import random
from os import listdir, getcwd
from os.path import join

sets=['train','valid']

classes = ["target"]


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# 每一个xml文件转成txt文件
def convert_xml(image_id):
    # xml path
    in_file = open('D:\\MyNetWork\\Vrep_yolov3_training\\data\\labels\\%s.xml'%(image_id), 'r')
    # txt path
    out_file = open('D:\\MyNetWork\\Vrep_yolov3_training\\data\\Images\\%s.txt'%(image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# 生成一个列表储存所有图片的名称
filelist = os.listdir('D:\\MyNetWork\\Vrep_yolov3_training\\data\\Images')
filelist = [x.split('.')[0] for x in filelist]
filelist = list(set(filelist))
filelist.sort()
print(filelist)

# 先清空文件内容再重新写过
f = open('D:\\MyNetWork\\Vrep_yolov3_training\\data\\train.txt', "r+")
f.truncate()
f.close()
f = open('D:\\MyNetWork\\Vrep_yolov3_training\\data\\valid.txt', "r+")
f.truncate()
f.close()

for image_id in filelist:
    # 每一个xml文件转成txt文件
    convert_xml(image_id)
    # 按照9:1生成训练集和验证集
    temp = random.uniform(0,1)
    #print(temp)
    if temp <= 0.9:
        #print('0')
        file = open('D:\\MyNetWork\\Vrep_yolov3_training\\data\\train.txt' ,'a')
        file.write('D:\MyNetWork\\Vrep_yolov3_training\\data\\Images\\%s.jpg\n'%(image_id))
        file.close()
    else:
        #print('1')
        file = open('D:\\MyNetWork\\Vrep_yolov3_training\\data\\valid.txt' ,'a')
        file.write('D:\MyNetWork\\Vrep_yolov3_training\\data\\Images\\%s.jpg\n'%(image_id))
        file.close()



