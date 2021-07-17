#!/usr/bin/env python3
# http://e-learn.cyber.org.il/python/rolling_assignment/resources/hangman_welcome_screen.txt

import string

MAX_TRIES = 6
HANGMAN_ASCII_ART = """
     _    _   
    | |  | |   
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |  
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                         _/  | 
                        |___/ """

p1 = """
    x-------x""";

p2 = """
    x-------x   
    |  
    |  
    |  
    |  
    |""";

p3 = """
    x-------x
    |       |
    |       0
    |
    |
    |""";

p4 = """
    x-------x
    |       |
    |       0
    |       | 
    |    
    |""";

p5 = """
    x-------x
    |       |
    |       0
    |      [|]
    |    
    |""";
p6 = """
    x-------x
    |       |
    |       0
    |      [|]
    |     [     
    |""";

p7 = """
    x-------x
    |       |
    |       0
    |      [|]
    |     [   ]  
    |"""




HANGMAN_PHOTOS ={1:p1, 2:p2, 3:p3, 4:p4, 5:p5, 6:p6, 7:p7}
def print_hangman(num_of_tries):
   print(HANGMAN_PHOTOS[num_of_tries])


def check_win(secret, old):
    len_old = len(old)
    for c in range(len_old):
        if not (old[c] in secret):
                return False
    return True


def show_hidden_word(secret, old):
    len_old = len(old)
    len_secret = len(secret)
    out = len(secret)*['_ ']
    for c in range(len_old):
        for n in range(len_secret):
            if secret_word[n] == old[c]:
                    out[n] = old[c]
    final_str = ''.join(out)
    return final_str




def printOpenningScreen(title, tryCounter):
    print(title + '\n' + str(tryCounter))


def try_update_letter_guessed(newChr, ltrs):

    if not(newChr in ltrs):
        ltrs.append(newChr)
        print(ltrs)
        return False
    else:
        return True


def check_valid_input(letter, old_letters):
    ''' Test legal  input   '''
    only_one_char = len(letter) == 1
    only_english_char = letter.isalpha()

    if not only_english_char and not only_one_char:
            print('E3')
            result = False
    elif not only_one_char:
            print('E1')  # More then one  letter
            result = False
    elif not only_english_char:
            print('E2')  # This is not english letter
            result = False
    else:
            if try_update_letter_guessed(letter, old_letters):

                        result = False
                        print('E8')
            else:
                result = True

    return result


printOpenningScreen(HANGMAN_ASCII_ART, MAX_TRIES)


num_of_tries = 7
print_hangman(num_of_tries)
letter_guessed = input("Guess a letter  ").lower()
secret_word = "yes"
old_letters_guessed = ['m', 'e', 'j', 'i', 'm', 'k']
print(check_valid_input(letter_guessed,  old_letters_guessed))
print(show_hidden_word(secret_word, old_letters_guessed))
print(check_win(secret_word, old_letters_guessed))






#print(pic[6])
'''>>> cool_trick = [1, 2, 3]
>>> a, b, c = cool_trick
>>> a
1
>>> c


# e3 = encrypted_message[-1 : :-2]# slice end to  start step 2

#https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_selfpy101+3_2019/courseware/91cf76a4af684d78a4be834f626f298d/0320c867b72549fa926b3daed93c749a/

3


'''