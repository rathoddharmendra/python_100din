import pandas as pd

new_row= {
        "website": {
            "email": "current_email",
            "password": "password",
        },
        "website_2": {
            "email": "some_email",
            "password": "1235",
            "password_confirmation": None
        },
        "website_3": {
            "email": "new_email",
            "password": "keloa",
        }
}

# df = pd.DataFrame(new_row.items(), columns=['email', 'password', 'password_confirmation'])
df = pd.DataFrame(new_row.values())
df.columns = ['email', 'password', 'password_confirmation']
df = df.set_index('email')
df.index.name = 'website'

# df = df.drop('password_confirmation', axis=1)

print(df)
