Samuel Yang - sy369
Brian Lin - bwl25

Assignment 1

The main program that runs the visual interface for the user is pathFinder.py.  
Pygame must be installed in order for the program to run properly.  Open a command
terminal and run python pathFinder.py.  The program will then ask for a test case
number from 1-50.

All test cases are in the testcases directory, and labeled from 1- 50.  The test cases
store the gridworlds as 0 or 1 to represent each cell.  At the beginning of each file
there are two sets of points, one that correlates to the start point and one to the
goal point.  These test cases were built using the mazeBuild.py program.

The tests.py function was used to generate and record data of the various A* variants
and wrote them into various labeled directories under the data directory.  The computation
time of each iteration of A* was recorded until the agent reached the target.  This
data was stored in a csv file and then combined into a single data.csv document in the
main directory using a function in the tests.py.  That data was then used to generate charts
for the report.  

The report for this assignment was generated using LaTeX, and all relevant files for the
report are found in the report directory.  Data recorded in the csv format was converted
to strings so that they could be input into the LaTeX document in a table format using
convert.py and is written into the toLatex.txt.  The repository can be found online for this
assignment at: (A1)

https://www.github.com/samuel-yang/cs440
