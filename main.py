import re
import numpy as np

def get_input(input_data_dir):
    #取得input code

    input = [[] for i in range(30)]
    count = 0
    with open(input_data_dir, 'r') as f:
        for line in f:
            input[count].append(line)
            count += 1
    input_code = [0 for i in range(count)]
    input_code = input[0:count]
    del input

    for j in range(len(input_code)):
        #clear the blank in front of the code
        input_code[j] = listToString(input_code[j]).lstrip()
    return input_code

def listToString(s):
    """
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1
    """
    my_list = s
    my_string = " "
    for a in my_list:
        my_string = my_string + ' ' + a
    return my_string

def stringToList(s):
    #s = re.sub("[^\w]", " ", s).split()
    s = re.sub(r",", " ", s)
    s = s.replace("(", " ")
    s = s.replace(")", " ")
    s = s.replace(":", " ")
    s = s.lstrip().rstrip()
    return s.split()

def get_code_element(first_line_code, which_element):
    first_line_code = first_line_code.rstrip("\n")
    first_line_code = stringToList(first_line_code)  # first_line_code變list型式
    if which_element == 0:
        first_line_code_1 = first_line_code[0]
        return first_line_code_1
    elif which_element == 1:
        first_line_code_2 = first_line_code[1]
        return first_line_code_2
    elif which_element == 2:
        first_line_code_3 = first_line_code[2]
        return first_line_code_3
    elif which_element ==3:
        first_line_code_4 = first_line_code[3]
        return first_line_code_4

def print_all_RS(RS, cycle, add_buffer, mul_buffer):
    print("\nCYCLE: " + str(cycle+1) + "----------------------------------------------------------")
    print("\n---RS---ADD---")
    print("RS1| " + RS[0][0] + " |" + RS[0][1] + " |" + RS[0][2] + " |")
    print("RS2| " + RS[1][0] + " |" + RS[1][1] + " |" + RS[1][2] + " |")
    print("RS3| " + RS[2][0] + " |" + RS[2][1] + " |" + RS[2][2] + " |")
    print("---------------")
    print("Buffer: (" + add_buffer[0] + ") " + add_buffer[1] + " " + add_buffer[2] + " " +add_buffer[3])
    print("\n---RS---MUL---")
    print("RS4| " + RS[3][0] + " |" + RS[3][1] + " |" + RS[3][2] + " |")
    print("RS5| " + RS[4][0] + " |" + RS[4][1] + " |" + RS[4][2] + " |")
    print("---------------")
    print("Buffer: (" + mul_buffer[0] + ") " + mul_buffer[1] + " " + mul_buffer[2] + " " + mul_buffer[3])

def print_all_RAT(RAT):
    print("\n---RAT---")
    print("F1| " + RAT[0] + " |")
    print("F2| " + RAT[1] + " |")
    print("F3| " + RAT[2] + " |")
    print("F4| " + RAT[3] + " |")
    print("F5| " + RAT[4] + " |")

def print_all_RF(RF):
    print("\n---RF---")
    print("F1| " + RF[0] + " |")
    print("F2| " + RF[1] + " |")
    print("F3| " + RF[2] + " |")
    print("F4| " + RF[3] + " |")
    print("F5| " + RF[4] + " |")

input_data_dir = "C:/Users/Hans/PycharmProjects/Tomasulo/input.txt"

print_cycle = input("Please enter the cycle you want to print?")

al_code = get_input(input_data_dir)
first_line_code = ""
print("Input Code => ")
for i in range(len(al_code)):
    al_code[i] = al_code[i].replace("\n", "")
    print(al_code[i])#, end=''


#initial intergers for tamasulo algorithm
RF = ["0", "2", "4", "6", "8"]
RAT = ["", "", "", "", ""]
RS = [["None", "None", "None", "status"], ["None", "None", "None", "status"], ["None", "None", "None", "status"], ["None", "None", "None", "status"], ["None", "None", "None", "status"]]
RS_count_ADD = [0, 1, 2] #RS位置剩多少
RS_count_MUL = [3, 4] #RS位置剩多少
code_count = len(al_code) #總共code行數
PC = 0 #現在在處理哪一行code
add_buffer = ["", "", "", "", ""]#RS1 ADD rs rs rd(rd=rs+rs)
mul_buffer = ["", "", "", "", ""]

for cycle in range(100):

    #Issue
    if code_count > 0:
        PC_code = al_code[PC]
        PC_code_1 = get_code_element(PC_code, 0)

        if (PC_code_1 == "ADD" or PC_code_1 == "ADDI" or PC_code_1 == "SUB" or PC_code_1 == "SUBI") and len(RS_count_ADD) > 0:
            RS[RS_count_ADD[0]][0] = PC_code_1
            RS[RS_count_ADD[0]][1] = get_code_element(PC_code, 2)
            RS[RS_count_ADD[0]][2] = get_code_element(PC_code, 3)
            # 把RAT RF上的直填入RS
            for i in range(5):
                for j in range(1, 4):
                    if RS[i][j] == "F1":
                        if RAT[0] != "":
                            RS[i][j] = RAT[0]
                        else:
                            RS[i][j] = RF[0]
                    if RS[i][j] == "F2":
                        if RAT[1] != "":
                            RS[i][j] = RAT[1]
                        else:
                            RS[i][j] = RF[1]
                    if RS[i][j] == "F3":
                        if RAT[2] != "":
                            RS[i][j] = RAT[2]
                        else:
                            RS[i][j] = RF[2]
                    if RS[i][j] == "F4":
                        if RAT[3] != "":
                            RS[i][j] = RAT[3]
                        else:
                            RS[i][j] = RF[3]
                    if RS[i][j] == "F5":
                        if RAT[4] != "":
                            RS[i][j] = RAT[4]
                        else:
                            RS[i][j] = RF[4]

            # 把自己最後結果的值 RS1等代號放入RAT等代號放入RAT
            if get_code_element(PC_code, 1) == "F1":
                RAT[0] = "RS" + str(RS_count_ADD[0] + 1)
            if get_code_element(PC_code, 1) == "F2":
                RAT[1] = "RS" + str(RS_count_ADD[0] + 1)
            if get_code_element(PC_code, 1) == "F3":
                RAT[2] = "RS" + str(RS_count_ADD[0]+1)
            if get_code_element(PC_code, 1) == "F4":
                RAT[3] = "RS" + str(RS_count_ADD[0]+1)
            if get_code_element(PC_code, 1) == "F5":
                RAT[4] = "RS" + str(RS_count_ADD[0]+1)

            RS_count_ADD.pop(0)
            code_count = code_count-1
            PC += 1

        if (PC_code_1 == "MUL" or PC_code_1 == "DIV") and len(RS_count_ADD) > 0:
            RS[RS_count_MUL[0]][0] = PC_code_1
            RS[RS_count_MUL[0]][1] = get_code_element(PC_code, 2)
            RS[RS_count_MUL[0]][2] = get_code_element(PC_code, 3)
            # 把RAT RF上的直填入RS
            for i in range(5):
                for j in range(1, 4):
                    if RS[i][j] == "F1":
                        if RAT[0] != "":
                            RS[i][j] = RAT[0]
                        else:
                            RS[i][j] = RF[0]
                    if RS[i][j] == "F2":
                        if RAT[1] != "":
                            RS[i][j] = RAT[1]
                        else:
                            RS[i][j] = RF[1]
                    if RS[i][j] == "F3":
                        if RAT[2] != "":
                            RS[i][j] = RAT[2]
                        else:
                            RS[i][j] = RF[2]
                    if RS[i][j] == "F4":
                        if RAT[3] != "":
                            RS[i][j] = RAT[3]
                        else:
                            RS[i][j] = RF[3]
                    if RS[i][j] == "F5":
                        if RAT[4] != "":
                            RS[i][j] = RAT[4]
                        else:
                            RS[i][j] = RF[4]

            # 把自己最後結果的值 RS1等代號放入RAT等代號放入RAT
            if get_code_element(PC_code, 1) == "F1":
                RAT[0] = "RS" + str(RS_count_MUL[0]+1)
            if get_code_element(PC_code, 1) == "F2":
                RAT[1] = "RS" + str(RS_count_MUL[0] + 1)
            if get_code_element(PC_code, 1) == "F3":
                RAT[2] = "RS" + str(RS_count_MUL[0]+1)
            if get_code_element(PC_code, 1) == "F4":
                RAT[3] = "RS" + str(RS_count_MUL[0]+1)
            if get_code_element(PC_code, 1) == "F5":
                RAT[4] = "RS" + str(RS_count_MUL[0]+1)
            RS_count_MUL.pop(0)
            code_count = code_count-1
            PC += 1
    #Capture
    if add_buffer[0]!= "":
        if add_buffer[1] == "ADD" or add_buffer[1] == "ADDI":
            add_buffer[4] = str(int(add_buffer[2]) + int(add_buffer[3]))
        elif add_buffer[1] == "SUB" or add_buffer[1] == "SUBI":
            add_buffer[4] = str(int(add_buffer[2]) - int(add_buffer[3]))
        # 把值給RS
        for i in range(5):
            for j in range(3):
                if RS[i][j] == add_buffer[0]:
                    RS[i][j] = add_buffer[4]
        # 把值給RAT
        for i in range(5):
            if RAT[i] == add_buffer[0]:
                RAT[i] == add_buffer[4]
        # 把值給RF
        for i in range(5):
            if str(i+1) == add_buffer[0].replace("RS", ""):
                RF[i] = add_buffer[4]
        RS[int(add_buffer[0].replace("RS", ""))-1]=["None", "None", "None", "status"]
        RS_count_ADD.append(int(add_buffer[0].replace("RS", "")))

    if mul_buffer[0]!= "":
        if mul_buffer[1] == "DIV" or mul_buffer[1] == "DIVI":
            mul_buffer[4] = str(int(mul_buffer[2]) // int(mul_buffer[3]))
        elif mul_buffer[1] == "MUL" or mul_buffer[1] == "MULI":
            mul_buffer[4] = str(int(mul_buffer[2]) * int(mul_buffer[3]))
        # 把值給RS
        for i in range(5):
            for j in range(3):
                if RS[i][j] == mul_buffer[0]:
                    RS[i][j] = mul_buffer[4]
        # 把值給RAT
        for i in range(5):
            if RAT[i] == mul_buffer[0]:
                RAT[i] == mul_buffer[4]

        # 把值給RF
        for i in range(5):
            if str(i + 1) == mul_buffer[0].replace("RS", ""):
                RF[i] = mul_buffer[4]

        RS[int(mul_buffer[0].replace("RS", ""))-1]=["None", "None", "None", "status"]
        RS_count_MUL.append(int(mul_buffer[0].replace("RS", "")))

    add_buffer = ["", "", "", "", ""]  # RS1 ADD rs rs rd(rd=rs+rs)
    mul_buffer = ["", "", "", "", ""]

    #Dispatch
    for k in range(3):
        if RS[k][1] != "None" and RS[k][2] != "None" and RS[k][1] != "RS1" and RS[k][1] != "RS2"and RS[k][1] != "RS3"and RS[k][1] != "RS4"\
            and RS[k][1] != "RS5" and RS[k][2] != "RS1" and RS[k][2] != "RS2"and RS[k][2] != "RS3"and RS[k][2] != "RS4"and RS[k][2] != "RS5":
            RS[k][3] = "Done"
    for l in range(3, 5):
        if RS[l][1] != "None" and RS[l][2] != "None" and RS[l][1] != "RS1" and RS[l][1] != "RS2" and RS[l][1] != "RS3" and RS[l][1] != "RS4"\
                and RS[k][1] != "RS5" and RS[l][2] != "RS1" and RS[l][2] != "RS2" and RS[l][2] != "RS3" and RS[l][2] != "RS4" and RS[l][2] != "RS5":
            RS[l][3] = "Done"

    for m in range(3):
        if RS[m][3] == "Done":
            add_buffer[0] = "RS" + str(m+1)
            add_buffer[1] = RS[m][0]
            add_buffer[2] = RS[m][1]
            add_buffer[3] = RS[m][2]
            break

    for n in range(3, 5):
        if RS[n][3] == "Done":
            mul_buffer[0] = "RS" + str(n+1)
            mul_buffer[1] = RS[n][0]
            mul_buffer[2] = RS[n][1]
            mul_buffer[3] = RS[n][2]
            break


    if cycle+1 == int(print_cycle):
        print_all_RS(RS, cycle, add_buffer, mul_buffer)
        print_all_RAT(RAT)
        print_all_RF(RF)
        break