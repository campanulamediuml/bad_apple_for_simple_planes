from PIL import Image
import os
from multiprocessing import Pool

def get_matrix_for_pixel(pic_object):
    return 0

result_matrix = []

for i in range(8,324):
    img = Image.open('pictures/'+str(i)+'.jpg')
    pix = img.load()
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
            matrix_line.append(result)
    pic_matrix.append(matrix_line)
result_matrix.append(pic_matrix)

print result_matrix
            
