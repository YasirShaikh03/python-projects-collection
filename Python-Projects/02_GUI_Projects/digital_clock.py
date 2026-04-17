from tkinter import Label, Tk
import time

# Create main window
clk_window = Tk()
clk_window.title("Digital Clk")
clk_window.geometry("420x150")
clk_window.resizable(1, 1)

# Styling
text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

# Create label inside the window
label = Label(clk_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

# Function to update time
def digital_clk():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clk)   # recall the same function

# Start the clock
digital_clk()
clk_window.mainloop()
