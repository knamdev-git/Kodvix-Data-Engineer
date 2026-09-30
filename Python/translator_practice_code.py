#  phrase = "kanha" -> translated_word = "kgnhg"
def translator(phrase) : 
    translated_word = phrase
    for each_letter in phrase : 
        if each_letter in "y": 
            translated_word = translated_word.replace(each_letter, "g")

    return translated_word


# main code 

phrase = "Payal"
print(translator(phrase))
