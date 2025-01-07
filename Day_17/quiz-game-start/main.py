import random
from data import question_data
from question_model import Question

question_bank = [ Question(question['text'], question['answer']) for question in question_data]

# print([f'{question.text}:{question.answer}\n' for question in question_bank])