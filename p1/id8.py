#!/usr/bin/env python3
# Find the control number in 8 digits id number
id8 = "03054825"


def scan_id(idn):
    lst = []
    for dg in range(0, len(idn)):
        lst.append(int(id8[dg]))

    lst.reverse()
    return lst


print('The id number is ', id8)
list_of_digit = scan_id(id8)

temp_sum = 0
c = 0
while c < len(list_of_digit):
    if (c + 1) % 2:  # The index is odd number
        x = 2 * list_of_digit[c]
        if (x >= 10):  # temp_sum of digits
            x = 1 + x % 10
        # print ('odd',list_of_digit[c],x)
    else:  # even index
        x = list_of_digit[c]
        # print ('even',list_of_digit[c],x)
    temp_sum += x
    c += 1
ten = 0
while ten < temp_sum:
    ten += 10
print('The control number is ', ten - temp_sum)
