def format_name(first_name: str, last_name: str) -> str:
     """
    Returns a formatted full name.
    
    Args:
        first_name (str): The first name.
        last_name (str): The last name.
    Returns:
        full_name (str): The formatted full name.
    """
    
    full_name = (first_name + " " + last_name).title()
    # new_learnen : title() makes each word start with capital letter against capitalize()
    return f"{full_name}"

print(format_name("JOhN", "dOe"))


