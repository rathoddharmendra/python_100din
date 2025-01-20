import requests

api_question_data = [
{"type":"boolean","difficulty":"hard","category":"General Knowledge","question":"In Scandinavian languages, the letter &Aring; means river.","correct_answer":"True","incorrect_answers":["False"]},
{"type":"boolean","difficulty":"medium","category":"General Knowledge","question":"The pickled gherkin was first added to hamburgers because a US health law required all fast-food to include a source of Vitamin C.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"medium","category":"General Knowledge","question":"Kissing someone for one minute burns about 2 calories.","correct_answer":"True","incorrect_answers":["False"]},
{"type":"boolean","difficulty":"medium","category":"General Knowledge","question":"Coca-Cola&#039;s original colour was green.","correct_answer":"False","incorrect_answers":["True"]},
{"type":"boolean","difficulty":"easy","category":"General Knowledge","question":"Video streaming website YouTube was purchased in it&#039;s entirety by Facebook for US$1.65 billion in stock.","correct_answer":"False","incorrect_answers":["True"]}
]
def question_response():
    global api_question_data
    base_url = 'https://opentdb.com/api.php'

    parameters = {
        'amount': 10,
        'type': 'boolean'
    }
    response = requests.get(base_url, params=parameters)
    response.raise_for_status()


    # exports response as 'api_question_data'
    api_question_data = response.json()['results']
    return api_question_data

question_response()