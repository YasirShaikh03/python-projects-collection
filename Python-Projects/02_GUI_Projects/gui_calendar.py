import tkinter as tk
from tkcalendar import Calendar

# Create window
root = tk.Tk()
root.title("Calendar")
root.geometry("300x300")

# Calendar widget
cal = Calendar(
    root,
    selectmode="day",
    year=2026,
    month=1,
    day=11
)
cal.pack(pady=20)

# Function to get date
def get_date():
    selected_date = cal.get_date()
    label.config(text="Selected Date: " + selected_date)

# Button
btn = tk.Button(root, text="Get Date", command=get_date)
btn.pack(pady=10)

# Label
label = tk.Label(root, text="")
label.pack()

root.mainloop()
