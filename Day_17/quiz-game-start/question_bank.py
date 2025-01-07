from data import question_data
from question_model import Question
from random_question_bank import random_question_data

# Create a question bank
question_bank = [ Question(question['text'], question['answer']) for question in question_data]
random_question_data = [ Question(question['question'], question['correct_answer']) for question in random_question_data]
