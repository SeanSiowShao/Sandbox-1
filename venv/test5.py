"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    st_in = input("please enter the sentance")
    dict_1 = {}
    i = 0
    total_word =""
    inital_count = 1
    for word in st_in:
        if word == " ":
            i = i+1
            if total_word not in dict_1:
                dict_1[total_word] = inital_count
            else:
                dict_1[total_word] += 1
            total_word = ""

        else:
            total_word = total_word + word
    print(dict_1)

main()