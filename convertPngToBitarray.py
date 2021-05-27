import cv2
import numpy as np
import sys

def negate(x):
    if x == 255:
        return 0
    else:
        return 1
    
def display_img(img,title):
    print(f"{title}: {img}")
    cv2.imshow(title,img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()

def bit_arr_to_int(bit_arr):
    if len(bit_arr) != 8:
        print("Bit array must be 8 long")
    res = 0
    for i,bit in enumerate(bit_arr):
        res += bit * (2**i)
    return res

img = cv2.imread(sys.argv[1],0)
print(f"Shape of image: {img.shape}")
display_img(img,'og')

img = np.vectorize(negate)(img)

print('{')
for i in range(8):
    page = '\t{'
    for j in range(128):
        page+= hex(bit_arr_to_int(img[i*8:(i+1)*8,j]))+','
    page = page[:-1]
    page += '}'
    page += ',' if i != 7 else ''
    print(page)
print('}')
