#measure_of_edginess.py

#Daily Programmer Challenge #248.
#Edge detection of PPM image files.
#Problemset found here: https://www.reddit.com/r/dailyprogrammer/comments/3zqiiq/20160106_challenge_248_intermediate_a_measure_of/. PPMs used are also found there.


#SOBEL FILTER INCOMPLETE

import os
import sys
import mmap




#Using recommended Sobel method. Convert RGB to Grayscale first, averaging RGB values. 

#-----------------------------#
#    CONVERT TO GRAYSCALE     #
#-----------------------------#

f = open('test.ppm', 'r+')
rgb_ppm = f.readlines()
f.close()

tmp = "" #temporary storage for original PPMs conditions
tmp_ppm = []
for line in rgb_ppm:
    if len(line) <= 12:
        tmp = tmp + line
    else:
        for i in line.split():
            tmp_ppm.append(int(i))

tmp.replace("P3", "P2") #PPM Grayscale 
grayscale_ppm  = []
for i in range(0, len(tmp_ppm), 3):
    grayscale_ppm.append(sum(tmp_ppm[i:i+3])//3)

#Convert to string for write-to-file
grayscale_ppm_str = ' '.join(str(x) for x in grayscale_ppm)
#Divide into neat rows and columns


#write-to-file
f = open('test_gray.ppm', 'r+')
f.write(tmp+grayscale_ppm_str)
f.close()

#----------------------#
#    EDGINESS          #
#----------------------#

#Using Sobel Operator
#e_h = (c + 2*e + h) - (a + 2*d + f) #Edge Horiziontal
#e_v = (f + 2*g + h) - (a + 2*b  + c)#Edge Vertical

#Split into 3s to make it easier to calculate using matrices

sobel_ppm_calc = []
for i in range(0, len(grayscale_ppm), 3):
    sobel_ppm_calc.append(grayscale_ppm[i:i+3])


test = []
for i in range(0, len(sobel_ppm_calc), 4):
    test.append(sobel_ppm_calc[i:i+4])
    print(test)
