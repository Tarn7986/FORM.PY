import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()  # Get the selected title
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name:")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name:")
last_name_label.grid(row=1, column=0)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=0, column=1)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title:")
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Miss", "Ms.", "Dr."])
title_label.grid(row=2, column=0)
title_combobox.grid(row=2, column=1)

gender_label = tkinter.Label(user_info_frame, text="Gender:")
gender_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "N/K"])
gender_label.grid(row=0, column=2)
gender_combobox.grid(row=0, column=3)

age_label = tkinter.Label(user_info_frame, text="Age:")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=1, column=2)
age_spinbox.grid(row=1, column=3)

nationality_label = tkinter.Label(user_info_frame, text="Nationality:")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=2)
nationality_combobox.grid(row=2, column=3)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

reg_status_label = tkinter.Label(courses_frame, text="Registration Status:")
reg_status_var = tkinter.StringVar(value="Not Registered")
reg_status_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not Registered")
reg_status_label.grid(row=0, column=0)
reg_status_check.grid(row=0, column=1)

num_courses_label = tkinter.Label(courses_frame, text="# Completed Courses:")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=999)
num_courses_label.grid(row=1, column=0)
numcourses_spinbox.grid(row=1, column=1)

num_semesters_label = tkinter.Label(courses_frame, text="# Semesters:")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to=20)
num_semesters_label.grid(row=2, column=0)
numsemesters_spinbox.grid(row=2, column=1)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()