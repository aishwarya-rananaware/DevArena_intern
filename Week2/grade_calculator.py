# Function to calculate the grade based on marks

def calculate_grade(marks):

     # Check if marks are 90 or above
    if marks >= 90:
        return "A" ,"Excellent! keep up the grate work !"

    # Check if marks are between 80 and 89
    elif marks>=80:
        return "B" ,"Very Good! Keep it up"

    # Check if marks are between 70 and 79
    elif marks>=70:
        return "c" ,"Good job! keep it up"

    # Check if marks are between 60 and 69
    elif marks>=60:
        return "D" ,"You passed ! keep working hard !"

    # If marks are below 60
    else:
        return "F" , "Don't give up! You can improve!" 
    
# Get the student's name from the user
student_name=input("Stdent Name   ")

# Keep asking for marks until the user enters valid marks
while True:
    try:
        # Get marks from the user and convert the input into an integer
        marks=int(input("Enter your marks  "))
         # Check whether marks are within the valid range of 0 to 100
        if 0<=marks<=100:
            break

         # If marks are outside the valid range, display an error message
        else:
            print("Invalid input ! Please enter marks from 0 to 100")
            
    # Handle the error if the user enters something that is not a number
    except:
        print("Invalid input ! please enter number")

# Call the function and receive the grade and message
grade,message=calculate_grade(marks)

# Display the final result
print("\n RESULT FOR",student_name.upper())
print("Marks",marks,"/100")
print("Grade", grade)
print("Message",message)