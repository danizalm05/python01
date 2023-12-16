
https://www.coursera.org/learn/build-a-computer/home/week/1
https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/course/

 
HDL-Based Chip Simulation 
https://www.youtube.com/watch?v=iSNfqzJUWW4

http://nand2tetris-questions-and-answers-forum.52.s1.nabble.com/Hardware-Construction-Survival-Kit-td3385741.html
http://nand2tetris-questions-and-answers-forum.52.s1.nabble.com/Comparison-Failure-for-quot-AND-quot-gate-td4037234.html

https://github.com/Gunasekare/nand2tetris
https://www.nand2tetris.org/

project 1
----------
https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/courseware/edaa595f40af4f2a867b7a489176237f/78da93dc6ad64d6cb59630acecadcc50/?child=first

Not ,And, Or, Xor, Mux, DMux, Not16, And16 Or16 Mux16
Or8Way Mux4Way16  Mux8Way16 DMux4Way DMux8Way
The Hack chip-set API
------------------------------
Below is a list of all the chip interfaces in the Hack chip-set, 
prepared by Warren Toomey. 
If you need to use a chip-part, you can copy-paste the chip interface
 and proceed to fill in the missing data. 
 This is a very useful list to have bookmarked or printed.

  Add16(a= ,b= ,out= ); 
  ALU(x= ,y= ,zx= ,nx= ,zy= ,ny= ,f= ,no= ,out= ,zr= ,ng= ); 
  And16(a= ,b= ,out= ); 
  And(a= ,b= ,out= ); 
  ARegister(in= ,load= ,out= ); 
  Bit(in= ,load= ,out= ); 
  CPU(inM= ,instruction= ,reset= ,outM= ,writeM= ,addressM= ,pc= ); 
  DFF(in= ,out= ); 
  DMux4Way(in= ,sel= ,a= ,b= ,c= ,d= ); 
  DMux8Way(in= ,sel= ,a= ,b= ,c= ,d= ,e= ,f= ,g= ,h= ); 
  DMux(in= ,sel= ,a= ,b= ); 
  DRegister(in= ,load= ,out= ); 
  FullAdder(a= ,b= ,c= ,sum= ,carry= );
  HalfAdder(a= ,b= ,sum= , carry= ); 
  Inc16(in= ,out= ); 
  Keyboard(out= ); 
  Memory(in= ,load= ,address= ,out= ); 
  Mux16(a= ,b= ,sel= ,out= ); 
  Mux4Way16(a= ,b= ,c= ,d= ,sel= ,out= ); 
  Mux8Way16(a= ,b= ,c= ,d= ,e= ,f= ,g= ,h= ,sel= ,out= ); 
  Mux(a= ,b= ,sel= ,out= ); 
  Nand(a= ,b= ,out= ); 
  Not16(in= ,out= ); 
  Not(in= ,out= ); 
  Or16(a= ,b= ,out= ); 
  Or8Way(in= ,out= ); 
  Or(a= ,b= ,out= ); 
  PC(in= ,load= ,inc= ,reset= ,out= ); 
  RAM16K(in= ,load= ,address= ,out= ); 
  RAM4K(in= ,load= ,address= ,out= ); 
  RAM512(in= ,load= ,address= ,out= ); 
  RAM64(in= ,load= ,address= ,out= ); 
  RAM8(in= ,load= ,address= ,out= ); 
  Register(in= ,load= ,out= ); 
  ROM32K(address= ,out= ); 
  Screen(in= ,load= ,address= ,out= ); 
  Xor(a= ,b= ,out= ); 
