import random
def main():
    num_qp = int(input("How many quick pics do you want?"))
    final_list= []
    temp_list=[]
    for i1 in range(num_qp):
        i2 = 0
        while i2 != 6:
            ran_int = random.randint(1, 45)
            if ran_int not in temp_list:
                temp_list.append(ran_int)
                i2= i2 + 1

        temp_list.sort()
        final_list.append(temp_list)
        temp_list = []
    for e in final_list:
        print(e)

main()