 //if R0>0 then R1=1 else R1=-1
 //  
//https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/courseware/e966e5c59f414d1f9b92396f05889394/67a24e613f304e449ade48ad3eaeab81/?child=first
//6:03

 
  @R0            // A = R0= RAM[0]
  D = M          // D = R0= RAM[0] 

               
  @POS           //A = address of the POS label
  D;JGE        //  if D = R0 = RAM[0] >=0  jump to POS

// If we are here  it means R0 < 0 
  @R1            // A = R1= RAM[1]
  M = -1
  @END
  0;JMP
(POS)
  @R1
  M = 1
(END)  

