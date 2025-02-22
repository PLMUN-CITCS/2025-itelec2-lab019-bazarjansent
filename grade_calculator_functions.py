def get_student_score() -> float:
    """
    Prompts the user to enter their score and validates the input.

    Returns:
        float: The validated numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.

    Args:
        score (float): The student's score.

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
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
    """
    Main program flow:
    1. Gets the student's score using `get_student_score`.
    2. Calculates the grade using `calculate_grade`.
    3. Displays the grade to the user.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")


if __name__ == "__main__":
    main()
