#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX = 16
list = []


def hex_num():
    num = int(input("Введите целое число: "))
    print(hex(num), "hex")
    while num / HEX != 0:
        division = str(num % HEX)
        match division:
            case "10":
                division = "a"
            case "11":
                division = "b"
            case "12":
                division = "c"
            case "13":
                division = "d"
            case "14":
                division = "e"
            case "15":
                division = "f"
        list.append(division)
        num //= HEX

    print(f"0x{''.join(list[::-1])} nex_num")

    return list.clear(), hex_num()


hex_num()