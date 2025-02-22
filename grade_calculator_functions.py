# Function to get the student's score from user input
def get_student_score():
    while True:
        try:
            # Prompt the user to enter their score
            score = float(input("Enter your score: "))
            
            # Validate the score (must be between 0 and 100)
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


# Function to calculate the grade based on the score
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Main program flow
if __name__ == "__main__":
    # Get the student's score
    score = get_student_score()
    
    # Calculate the grade
    grade = calculate_grade(score)
    
    # Display the result
    print(f"Your Grade is: {grade}")
