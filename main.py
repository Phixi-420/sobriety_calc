import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_sober_days():
    stop_date_str = "11/17/2023"

    try:
        stop_date = datetime.strptime(stop_date_str, "%m/%d/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use MM/DD/YYYY.")
        return

    today = datetime.now()
    days_sober = (today - stop_date).days
    result_label.config(text=f"You have been sober for {days_sober} days.")

# Create the main window
root = tk.Tk()
root.title("Sobriety Calculator")

# Create and place widgets
calculate_button = tk.Button(root, text="Calculate", command=calculate_sober_days)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the main loop
root.mainloop()
