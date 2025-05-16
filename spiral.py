# import turtle

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(2)  # Moderate speed for visibility
# t.color("red")  # Outline color
# t.fillcolor("red")  # Fill color
# t.begin_fill()

# # Draw the left side of the heart
# t.left(140)  # Tilt for heart shape
# t.forward(111.65)  # Straight line length
# for _ in range(200):  # Left semicircle
#     t.right(1)
#     t.forward(1)
# t.left(120)  # Adjust angle for right side
# for _ in range(200):  # Right semicircle
#     t.right(1)
#     t.forward(1)
# t.forward(111.65)  # Complete the right side

# # End filling
# t.end_fill()

# # Hide turtle and display window
# t.hideturtle()
# turtle.exitonclick()

# import turtle

# # Set up the turtle
# t = turtle.Turtle()
# # t.speed(2)  # Moderate speed for visibility
# # t.color("blue")  # Outline color
# # t.fillcolor("blue")  # Fill color
# # t.begin_fill()

# # Draw a circle with radius 100
# t.circle(100)

# # End filling
# # t.end_fill()

# # Hide turtle and display window
# t.hideturtle()
# turtle.exitonclick()

# import turtle

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(3)  # Moderate speed for visibility

# # Draw the face (yellow circle)
# t.penup()
# t.goto(0, -100)  # Center the face
# t.pendown()
# t.color("black")  # Outline color
# t.fillcolor("yellow")  # Fill color
# t.begin_fill()
# t.circle(100)  # Radius 100
# t.end_fill()

# # Draw left eye
# t.penup()
# t.goto(-40, 20)  # Position for left eye
# t.pendown()
# t.fillcolor("black")
# t.begin_fill()
# t.circle(15)  # Smaller circle for eye
# t.end_fill()

# # Draw right eye
# t.penup()
# t.goto(40, 20)  # Position for right eye
# t.pendown()
# t.begin_fill()
# t.circle(15)  # Smaller circle for eye
# t.end_fill()

# # Draw smiling mouth
# t.penup()
# t.goto(-40, -20)  # Start of mouth
# t.pendown()
# t.setheading(-60)  # Curve downward
# t.circle(40, 120)  # Arc for smile

# # Hide turtle and display window
# t.hideturtle()
# turtle.exitonclick()

# import turtle

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(1)  # Slow speed for visibility
# t.color("red")  # Dot color

# # Draw a dot at (0, 0)
# t.penup()  # Ensure no line is drawn
# t.goto(0, 0)  # Move to (0, 0)
# t.dot(10)  # Draw a dot with size 10

# # Hide turtle and display window
# t.hideturtle()
# turtle.exitonclick()

# import tkinter as tk
# from tkinter import messagebox

# # Function to handle button click
# def add_numbers():
#     try:
#         num1 = float(entry1.get())
#         num2 = float(entry2.get())
#         result = num1 + num2
#         result_label.config(text=f"Result: {result}")
#     except ValueError:
#         messagebox.showerror("Error", "Please enter valid numbers!")

# # Create the main window
# window = tk.Tk()
# window.title("Simple Calculator")
# window.geometry("300x200")  # Set window size

# # Create and place widgets
# label1 = tk.Label(window, text="Enter first number:")
# label1.pack(pady=5)

# entry1 = tk.Entry(window)
# entry1.pack(pady=5)

# label2 = tk.Label(window, text="Enter second number:")
# label2.pack(pady=5)

# entry2 = tk.Entry(window)
# entry2.pack(pady=5)

# add_button = tk.Button(window, text="Add", command=add_numbers)
# add_button.pack(pady=10)

# result_label = tk.Label(window, text="Result: ")
# result_label.pack(pady=10)

# # Start the main event loop
# window.mainloop()



import numpy as np

ar=np.array([[4,6],[3,11]])

result=ar@ar

print(result)