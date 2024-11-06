import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Function to connect to the database and view student records
def view_students():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    records = c.fetchall()
    conn.close()
    return records

# Function to search for a student record based on ID or Name
def search_student(query):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id LIKE ? OR name LIKE ?", ('%' + query + '%', '%' + query + '%'))
    records = c.fetchall()
    conn.close()

    # Clear the Treeview table
    for record in tree.get_children():
        tree.delete(record)

    # Display only the matching records
    for record in records:
        tree.insert("", tk.END, values=record)

# Function to add a new student and clear input fields after adding
def add_student(name, age, grade, address, course_name):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, grade, address, course_name) VALUES (?, ?, ?, ?, ?)",
              (name, age, grade, address, course_name))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student added successfully")
    clear_fields()
    display_records()

# Function to delete a student record by ID
def delete_student(student_id):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully")
    display_records()

# Function to select a student record for modification
def select_student(event):
    try:
        # Clear current entries
        clear_fields()

        # Get selected record
        selected = tree.focus()
        record = tree.item(selected, 'values')

        # Set fields based on selected student
        if record:
            id_entry.insert(0, record[0])
            name_entry.insert(0, record[1])
            age_entry.insert(0, record[2])
            grade_entry.insert(0, record[3])
            address_entry.insert(0, record[4])
            course_name_entry.insert(0, record[5])
    except IndexError:
        messagebox.showwarning("Selection Error", "No student selected.")

# Function to update an existing student record
def update_student(student_id, name, age, grade, address, course_name):
    if not student_id:
        messagebox.showwarning("Error", "Please select a student to update.")
        return

    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("""UPDATE students SET name = ?, age = ?, grade = ?, address = ?, course_name = ? 
                 WHERE id = ?""", (name, age, grade, address, course_name, student_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Student ID {student_id} updated successfully")
    clear_fields()
    display_records()

# Function to clear the input fields
def clear_fields():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    course_name_entry.delete(0, tk.END)

# Function to display student records in the Treeview
def display_records():
    # Clear the existing records in the tree
    for record in tree.get_children():
        tree.delete(record)

    # Insert new records from the database
    records = view_students()
    for record in records:
        tree.insert("", tk.END, values=record)

# Main window setup
root = tk.Tk()
root.title("Student Database")

# Create a custom style for the Treeview
style = ttk.Style()
style.configure("Treeview",
                font=("Arial", 12),  # Font for the rows
                rowheight=25,        # Row height
                background="lightgrey",  # Background color for rows
                fieldbackground="white", # Background color for editable cells
                foreground="black",      # Text color for the rows
                justify="center")        # Center align the text

style.configure("Treeview.Heading",
                font=("Arial", 14, "bold"),  # Font for the headers
                foreground="black",          # Color of the headers
                justify="center")            # Center align the header text

# Frames for Input and Display
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(padx=10, pady=10)

display_frame = tk.Frame(root, padx=10, pady=10)
display_frame.pack(padx=10, pady=10)

# Search bar and Search button
search_label = tk.Label(input_frame, text="Search Student (ID or Name):")
search_label.grid(row=3, column=3, padx=5, pady=5)

search_entry = tk.Entry(input_frame, width=30)
search_entry.grid(row=3, column=4, padx=5, pady=5)

search_button = tk.Button(input_frame, text="Search", command=lambda: search_student(search_entry.get()))
search_button.grid(row=3, column=5, padx=5, pady=5)

# Labels and Entries for Input
tk.Label(input_frame, text="ID (for update/delete)", width=20).grid(row=1, column=0)
id_entry = tk.Entry(input_frame, width=40)
id_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Name").grid(row=2, column=0)
name_entry = tk.Entry(input_frame, width=40)
name_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Age").grid(row=3, column=0)
age_entry = tk.Entry(input_frame, width=40)
age_entry.grid(row=3, column=1)

tk.Label(input_frame, text="Grade").grid(row=4, column=0)
grade_entry = tk.Entry(input_frame, width=40)
grade_entry.grid(row=4, column=1)

tk.Label(input_frame, text="Address").grid(row=5, column=0)
address_entry = tk.Entry(input_frame, width=40)
address_entry.grid(row=5, column=1)

tk.Label(input_frame, text="Course Name").grid(row=6, column=0)
course_name_entry = tk.Entry(input_frame, width=40)
course_name_entry.grid(row=6, column=1)

# Buttons
add_button = tk.Button(input_frame, text="Add Student",
                       command=lambda: add_student(name_entry.get(), age_entry.get(), grade_entry.get(),
                                                   address_entry.get(), course_name_entry.get()))
add_button.grid(row=9, column=0, pady=5, padx=5)

update_button = tk.Button(input_frame, text="Update Student",
                          command=lambda: update_student(id_entry.get(), name_entry.get(), age_entry.get(),
                                                         grade_entry.get(), address_entry.get(), course_name_entry.get()))
update_button.grid(row=9, column=1, pady=5, padx=5)

delete_button = tk.Button(input_frame, text="Delete Student",
                          command=lambda: delete_student(id_entry.get()))
delete_button.grid(row=9, column=2, pady=5, padx=5)

clear_button = tk.Button(input_frame, text="Clear Fields", command=clear_fields)
clear_button.grid(row=9, column=3, pady=5, padx=5)

# Display Area: Using Treeview widget for the table-like display
columns = ("ID", "Name", "Age", "Grade", "Address", "Course Name")
tree = ttk.Treeview(display_frame, columns=columns, show='headings', style="Treeview")

# Define headings and set column properties
for col in columns:
    tree.heading(col, text=col, anchor="center")  # Center align the header text
    tree.column(col, width=150, anchor="center")  # Center align the content text

tree.pack(padx=10, pady=10)

# Bind the select event to the Treeview
tree.bind("<<TreeviewSelect>>", select_student)

# Start the GUI loop
display_records()
root.mainloop()





