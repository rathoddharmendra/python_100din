from quiz_brain import QuizBrain

# Create a quiz brain object
quiz = QuizBrain()

while quiz.still_has_questions():
    quiz.next_question()

print(f"Woo-whoo! You have completed the quiz!\nYour final score is: {quiz.score}/{quiz.question_nr}")
