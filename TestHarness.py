# ------------------------------------------------- #
# Title: <Listing08>
# Description: <A main module for testing>
# ChangeLog: (Who, When, What)
# <DMichalove, 11.06.23, Created Script>
# ------------------------------------------------- #
if __name__ == "__main__":
    #import DataClasses as D #data classes
    #import ProcessingClasses as P #processing classes

    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# #test data module
# objP1 = D.Person("Bob", "Smith")
# objP2 = D.Person("Sue", "Jones")
# lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))
#
# # Test processing module
# P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
# lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
# for row in lstFileData:
#     p = D.Person(row[0],row[1])
#     print(p.to_string().strip(), type(p))

#Test data module
# objP3 = D.Employee(1, "Bob", "Smith")
# objP4 = D.Employee(2, "Sue", "Jones")
# lstTable = [objP3, objP4]
# for row in lstTable:
#     print(row.to_string(), type(row))
#
# # Test processing module
# P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
# lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
# lstTable.clear() # clears list before loading frm file
# for line in lstFileData: # Converts list of strings to Employee Objects
#     lstTable.append(D.Employee(line[0], line[1], line[2].strip()))
# for row in lstTable: # show Employee data frm refilled list
#     print(row.to_string(),type(row))

# Test IO classes
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
# Fp.save_data_to_file("EmployeeData.txt", lstTable)
# lstFileData = Fp.read_data_from_file("EmployeeData.txt")
# lstTable.clear()
# for line in lstFileData:
#     lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:
#     print(row.to_string(), type(row))

# Test IO classes
# Eio.print_menu_items()
# Eio.print_current_list_items(lstTable)
# print(Eio.input_employee_data())
# print(Eio.input_menu_options())
# Eio.try_again_question()
#print(Eio.try_again_question())
