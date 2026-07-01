import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import matplotlib.pyplot as plt


# ---------------------- Calculate BMI ----------------------
def calculate_bmi():
    try:
        name = name_entry.get()

        if name == "":
            messagebox.showerror("Error", "Please enter your name.")
            return

        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be greater than 0.")
            return

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
            color = "blue"
        elif bmi < 25:
            category = "Normal Weight"
            color = "green"
        elif bmi < 30:
            category = "Overweight"
            color = "orange"
        else:
            category = "Obese"
            color = "red"

        result_label.config(
            text=f"Hello {name}\n\nBMI : {bmi:.2f}\nCategory : {category}",
            fg=color
        )

        file_exists = os.path.isfile("bmi_records.csv")

        with open("bmi_records.csv", "a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Weight", "Height", "BMI", "Category"])

            writer.writerow([
                name,
                weight,
                height,
                round(bmi, 2),
                category
            ])

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

    except Exception as e:
        messagebox.showerror("File Error", f"Unable to save record.\n\n{e}")

# ---------------------- Clear Fields ----------------------
def clear_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


    # ---------------------- Show Graph ----------------------
def show_graph():

    if not os.path.exists("bmi_records.csv"):
        messagebox.showinfo("No Records", "No BMI records found.")
        return

    names = []
    bmi_values = []

    with open("bmi_records.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            names.append(row[0])
            bmi_values.append(float(row[3]))

    plt.figure(figsize=(8, 5))
    plt.plot(names, bmi_values, marker="o")

    plt.title("BMI Records")
    plt.xlabel("Name")
    plt.ylabel("BMI")
    plt.grid(True)

    plt.show()

# ---------------------- View Records ----------------------

def view_records():

    try: 

        if not os.path.exists("bmi_records.csv"):
            messagebox.showinfo("No Records", "No BMI records found.")
            return

        record_window = tk.Toplevel(window)
        record_window.title("BMI Records")
        record_window.geometry("700x400")

        tree = ttk.Treeview(
            record_window,
            columns=("Name", "Weight", "Height", "BMI", "Category"),
            show="headings"
        )

        tree.heading("Name", text="Name")
        tree.heading("Weight", text="Weight")
        tree.heading("Height", text="Height")
        tree.heading("BMI", text="BMI")
        tree.heading("Category", text="Category")

        tree.pack(fill="both", expand=True)

        with open("bmi_records.csv", "r") as file:

            reader = csv.reader(file)

            next(reader)

            for row in reader:
                tree.insert("", tk.END, values=row)

    except Exception as e:
        messagebox.showerror(
            "File Error",
            f"Unable to read records.\n\n{e}"
        )
# ---------------------- Main Window ----------------------
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("450x600")
window.configure(bg="#E8F6F3")


# ---------------------- Heading ----------------------
title = tk.Label(
    window,
    text="BMI CALCULATOR",
    font=("Arial", 22, "bold"),
    bg="#E8F6F3",
    fg="darkblue"
)
title.pack(pady=20)


# ---------------------- Name ----------------------
name_label = tk.Label(
    window,
    text="Name",
    font=("Arial", 12),
    bg="#E8F6F3"
)
name_label.pack()

name_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
name_entry.pack(pady=5)


# ---------------------- Weight ----------------------
weight_label = tk.Label(
    window,
    text="Weight (kg)",
    font=("Arial", 12),
    bg="#E8F6F3"
)
weight_label.pack()

weight_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
weight_entry.pack(pady=5)


# ---------------------- Height ----------------------
height_label = tk.Label(
    window,
    text="Height (m)",
    font=("Arial", 12),
    bg="#E8F6F3"
)
height_label.pack()

height_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 12)
)
height_entry.pack(pady=5)


# ---------------------- Calculate Button ----------------------
calculate_button = tk.Button(
    window,
    text="Calculate BMI",
    width=20,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=calculate_bmi
)
calculate_button.pack(pady=10)


# ---------------------- Clear Button ----------------------
clear_button = tk.Button(
    window,
    text="Clear",
    width=20,
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=clear_fields
)
clear_button.pack(pady=5)


# ---------------------- View Records Button ----------------------
view_button = tk.Button(
    window,
    text="View Records",
    width=20,
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=view_records
)
view_button.pack(pady=5)
graph_button = tk.Button(
    window,
    text="Show BMI Graph",
    width=20,
    font=("Arial",12,"bold"),
    bg="purple",
    fg="white",
    command=show_graph
)

graph_button.pack(pady=5)


# ---------------------- Result ----------------------
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14, "bold"),
    bg="#E8F6F3"
)
result_label.pack(pady=20)


window.mainloop()