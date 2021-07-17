#https://www.w3schools.com/python/matplotlib_pyplot.asp
import numpy as np
import matplotlib.pyplot as plt

# create a 8x8 matrix of two numbers-0 and 1.
# O represents dark color and 1 represents bright color
arr=np.array([[1,0]*4,[0,1]*4]*4)
arr2=np.array([[1,1]*4,[1,1]*4]*4)
print(arr)
# use the imshow function to display the image made from the above array
plt.imshow(arr)
plt.colorbar()
plt.show()
plt.imshow(arr,origin="lower",cmap="gray",alpha=0.5)
# set the transparency to 0.5
# change the origin of the image from upper left to lower

plt.show()

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, marker = 'o',color = 'r')
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1,loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.grid()
plt.show()

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)  #  1 row, 2 columns, and this plot is the first plot.
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)# 1 row, 2 columns, and this plot is the second plot.
plt.plot(x,y)
plt.title("SALES")
plt.suptitle("MY SHOP")
plt.show()

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')

plt.show()


fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True,
                         figsize=(18, 18))
ax = axes.ravel()

ax[0].imshow(arr, cmap=plt.cm.gray)
ax[0].set_title('Original image')

ax[1].imshow(arr2, cmap=plt.cm.gray)
ax[1].set_title('Roberts Edge Detection')

ax[2].imshow(arr, cmap=plt.cm.gray)
ax[2].set_title('Sobel')

ax[3].imshow(arr2, cmap=plt.cm.gray)
ax[3].set_title('Scharr')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()