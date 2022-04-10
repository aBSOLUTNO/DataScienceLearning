# Git commands. ls-> git init -> git add . -> git status -> 
# git commit - m "Commit" -> git push origin -> 
# git remote add origin 'your_url_name' -> git push -u origin master -> git reset --hard -> git pull





from gettext import find
from random import random
import pandas as pd


#Image process stuff.

from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm


# Working with XML code.

from lxml import objectify

xml = objectify.parse(open("XMLData.xml"))





# Getting the file from net.
example_file = ("http://upload.wikimedia.org/" + 
"wikipedia/commons/7/7d/Dog_face.png")

#Stores the image as gray in variable. And then shows it frm matplotlib.
image = imread(example_file, as_gray=True)

plt.imshow(image, cmap=cm.gray)
plt.show()

#Shows the data from image.
print("data type: %s, shape: %s" %(type(image), image.shape))

#Manipulating the image array. Cropping is essential so images are the same size.

image2 = image[5:70,0:70]
plt.imshow(image2, cmap=cm.gray)
plt.show()

#Resize image to specific size for anlysis.

image3 = resize(image2, (30,30))
plt.imshow(image3, cmap=cm.gray)
plt.show()

  
#Multiple images.

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(image, cmap=cm.gray)
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(image2, cmap=cm.gray)
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(image3, cmap=cm.gray)
plt.show()

#Flattenig images.

image_row = image3.flatten()
print(("data type: %s. shape: %s" % (type(image_row), image_row.shape)))




#Reading CSV formats. Reads ages from titanic.csv

titanic = pd.read_csv("titanic.csv")
x = titanic[['age']]
print(x)
(type(image_row), image_row.shape)




#Reading CSV formats. Reads ages from titanic.csv

titanic = pd.read_csv("titanic.csv")
x = titanic[['age']]
print(x)

#Reading Excel files.

xls = pd.ExcelFile("Values.xls")
trig_values = xls.parse('Sheet1', index_col=None, na_values=['NA'])

print(trig_values)


#Reading Excel files.

xls = pd.ExcelFile("Values.xls")
trig_values = xls.parse('Sheet1', index_col=None, na_values=['NA'])

print(trig_values)


#Loading all of the data in memory.
with open("Colors.txt", 'rb') as open_file:
    the_files = open_file
    print("Content of files:" + str(the_files.read()))


# Streaming data in pieces.
with open("Colors.txt", 'rb') as open_file:
    for observation in open_file:
        print("Reading data:" + str(observation))

#Sampling every other data.

n = 2
with open("Colors.txt", 'rb') as open_file:
    for j, observation_new in enumerate(open_file):
        if j % n==0:
            print('Reading Line:' + str(j) + 'Content:' + str(observation_new))


#Sampling random data.
sample_size = 0.25 # Basically a percentege which random selects from 0 - 1.
with open("Colors.txt", 'rb') as open_file:
    for j, newest_observation in enumerate(open_file):
        if random() <= sample_size:
            print ('Reading Line by random:' + str(j) + "Content : " + str(newest_observation))
