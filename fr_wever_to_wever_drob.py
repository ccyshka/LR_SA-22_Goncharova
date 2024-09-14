def int_fract():
    try:
        dec_num = str(input("Введите десятичное число: "))
        base = int(input("Введите основание: "))
    except:
        return("Введите корректное число в десятичной системе!")
    alf = {
        "0" : "0", 
        "1" : "1", 
        "2" : "2", 
        "3" : "3", 
        "4" : "4", 
        "5" : "5", 
        "6" : "6", 
        "7" : "7", 
        "8" : "8", 
        "9" : "9", 
        "10" : "A", 
        "11" : "B", 
        "12" : "C",
        "13" : "D",
        "14" : "E",
        "15" : "F",
        }
    int_part = ""
    fract_part = ""
    flag = False
    for i in dec_num:
        if i == ",":
            flag = True
            continue
        if flag == False:
            int_part = int_part + i
        else:
            fract_part = fract_part + i
    if flag == False:
        fract_part = "0"
    return str(int_conv(int_part, base, alf)) + "," + str(fract_conv(fract_part, base, alf))

def int_conv(int_part, base, alf):
    if int(int_part) == 0:
        return "0"
    quotient = int(int_part)
    remains = ""
    while (quotient > (base - 1)):
        remains = alf[str(quotient % base)] + remains
        quotient = quotient // base
    else:
        remains = alf[str(quotient)] + remains
    return remains

def fract_conv(fract_part, base, alf):
    if int(fract_part) == 0:
        return 0
    result = ""
    compose = str(fract_part)
    iter = 0
    while (int(compose[-(len(fract_part)):]) > 0) and (iter < 100):
        iter = iter + 1
        compose = str(int(compose[-(len(fract_part)):]) * base)
        if base == 2:
            if int(compose) < 10 ** len(fract_part):
                compose = "0" + compose
        elif base == 8:
            if int(compose) < 10 ** len(fract_part):
                compose = "0" + compose
        elif base == 16:
            if int(compose) < 10 ** len(fract_part):
                compose = "0" + alf[compose[0:1]]
        result = result + compose
    return result
        
if __name__ == "__main__":
    print(int_fract())