import cv2 
import matplotlib.pyplot as Plt 
from pylab import rcParams 
import pytesseract 
rcParams[ 'figure . figsize' ]=8,16 
filename="./image.png" 
img=cv2. imread(filename) 
print( 'The Image is : ' )
Plt.imshow(cv2. cvtColor(img,cv2.COLOR_BGR2RGB) )
string = pytesseract.image_to_string(img)
print(string)
