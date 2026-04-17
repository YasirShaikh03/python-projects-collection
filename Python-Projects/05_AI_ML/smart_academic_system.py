import tkinter as tk
from tkinter import messagebox
import db, ml_model, analyzer, report, dashboard

db.setup()

BG = "#1e1e2f"
CARD = "#2b2b45"
BTN = "#4cafef"
TXT = "white"

root = tk.Tk()
root.title("Smart Academic Intelligence System")
root.geometry("520x520")
root.configure(bg=BG)

user = tk.StringVar()
pwd = tk.StringVar()

# ---------------- LOGIN CARD ----------------

card = tk.Frame(root, bg=CARD, padx=30, pady=30)
card.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(card, text="SAIS Login", bg=CARD, fg=TXT, font=("Arial",18,"bold")).pack(pady=10)

tk.Entry(card, textvariable=user, width=25).pack(pady=5)
tk.Entry(card, textvariable=pwd, show="*", width=25).pack(pady=5)

def login():
    if db.login(user.get(), pwd.get()):
        dashboard_ui()
    else:
        messagebox.showerror("Error","Invalid Login")

def register():
    if db.register(user.get(), pwd.get()):
        messagebox.showinfo("OK","Registered Successfully")
    else:
        messagebox.showerror("Error","User Exists")

tk.Button(card, text="Login", bg=BTN, fg="black", width=20, command=login).pack(pady=5)
tk.Button(card, text="Register", bg="gray", fg="black", width=20, command=register).pack()

# ---------------- DASHBOARD ----------------

def dashboard_ui():
    win = tk.Toplevel(root)
    win.title("Student Dashboard")
    win.geometry("600x600")
    win.configure(bg=BG)

    panel = tk.Frame(win, bg=CARD, padx=20, pady=20)
    panel.pack(pady=20)

    tk.Label(panel, text="Enter Marks", bg=CARD, fg=TXT, font=("Arial",16)).pack()

    entries = {}

    for s in ml_model.SUBJECTS:
        f = tk.Frame(panel, bg=CARD)
        f.pack(pady=4)
        tk.Label(f, text=s, bg=CARD, fg=TXT, width=12).pack(side="left")
        e = tk.Entry(f, width=10)
        e.pack(side="left")
        entries[s] = e

    def analyze():
        try:
            marks = {s:int(entries[s].get()) for s in entries}
        except:
            messagebox.showerror("Error","Invalid Marks")
            return

        res = ml_model.predict(marks)
        weak = ml_model.weak_subjects(marks)
        total = sum(marks.values())
        cg = analyzer.cgpa(total)
        rk = analyzer.rank_estimate(total)
        rec = analyzer.study_recommendation(weak)

        report.create_report(
            user.get(), marks,
            "PASS" if res==1 else "FAIL",
            weak, cg, rk, rec
        )

        messagebox.showinfo("Done","ReportCard.pdf Generated")

    def graph():
        try:
            marks = {s:int(entries[s].get()) for s in entries}
        except:
            return
        dashboard.show_subject_graph(marks, ml_model.avg)

    tk.Button(panel, text="Analyze + PDF", bg=BTN, width=20, command=analyze).pack(pady=8)
    tk.Button(panel, text="Show Graph", bg="orange", width=20, command=graph).pack()

root.mainloop()
