 //loops  1+2+3....,n = ?    R0 = n      R1 <== Output
 //https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/courseware/e966e5c59f414d1f9b92396f05889394/c05f41d56e344094844aaf8ebafa0b9a/
 //5:20
 
   // i = 1  sum=0
   @2
   D=M   
   @R0
   M=D
   @i
   M=1        // i = 1 R0=1
 
   
   @sum
   M=0       //sum=0   R1=0
 (LOOP)
   //If(i>R0) goto STOP
   @i
   D = M      //
   @R0        
   D = D - M
   @STOP
   D;JGT
   //sum = sum + 1
   @sum
   M = D 
   //i=i+1
   @i
   M = M + 1
   @LOOP
   0;JMP
   
   @SUM
   D=M
   @R1
   0;JMP  
   
   M=D