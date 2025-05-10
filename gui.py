from main import preprocess_data, classify_button_clicked, load_dataset, classify_drug
import tkinter as tk
from tkinter import filedialog, messagebox

# Create main window
root = tk.Tk()
root.title("Drug classifier")

# Input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Molecular Weight
tk.Label(input_frame, text="Molecular Weight:").grid(row=0, column=0, padx=5, pady=5)
molecular_weight_entry = tk.Entry(input_frame)
molecular_weight_entry.grid(row=0, column=1, padx=70, pady=5)

# Solubility
tk.Label(input_frame, text="Solubility:").grid(row=1, column=0, padx=5, pady=5)
solubility_var = tk.StringVar()
solubility_menu = tk.OptionMenu(input_frame, solubility_var, "High", "Medium", "Low")
solubility_menu.grid(row=1, column=1, padx=5, pady=5)
solubility_var.set("High")  # Default value

# Absorption (%)
tk.Label(input_frame, text="Absorption (%):").grid(row=2, column=0, padx=5, pady=5)
absorption_entry = tk.Entry(input_frame)
absorption_entry.grid(row=2, column=1, padx=5, pady=5)

# Patient Age
tk.Label(input_frame, text="Patient Age:").grid(row=3, column=0, padx=5, pady=5)
patient_age_entry = tk.Entry(input_frame)
patient_age_entry.grid(row=3, column=1, padx=5, pady=5)

# Genetic Marker
# Represents genetic characteristics that influence drug efficacy (e.g., genetic mutations or markers).
tk.Label(input_frame, text="Genetic Marker:").grid(row=4, column=0, padx=5, pady=5)
genetic_marker_var = tk.IntVar()
genetic_marker_menu = tk.OptionMenu(input_frame, genetic_marker_var, 0, 1, 2)
genetic_marker_menu.grid(row=4, column=1, padx=5, pady=5)
genetic_marker_var.set(0)  # Default value

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

classify_button = tk.Button(button_frame, text="Classify", command=classify_button_clicked)
classify_button.pack(side=tk.LEFT, padx=5)

load_button = tk.Button(button_frame, text="Load Dataset", command=load_dataset)
load_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
