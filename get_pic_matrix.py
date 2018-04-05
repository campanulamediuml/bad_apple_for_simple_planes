from PIL import Image
import os
from multiprocessing import Pool

try:
    os.mkdir('matrix')
except:
    pass


golang_headers = '''
package constants

var Pic_constant'''

fh = open('constants/constants.go','w')
fh.write(golang_headers+' = [318][33][65]int64 {\n')

print len(range(6,324))
for i in range(6,324):
    img = Image.open('pictures/'+str(i)+'.jpg')
    pix = img.load()
    width = img.size[0]
    height = img.size[1]
    
    fh.write('{')
    count_y = 0
    for y in range(0,height,33):
        count_y += 1
        fh.write('{')
        count_x = 0
        for x in range(0,width,33):
            count_x+=1
            if sum(pix[x,y]) < 381:
                result = 0
            else:
                result = 1
            fh.write(str(result)+',')
        # print count_x
        fh.write('},\n')
    fh.write('},\n')
    # print count_x
    # print count_y
fh.write('}\n')
print count_x
print count_y
    #         count_x += 1
    #     # print count_x
    #     count_y += 1
    # print count_x
    # print count_y
    # print count_y
#         fh.write()









            

