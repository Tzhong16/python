var1 = [1, 2, 3, 4]
var2 = True

print(type(var1))

print(len(var1))

out2 = int(var2)

help(complex)

max()
len()


#string method
room = "poolhouse"

room_up = room.upper()

print(room_up)
print(room)

print(room.count("o"))

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

print(areas.index(20.0))
print(areas.count(14.5))

areas.append(24.5)
areas.append(15.45)

print(areas)

areas.reverse()

print(areas)

#calculate circumference and area
r = 0.43
import math
C = 2 * math.pi * r

A = math.pi * r **2

print("Circumference: " + str(C))
print("Area: " + str(A))


#Calculate the distance travelled by the Moon over 12 degrees of its orbit
r = 192500

from math import radians

# Travel distance of Moon if 12 degrees
dist = r * radians(12)

print(dist)

# Numpy arrays contain only one type


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

import numpy as np

np_baseball = np.array(baseball)

print(type(np_baseball))

# calculate BMI

import numpy as np

np_height = np.array(height)
print(np_height)

np_height_m = np_height * 0.0254

np_weight_kg = np.array(weight) * 0.453592

bmi = np_weight_kg / np_height_m ** 2

print(bmi)

light = bmi < 21

print(light)

print(bmi[light])

#sub-array 
print(np_weight[50])

print(np_height[100:111])


#2D numpy array
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

import numpy as np

np_baseball = np.array(baseball)

print(type(np_baseball))
print(np_baseball.shape)

#subsetting 2D Numpy arrays

np_baseball = np.array(baseball)

print(np_baseball[49, :])

np_weight = np_baseball[:, 1]

print(np_baseball[123, 0])

# arithmetic

np_baseball = np.array(baseball)

print(np_baseball + update)

conversion = np.array([0.0254, 0.453592, 1])

print(np_baseball * conversion)

#Basic statistics in numpy

np_height = np.array(np_baseball[:, 0])

print(np.mean(np_height))

print(np.median(np_height))

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("Correlation: " + str(corr))

#compare the median hights between GK position and other position
np_heights = np.array(heights)
np_positions = np.array(positions)


gk_heights = np_heights[np_positions == 'GK']

other_heights = np_heights[np_positions != 'GK']

print("Median height of goalkeepers: " + str(np.median(gk_heights)))

print("Median height of other players: " + str(np.median(other_heights)))
