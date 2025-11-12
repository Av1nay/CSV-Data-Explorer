# ==========================================================
# 📊 CSV Data Explorer
# A beginner-friendly data analysis tool built using Pandas,
# Matplotlib, and Seaborn to summarize and visualize datasets.
# ==========================================================

# ----------------------------------------------------------
# 📦 Importing required libraries
# ----------------------------------------------------------
import pandas as pd  # Pandas: for loading, cleaning, and analyzing tabular data (DataFrame)
import matplotlib.pyplot as plt  # Matplotlib: for creating charts and plots
import seaborn as sbn  # Seaborn: for visually appealing statistical plots (built on Matplotlib)

# ----------------------------------------------------------
# 🧮 Step 1 — Load CSV file
# ----------------------------------------------------------
# Ask the user for a CSV file path, or use the default sample file if they just press Enter
file_path = (
    input("Enter CSV file path (or press Enter for sample): ")
    or "data/sample_sales.csv"
)

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(file_path)

# Confirm successful file loading
print("\n✅ File Loaded Successfully!\n")

# ----------------------------------------------------------
# 🧾 Step 2 — Display dataset overview
# ----------------------------------------------------------
print("📊 Data Overview:")
print("_" * 50)  # Print a visual separator line (50 underscores)

# Display the shape → (number of rows, number of columns)
print(f"Shape (rows, columns): {data.shape}")

# Print the column names
print("\nColumns:", list(data.columns))

# Print data types for each column (int, float, object, etc.)
print("\nData Types:\n", data.dtypes)

# Show missing value count per column (helps detect nulls)
print("\nMissing Values:\n", data.isnull().sum())

# Show the first 5 rows of the dataset (a sample preview)
print("\nFirst 5 rows:\n", data.head())

# ----------------------------------------------------------
# 📈 Step 3 — Display summary statistics with Optional Exclusion
# ----------------------------------------------------------
print("\nAvailable columns:")
print(list(data.columns))

# asking user if they want to exclude any columns
exclude_input = input(
    "\nEnter column names to exclude (comma-separated), or press Enter to skip:"
)
# Convert user input into clean list
exclude_cols = [
    col.strip() for col in exclude_input.split(",") if col.strip()
]  # removes spaces and blanks
# if user entered something, then drop those columns before describing
if exclude_cols:
    print(f"\nExcluding columns: {exclude_cols}")
    print(data.drop(columns=exclude_cols, errors="ignore").describe())
else:
    print("\nNo columns excluded.")
    print(data.describe())
# ----------------------------------------------------------
# 🎨 Step 4 — Visualize numeric data distributions
# ----------------------------------------------------------

# Select numeric columns only (exclude OrderID because it’s just an identifier)
numeric_cols = [
    col for col in data.select_dtypes(include="number").columns if col != "OrderID"
]

# Define grid layout for subplots (2 rows × 2 columns)
rows = 2
cols = 2

# Create one large figure window
plt.figure(figsize=(12, 8))

# Add a main title across all subplots
plt.suptitle("Numeric Column Distributions", fontsize=16, y=1.02)

# Loop through numeric columns and create a subplot for each
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(rows, cols, i)  # Define subplot position in grid
    sbn.histplot(data[col], kde=True, color="skyblue")  # Draw histogram + smooth curve
    plt.title(f"Distribution of {col}")  # Add individual title per plot

# Adjust spacing to avoid overlapping text
plt.tight_layout()

# Display the combined figure with all histograms
plt.show()
