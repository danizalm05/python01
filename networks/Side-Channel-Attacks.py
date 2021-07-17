"""
The function check_password(password) is used by a safe with 4-digits passwords,
and is susceptible to timing attacks.
More specifically, it takes it around 0.1 seconds to check one digit – so
brute-forcing all the possible combinations will take more than an hour.
Can you implement a way to crack its password in less than a minute?



"""
#https://courses.edx.org/courses/course-v1:IsraelX+infosec101+3T2019a/discussion/forum/bd41341ea1cd4719f1587960e4aa7fccba43b96b/threads/5e29f58295b0620926003019
import time
import sys # ignore
sys.path.insert(0,'.') # ignore
real_password = '9234'
#from Root.pswd import real_password


def check_password(password): # Don't change this  function
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True

 

def crack_password():
 password = list("0000")
 for i in range(4):
    #print(i) Commented lines show algorithm progress
    for j in range(10):
        password[i] = j
        start = time.time()
        success = check_password(password)
        elapsed = time.time() - start
        print(''.join(str(x) for x in password))
        print(elapsed)
        if elapsed >= 0.2 + (0.1 * i) or success:
            break
 return ''.join(str(x) for x in password)

print(crack_password())
  
   