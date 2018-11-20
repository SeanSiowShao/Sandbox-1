def main():
    choice = int(input("Please enter 1. for ascii to alphabet or 2. for the reverse"))
    if choice == 1:
        asc = int(input("Enter ascii between 33 and 127"))
        if 127 > asc > 33:
            print(chr(asc))
    elif choice == 2:
        cha = (input("Enter a character"))
        print(ord(cha))
main()