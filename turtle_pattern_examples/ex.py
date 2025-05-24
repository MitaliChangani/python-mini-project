import tkinter as tk

# Function to update label with selected color
def update_label():
    label.config(text=f"Selected Color: {color_var.get()}", fg=color_var.get())

# Create main window
root = tk.Tk()
root.title("Color Selection")

# Define a variable to store the selected color
color_var = tk.StringVar(value="Red")  # Default selection

# Create Radiobuttons for Red, Blue, and Green
rb_red = tk.Radiobutton(root, text="Red", variable=color_var, value="Red", command=update_label, fg="red")
rb_red.pack()

rb_blue = tk.Radiobutton(root, text="Blue", variable=color_var, value="Blue", command=update_label, fg="blue")
rb_blue.pack()

rb_green = tk.Radiobutton(root, text="Green", variable=color_var, value="Green", command=update_label, fg="green")
rb_green.pack()

# Label to display selected color
label = tk.Label(root, text="Selected Color: Red", font=("Arial", 12), fg="Red")
label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()