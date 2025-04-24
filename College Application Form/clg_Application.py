import tkinter as tk
from tkinter import messagebox

def display_course_details():
    selected_course = course_var.get()

    if selected_course == "Engineering":
        course_details = "Engineering Course: \n- B.Tech in various specializations\n*Information Technology \n*Bio-Technology \n*Petrochemical \n- Duration: 4 years\n- Fees: 1,00,000\n- Career prospects: Software, Hardware, Research, etc."
    elif selected_course == "Arts":
        course_details = "Arts Course: \n- B.A in various specializations\n*English\n*Mathematics\n*Economy\n*Chemistry\n*Botany\n*Zoology\n- Duration: 3 years\n- Fees: 50,000\n- Career prospects: Teaching, Journalism, Social Work, etc."

    result_label.config(text=course_details)

def submit():
    name_val = ename.get()
    dob_val = edob.get()
    fname_val = efname.get()
    eadd_val = eadd.get()
    ephone_val = ephone.get()
    egender_val = egender.get()
    epass_val = epass.get()
    enationality_val = enationality.get()
    em1_val = em1.get()
    em2_val = em2.get()
    percent_val = epercent.get()

    if not name_val or not dob_val or not fname_val or not eadd_val or not ephone_val or not egender_val or not epass_val or not enationality_val or not em1_val or not em2_val or not percent_val:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    if not em1_val.isdigit() or not em2_val.isdigit() or not percent_val.replace('.', '', 1).isdigit():
        messagebox.showerror("Input Error", "Marks and percentage must be numbers!")
        return

    if float(percent_val) > 50:
        course_label.config(state="normal")
        arts_course.config(state="normal")
        engineering_course.config(state="normal")
    else:
        course_label.config(state="normal")
        arts_course.config(state="normal")
        engineering_course.config(state="disabled")

    result = f"Name: {name_val}\nDOB: {dob_val}\nFather's Name: {fname_val}\nAddress: {eadd_val}\nPhone Number: {ephone_val}\nGender: {egender_val}\nPass out: {epass_val}\nNationality: {enationality_val}\n10th mark: {em1_val}\n12th mark: {em2_val}\nPercent: {percent_val}"
    result_label.config(text=result)

root = tk.Tk()
root.geometry("1500x800")
root.title("College Application Form")

canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)
label = tk.Label(scrollable_frame, text="Student Details", font=('Arial', 18))
label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

name = tk.Label(scrollable_frame, text="Name", font=('Arial', 14))
name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
ename = tk.Entry(scrollable_frame, font=('Arial', 14))
ename.grid(row=1, column=1, padx=10, pady=10)

dob = tk.Label(scrollable_frame, text="DOB (yyyy-mm-dd)", font=('Arial', 14))
dob.grid(row=2, column=0, padx=10, pady=10, sticky="w")
edob = tk.Entry(scrollable_frame, font=('Arial', 14))
edob.grid(row=2, column=1, padx=10, pady=10)

fname = tk.Label(scrollable_frame, text="Father's Name", font=('Arial', 14))
fname.grid(row=3, column=0, padx=10, pady=10, sticky="w")
efname = tk.Entry(scrollable_frame, font=('Arial', 14))
efname.grid(row=3, column=1, padx=10, pady=10)

address = tk.Label(scrollable_frame, text="Address", font=('Arial', 14))
address.grid(row=4, column=0, padx=10, pady=10, sticky="w")
eadd = tk.Entry(scrollable_frame, font=('Arial', 14))
eadd.grid(row=4, column=1, padx=10, pady=10)

phone_label = tk.Label(scrollable_frame, text="Phone Number", font=('Arial', 14))
phone_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
ephone = tk.Entry(scrollable_frame, font=('Arial', 14))
ephone.grid(row=5, column=1, padx=10, pady=10)

gender = tk.Label(scrollable_frame, text="Gender", font=('Arial', 14))
gender.grid(row=6, column=0, padx=10, pady=10, sticky="w")
egender = tk.Entry(scrollable_frame, font=('Arial', 14))
egender.grid(row=6, column=1, padx=10, pady=10)

pass_out = tk.Label(scrollable_frame, text="Year of Passout", font=('Arial', 14))
pass_out.grid(row=7, column=0, padx=10, pady=10, sticky="w")
epass = tk.Entry(scrollable_frame, font=('Arial', 14))
epass.grid(row=7, column=1, padx=10, pady=10)

nationality_label = tk.Label(scrollable_frame, text="Nationality", font=('Arial', 14))
nationality_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
enationality = tk.Entry(scrollable_frame, font=('Arial', 14))
enationality.grid(row=8, column=1, padx=10, pady=10)

m1 = tk.Label(scrollable_frame, text="10th Marks", font=('Arial', 14))
m1.grid(row=9, column=0, padx=10, pady=10, sticky="w")
em1 = tk.Entry(scrollable_frame, font=('Arial', 14))
em1.grid(row=9, column=1, padx=10, pady=10)

m2 = tk.Label(scrollable_frame, text="12th Marks", font=('Arial', 14))
m2.grid(row=10, column=0, padx=10, pady=10, sticky="w")
em2 = tk.Entry(scrollable_frame, font=('Arial', 14))
em2.grid(row=10, column=1, padx=10, pady=10)

percent = tk.Label(scrollable_frame, text="Percentage", font=('Arial', 14))
percent.grid(row=11, column=0, padx=10, pady=10, sticky="w")
epercent = tk.Entry(scrollable_frame, font=('Arial', 14))
epercent.grid(row=11, column=1, padx=10, pady=10)

submit_button = tk.Button(scrollable_frame, text="Submit", font=('Arial', 14), command=submit)
submit_button.grid(row=12, column=0, columnspan=2, padx=10, pady=20)

course_label = tk.Label(scrollable_frame, text="Select Course", font=('Arial', 14))
course_label.grid(row=13, column=0, padx=10, pady=10, sticky="w")
course_var = tk.StringVar()

arts_course = tk.Radiobutton(scrollable_frame, text="Arts", variable=course_var, value="Arts", font=('Arial', 14), state="disabled", command=display_course_details)
arts_course.grid(row=13, column=1, padx=10, pady=10, sticky="w")

engineering_course = tk.Radiobutton(scrollable_frame, text="Engineering", variable=course_var, value="Engineering", font=('Arial', 14), state="disabled", command=display_course_details)
engineering_course.grid(row=13, column=2, padx=10, pady=10, sticky="w")

result_label = tk.Label(root, font=('Arial', 14), justify="left", width=40, anchor="w")
result_label.pack(side="right", padx=10, pady=10)

root.mainloop()
