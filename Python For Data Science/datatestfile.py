import enum
from random import random


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
