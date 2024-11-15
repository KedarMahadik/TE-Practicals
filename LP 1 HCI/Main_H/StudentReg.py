import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Get values from entries
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = listbox_course.get(tk.ACTIVE)
    consent = consent_var.get()

    # Check if all fields are filled
    if not name or not age or not gender or not course:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    # Show collected information in a message box
    msg = f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}\nConsent: {'Yes' if consent else 'No'}"
    messagebox.showinfo("Registration Information", msg)

# Initialize the main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500")
root.config(bg="#f2f2f2")  # Light grey background

# Title Label
title_label = tk.Label(root, text="Student Registration Form", font=("Times New Roman", 18, "bold"), bg="#f2f2f2", fg="#333")
title_label.pack(pady=15)

# Frame for the form
form_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="groove", borderwidth=2)
form_frame.pack(pady=20, padx=20)

# Name Label and Entry
label_name = tk.Label(form_frame, text="Full Name:", font=("Times New Roman", 12), bg="#ffffff")
label_name.grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame, width=30, font=("Times New Roman", 12))
entry_name.grid(row=0, column=1, pady=5)

# Age Label and Entry
label_age = tk.Label(form_frame, text="Age:", font=("Times New Roman", 12), bg="#ffffff")
label_age.grid(row=1, column=0, sticky="w", pady=5)
entry_age = tk.Entry(form_frame, width=30, font=("Times New Roman", 12))
entry_age.grid(row=1, column=1, pady=5)

# Gender Label and RadioButtons
label_gender = tk.Label(form_frame, text="Gender:", font=("Times New Roman", 12), bg="#ffffff")
label_gender.grid(row=2, column=0, sticky="w", pady=5)
gender_var = tk.StringVar()
radio_male = tk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male", font=("Times New Roman", 10), bg="#ffffff")
radio_female = tk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female", font=("Times New Roman", 10), bg="#ffffff")
radio_other = tk.Radiobutton(form_frame, text="Other", variable=gender_var, value="Other", font=("Times New Roman", 10), bg="#ffffff")
radio_male.grid(row=2, column=1, sticky="w")
radio_female.grid(row=2, column=1)
radio_other.grid(row=2, column=1, sticky="e")

# Course Label and ListBox
label_course = tk.Label(form_frame, text="Course:", font=("Times New Roman", 12), bg="#ffffff")
label_course.grid(row=3, column=0, sticky="w", pady=5)
listbox_course = tk.Listbox(form_frame, height=5, selectmode=tk.SINGLE, font=("Times New Roman", 10))
courses = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"]
for course in courses:
    listbox_course.insert(tk.END, course)
listbox_course.grid(row=3, column=1, pady=5)

# Consent Checkbutton
consent_var = tk.IntVar()
check_consent = tk.Checkbutton(form_frame, text="I agree to the terms and conditions", variable=consent_var, font=("Times New Roman", 10), bg="#ffffff")
check_consent.grid(row=4, columnspan=2, pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form, font=("Times New Roman", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
submit_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
