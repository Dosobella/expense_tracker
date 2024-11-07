# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:57:03 2024

@author: Dosobella
"""


def add_expense(category, amount):
    """
    Adds an expense to the expense list.

    Args:
        category (str): The category of the expense.
        amount (float): The amount of the expense.
    """
    expense = {"category": category, "amount": amount}
    expenses.append(expense)


def get_total_expense():
    """
    Calculates the total expense by summing up all expenses.

    Returns:
        float: The total expense.
    """
    total = sum(expense["amount"] for expense in expenses)
    return total


def get_expense_by_category(category):
    """
    Calculates the total expense for a specific category.

    Args:
        category (str): The category to filter by.

    Returns:
        float: The total expense for the category.
    """
    category_expenses = [
        expense for expense in expenses if expense["category"] == category]
    category_total = sum(expense["amount"] for expense in category_expenses)
    return category_total


# Initialize an empty list to store expenses
expenses = []

# Main loop for user interaction
while True:
    command = input("\nEnter a command (add, total, category, quit): ").lower()

    if command == "add":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        add_expense(category, amount)
        print("Expense added successfully!")

    elif command == "total":
        total_expense = get_total_expense()
        print(f"Total expense: ${total_expense:.2f}")

    elif command == "category":
        category = input("Enter expense category: ")
        category_total = get_expense_by_category(category)
        if category_total > 0:
            print(f"Total expense for '{category}': ${category_total:.2f}")
        else:
            print(f"No expenses found for category '{category}'.")

    elif command == "quit":
        print("Exiting expense tracker...")
        break

    else:
        print("Invalid command. Please try again.")

print("\nThank you for using the expense tracker!")
