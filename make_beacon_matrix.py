#coding=utf-8
from PIL import Image
import os
from multiprocessing import Pool
import bad_apple_matrix
import time



def get_pic_matrix():
    result_matrix = []
    for i in range(6,324):
        img = Image.open('pictures/'+str(i)+'.jpg')
        # 从第六帧开始读取
        pix = img.load()
        # 加载图片
        width = img.size[0]
        height = img.size[1]
        pic_matrix = []
        for y in range(0,height,33):
            matrix_line = []
            for x in range(0,width,33):
                if sum(pix[x,y]) < 381:
                    result = 0
                else:
                    result = 1
        # 对每一个像素进行分析。黑色为0，白色为1
                matrix_line.append(result)
            pic_matrix.extend(matrix_line)
        result_matrix.append(pic_matrix)
    return result_matrix
    # 组成一个图像矩阵，每个元素为一张图片矩阵，图片矩阵内每个元素为一行


def get_time_matrix(result_matrix):
    time_matrix = []
    for index in range(0,1200):
        pixel_time_matrix = []
        for pic in result_matrix:
            pixel_time_matrix.append(pic[index])
        time_matrix.append(pixel_time_matrix)
    return time_matrix
    # 傅里叶变换，把图像信息从空间转化为时间矩阵
            
        

def cal_time_by_line(pixel_array):
    result_matrix = []
    start_pixel = pixel_array[0]
    
    # if pixel_array[0] != 1:
    #         result_matrix = [0]


    start_index = 0
    pixel_time_sheet = []
    temp = 0
    while 1:
        count = 0
        for i in range(start_index,318):
            if pixel_array[i] == start_pixel:
                count += 1
                start_index += 1
            else:
                start_pixel = pixel_array[i]
                count = 0
                tmp = start_index - temp
                # print tmp
                temp = start_index
                break

        if start_index == 318:
            break
        pixel_time_sheet.append(tmp*3)
        # print pixel_time_sheet
        # time.sleep(0.5)
    result = result_matrix + pixel_time_sheet
    if sum(result) < 951:
        result = result + [950-sum(result),1]
    if len(result)%2 != 0:
        result = result+[0]
    return result



time_matrix = bad_apple_matrix.matrix
# print time_matrix[0]
# print time_matrix[-1]

# print time_matrix[600]
result = []
for i in time_matrix:
    result.append(cal_time_by_line(i))
# print result
# print result
# for i in result:
#     if len(i)%2 != 0:
#         print i

# time_length = []

# for i in result:
#     time_length.append(sum(i))
    
# print list(set(time_length))

# fh = open('/Users/JingjingHe/Library/Application Support/unity.Jundroo.SimplePlanes/AircraftDesigns/bad_apple.xml','w')
# fh.close()

# xml_head = '''<?xml version="1.0" encoding="utf-8"?>
# <Aircraft name="bad_apple" url="" theme="Default" size="150,1.645,100" boundsMin="-75,1.733354,-50" xmlVersion="6">
#   <Assembly>
#     <Parts>
#         <Part id="1" partType="Fuselage-Body-1" position="-1.907349E-06,2.233355,1.907349E-06" rotation="0,0,0" drag="392.6389,392.6389,15003.95,15003.95,343.7867,342.9735" materials="13" scale="150,1,100" massScale="1">
#         <FuelTank.State fuel="0" capacity="0" />
#         <Fuselage.State version="2" frontScale="2,2" rearScale="2,2" offset="0,0,2" deadWeight="0" buoyancy="1" fuelPercentage="0" cornerTypes="0,0,0,0,0,0,0,0" />
#       </Part>
#       <Part id="2" partType="Cockpit-4" position="-1.907349E-06,2.473356,-12.5" rotation="0,0,0" drag="0,0,0,0,0,0" materials="7,0,1" scale="1,1,1" massScale="1">
#         <Cockpit.State primaryCockpit="True" />'''


# for x in range(0,40)
#     part_content = '''
#     </Part>
#         <Part id="'''+str(i+3)+'''" partType="BeaconLight" position="63.875,2.733355,0" rotation="0,0,0" drag="0,0,0.7739998,0.7739998,0.7739998,0.7739999" materials="14,0" scale="10,10,10" massScale="0">
#         <BeaconLight.State activationGroup="0" designerBlinkProgram="Quick Blink" input="None" showHalo="true" />
#     </Part>
#       '''



