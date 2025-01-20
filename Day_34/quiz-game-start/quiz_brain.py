from question_bank import question_bank, random_question_bank, api_question_bank

"""
ASK USER QUESTIONS FROM A LIST

next_question(): Asks user the next question from question_bank list, and returns true or false depending on user's answer.
   
"""

# TODO: Ask questions from the list
# TODO: KEEP TRACK OF QUESTION FROM A LIST
# TODO: Retrieve next questions and update index
# TODO: ask question to user, take input as question text and store answer

class QuizBrain:
    def __init__(self):
        # self.question_bank = question_bank
        self.question_bank = api_question_bank
        self.question_nr = 0
        self.score = 0
    

    def next_question(self) -> None:
        # if len of questions are over, declare winner
        current_question = self.question_bank[self.question_nr]
        user_answer = input(f'Q.{self.question_nr + 1}: {current_question.text} (true/false)?: ').lower()
        self.question_nr += 1
        self.check_answer(current_question.answer.lower(), user_answer)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer == user_answer:
            self.score += 1
            print('You guessed it correct!')
        else:
            print(f'Incorrect! you guessed it wrong!')
            
        print(f"The correct answer is: {correct_answer}")
        print(f'Your current score is {self.score}/{self.question_nr} \n\n')

    def still_has_questions(self) -> bool:
        return self.question_nr < len(self.question_bank)

