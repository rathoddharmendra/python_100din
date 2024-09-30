## demo at https://appbrewery.github.io/python-day2-demo/

# demo at https://repl.it/@appbrewery/day-2-exercises

print("Hello there, welcome to Tipsy - a tip calculator ")
print('''

___________.__                     
\__    ___/|__|_____  _________.__.
  |    |   |  \____ \/  ___<   |  |
  |    |   |  |  |_> >___ \ \___  |
  |____|   |__|   __/____  >/ ____|
              |__|       \/ \/     

A tip calculating software make available by S&D Inc.
''')

bill = float(input("What was the total bill?  $"))
tip_rate = float(input("How much tip would you like to add? 10, 12, or 20%? "))
people = int(input("How many people to split the bill? "))

bill_incl_tip = bill * (1 + tip_rate/100)
share_pp = round(bill_incl_tip/people, 2)
print(f"Each person should pay: ${share_pp}")
