from raw_data import question_data
from question_model import Question
from raw_random_question_data import random_question_data
from raw_api_question_data import api_question_data

# Create a question bank
question_bank = [ Question(question['text'], question['answer']) for question in question_data]
random_question_bank = [ Question(question['question'], question['correct_answer']) for question in random_question_data]
api_question_bank = [ Question(question['question'], question['correct_answer']) for question in api_question_data]