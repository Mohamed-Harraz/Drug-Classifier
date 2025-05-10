import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Global variables
data = None
model = None
scaler = None

def preprocess_data():
    global data, model, scaler
    # Encoding categorical data
    data["Solubility"] = data["Solubility"].map({"High": 2, "Medium": 1, "Low": 0})
    data["Genetic Marker"] = data["Genetic Marker"].map({"Marker A": 0, "Marker B": 1, "Marker C": 2})
    data["Effectiveness"] = data["Effectiveness"].map({"Effective": 2, "Partially Effective": 1, "Ineffective": 0})

    # Extract features and labels
    X = data[["Molecular Weight", "Solubility", "Absorption (%)", "Patient Age", "Genetic Marker"]].values
    y = data["Effectiveness"].values

    # Stratified train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale the feature data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train a Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    #print(f"Model Accuracy: {accuracy:.2f}")
    #print("\nClassification Report:")
    #print(classification_report(y_test, y_pred))

def classify_drug(features):
    global scaler, model
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)
    return prediction[0]

def classify_button_clicked():
    if data is None or model is None or scaler is None:
        messagebox.showerror("Error", "Please load and preprocess the dataset first.")
        return

    try:
        molecular_weight = float(molecular_weight_entry.get())
        solubility_text = solubility_var.get().strip().lower()
        solubility_map = {"low": 0, "medium": 1, "high": 2}
        solubility = solubility_map[solubility_text]
        absorption = float(absorption_entry.get())
        patient_age = int(patient_age_entry.get())
        genetic_marker = genetic_marker_var.get()

        features = [molecular_weight, solubility, absorption, patient_age, genetic_marker]
        result = classify_drug(features)
        effectiveness_map = {2: "Effective", 1: "Partially Effective", 0: "Ineffective"}
        messagebox.showinfo("Prediction Result", f"Predicted Effectiveness: {effectiveness_map[result]}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def load_dataset():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        data = pd.read_csv(file_path)
        preprocess_data()
        messagebox.showinfo("Dataset Loaded", f"Dataset loaded and processed successfully from {file_path}.")

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
