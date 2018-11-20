def main():
    name = str(input("Please input name"))
    file = open("testfile.txt", "w")
    file_num = open("numbers.txt", "r+")
    total = 0
    for line in file_num:
        total = total+int(line)

    file.write("your name is "+name)
    print(total)
    file_num.write("\n"+str(total))
    file.close()
    file_num.close()

main()