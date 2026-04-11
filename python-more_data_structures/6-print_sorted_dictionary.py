#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Açarları götürürük və əlifba sırası ilə çeşidləyirik
    sorted_keys = sorted(a_dictionary.keys())
    
    # Çeşidlənmiş açarlar üzərində dövr qurub nəticəni çap edirik
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
