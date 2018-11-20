import random

def main():


    NUMBERS = "1234567890"
    CONSONANTS = "bcdfghjklmnpqrstvwxyzaeiou"
    SPCGAR = "!@#$%^&*()_+"
    count = int(input("please the length of password"))
    reps = 0

    word_format = "cnscsnssnsccnssncssc"
    word = ""
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

    print(word)
main()