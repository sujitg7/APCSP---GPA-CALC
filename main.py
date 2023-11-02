# Defines a function called calculate_GPA with an optional filename parameter.
def calculate_GPA(filename=None): 
 # Defines a dictionary that maps class types to GPA values for each grade.
    class_grade = {  
        "Career Prep" : {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0},
        "CP" : {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0},
        "Honors" : {"A": 4.5, "B": 3.5, "C": 2.5, "D": 1.5, "F": 0.5},
        "AP" : {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "F": 1.0},
        "AP+" : {"A": 5.5, "B": 4.5, "C": 3.5, "D": 2.5, "F": 1.5}
    }
    total_gpa = 0 # A variable with an intial value of 0 to store the total GPA points.
    total_classes = 0 # Initalizes a variable to count the total number of classes.
    lines = 0 # Count the numbers of lines read from the file.
  # Checks if 'filename' has been provided. If not None, then read from the file. 
    if filename is not None:
      # Opens the 'filename' in read mode 'r' using a 'with' statement.
      with open(filename, 'r') as f:
        for line in f: #It will go through each line in the file. 
          lines += 1 #Increases 'lines' by 1 every line 
          class_type, grade = line.strip().split() # Splits line into class_type, grade
          try:
            # Adds the GPA value for the class they entered and their total GPA. 
            total_gpa += class_grade[class_type][grade]
            # Increase the total number of classes entered.
            total_classes += 1
          except KeyError:
            # If class type / grade is not found in the dicitonary then prints 'invalid'
                print("Invalid class type or grade")
    if filename is None or lines == 0:
# A while loop that allows the user to input multiple classes and grades until 'done'.
      while True:
        # Makes the user enter what their class level is and type 'done' when finished.
        class_type = input("Enter the class type or 'done' if finished: ")
        # Checks if the user wants to finish entering their classes. 
        if class_type.lower() == 'done':
            break
        # Prompts the user to enter their grade for their class. 
        grade = input("Enter your grade for this class: ")

        try:
          # Adds the GPA value for the class they entered and their total GPA. 
            total_gpa += class_grade[class_type][grade]
          # Increase the total number of classes entered.
            total_classes += 1
        except KeyError:
          # If class type or grade is not found in the dicitonary then prints 'invalid'.
            print("Invalid class type or grade")
# Calculate the avgerage GPA and return it. If no classes were entered then return '0'.
    return total_gpa / total_classes if total_classes else 0
# Calculate GPA from a file named 'GPA.txt and rounds to the nearest thousand.
a = (calculate_GPA('GPA.txt'))
print(round(a,3))
