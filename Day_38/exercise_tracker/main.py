from nutritionix import Nutritionix
from google_sheet import update_workouts
import datetime as dt

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