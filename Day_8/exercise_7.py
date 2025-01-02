def life_in_weeks(age: int) -> str:
    """
    Calculates and returns number of weeks until 90 years old.
    Args:
        Age(int)
    Returns
        "You have x weeks left.", where x is the no. of weeks left until 90
    """
    no_of_years_until_90 = 90 - age
    no_of_weeks_until_90 = no_of_years_until_90 * 52
    
    print(f"You have {no_of_weeks_until_90} weeks left.")