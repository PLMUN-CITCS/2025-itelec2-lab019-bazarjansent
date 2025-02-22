def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    try:
        score = float(input("Enter your score: "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"Your Grade is: {grade}")
        else:
            print("Invalid score! Please enter a score between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
