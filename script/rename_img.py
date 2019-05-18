"""
used to rename images
"""
import os

img_path = "D:\\MyNetWork\\Vrep_yolov3_training\\Image_origin"
new_img_save_path = "D:\\MyNetWork\\Vrep_yolov3_training\\data\\Images"

filelist = os.listdir(img_path)
count = 0

"""
for file in filelist:
    count += 1
    print(file)
    print(count)
"""

for file in filelist:
    old_dir = os.path.join(img_path, file)
    print(old_dir)
    
    if os.path.exists(old_dir):
        filename = os.path.splitext(file)[0]
        filetype = os.path.splitext(file)[1]
        new_dir = os.path.join(new_img_save_path, str(count).zfill(6)+filetype)
        os.rename(old_dir, new_dir)
        print("saving: " + str(count).zfill(6)+filetype)
        count += 1
