import json
import csv
from datetime import datetime

DATA_FILE = "budget_data.json"
REPORT_FILE = "budget_report.csv"


# ============================================================
# DATA HANDLING
# ============================================================

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "income": [],
            "expenses": [],
            "savings_goals": []
        }


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# ============================================================
# INPUT VALIDATION
# ============================================================

def get_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount >= 0:
                return amount

            print("Amount cannot be negative.")

        except ValueError:
            print("Please enter a valid amount.")


def get_integer(message, minimum=0):
    while True:
        try:
            value = int(input(message))

            if value >= minimum:
                return value

            print("Please enter a valid number.")

        except ValueError:
            print("Please enter a valid integer.")


# ============================================================
# ADD INCOME
# ============================================================

def add_income(data):
    print("\n" + "=" * 60)
    print("ADD INCOME")
    print("=" * 60)

    source = input("Enter income source: ").strip()

    if not source:
        print("Income source cannot be empty.")
        return

    amount = get_amount("Enter income amount: ")

    record = {
        "source": source,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["income"].append(record)
    save_data(data)

    print("\nIncome added successfully!")


# ============================================================
# ADD EXPENSE
# ============================================================

def add_expense(data):
    print("\n" + "=" * 60)
    print("ADD EXPENSE")
    print("=" * 60)

    category = input("Enter expense category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter expense description: ").strip()
    amount = get_amount("Enter expense amount: ")

    record = {
        "category": category,
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    data["expenses"].append(record)
    save_data(data)

    print("\nExpense added successfully!")


# ============================================================
# ADD SAVINGS GOAL
# ============================================================

def add_savings_goal(data):
    print("\n" + "=" * 60)
    print("ADD SAVINGS GOAL")
    print("=" * 60)

    goal_name = input("Enter savings goal: ").strip()

    if not goal_name:
        print("Goal name cannot be empty.")
        return

    target = get_amount("Enter target amount: ")

    goal = {
        "name": goal_name,
        "target": target,
        "saved": 0.0,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    data["savings_goals"].append(goal)
    save_data(data)

    print("\nSavings goal added successfully!")


# ============================================================
# ADD SAVINGS
# ============================================================

def add_savings(data):
    print("\n" + "=" * 60)
    print("ADD SAVINGS")
    print("=" * 60)

    if not data["savings_goals"]:
        print("No savings goals found.")
        print("Please create a savings goal first.")
        return

    view_savings_goals(data)

    index = get_integer(
        "\nEnter goal number: ",
        1
    )

    if index > len(data["savings_goals"]):
        print("Invalid goal number.")
        return

    goal = data["savings_goals"][index - 1]

    amount = get_amount(
        f"Enter amount to add to '{goal['name']}': "
    )

    goal["saved"] += amount

    if goal["saved"] > goal["target"]:
        goal["saved"] = goal["target"]

    save_data(data)

    print("\nSavings updated successfully!")


# ============================================================
# VIEW INCOME
# ============================================================

def view_income(data):
    print("\n" + "=" * 60)
    print("INCOME RECORDS")
    print("=" * 60)

    if not data["income"]:
        print("No income records found.")
        return

    total = 0

    for number, record in enumerate(
        data["income"], 1
    ):
        print(f"\n{number}. {record['source']}")
        print(f"   Amount : ₹{record['amount']:.2f}")
        print(f"   Date   : {record['date']}")

        total += record["amount"]

    print("\n" + "-" * 60)
    print(f"Total Income: ₹{total:.2f}")


# ============================================================
# VIEW EXPENSES
# ============================================================

def view_expenses(data):
    print("\n" + "=" * 60)
    print("EXPENSE RECORDS")
    print("=" * 60)

    if not data["expenses"]:
        print("No expense records found.")
        return

    total = 0

    for number, record in enumerate(
        data["expenses"], 1
    ):
        print(f"\n{number}. {record['category']}")
        print(f"   Description : {record['description']}")
        print(f"   Amount      : ₹{record['amount']:.2f}")
        print(f"   Date        : {record['date']}")

        total += record["amount"]

    print("\n" + "-" * 60)
    print(f"Total Expenses: ₹{total:.2f}")


# ============================================================
# VIEW SAVINGS GOALS
# ============================================================

def view_savings_goals(data):
    print("\n" + "=" * 60)
    print("SAVINGS GOALS")
    print("=" * 60)

    if not data["savings_goals"]:
        print("No savings goals found.")
        return

    for number, goal in enumerate(
        data["savings_goals"], 1
    ):
        target = goal["target"]
        saved = goal["saved"]

        if target > 0:
            progress = (saved / target) * 100
        else:
            progress = 0

        if progress > 100:
            progress = 100

        print(f"\n{number}. {goal['name']}")
        print(f"   Target   : ₹{target:.2f}")
        print(f"   Saved    : ₹{saved:.2f}")
        print(f"   Progress : {progress:.2f}%")

        if saved >= target:
            print("   Status   : GOAL COMPLETED")
        else:
            print("   Status   : IN PROGRESS")


# ============================================================
# CALCULATE TOTAL INCOME
# ============================================================

def total_income(data):
    return sum(
        record["amount"]
        for record in data["income"]
    )


# ============================================================
# CALCULATE TOTAL EXPENSES
# ============================================================

def total_expenses(data):
    return sum(
        record["amount"]
        for record in data["expenses"]
    )


# ============================================================
# FINANCIAL SUMMARY
# ============================================================

def financial_summary(data):
    print("\n" + "=" * 60)
    print("FINANCIAL SUMMARY")
    print("=" * 60)

    income = total_income(data)
    expenses = total_expenses(data)
    balance = income - expenses

    print(f"Total Income    : ₹{income:.2f}")
    print(f"Total Expenses  : ₹{expenses:.2f}")
    print(f"Available Money : ₹{balance:.2f}")

    if income > 0:
        savings_rate = (
            balance / income
        ) * 100

        if savings_rate < 0:
            savings_rate = 0

        print(
            f"Savings Rate    : {savings_rate:.2f}%"
        )

    print("\nFinancial Status:")

    if balance > 0:
        print("🟢 Positive balance")
    elif balance == 0:
        print("🟡 Income and expenses are equal")
    else:
        print("🔴 Expenses are higher than income")


# ============================================================
# EXPENSE ANALYTICS
# ============================================================

def expense_analytics(data):
    print("\n" + "=" * 60)
    print("EXPENSE ANALYTICS")
    print("=" * 60)

    if not data["expenses"]:
        print("No expense records found.")
        return

    categories = {}

    for expense in data["expenses"]:
        category = expense["category"]
        amount = expense["amount"]

        if category not in categories:
            categories[category] = 0

        categories[category] += amount

    total = total_expenses(data)

    print(f"Total Expenses: ₹{total:.2f}")

    print("\nCategory Breakdown")
    print("-" * 60)

    for category, amount in categories.items():

        percentage = (
            amount / total * 100
            if total > 0
            else 0
        )

        print(
            f"{category:<20} "
            f"₹{amount:>10.2f} "
            f"({percentage:.2f}%)"
        )

    highest_category = max(
        categories,
        key=categories.get
    )

    print("\nHighest Spending Category:")
    print(
        f"{highest_category} - "
        f"₹{categories[highest_category]:.2f}"
    )


# ============================================================
# SEARCH TRANSACTIONS
# ============================================================

def search_transactions(data):
    print("\n" + "=" * 60)
    print("SEARCH TRANSACTIONS")
    print("=" * 60)

    keyword = input(
        "Enter keyword to search: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False

    print("\nIncome Results")
    print("-" * 60)

    for record in data["income"]:

        if keyword in record["source"].lower():

            found = True

            print(
                f"{record['source']} - "
                f"₹{record['amount']:.2f}"
            )

    print("\nExpense Results")
    print("-" * 60)

    for record in data["expenses"]:

        if (
            keyword in record["category"].lower()
            or keyword in record["description"].lower()
        ):

            found = True

            print(
                f"{record['category']} - "
                f"{record['description']} - "
                f"₹{record['amount']:.2f}"
            )

    if not found:
        print("No matching transactions found.")


# ============================================================
# UPDATE EXPENSE
# ============================================================

def update_expense(data):
    print("\n" + "=" * 60)
    print("UPDATE EXPENSE")
    print("=" * 60)

    if not data["expenses"]:
        print("No expense records found.")
        return

    view_expenses(data)

    index = get_integer(
        "\nEnter expense number: ",
        1
    )

    if index > len(data["expenses"]):
        print("Invalid expense number.")
        return

    expense = data["expenses"][index - 1]

    category = input(
        "Enter new category: "
    ).strip()

    description = input(
        "Enter new description: "
    ).strip()

    amount = get_amount(
        "Enter new amount: "
    )

    expense["category"] = category
    expense["description"] = description
    expense["amount"] = amount

    save_data(data)

    print("\nExpense updated successfully!")


# ============================================================
# DELETE EXPENSE
# ============================================================

def delete_expense(data):
    print("\n" + "=" * 60)
    print("DELETE EXPENSE")
    print("=" * 60)

    if not data["expenses"]:
        print("No expense records found.")
        return

    view_expenses(data)

    index = get_integer(
        "\nEnter expense number: ",
        1
    )

    if index > len(data["expenses"]):
        print("Invalid expense number.")
        return

    removed = data["expenses"].pop(index - 1)

    save_data(data)

    print(
        f"\nDeleted expense: "
        f"{removed['description']}"
    )


# ============================================================
# BUDGET ANALYSIS
# ============================================================

def budget_analysis(data):
    print("\n" + "=" * 60)
    print("BUDGET ANALYSIS")
    print("=" * 60)

    monthly_budget = get_amount(
        "Enter your monthly budget: ₹"
    )

    expenses = total_expenses(data)

    remaining = monthly_budget - expenses

    print("\n" + "-" * 60)
    print(f"Monthly Budget : ₹{monthly_budget:.2f}")
    print(f"Spent          : ₹{expenses:.2f}")
    print(f"Remaining      : ₹{remaining:.2f}")

    if remaining > 0:
        print("Status         : 🟢 Within Budget")
    elif remaining == 0:
        print("Status         : 🟡 Budget Fully Used")
    else:
        print("Status         : 🔴 Budget Exceeded")


# ============================================================
# DASHBOARD
# ============================================================

def dashboard(data):
    print("\n" + "=" * 60)
    print("PERSONAL BUDGET & SAVINGS DASHBOARD")
    print("=" * 60)

    income = total_income(data)
    expenses = total_expenses(data)
    balance = income - expenses

    completed_goals = 0

    for goal in data["savings_goals"]:
        if goal["saved"] >= goal["target"]:
            completed_goals += 1

    print(f"Income Records       : {len(data['income'])}")
    print(f"Expense Records      : {len(data['expenses'])}")
    print(f"Savings Goals        : {len(data['savings_goals'])}")
    print(f"Completed Goals      : {completed_goals}")

    print("\nFinancial Overview")
    print("-" * 60)

    print(f"Total Income         : ₹{income:.2f}")
    print(f"Total Expenses       : ₹{expenses:.2f}")
    print(f"Available Balance    : ₹{balance:.2f}")


# ============================================================
# EXPORT CSV REPORT
# ============================================================

def export_report(data):
    print("\n" + "=" * 60)
    print("EXPORT BUDGET REPORT")
    print("=" * 60)

    with open(
        REPORT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Type",
            "Category/Source",
            "Description",
            "Amount",
            "Date"
        ])

        for record in data["income"]:

            writer.writerow([
                "Income",
                record["source"],
                "",
                record["amount"],
                record["date"]
            ])

        for record in data["expenses"]:

            writer.writerow([
                "Expense",
                record["category"],
                record["description"],
                record["amount"],
                record["date"]
            ])

    print("\nBudget report exported successfully!")
    print("File:", REPORT_FILE)


# ============================================================
# MAIN MENU
# ============================================================

def main():

    data = load_data()

    while True:

        print("\n" + "=" * 60)
        print("       PERSONAL BUDGET & SAVINGS ANALYZER")
        print("=" * 60)

        print("1. Add Income")
        print("2. Add Expense")
        print("3. Add Savings Goal")
        print("4. Add Savings")
        print("5. View Income")
        print("6. View Expenses")
        print("7. View Savings Goals")
        print("8. Financial Summary")
        print("9. Expense Analytics")
        print("10. Budget Analysis")
        print("11. Search Transactions")
        print("12. Update Expense")
        print("13. Delete Expense")
        print("14. Dashboard")
        print("15. Export CSV Report")
        print("16. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            add_income(data)

        elif choice == "2":
            add_expense(data)

        elif choice == "3":
            add_savings_goal(data)

        elif choice == "4":
            add_savings(data)

        elif choice == "5":
            view_income(data)

        elif choice == "6":
            view_expenses(data)

        elif choice == "7":
            view_savings_goals(data)

        elif choice == "8":
            financial_summary(data)

        elif choice == "9":
            expense_analytics(data)

        elif choice == "10":
            budget_analysis(data)

        elif choice == "11":
            search_transactions(data)

        elif choice == "12":
            update_expense(data)

        elif choice == "13":
            delete_expense(data)

        elif choice == "14":
            dashboard(data)

        elif choice == "15":
            export_report(data)

        elif choice == "16":
            print("\nThank you for using Personal Budget & Savings Analyzer!")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
