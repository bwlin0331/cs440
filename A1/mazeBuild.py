import random
import sys
import math

#sets the ratio for number of blocked blocks in the maze
unblockedBias = 70
blockedBias = 100 - unblockedBias
weight_list = [1] * unblockedBias +  [0] * blockedBias

#of rows and columns
x_size = 101
y_size = 101

directory = "testcases/"
file_head = "testcase"

def randomPoint(x,y):
	return (random.randint(0,x-1),random.randint(0,y-1))


def create_testcase(version):
	try:
		filename = directory + file_head + str(version) + ".txt"
		f = open(filename, 'w')
	except FileNotFoundError:
		print ("Could not find the directory or file: " + filename)
		return

	start = randomPoint(x_size, y_size)
	goal = randomPoint(x_size, y_size)

	f.write(str(start[0]) + ',  ' + str(start[1]) + ', \n')
	f.write(str(goal[0]) + ', ' + str(goal[1]) + ', \n')

	#writes values per column
	for y in range(y_size):
		#writes values per row
		for x in range(x_size):
			val = random.choice(weight_list)
			f.write( str(val) + ', ')

		f.write('\n')

	f.close()

def create_testMASSIVE(version):
	try:
		filename = directory + file_head + str(version) + ".txt"
		f = open(filename, 'w')
	except FileNotFoundError:
		print ("Could not find the directory or file: " + filename)
		return
	x_size = 1001
	y_size = 1001
	#writes values per column
	for y in range(y_size):
		#writes values per row
		for x in range(x_size):
			val = random.choice(weight_list)
			f.write( str(val) + ', ')

		f.write('\n')

	f.close()

def test_to_array(version):
	try:
		filename = directory + file_head + version + ".txt"
		f = open(filename)
	except FileNotFoundError:
		print ("Could not find the file to open: " + filename)
		return

	#final 2d array
	maze = []
	#for each line in test case
	count = 0
	for line in f:
		if count < 2:
			count += 1
		else:
			temp = line.split(', ')
			temp = temp[:-1]
			temp = [int(i) for i in temp]
			maze.append(temp)

	return maze

def startPoint(version):
	try:
		filename = directory + file_head + version + ".txt"
		f = open(filename)
	except FileNotFoundError:
		print ("Could not find the file to open: " + filename)
		return

	temp = f.readline().split(', ')
	return (int(temp[0]), int(temp[1]))

def goalPoint(version):
	try:
		filename = directory + file_head + version + ".txt"
		f = open(filename)
	except FileNotFoundError:
		print ("Could not find the file to open: " + filename)
		return
	skip = f.readline()
	temp = f.readline().split(', ')
	return (int(temp[0]), int(temp[1]))

def main():
	# writing test cases - stored in directory labeled above
	for i in range(50):
		version = i+1
		create_testcase(version)

	# test_num = input("which test case number (1-50) would you like to run?  ")
	# print(test_to_array(test_num))
	#
	# print(startPoint('3'))
	# print(goalPoint('3'))
	# create_testcase(100)
	tasks = None


if __name__ == "__main__":
	main()
