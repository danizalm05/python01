__author__ = "book"
print('you say', )


def main():
    name = input('Name')
    print('Hello ' + name)


print('Goodbye')

if __name__ == '__main__':
    msg = 'me say'
    print('Addres of msg:  {} msg: {}'.format(id(msg), msg))
    msg2 = msg
    print('Addres of msg2:  {} msg2: {}'.format(id(msg2), msg2))
    msg = 'xxffgdgfgdgfd'
    print('Addres of msg:  {} msg: {}'.format(id(msg), msg))
    print('Addres of msg2:  {} msg2: {}'.format(id(msg2), msg2))
    print(msg, )
    print(msg2, )
    main()