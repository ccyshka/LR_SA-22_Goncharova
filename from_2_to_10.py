def int_fract(num):
    int_part = ""
    fract_part = ""
    flag = False
    for i in num:
        if i == ",":
            flag = True
            continue
        if flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    if flag == False:
        return str(int_conv(int_part))
    else:
        return str(int_conv(int_part)) + "," + str(fract_conv(fract_part))[2:]

def int_conv(num):
    index = len(num) - 1
    result = 0
    for i in num:
        result += int(i) * (2 ** index)
        index -= 1
    return result

def fract_conv(num):
    index = 1
    result = 0
    for i in num:
        if index <= len(num):
            result += int(i) * (2 ** -index)
            index += 1
    return result

if __name__ == "__main__":
    num = str(input("Введите двоичное число: "))
    print(int_fract(num))