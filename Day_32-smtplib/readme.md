# TODO:
* [x] create a new dev account
```
dee.services.berlin@gmail.com
```
* [x] send an email to the dev account

first problem statement:

1. check if it's Saturday, and send a quote to the recipients address

```
# check if Saturday:
#     select random quote
#     create body message
#     send_email
# SEND EMAIL
# send_email("Love You", "I know you care for me!\n And that's why you are irritated with my pain\n No matter, I will love you always bubu \n Yours, Dee")
```

# enabled cron job to trigger everyday at 11:11 AM on Saturday
11 - min
11 - hours
6 - Saturday
```
11 11 * * 6 /usr/bin/python3 /Users/mac_dee/Documents/Dee/code/../Day_32-smtplib/automated_birthday_wisher/main.py > /Users/mac_dee/Documents/Dee/code/../Day_32-smtplib/automated_birthday_wisher/cron_output.log 2>&1
```
