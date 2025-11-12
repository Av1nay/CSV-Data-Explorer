# 📊 CSV Data Explorer

A beginner-friendly **data analysis tool** built using **Python, Pandas, Matplotlib, and Seaborn**.  
This project helps users **load, summarize, and visualize any CSV dataset** with a few simple commands — making it a great starting point for learning **data analytics and visualization**.

---

## 🚀 Features

✅ **Load Any CSV File**  
Easily import your own dataset or use the included sample file.

✅ **Automatic Data Summary**  
Displays:

- Total rows and columns
- Column names and data types
- Missing value counts
- Preview of the first 5 rows

✅ **Interactive Summary Statistics**  
Optionally exclude any columns (like IDs or text fields) before generating summary statistics.

✅ **Visualize Numeric Columns**  
Automatically detects numeric columns and displays clean histograms (all on one page) using **Matplotlib + Seaborn**.

✅ **Beginner-Friendly Comments**  
The code is fully commented and easy to understand — perfect for learners transitioning into **data science or analytics**.

---

## 🧠 What You’ll Learn

By working through this project, you’ll gain practical skills in:

- Reading and exploring CSV data with `pandas`
- Understanding dataset structure and data types
- Performing basic **EDA (Exploratory Data Analysis)**
- Creating statistical visualizations with **Seaborn**
- Writing modular, documented Python scripts

---

## 🧩 Project Structure

csv_data_explorer/
│
├── data/
│ └── sample_sales.csv # Example dataset
│
├── explorer.py # Main Python script
└── README.md # Project documentation

---

## ⚙️ How to Run

1. **Clone or Download** this repository.
2. Open a terminal in the project directory.
3. (Optional) Create and activate a virtual environment.
4. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
5. Run the script

```bash
python explorer.py
```

6.  When promted:

- Enter your own CSV file path
- Or press Enter to use the sample dataset

## 📝 Example Output

```sql
**✅ File Loaded Successfully!**

**📊 Data Overview:**

---

Shape (rows, columns): (15, 11)

Columns: ['OrderID', 'Date', 'Customer', 'Region', 'Product', 'Category', 'Quantity', 'UnitPrice', 'TotalSale', 'PaymentMode', 'Profit']

Missing Values:
OrderID 0
Date 0
Customer 0
...

📈 Summary Statistics:
Quantity UnitPrice TotalSale Profit
count 15.000000 15.000000 15.000000 15.000000
mean 2.866667 243.333333 456.666667 91.333333
...
✅ File Loaded Successfully!

📊 Data Overview:
__________________________________________________
Shape (rows, columns): (15, 11)

Columns: ['OrderID', 'Date', 'Customer', 'Region', 'Product', 'Category', 'Quantity', 'UnitPrice', 'TotalSale', 'PaymentMode', 'Profit']

Missing Values:
OrderID       0
Date          0
Customer      0
...

📈 Summary Statistics:
           Quantity   UnitPrice   TotalSale    Profit
count     15.000000    15.000000    15.000000    15.000000
mean       2.866667   243.333333   456.666667    91.333333
...
```

**📊 Histograms are automatically shown in one figure window — making it easy to interpret your data visually.**
🛠️ Technologies Used
|Tool | Purpose|
|-----|--------|
|Python 3 | Core programming language|
Pandas |Data manipulation & cleaning
Matplotlib |Data visualization
Seaborn |Statistical plotting

## **📚 Future Improvements**

- Add interactive column exclusion for visualizations (user input for plot selection).
- Include correlation heatmap and pairplot for deeper analysis.
- Build a Streamlit web version for an interactive EDA dashboard.

## **👨‍💻 Author**

**Abhinay Chaudhary**

Python Developer | Data Enthusiast | AI Learner

[**💼 LinkedIn Profile**](https://www.linkedin.com/in/abhinay-chaudhary-822180b4)

[**🗂️Github**](https://github.com/Av1nay/CSV-Data-Explorer.git)
