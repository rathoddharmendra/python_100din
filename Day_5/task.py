import random

fruits = ["apple", "banana", "cherry", "date", "elderberry"]    
# for fruit in fruits:
#     print(f"I'm eating a {fruit} right now.")
#     print(f"Now, I have {random.randint(0, 10)} pieces left.")

# Highest score exexrice #5.39
student_scores = [random.randint(0, 250) for x in range(50)]
print(student_scores)

def calculate_highest_score(scores:list) -> int:
    """
    Returns the highest score in a list of scores.
    Args:
        scores (List[int]): A list of student scores.
    """
    highest_score = 0
    for score in scores:
        if score > highest_score:
            highest_score = score
    return highest_score


# Call the function with the list of student scores.
print(f"The highest score is: {calculate_highest_score(student_scores)}")