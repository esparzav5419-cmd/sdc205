from datetime import datetime
# This application displays a Spreadsheet Automation Menu, collects the
# user's menu selection, and confirms the choice along with the current date and time.

# Display application name and menu options
print("valesp7141 Spreadsheet Automation Menu")
print()
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")
print()

# The next line retrieves the inputted option and stores into the variable called option.
option = input("Enter the number of your selection: ")

# Confirm selection and display current date and time
print()
print("You selected option", option)
print("The time and date is", str(datetime.now()))
