import os, sys
from PIL import Image

size_75 = (75,75)
counter = 1
os.mkdir('./new_images')

for f in os.listdir('./images'):
    #outfile = os.path.splitext(f)[0] + ".png"
    if f.endswith(".jpg"):
        # try:
            i = Image.open(f)
            i = i.convert("L")
            i = i.crop((0,0,75,75))
            i = i.transpose(Image.ROTATE_270)
            outfile = "./new_images/pic" + str(counter).zfill(4) + ".png"            
            i.save(outfile,"PNG")
            counter+=1
            # print(i.size)
        # except IOError:
        #     print("ERRLIN SUCKS")