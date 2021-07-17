
'''
https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_selfpy101+3_2019/courseware/bb1255da2f294bffb8066472d9db592e/b0713462bbd54813af90aef7c415c0f7/
 Sort  a tuple according to price
'''

import tensorflow as tf
hello = tf.constant('Hello, Codacus!')
sess = tf.Session()
print(sess.run(hello))
def getKey(item):
    return item[1]


products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0'), ('cagndy', '1.5')]
print (getKey(products[1]))
print (sorted(products, key=getKey,reverse = True))