# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2023,Created started script
# RRoot,1.1.2023,Added pseudo-code to start assignment 9
# DMichalove,06.11.23,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# Import Modules --------------------------------------------------------- #
if __name__ == "__main__":
    import os.path
    import DataClasses as D # data classes
    import ProcessingClasses as P # processing classes
    import IOClasses as IO # io classes
else:
    raise Exception("This file was not created to be imported")

# Variables -------------------------------------------------------------- #
lstTable = []
answer = ""
file_name_str = "EmployeeDataNew.txt"

# Main Body of Script  --------------------------------------------------- #
if os.path.isfile(file_name_str) == True:
    lstFileData = P.FileProcessor.read_data_from_file(file_name_str)
    for line in lstFileData:
        lstTable.append(D.Employee(line[0], line[1], line[2].strip()))
else:
    P.FileProcessor.save_data_to_file(file_name_str, lstTable)

while answer != "4": # If the user selects 4 then the while loop will be broken
    IO.EmployeeIO.print_menu_items() # Prints menu to user
    answer = IO.EmployeeIO.input_menu_options()
    if answer == "1": # Shows current employee data
        IO.EmployeeIO.print_current_list_items(lstTable)
    if answer == "2": # Add new employee data
        toSave = IO.EmployeeIO.input_employee_data()
        lstTable.append(toSave)
        print(toSave)
    if answer == "3": # Save employee data to file
        P.FileProcessor.save_data_to_file(file_name_str, lstTable)
    # if answer == "4": # Exit program
print("Thank you!")