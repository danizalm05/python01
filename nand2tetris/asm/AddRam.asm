 //RAM[2] =  RAM[0]+RAM[1]+17  
//https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/courseware/e966e5c59f414d1f9b92396f05889394/34ce5d59bfd4475390c571028c594839/


    
@0             // A = 0
D = M          // D = RAM[0]

               //D = D+RAM[1]
@1             //A = 1
D = D + M      //D = D+RAM[1]

@17            //A = 17
D=D+A          //D = D+17

@2
M=D            //RAM[2] = D
 