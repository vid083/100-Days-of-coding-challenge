def format_name(first,last):
    if first == "" or last == "":
        return "Invalid name"
    formatted_first = first.title()
    formatted_last = last.title()
    return f"Fullname: {formatted_first} {formatted_last}"

# format_name('aNgelA','yU')
print(format_name(input("wat is your first name? "), input("wat is your last name? ")))