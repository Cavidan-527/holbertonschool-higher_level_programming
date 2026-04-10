#!/usr/bin/python3

def print_last_digit(number):
    # Ədədin mənfi olub-olmamasından asılı olmayaraq son rəqəmi tapırıq
    last_digit = abs(number) % 10
    # Son rəqəmi çap edirik (yan-yana çap üçün end="" istifadə etmirik, 
    # çünki tapşırıq nümunəsində hər çağırış çap olunur)
    print("{}".format(last_digit), end="")
    # Son rəqəmi geri qaytarırıq (return)
    return last_digit
