import math

def task1(a, b, c, d):  #17 задание
    d = d * 8
    i = 2 ** (d / (a * b * c))
    return int(i)

def task2(a, b):
    i = (math.log2(a)) / (math.log2(b)) 
    return i

def task3(N, soo):
    K = soo / math.log2(N)
    return int(K)

def task4(gde):
    i = 2 ** int(gde)
    return i

def task5(blue, bit):
    i = (blue * blue) / (2 ** bit)
    return int(i)

if __name__ == "__main__":
    #inp1 = int (input("кол-во страниц: "))  #task1 (18 номер)
    #inp2 = int (input("кол-во строк: "))
    #inp3 = int (input("кол-во символов: "))
    #inp4 = int (input("кол-во бит: "))
    #print(task1(inp1, inp2, inp3, inp4))

    #inp5 = int(input("мощность одного алфавита: "))    #task2 (19 номер)
    #inp6 = int(input("мощность второго алфавита: "))
    #print(task2(inp5, inp6))

    #inp7 = int(input("сколько букв в алфавите: "))    #task3 (20 номер)
    #inp8 = int(input("сколько бит сообщение: "))
    #print(task3(inp7, inp8))

    #inp9 = int(input("сколько бит несёт соо: "))    #task4 (19 и 20 номера)
    #print(task4(inp9))

    inp10 = int(input("сколько потратили синей краски: "))   #task4 (7 номер)
    inp11 = int(input("сколько бит: "))
    print(task5(inp10, inp11))