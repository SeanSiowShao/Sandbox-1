import random

def main():


    NUMBERS = "1234567890"
    CONSONANTS = "bcdfghjklmnpqrstvwxyzaeiou"
    SPCGAR = "!@#$%^&*()_+"
    VOWELS = "aeiou"
    count = int(input("please the length of password"))
    reps = 0

    word_format = str(input("Please enter format"))
    word = ""
    if format_test(word_format) == True:
        for kind in word_format:
            if(count >= reps):
                if kind == "c":
                    word += random.choice(CONSONANTS)
                elif kind == "n":
                    word += random.choice(NUMBERS)
                elif kind == "s":
                    word += random.choice(SPCGAR)
                else:
                    word += random.choice(VOWELS)
                reps= reps + 1
    else:
        print("please enter valid string and re-run the program")
    print(word)

def format_test(str_test):
    trig = 0
    print(str_test)
    for w in str_test:
        if (w != "c" and w!="v" and w!="n" and w != "s"):
            print("*")
            return False
            trig = 1
    if trig == 0:
        return True
main()