# Graphic User Interface
# USED:
    # 1. https://docs.python.org/3/library/tkinter.html
    # 2. https://www.techtarget.com/whatis/definition/Fibonacci-sequence

# Necessary importers
import math
import tkinter as tk
import random

def mainScreen():
    '''
    mainScreen will display the following:
        1. Title name
        2. A quick description of what the fib sequence is
        3. A user input for the num of spirals they want

    NO parameters are required
    NO Return value
    '''
    
    top = tk.Tk() # Create a GUI window
    canvas = tk.Canvas(top, bg="#FFE9B6", height=500, width=500, name="fibonacci spiral generator") # Create a canvas
    
    # display "Welcome to the Fibonacci Spiral Generator" (1)
    label1 = tk.Label(canvas, justify="center",
                      text="Welcome to the Fibonacci Spiral",
                      font=("Georgia", 25, "bold"),
                      bg="#FFE9B6",
                      fg="black"
                      )
    label1.pack()
    canvas.create_window(30, 10, window=label1, anchor=tk.NW)
    
    # display a quick description of the fib sequence w/ the source below (2)
    '''
    source: https://www.techtarget.com/whatis/definition/Fibonacci-sequence
    '''
    label2 = tk.Label(canvas, 
                      text="The Fibonacci sequence is a set of integers\n that starts with a zero, followed by a one,\nthen by another one,"
                           "and then by a series of\nsteadily increasing numbers. The sequence follows the rule \nthat each number is equal to the sum of \nthe preceding two numbers!\n",
                      font=("Georgia", 16),
                      bg="#FFE9B6", 
                      fg="black"
                      )
    label2.pack()
    canvas.create_window(40, 50, window=label2, anchor=tk.NW)
    
    # display the user prompt to enter the number of spirals
    label3 = tk.Label(canvas,
                      text="Enter a number for the spiral:", 
                      font=("Georgia", 15, "bold"), 
                      bg="#FFE9B6", 
                      fg="black"
                      )
    
    label3.pack(side="left")
    canvas.create_window(250, 242, window=label3, anchor=tk.NW)
    
    # this is where the user will enter the number of spirals (3)
    entry1 = tk.Entry(top, bd=5)
    entry1.pack(side="right")
    
    # display the enter and quit buttons
    quitButton(canvas, top)
    enterButton(canvas, entry1)
    
    canvas.pack()
    top.mainloop()
    
    spiralGenerator(int(entry1.get()))


# displays the "enter" button
def enterButton(canvas, entry):
    '''
    enterButton will be used for once the user has passed in a number
    :param1, canvas --> the GUI canvas
    :param2, entry --> this is used so that we can store the users calue
    
    NO return value
    '''
    def checkEntry():
        '''
        checkEntry makes sure to handle the users input:
            1. NO negative values
            2. NO characters being passed in
            3. NO blank responses, i.e a num NEEDS to be passed-in
        '''
        
        value = entry.get()
        if value == '': # no blank responses
            label4["text"] = "Invalid, you must enter a number!"
        elif not value.isdigit(): # no charactesr, only integers
            label4["text"] = "Invalid, you must enter a valid integer!"
        elif int(value) <= 0: # greater than 0 (not including 0 too)
            label4["text"] = "Invalid, you must enter a number greater than 0!"
        else:
            label4["text"] = ""
            label5["text"] = f"Entered value: {value}"
        
        canvas.after(100, checkEntry)  # repeat the check after 100 milliseconds

    # create and display the ENTER button
    button = tk.Button(canvas, text="ENTER", command=checkEntry)
    canvas.create_window(250, 360, window=button)

    # Create the label for error messages
    label4 = tk.Label(canvas, text="", font=("Georgia", 15, "bold"), bg="#FFE9B6", fg="red")
    label5 = tk.Label(canvas, text="", font=("Georgia", 15, "bold"), bg="#FFE9B6", fg="green")
    canvas.create_window(180, 272, window=label4, anchor=tk.NW)
    canvas.create_window(180, 300, window=label5, anchor=tk.NW)


# displays the "quit" button and exits program
def quitButton(canvas, top):
    button = tk.Button(canvas, text="QUIT", command=top.quit)
    canvas.create_window(250, 400, window=button)


# creates a new window for spiral generator
def spiralGenerator(num):
    top2 = tk.Tk()  #  new window for the spiral generator
    canvas2 = tk.Canvas(top2, bg="#FFE9B6", height=1000, width=1000)  # new canvas for the spiral pattern

    # starting points for diff locations on the canvas
    x = 500 
    y = 400  
    radius = 2
    angle = 0  
    
    # USED: https://htmlcolorcodes.com to generate the cool red colors :)
    fill = ['#2E0703', '#420A04','#590D05', '#741107', '#851206', '#AB190A', '#C41908', '#DB1D0A','#F32915', '#3A0B07', '#510902', '#F0A49C']
    r_fill = random.randint(0, len(fill) - 1)
    for _ in range(num):
        x += radius * math.cos(math.radians(angle))
        y += radius * math.sin(math.radians(angle))
        
        canvas2.create_oval(x - radius, y - radius, x + radius, y + radius, fill=str(fill[r_fill]))  
        r_fill = random.randint(0, len(fill) - 1) # generates a new color
        
        # increase the size of radius + angle to create the fib sequence:
        radius += 10  
        angle += 30

    canvas2.pack()
    top2.mainloop()


if __name__ == "__main__":
    mainScreen()
