def format_name(first_name: str, last_name: str) -> str:
    full_name = (first_name + " " + last_name).title()
    # new_learnen : title() makes each word start with capital letter against capitalize()
    return f"{full_name}"

print(format_name("JOhN", "dOe"))