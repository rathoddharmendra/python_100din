from data import question_data
from question_model import Question

# Create a question bank
question_bank = [ Question(question['text'], question['answer']) for question in question_data]

