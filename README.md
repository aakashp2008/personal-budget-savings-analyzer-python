# 💰 Personal Budget & Savings Analyzer

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue.svg">
<img src="https://img.shields.io/badge/JSON-Data%20Storage-orange.svg">
<img src="https://img.shields.io/badge/CSV-Reports-green.svg">
<img src="https://img.shields.io/badge/Analytics-Budget%20%26%20Savings-purple.svg">
<img src="https://img.shields.io/badge/CLI-Application-black.svg">
<img src="https://img.shields.io/badge/Status-Completed-success.svg">
<img src="https://img.shields.io/badge/License-Educational-yellow.svg">

</p>

<p align="center">
  <b>💵 A Python-based application for managing income, expenses, budgets, and savings goals.</b>
</p>

---

## 📖 Overview

The **Personal Budget & Savings Analyzer** is a professional Python-based application designed to help users manage their income, expenses, budgets, savings goals, and overall financial activity.

The system allows users to record income, track expenses, create savings goals, analyze spending patterns, monitor budgets, calculate available balances, search transactions, update records, and generate CSV reports.

This project demonstrates practical implementation of **Python programming, data management, financial analysis, JSON storage, CSV reporting, CRUD operations, and command-line application development**.

---

## ✨ Features

- 💵 Income Management
- 💸 Expense Management
- 🏷️ Expense Category Management
- 🎯 Savings Goal Tracking
- 💰 Savings Progress Tracking
- 📊 Financial Summary
- 📈 Expense Analytics
- 📋 Budget Analysis
- 🔍 Transaction Search
- ✏️ Update Expense Records
- 🗑️ Delete Expense Records
- 📊 Financial Dashboard
- 📄 CSV Report Generation
- 💾 JSON Data Storage
- 🖥️ Command-Line Interface

---

## 🏆 Savings Goals

The system allows users to create and track personal savings goals.

Each savings goal includes:

- Goal Name
- Target Amount
- Saved Amount
- Progress Percentage
- Goal Status
- Creation Date

### Savings Status

| Progress | Status |
| -------- | ------ |
| 100% | 🟢 Goal Completed |
| Below 100% | 🟡 In Progress |

Example:

```text
============================================================
SAVINGS GOALS
============================================================

1. New Laptop
   Target   : ₹50000.00
   Saved    : ₹30000.00
   Progress : 60.00%
   Status   : IN PROGRESS
```

---

## 📊 Financial Analytics

The application provides detailed financial analytics including:

- Total Income
- Total Expenses
- Available Balance
- Savings Rate
- Expense Categories
- Highest Spending Category
- Budget Status
- Savings Goal Progress

Example:

```text
============================================================
FINANCIAL SUMMARY
============================================================

Total Income    : ₹50000.00
Total Expenses  : ₹32000.00
Available Money : ₹18000.00
Savings Rate    : 36.00%

Financial Status:
🟢 Positive balance
```

---

## 💡 Smart Budget Analysis

The system allows users to enter a monthly budget and compare it with their recorded expenses.

Example:

```text
============================================================
BUDGET ANALYSIS
============================================================

Enter your monthly budget: ₹40000

------------------------------------------------------------
Monthly Budget : ₹40000.00
Spent          : ₹32000.00
Remaining      : ₹8000.00
Status         : 🟢 Within Budget
```

The system identifies whether the budget is:

- 🟢 Within Budget
- 🟡 Fully Used
- 🔴 Exceeded

---

## 🛠️ Technologies Used

- Python 3
- JSON
- CSV
- Datetime
- File Handling
- Lists
- Dictionaries
- Functions
- Exception Handling
- Data Processing
- Command-Line Interface

---

## 📂 Project Structure

```text
personal-budget-savings-analyzer-python/
│
├── personal_budget_savings_analyzer.py
├── budget_data.json
├── budget_report.csv
└── README.md
```

The `budget_data.json` and `budget_report.csv` files are generated automatically when the corresponding features are used.

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/aakashp2008/personal-budget-savings-analyzer-python.git
```

### Navigate to the Project

```bash
cd personal-budget-savings-analyzer-python
```

### Run the Program

```bash
python personal_budget_savings_analyzer.py
```

No external Python packages are required.

### Programiz

The project uses only Python's standard library, so it can also be executed using the **Programiz Python Online Compiler** without installing external packages.

---

## 🖥️ Main Menu

```text
============================================================
       PERSONAL BUDGET & SAVINGS ANALYZER
============================================================

1. Add Income
2. Add Expense
3. Add Savings Goal
4. Add Savings
5. View Income
6. View Expenses
7. View Savings Goals
8. Financial Summary
9. Expense Analytics
10. Budget Analysis
11. Search Transactions
12. Update Expense
13. Delete Expense
14. Dashboard
15. Export CSV Report
16. Exit
```

---

## 📋 Example

### Add Income

```text
============================================================
ADD INCOME
============================================================

Enter income source: Part-Time Work
Enter income amount: 15000

Income added successfully!
```

### Add Expense

```text
============================================================
ADD EXPENSE
============================================================

Enter expense category: Education
Enter expense description: Books
Enter expense amount: 2500

Expense added successfully!
```

### Add Savings Goal

```text
============================================================
ADD SAVINGS GOAL
============================================================

Enter savings goal: New Laptop
Enter target amount: 50000

Savings goal added successfully!
```

### Dashboard

```text
============================================================
PERSONAL BUDGET & SAVINGS DASHBOARD
============================================================

Income Records       : 3
Expense Records      : 8
Savings Goals        : 2
Completed Goals      : 1

Financial Overview
------------------------------------------------------------
Total Income         : ₹45000.00
Total Expenses       : ₹28000.00
Available Balance    : ₹17000.00
```

---

## 📄 Reports

The application can generate a detailed CSV financial report containing:

- Transaction Type
- Category / Income Source
- Description
- Amount
- Date

Generated file:

```text
budget_report.csv
```

The report can be opened using spreadsheet applications such as Microsoft Excel or other compatible software.

---

## 💾 Data Storage

Financial information is stored locally using JSON.

Generated file:

```text
budget_data.json
```

The JSON file stores:

- Income Records
- Expense Records
- Savings Goals
- Amounts
- Categories
- Descriptions
- Dates
- Savings Progress

This makes the application lightweight and easy to run without requiring a database server.

---

## 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Python Programming
- Personal Finance Data Management
- Budget Analysis
- Expense Analysis
- Savings Tracking
- File Handling
- JSON Data Storage
- CSV Report Generation
- Data Structures
- CRUD Operations
- Input Validation
- Functions
- Data Processing
- Conditional Statements
- Exception Handling
- Command-Line Application Development
- Problem-Solving Skills

---

## 🚀 Future Enhancements

- 🌐 Web-Based Budget Management
- 🖥️ Graphical User Interface using Tkinter
- 📱 Mobile Application
- 🗄️ MySQL / SQLite Database
- 📊 Interactive Financial Charts
- 📈 Monthly Spending Reports
- 🎯 Advanced Savings Goal Tracking
- 🔔 Budget Alert Notifications
- 📧 Financial Summary Emails
- 📄 PDF Report Generation
- ☁️ Cloud Data Storage
- 🔐 User Authentication
- 📅 Recurring Expense Management
- 🤖 Smart Spending Recommendations
- 🧠 AI-Based Financial Insights

---

## 🌟 Project Purpose

Managing personal income, expenses, budgets, and savings manually can be difficult and time-consuming.

The **Personal Budget & Savings Analyzer** provides a simple solution for recording financial transactions, analyzing spending patterns, monitoring budgets, tracking savings goals, and generating reports.

The project can be extended into a complete **personal finance management and financial analytics platform**.

---

## 👨‍💻 About

The **Personal Budget & Savings Analyzer** was developed as a Python project to demonstrate practical financial data management, analytics, file handling, and reporting concepts.

The application combines **income management, expense tracking, budget analysis, savings goals, financial analytics, JSON storage, and CSV reporting** into one professional command-line system.

---

## ⭐ Support

If you find this project useful, please consider giving the repository a **⭐ Star** on GitHub.

---

## 📄 License

This project is developed for educational and learning purposes.
