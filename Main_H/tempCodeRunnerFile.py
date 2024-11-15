import tkinter as tk
from tkinter import messagebox

def submit_registration():
    # Retrieving values from the form
    patient_name = entry_patient_name.get().strip()
    patient_age = entry_patient_age.get().strip()
    patient_contact = entry_patient_contact.get().strip()
    patient_email = entry_patient_email.get().strip()
    patient_address = text_address.get("1.0", tk.END).strip()
    emergency_contact = entry_emergency_contact.get().strip()

    # Debugging: Print all field values to check what's being submitted
    print(f"Name: '{patient_name}'")
    print(f"Age: '{patient_age}'")
    print(f"Contact: '{patient_contact}'")
    print(f"Email: '{patient_email}'")
    print(f"Address: '{patient_address}'")
    print(f"Emergency Contact: '{emergency_contact}'")

    # Validate if any required field is empty
    if not patient_name or not patient_age or not patient_contact or not patient_email or not patient_address or not emergency_contact:
        messagebox.showwarning("Incomplete Form", "Please fill in all required fields!")
        return

    # Validate Age is an integer
    try:
        patient_age = int(patient_age)
    except ValueError:
        messagebox.showwarning("Invalid Age", "Age must be a valid integer.")
        return

    # Validate Contact Number is digits only
    if not patient_contact.isdigit():
        messagebox.showwarning("Invalid Contact", "Contact number must contain only digits.")
        return

    # Validate Emergency Contact is digits only
    if not emergency_contact.isdigit():
        messagebox.showwarning("Invalid Emergency Contact", "Emergency contact must contain only digits.")
        return

    # If all validations pass, show the success message
    messagebox.showinfo("Registration Successful", "Patient registered successfully!")
    clear_form()

def clear_form():
    entry_patient_name.delete(0, tk.END)
    entry_patient_age.delete(0, tk.END)
    entry_patient_contact.delete(0, tk.END)

    gender_var.set("")
    entry_patient_contact.delete(0, tk.END)
    entry_patient_email.delete(0, tk.END)
    text_address.delete("1.0", tk.END)
    blood_group_var.set("")
    entry_emergency_contact.delete(0, tk.END)

root = tk.Tk()
root.title("Patient Registration Form")
root.geometry("600x650")
root.config(bg="#f4f6f9")

main_frame = tk.Frame(root, bg="#ffffff", padx=30, pady=30, relief="groove", borderwidth=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(main_frame, text="Patient Registration Form", font=("Helvetica", 18, "bold"), fg="#2C3E50").grid(row=0, column=0, columnspan=2, pady=20)

# Fields
fields = [
    ("Patient Name", entry_patient_name := tk.Entry(main_frame, font=("Helvetica", 12), width=30)),
    ("Patient Age", entry_patient_age := tk.Entry(main_frame, font=("Helvetica", 12), width=30)),
    ("Contact Number", entry_patient_contact := tk.Entry(main_frame, font=("Helvetica", 12), width=30)),
    ("Email", entry_patient_email := tk.Entry(main_frame, font=("Helvetica", 12), width=30)),
    ("Emergency Contact No", entry_emergency_contact := tk.Entry(main_frame, font=("Helvetica", 12), width=30)),
]

for i, (label, entry) in enumerate(fields, 1):
    tk.Label(main_frame, text=label+":", font=("Helvetica", 12), fg="#34495E").grid(row=i, column=0, sticky="e", pady=5)
    entry.grid(row=i, column=1, pady=5)

tk.Label(main_frame, text="Address:", font=("Helvetica", 12), fg="#34495E").grid(row=6, column=0, sticky="ne", pady=5)
text_address = tk.Text(main_frame, font=("Helvetica", 12), width=30, height=4, bd=2, relief="solid")
text_address.grid(row=6, column=1, pady=5)

tk.Label(main_frame, text="Blood Group:", font=("Helvetica", 12), fg="#34495E").grid(row=7, column=0, sticky="e", pady=5)
blood_group_var = tk.StringVar()
tk.OptionMenu(main_frame, blood_group_var, "A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-").grid(row=7, column=1, pady=5)


tk.Label(main_frame, text="Gender:", font=("Helvetica", 12), fg="#34495E").grid(row=3, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(main_frame, text="Male", variable=gender_var, value="Male", font=("Helvetica", 12)).grid(row=3, column=1, sticky="w", pady=5)
tk.Radiobutton(main_frame, text="Female", variable=gender_var, value="Female", font=("Helvetica", 12)).grid(row=3, column=1, pady=5)

tk.Button(main_frame, text="Submit", command=submit_registration, font=("Helvetica", 14, "bold"), bg="#2ecc71", fg="white").grid(row=10, column=0, columnspan=2, pady=20)
tk.Button(main_frame, text="Clear", command=clear_form, font=("Helvetica", 12), bg="#f39c12", fg="white").grid(row=11, column=0, columnspan=2, pady=5)

root.mainloop()
