from tkinter import Tk, Canvas
import time
import math

# Create window
clk_win = Tk()
clk_win.title("CIRCLE CLOCK")
clk_win.geometry("400x400")
clk_win.resizable(0, 0)

# Canvas for drawing
canvas = Canvas(clk_win, width=400, height=400, bg="black")
canvas.pack()

center_x = 200
center_y = 200
radius = 150

# Draw clock circle
canvas.create_oval(center_x-radius, center_y-radius,
                   center_x+radius, center_y+radius,
                   outline="white", width=4)

# Draw hour marks
for i in range(12):
    angle = math.radians(i * 30)  # 360/12 = 30 degrees per hour
    x_inner = center_x + (radius-20) * math.sin(angle)
    y_inner = center_y - (radius-20) * math.cos(angle)
    x_outer = center_x + radius * math.sin(angle)
    y_outer = center_y - radius * math.cos(angle)
    canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill="white", width=3)

# Function to update clock hands
def update_clock():
    canvas.delete("hands")  # Remove previous hands

    t = time.localtime()
    sec = t.tm_sec
    minute = t.tm_min
    hour = t.tm_hour % 12

    # Calculate angles
    sec_angle = math.radians(sec * 6)  # 360/60
    min_angle = math.radians(minute * 6 + sec*0.1)  # smooth
    hour_angle = math.radians(hour * 30 + minute*0.5)  # smooth

    # Second hand
    x_sec = center_x + (radius-20) * math.sin(sec_angle)
    y_sec = center_y - (radius-20) * math.cos(sec_angle)
    canvas.create_line(center_x, center_y, x_sec, y_sec, fill="red", width=1, tag="hands")

    # Minute hand
    x_min = center_x + (radius-40) * math.sin(min_angle)
    y_min = center_y - (radius-40) * math.cos(min_angle)
    canvas.create_line(center_x, center_y, x_min, y_min, fill="white", width=3, tag="hands")

    # Hour hand
    x_hour = center_x + (radius-70) * math.sin(hour_angle)
    y_hour = center_y - (radius-70) * math.cos(hour_angle)
    canvas.create_line(center_x, center_y, x_hour, y_hour, fill="white", width=5, tag="hands")

    # Center dot
    canvas.create_oval(center_x-5, center_y-5, center_x+5, center_y+5, fill="white", tag="hands")

    canvas.after(200, update_clock)

update_clock()
clk_win.mainloop()
