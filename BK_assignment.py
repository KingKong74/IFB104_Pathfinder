
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment task for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2023.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#  Put your student number here as an integer and your name as a
#  character string:
#
student_number = 11557761
student_name   = 'Bailey King'
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assessment Task 1 Description----------------------------------#
#
#  This assessment task tests your skills at processing large data
#  sets, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function.  You are required to complete this
#  function so that when the program runs it fills a grid with various
#  symbols, using data stored in a list to determine which symbols to
#  draw and where.  See the online video instructions for
#  full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by a paying
#  "client".  This single template file will be used for all parts
#  and you will submit your final solution as this single Python 3
#  file only, whether or not you complete all requirements for the
#  assignment.
#
#  This file relies on other Python modules but all of your code
#  must appear in this file only.  You may not change any of the code
#  in the other modules and you should not submit the other modules
#  with your solution.  The markers will use their own copies of the
#  other modules to test your code, so your solution will not work
#  if it relies on changes made to any other files.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions used to execute your code.
# You must NOT change any of the code in this section, and you may
# NOT import any non-standard Python modules that need to be
# downloaded and installed separately.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer), aborting!\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string), aborting!\n')
    abort()

# Import the functions for setting up the drawing canvas
if isfile('assignment_1_config.py'):
    print('\nConfiguration module found ...\n')
    from assignment_1_config import *
else:
    print("\nCannot find file 'assignment_1_config.py', aborting!\n")
    abort()

# Define the function for generating data sets, using the
# imported raw data generation function if available, but
# otherwise creating a dummy function that just returns an
# empty list
if isfile('assignment_1_data_source.py'):
    print('Data generation module found ...\n')
    from assignment_1_data_source import raw_data
    def data_set(new_seed = randint(0, 99999)):
        print('Using random number seed', new_seed, '...\n')
        seed(new_seed) # set the seed
        return raw_data() # return the random data set
else:
    print('No data generation module available ...\n')
    def data_set(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own function and any other functions needed to support it.
#  All of your solution code must appear in this section.  Do NOT put
#  any of your code in any other sections and do NOT change any of
#  the provided code except as allowed by the comments in the next
#  section.
#

# All of your code goes in, or is called from, this function.
# Make sure that your code does NOT call function data_set (or
# raw_data) because it's already called in the main program below.
boobs = [[0, 3, 'South east'],
        [1, 'Move & turn left'],
         [2, 'Move forward'],
         [3, 'Move & turn left'],
         [4, 'Move & turn left'],
         [5, 'Move forward']]

def visualise_data(something):

    #speed('slowest')
    
    # Follow direction from random seed 
    for data in something:


        # Define the all possible directions
        N= 90
        NE = 30
        NW = 150
        SE = 330
        S = 270
        SW = 210

        # Defining width of the cell
        cell_len = 104
        
        # Extract the parts of the dataset
        energy = something[0][1]
        command = data[1]
        facing = data[-1]
        sequence = data[0]

        # Floating point tolerance
        tolerance = 0.3
      
        # 'if' statements for intial direction
        if facing == 'North':
            direction = N
        elif facing == 'North east':
            direction = NE
        elif facing == 'North west':
            direction = NW
        elif facing == 'South east':
            direction = SE
        elif facing == 'South':
            direction = S
        elif facing == 'South west':
            direction = SW
        
        # Draw spooder
        whole_spider(xcor(), ycor(), direction)
        delay(50)
        
        # 'if' statements for  movement
        if command == 'Move forward':
            forward(cell_len)
        elif command == 'Move & turn left':
            forward(cell_len)
            direction = direction + 60
        elif command == 'Move & turn right':
            forward(cell_len)
            direction = direction - 60

        # 'if stamements hitting a special cell
        # H2
        if abs(xcor() - (270.20)) < tolerance and abs(ycor() - (51.99)) < tolerance:
            whole_spider(xcor(), ycor(), direction)
            goto(0,280)
            write(f"The Spider has gone down the waterspout on move {sequence}" , align = "center", font = ("bold", 25))
            break
        # D8
        if abs(xcor() - (-90.06)) < tolerance and abs(ycor() - (156.00)) < tolerance:
            whole_spider(xcor(), ycor(), direction)
            goto(0,280)
            write(f"The Spider has gone down the waterspout on move {sequence}" , align = "center", font = ("bold", 25))
            break
        # A3
        if abs(xcor() - (-360.27)) < tolerance and abs(ycor() - (-103.99)) < tolerance:
            whole_spider(xcor(), ycor(), direction)
            goto(0,280)
            write(f"The Spider has gone down the waterspout on move {sequence}" , align = "center", font = ("bold", 25))
            break

        # 'if' statements for leaving the grid
        if ycor() > 260:
            goto(0,280)
            write(f"The Spider took off in the wind after move {sequence}" , align = "center", font = ("bold", 25))
            break
        elif ycor() < -260:
            goto(0,280)
            write(f"The Spider took off in the wind after move {sequence}" , align = "center", font = ("bold", 25))
            break
        if xcor() > 405:
            goto(0,280)
            write(f"The Spider took off in the wind after move {sequence}" , align = "center", font = ("bold", 25))
            break
        if xcor() < -405:
            goto(0,280)
            write(f"The Spider took off in the wind after move {sequence}" , align = "center", font = ("bold", 25))
            break
        
        # Draw spooder
        whole_spider(xcor(), ycor(), direction)
        tracer(False)
        delay(50)
       

        # 'if' statments for amount of moves
        if sequence >= energy:
            goto(0,280)
            write(f"The Spider was exhausted after move {energy}" , align = "center", font = ("bold", 25))
            break
        


           

speed("fastest")

#create_drawing_canvas(canvas_title = "Spider goes down the water spout", write_instructions = False)

# Draw a hexagon
def hexagon():
    
    tracer(False)
    
    penup()
    setheading(90)
    backward(51)
    right(90)
    forward(30)
    pendown()

    color("black")

    begin_fill()
    fillcolor("turquoise")
    for i in range(6):
   
        left(60)
        forward(60.5)
    end_fill()
    
    penup()
    left(90)
    forward(51)
    left(90)
    forward(30)
    setheading(0)
    pendown()

    #tracer(True)

# Define functions for spider anatomy

def spider_rightside_leg(spider_leg_length = 25):
    color("black")
    
    right(40)
    forward(spider_leg_length)
    left(30)
    forward(30)

    up() # Tracing back to 0,0

    backward(30)
    right(30)
    backward(spider_leg_length)

    down()

    right(20)
    forward(spider_leg_length)
    left(20)
    forward(20)

    up()

    backward(20)
    right(20)
    backward(spider_leg_length)
    right(45)

    down()

    forward(spider_leg_length)
    left(30)
    forward(15)

    up()

    backward(15)
    right(30)
    backward(spider_leg_length)

    down()

    right(45)
    forward(spider_leg_length + 5)
    right(30)
    forward(15)

    up()

    backward(15)
    left(30)
    backward(spider_leg_length)

    down()

def spider_leftside_leg(spider_leg_length = 25):
    
    forward(spider_leg_length)
    right(30)
    forward(30)

    up() # Tracing back

    backward(30)
    left(30)
    backward(spider_leg_length)

    down()

    left(20)
    forward(spider_leg_length)
    right(20)
    forward(20)

    up()

    backward(20)
    left(20)
    backward(spider_leg_length)
    left(45)

    down()

    forward(spider_leg_length)
    right(30)
    forward(15)

    up()

    backward(15)
    left(30)
    backward(spider_leg_length)

    down()

    left(45)
    forward(spider_leg_length + 5)
    left(30)
    forward(15)

    up()

    backward(15)
    right(30)
    backward(spider_leg_length)

    down()

def spider_body(radius = 13):
    begin_fill()
    circle(radius)
    end_fill()

def spider_head(radius = 9):
    begin_fill()
    circle(radius)
    color('black')
    end_fill()

def spider_pattern():
    begin_fill()
    color('red')
    forward(8)
    right(135)
    forward(12)
    right(135)
    forward(8)
    right(135)
    forward(12)
    right(135)
    forward(8)
    
def label_4_setheading(direction):
    up()
    setheading(direction)
    forward(80)

def spider_pattern(straight = 10, across = 14):
    begin_fill()
    color('red')
    forward(8)
    right(135)
    forward(across)
    left(135)
    forward(straight)
    left(135)
    forward(across)
    right(135)
    forward(straight)
    end_fill()   
    
def whole_spider(x, y, direction):
    color("black")
    goto(x, y)
    hexagon()
    setheading(direction)
    spider_rightside_leg()

    # Reset back to centre
    right(120)
    forward(2.5)
    right(90)
    forward(4.33)
    left(40)

    # Back to drawing board
    spider_leftside_leg()

    # Reset & turn east 
    left(30)
    backward(4.33)
    left(90)
    forward(2.50)

    # Set up for body
    left(90)
    forward(4)
    left(90)
    spider_body()

    # Set up for head
    right(90)
    forward(9)
    left(90)
    spider_head()

    # Back pattern
    left(90)
    forward(17)
    left(90)
    backward(3)
    spider_pattern()

    # re-centre the turtle
    backward(5.20)
    left(90)
    forward(4)

    # Change colour for writing
    color('black')

    up()
    tracer(True)
    
    

# Setheadings
N = 90
NE = 30
NW = 150
SE = 330
S = 270
SW = 210


# DRAW SPIDERs
up()
whole_spider(550, 200, N)
label_4_setheading(270)
write("North", align = "center", font = "bold")

whole_spider(550, 0, NE)
label_4_setheading(270)
write("North-East", align = "center", font = "bold")


whole_spider(550, -200, SE)
label_4_setheading(270)
write("South-East", align = "center", font = "bold")

whole_spider(-550, 200, S)
label_4_setheading(270)
write("South", align = "center", font = "bold")

whole_spider(-550, 0, SW)
label_4_setheading(270)
write("South-West", align = "center", font = "bold")

whole_spider(-550, -220, NW)
label_4_setheading(270)
write("North-West", align = "center", font = "bold")

goto(0,0)
#
#--------------------------------------------------------------------#



#-----Main Program to Run Student's Solution-------------------------#
#
# This main program configures the drawing canvas, calls the student's
# function and closes the canvas.  Do NOT change any of this code
# except as allowed by the comments below.  Do NOT put any of
# your solution code in this section.
#

# Configure the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(canvas_title = "Spider goes down the water spout", write_instructions = False)

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "data_set" function with a fixed seed below for the
# ***** random number generator, but your final solution must
# ***** work with "data_set()" as the function call,
# ***** i.e., for any random data set that can be returned by
# ***** the function when called with no seed
visualise_data(data_set()) # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Do not change this function call
release_drawing_canvas(student_name)

#
#--------------------------------------------------------------------#
