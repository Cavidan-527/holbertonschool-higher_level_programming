#!/usr/bin/python3

def uppercase(str):
    for char in str:
        # Əgər simvol balaca hərfdirsə (97-122 aralığı)
        if ord(char) >= 97 and ord(char) <= 122:
            # Ondan 32 çıxırıq ki, böyük hərf olsun
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")  # Sonda yeni sətir üçün
