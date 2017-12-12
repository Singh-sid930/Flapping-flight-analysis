
##### this program is to find the windows in the image with a given pixel density. The window can be defined of any 
##### any pixel by pixel dimansion. This script is useful for finding areas of high vibration in an image taken from 
##### rolling shutter cameras. For the example image, experimental flight images of birds is taken. 

################# Importing necessary libraries ############3333
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
#from numba import jit
 
 ################ reading thresholded image and finding the edges of the object ###########33

img = cv2.imread('img.jpg',0)
edges = cv2.Canny(img,100,200)
edge = 'edge'+'IMG_1956'+'.png'
cv2.imwrite(edge,edges)
cv2.imshow('image',edges)
cv2.waitKey(1000)
cv2.destroyAllWindows()

################# Initializing necessary variables ################################################

ans = []
yhdata = []
xhdata = []
yvdata = []
xvdata = []
x = 0
y = 0
dx = 0 
dy = 0
t = 0
d = 0

################### fnding the x and y coordinates of the edges ###############################################

edges = np.array(edges)
ans = np.nonzero(edges)
ans = np.array(ans)

##################### creating a density array which stores density of every window of the image ###############

density_array = np.zeros([(np.ceil(edges.shape[0]/30))+1,(np.ceil(edges.shape[1]/30))+1])
density_array = np.array(density_array)
# print(density_array.shape[0])
# print(density_array.shape[1])
# print(edges.shape[0])
# print(edges.shape[1])
for y in range(0,edges.shape[0],30): 		### creatng a 30 pixels by 30 pixels window #######
	for x in range(0,edges.shape[1],30):
		kernel = edges[y:y+30,x:x+30]
		if np.sum(kernel)>0:
			t = t+1
		den = np.count_nonzero(kernel)
		density = den/900.0					##### finding density in each window ############
		if density > 0:
			d = d+1
		density_array[dy,dx] = density
		dx = dx+1
	dx = 0
	dy = dy+1

######################### finding the coordinates of the density windows as per the rquirement ############

req_density = np.where(density_array>0.18) 	####### checking the windows which have densities greater than 0.18 ###
req_density = np.array(req_density)
xdata = req_density[1]
ydata = req_density[0]
# print(xdata)
# print(ydata)
# print(len(xdata))
# print(len(ydata))

###################### finding the coordinates of the windows in the image as per the density coordinates ##########

for x in range(len(xdata)):
	arrx = np.arange(xdata[x]*30,(xdata[x]*30)+30)
	# print(arrx)
	arrx = list(arrx)
	xhdata = xhdata + arrx
	xhdata = xhdata + arrx
xhdata = np.array(xhdata)
# print(xhdata)
# print(len(xhdata))

for y in range(len(ydata)):
	arry = (ydata[y]*30) * (np.ones(30))
	arry = list(arry)
	# print(arry)
	yhdata = yhdata + arry
	arry = ((ydata[y]*30)+30) * (np.ones(30))
	arry=list(arry)
	yhdata=yhdata+arry
yhdata=np.array(yhdata)
	# print("####################")

for y in range(len(ydata)):
	arry1=np.arange(ydata[y]*30,(ydata[y]*30)+30)
	# print(arrx)
	arry1=list(arry1)
	yvdata=yvdata+arry1
	yvdata=yvdata+arry1
yvdata=np.array(yvdata)
# print(yvdata)
# print(len(yvdata))

for x in range(len(xdata)):
	arrx1=(xdata[x]*30)*(np.ones(30))
	arrx1=list(arrx1)
	# print(arry)
	xvdata=xvdata+arrx1
	arrx1=((xdata[x]*30)+30)*(np.ones(30))
	arrx1=list(arrx1)
	xvdata=xvdata+arrx1
xvdata=np.array(xvdata)
# print(xvdata)
# print(len(xvdata))

########################### plotting the windows on the image ##################3

img = plt.imread("edgeIMG_1956.png")
fig,ax=plt.subplots()
ax.imshow(edges, extent=[0, edges.shape[1], edges.shape[0], 0], cmap="gray")
ax.plot(xhdata, yhdata, '.', linewidth=1, color='red')
ax.plot(xvdata, yvdata, '.', linewidth=1, color='red')

plt.show()
