# Function to determine the grade based on the score
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

# Main program
if __name__ == "__main__":
    try:
        # Ask the user to enter their score
        score = float(input("Enter your score: "))
        
        # Validate the score
        if 0 <= score <= 100:
            # Calculate the grade
            grade = calculate_grade(score)
            print(f"Your Grade is: {grade}")
        else:
            print("Invalid score! Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
