import random
import sys
import math

#sets the ratio for number of blocked blocks in the maze
unblockedBias = 70
blockedBias = 100 - unblockedBias
weight_list = [0] * unblockedBias +  [1] * blockedBias

#of rows and columns
x_size = 10 
y_size = 10

directory = "tests/"
file_head = "test"


def create_testcase(version):
	f = open(directory + file_head + str(version) + ".txt", 'w')

	#writes values per column
	for y in range(y_size):
		#writes values per row
		for x in range(x_size):
			val = random.choice(weight_list)
			f.write( str(val) + ', ')
		
		f.write('\n')

	f.close()

def test_to_array(version):
	filename = directory + file_head + version + ".txt"
	f = open(filename)

	#final 2d array
	maze = []
	#for each line in test case
	for line in f:
		temp = line.split(', ')
		temp = temp[:-1]
		temp = [int(i) for i in temp]
		maze.append(temp)

	return maze

def main():
# 	for i in range(50):
# 		version = i+1
# 		create_testcase(version)

	test_num = input("which test case number (1-50) would you like to run?  ")
	print(test_to_array(test_num))



if __name__ == "__main__":
	main()