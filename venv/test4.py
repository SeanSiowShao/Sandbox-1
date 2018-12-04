import random
def main():
    names = ["Jack", "Jill", "Harry"]
    dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    merge_var = merge(names,dobs)
    print(merge_var)

def merge(l1,l2):
    ret_dict = {}
    for i in range(3):
        ret_dict[l1[i]]=l2[i]
    return ret_dict


main()