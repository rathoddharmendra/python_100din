def calculate_love_score(person_one: str, person_two: str) -> None:
    """
    Prints love score by checking letter match
    
    Args:
        person_one(str): name of a person
        person_two(str): name of a person
   
    """
    
    love_score = 0
    combined_name_letters = list((person_one + person_two).lower())
    
    # checks match and updates score
    #love_score += sum(1 for letter in combined_name_letters if letter in combined_bench_letter)
    
    true_score = sum(1 for letter in combined_name_letters if letter in "true")
    love_score = sum(1 for letter in combined_name_letters if letter in "love")
    
    print(f"{true_score}{love_score}")