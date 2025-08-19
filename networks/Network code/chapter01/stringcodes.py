#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter01/stringcodes.py

if __name__ == '__main__':
    # Translating from the outside world of bytes to Unicode characters.
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
                  # 4 1 3 i s i n. 
    
    input_characters = input_bytes.decode('utf-16')
    print('input_characters = ',repr(input_characters))

    # Translating characters back into bytes before sending them.
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')
    print('output_bytes = ',output_bytes) 
     
    output_string   = str(output_bytes , 'utf-8')
    print('output_string = ',output_string)  
    '''
             -------- output  ------------
    input_characters =  '413 is in.'
    output_bytes =  b'We copy you down, Eagle.\n'
    output_string =  We copy you down, Eagle.
    
    
    '''
   
    #with open('eagle.txt', 'wb') as f:
    #    f.write(output_bytes)