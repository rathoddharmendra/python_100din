from question_bank import api_question_bank
from question_model import Question
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
        self.current_question: Question
    
    def next_question(self) -> str:
        # if len of questions are over, declare winner
        self.current_question = self.question_bank[self.question_nr]
        print(self.current_question.text + ' ' + self.current_question.answer)
        self.question_nr += 1
        return f'Q.{self.question_nr}: {self.current_question.text}'

    def check_answer(self, response: str) -> bool:
        if self.current_question.answer == response:
            return True
        else:
            return False

    def still_has_questions(self) -> bool:
        print(f'{self.question_nr} vs {len(self.question_bank)}')
        return self.question_nr < len(self.question_bank)

