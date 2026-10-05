def main() : 
# {
    word = "Kanha"
    string = 'ama'
    number = 30
    # 1 1 2 3 5 8
    print(string == reverseString(string))
    print("There is ",countVowels(word)," vowels in ",word)
    print("Frequency of words are : ",frequencyCharacter(word))
    
    statement = 1 if(isPrime(number)) else "not prime"
    print(number,"This is", statement)
    print(number,"factorial is",fact(number))
    print("Fibonacci of",number,"is",fabonacci(number))

    phrase = "I am Kanha"
    print(translator(phrase))

# }    

#  phrase = "kanha" -> translated_word = "kgnhg"
def translator(phrase) : 
    translated_word = phrase
    for each_letter in phrase : 
        if each_letter in "aeiou" : 
            translated_word.replace(each_letter, "g")

    return translated_word


def recursion(series) : 
    return 
# fibonacci code 
def fabonacci(steps):
    if steps == 1 : return 1
    if steps == 0 : return 0
    if steps < 0 : return -1
    
    return fabonacci(steps-1) + fabonacci(steps-2);


#reverse the string
def reverseString(string) :
    rev_string = ""
    for i in range(len(string)-1, -1, -1) :    
        rev_string += string[i]
    
    return rev_string
    
#count the vowels in a string
def countVowels(word) : 
    count = 0
    for eachLetter in word: 
        if eachLetter in "aeiou" : 
            count += 1
    return count
    
#Frequency of characters in a word 
def frequencyCharacter(word) :
    freq = {}
    
    for eachLetter in word : 
        freq[eachLetter] = freq.get(eachLetter, 0) +1
    return freq

# check if the value is prime    
def isPrime(digit) :
    for i in range(2, digit) : 
        if digit % i == 0 : 
            return False
            
    return True


# factorial code
def fact(number) : 
    if number < 0 : return "Undefined"
    if (number == 1 or number == 0) :
        return 1
    return number * fact(number-1)

    
if __name__ == '__main__' :
    main()
