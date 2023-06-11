def capitalize(s):
"""коммент"""    
  
result = ""
    capitalize_next = True
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
def capitalize_naive_one(sentence: str) -> str:
    """Capitalizes the first letters and doesn't preserve the spaces"""

    words = sentence.split()

    for index_word, word in enumerate(words):
        word_list = split_char_by_char_list(word)
        for index_letter, letter in enumerate(word_list):
            if index_letter == 0:
                word_list[index_letter] = letter.upper()
                word = "".join(word_list)
                break
        words[index_word] = word

    return " ".join(words)
