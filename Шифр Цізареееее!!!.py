i = True
while i:
    alpha = ' abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNMабвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯ0123456789'
    step = 2
    step1 = 1
    text = input("Веди текст биром: ").strip()
    res = ''
    digit = ''
    for c in text:
        if c.isalpha():
            if digit:
                res += str(int(digit) + int(step1))
                digit = ''
            res += alpha[(alpha.index(c) + step) % len(alpha)]
        elif c == ' ':
            if digit:
                res += str(int(digit) + int(step1))
                digit = ''
            res += c
        elif c.isnumeric():
            digit += c
        else:
            res += c
    if digit:
        res += str(int(digit) + int(step1))
    print("Вот на тобі: " + res + "")
