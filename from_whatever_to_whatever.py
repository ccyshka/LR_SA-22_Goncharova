import math
def int_fract():
    try:
        num = str(input("Введите число: "))
        input_base = int(input("Введите начальную СС: "))
        output_base = int(input("Введите итоговую СС: "))
    except ValueError:
        return "Введите корректное число и основания систем счисления!"

    if input_base < 2 or input_base > 16 or output_base < 2 or output_base > 16:
        return "Основание системы счисления должно быть корректным!"
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
    if ',' in num:
        int_part, fract_part = num.split(',')
    else:
        int_part = num
        fract_part = "0"

    int_part_dec = int_conv_to_decimal(int_part, input_base)
    fract_part_dec = fract_conv_to_decimal(fract_part, input_base)
    int_result = int_conv_from_decimal(int_part_dec, output_base, alf)
    fract_result = fract_conv_from_decimal(fract_part_dec, output_base, alf)
    return str(int_result) + "," + str(fract_result) 

def int_conv_to_decimal(int_part, base):
     return int(int_part, base)

def fract_conv_to_decimal(fract_part, base):
    fract_value = 0
    for i, digit in enumerate(fract_part, 1):
        fract_value += int(digit, base) / (base ** i)
    return fract_value

def int_conv_from_decimal(int_part, base, alf):
    if int_part == 0:
        return "0"
    remains = ""
    while int_part > 0:
        remains = alf[str(int_part % base)] + remains
        int_part //= base
    return remains

def fract_conv_from_decimal(fract_part, base, alf): 
    result = ""
    while fract_part > 0:
        fract_part *= base
        digit = int(fract_part)
        result += alf[str(digit)]
        fract_part -= digit
    return result or "0" 

if __name__ == "__main__":
    print(int_fract())