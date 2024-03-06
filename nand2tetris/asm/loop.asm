//https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/courseware/e966e5c59f414d1f9b92396f05889394/3ee54628495d474f9e7e15297b643647/


//If D==0 jmp 30
@30
D=1
D;JEQ

//-----------------------------------------
//jump to 12 only if  RAM[1] <= 100

@1 
D=M // D = RAM[1]  

@100     //A=100
D = D-A	  //D =RAM[100]-100 

@12
D;JLT //if D<=0 jump to Rom 12