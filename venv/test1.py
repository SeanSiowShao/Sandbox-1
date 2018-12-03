def main():
    li = [1]
    Stop = True
    while(Stop == True):
        stri = str(input("Please enter a string"))
        if stri != "":
            li.append(stri)
        else:
            for e in range(len(li)):
                for i in range (len(li)):
                    if e != i:
                        if li[e] == li[i]:
                            print("Repeted strings:"+li[e])
            Stop = False

main()