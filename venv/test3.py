def main():
    num_entry = int(input("please input the number of people"))
    name_li = []
    age_li = []
    for i in range(num_entry):
        name_li.append(input("Enter name "+str(i)))
        age_li.append(int(input("Enter age " + str(i))))
    sort_li = sort(name_li,age_li)
    print(str(name_li[sort_li]) +" "+ str(age_li[sort_li]))

def sort(name_li, age_li):
    max_age = 0
    max_age_index = 0
    for i in range(len(age_li)):
        if max_age < age_li[i]:
            max_age = age_li[i]
            max_age_index = i
    return max_age_index

main()