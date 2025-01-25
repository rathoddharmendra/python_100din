Problem Statement:

Create a webpage application to play high_or_low game

Language - Python
```

Build Command - pip install -r requirements.txt

Start Command - gunicorn app:app

```


UJM:
user open into '/' -> displays random_giphy, and asks user to enter a number between 1-100 -loop-> users enters the number in path '/<int>'
condition: 
    - if higher than chosen number
      -> displays page "high number"
    - if lower than chosen number
      -> displays page "low number"
    - if same as chosen number
      -> displays 'found the number' page


ToDo:
1. create home page application at '/' using Flask
    