def main():
    inp = str(input("enter string"))
    pos = 0
    ns = ""
    if(len(inp)>0):
        for w in inp:
            pos = pos + 1
            if(pos % 2 ==1):
                ns = ns + w
        print("the new string is" + ns)
main()