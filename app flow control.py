"""
Name: Valentin Esparza
Date: May 24, 2026
Description: This program displays a spreadsheet automation menu,
checks if the user's selection is valid, and displays the selected
option along with the current date and time.
"""

from datetime import datetime

# Display application title
print("valesp7141 Spreadsheet Automation Menu")

# Store menu options in a list
menuOptions = [
    "1. Create Spreadsheet",
    "2. Update Spreadsheet",
    "3. Delete Spreadsheet",
    "4. View Spreadsheet"
]

# Display menu using a for loop
for option in menuOptions:
    print(option)

# Get user choice
userChoice = input("Select a menu option: ")

# Validate user choice
if userChoice in ["1", "2", "3", "4"]:
    currentDateTime = datetime.now()
    print(f"\nOption {userChoice} selected.")
    print(f"Current date and time: {currentDateTime}")
else:
    print("Error: Invalid choice selected.")
