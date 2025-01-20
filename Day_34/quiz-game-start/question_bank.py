from question_model import Question
from raw_api_question_data import api_question_data
from html import unescape

# Create a question bank
api_question_bank = [ Question(unescape(question['question']), question['correct_answer']) for question in api_question_data]