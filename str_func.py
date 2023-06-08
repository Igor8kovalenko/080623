def capitalize(s):
    result = ""
    capitalize_next = True
"""реклама"""
    for i in range(len(s)):
        if s[i] == " ":
            result += " "
            capitalize_next = True
        elif capitalize_next:
            result += s[i].upper()
            capitalize_next = False
        else:
            result += s[i]

        if s[i] in ".!?":
            capitalize_next = True


    return result
