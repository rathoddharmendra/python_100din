from nutritionix import Nutritionix
from google_sheet import update_workouts
import datetime as dt

# view results in https://docs.google.com/spreadsheets/d/1W6KCANQ-9Swoo5C_LIjmkw0kZN7y4ktLxtrHLEeJ9X8/edit?gid=0#gid=0

nutritionix = Nutritionix()
exercises = nutritionix.record_exercise()

for exercise in exercises:
    current_date = dt.datetime.now()
    body = {
        "workout": {
            "date": current_date.strftime('%d/%m/%Y'),
            "time": current_date.strftime('%H:%M'),
            "exercise": exercise["exercise_name"],
            "duration": exercise["duration_min"],
            "calories": exercise["calories_burned"]
        }
    }
    update_workouts(body)