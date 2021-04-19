import re

string_to_decode = 'AAABBBCCC'

letter_count_pre = {"A":0,"B":0}

list_print = []

for letter in string_to_decode:
    letter = letter.upper()
    if letter in letter_count_pre:
        if letter_count_pre[letter] == 0:
            letter_count_pre[letter] = 1
        else:
            letter_count_pre[letter] += 1
    else:
        letter_count_pre[letter] = 1

for letter_print in letter_count_pre:
    list_print.append(letter_print)
    list_print.append(letter_count_pre[letter_print])

print(''.join(str(list_print)))
