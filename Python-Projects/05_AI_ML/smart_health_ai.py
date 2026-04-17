import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import numpy as np

# ---------------- FOOD DATABASE ----------------

FOOD_CALORIES = {
    "chapati":120, "plain rice":200, "chicken biryani":450,
    "dal":180, "samosa":250, "idli":60,
    "burger":300, "pizza":285, "fries":350,
    "apple":95, "banana":110, "salad":80
}

def get_calorie(food):
    return FOOD_CALORIES.get(food.lower(), 200)

# ---------------- BMR ----------------

def bmr(weight, height, age):
    return int(10*weight + 6.25*height - 5*age + 5)

def exercise_plan(cal):
    if cal < 150:
        return "20 min walking"
    if cal < 300:
        return "30 min jogging"
    if cal < 500:
        return "45 min cardio"
    return "1 hour HIIT"

# ---------------- POSTURE CHECK ----------------

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
              np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180/np.pi)
    if angle > 180:
        angle = 360 - angle
    return angle

def start_posture():
    cap = cv2.VideoCapture(0)
    status = "UNKNOWN"

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if result.pose_landmarks:
            lm = result.pose_landmarks.landmark

            hip = [lm[mp_pose.PoseLandmark.LEFT_HIP].x,
                   lm[mp_pose.PoseLandmark.LEFT_HIP].y]
            knee = [lm[mp_pose.PoseLandmark.LEFT_KNEE].x,
                    lm[mp_pose.PoseLandmark.LEFT_KNEE].y]
            ankle = [lm[mp_pose.PoseLandmark.LEFT_ANKLE].x,
                     lm[mp_pose.PoseLandmark.LEFT_ANKLE].y]

            knee_angle = calculate_angle(hip, knee, ankle)

            if knee_angle < 100:
                status = "GOOD SQUAT"
                color = (0,255,0)
            else:
                status = "WRONG POSTURE"
                color = (0,0,255)

            mp_draw.draw_landmarks(img, result.pose_landmarks,
                                   mp_pose.POSE_CONNECTIONS)

            cv2.putText(img, f"Knee Angle: {int(knee_angle)}",
                        (30,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

        cv2.putText(img, status, (30,100),
                    cv2.FONT_HERSHEY_SIMPLEX,1.2,color,3)

        cv2.imshow("Posture Detection", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Smart Health & Fitness AI")
root.geometry("500x650")
root.configure(bg="#111827")

img_path = None

def upload():
    global img_path
    img_path = filedialog.askopenfilename()
    img = Image.open(img_path)
    img = img.resize((200,200))
    tk_img = ImageTk.PhotoImage(img)
    panel.config(image=tk_img)
    panel.image = tk_img

def analyze():
    food = food_entry.get()
    cal = get_calorie(food)

    try:
        w = int(weight.get())
        h = int(height.get())
        a = int(age.get())
    except:
        messagebox.showerror("Error","Enter valid body data")
        return

    body_bmr = bmr(w,h,a)
    exercise = exercise_plan(cal)

    result_label.config(text=
        f"Food Calories: {cal}\n"
        f"BMR: {body_bmr}\n"
        f"Exercise to Burn: {exercise}"
    )

tk.Label(root,text="Smart Health AI",
         fg="white",bg="#111827",
         font=("Arial",20,"bold")).pack(pady=10)

panel = tk.Label(root,bg="#111827")
panel.pack()

tk.Button(root,text="Upload Food Image",
          command=upload).pack(pady=5)

tk.Label(root,text="Food Name",
         fg="white",bg="#111827").pack()
food_entry = tk.Entry(root)
food_entry.pack()

form = tk.Frame(root,bg="#111827")
form.pack(pady=10)

tk.Label(form,text="Weight kg",
         fg="white",bg="#111827").grid(row=0,column=0)
weight = tk.Entry(form)
weight.grid(row=0,column=1)

tk.Label(form,text="Height cm",
         fg="white",bg="#111827").grid(row=1,column=0)
height = tk.Entry(form)
height.grid(row=1,column=1)

tk.Label(form,text="Age",
         fg="white",bg="#111827").grid(row=2,column=0)
age = tk.Entry(form)
age.grid(row=2,column=1)

tk.Button(root,text="Analyze",
          bg="#22c55e",
          command=analyze).pack(pady=10)

tk.Button(root,text="Start Posture Check",
          bg="#f59e0b",
          command=start_posture).pack(pady=10)

result_label = tk.Label(root,
                        fg="white",
                        bg="#111827",
                        font=("Arial",12))
result_label.pack()

root.mainloop()