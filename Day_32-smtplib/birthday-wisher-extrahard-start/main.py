##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv [x]

# 2. Check if today matches a birthday in the birthdays.csv [x]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


from birthday import Persons
from conn import Connection
from draft_letter import DraftLetter

conn = Connection()
persons = Persons()
letter = DraftLetter()

for person in persons:
    if person.is_birthday:
        body = letter.draft_letter(person.name)
        if body:
            conn.send_email(to_address=person.email, subject="Happy Birthday!", body=body)



