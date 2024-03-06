
https://www.coursera.org/learn/build-a-computer/home/week/1
https://courses.campus.gov.il/courses/course-v1:HUJI+ACD_HUJI_nand2tetris+2020_1/course/

 
HDL-Based Chip Simulation 
https://www.youtube.com/watch?v=iSNfqzJUWW4

http://nand2tetris-questions-and-answers-forum.52.s1.nabble.com/Hardware-Construction-Survival-Kit-td3385741.html
http://nand2tetris-questions-and-answers-forum.52.s1.nabble.com/Comparison-Failure-for-quot-AND-quot-gate-td4037234.html

https://github.com/Gunasekare/nand2tetris
https://www.nand2tetris.org/

project 1
------------
Not ,And, Or, Xor, Mux, DMux, Not16, And16 Or16 Mux16
Or8Way Mux4Way16  Mux8Way16 DMux4Way DMux8Way

project 2
-------------
HalfAdder,FullAdder,Add16, Inc16,    ALU

project 3
-------------
  Bit, Register, RAM8, RAM64  RAM512 RAM4K RAM16K  PC



The Hack chip-set API
------------------------------
Below is a list of all the chip interfaces in the Hack chip-set, 
prepared by Warren Toomey. 
If you need to use a chip-part, you can copy-paste the chip interface
 and proceed to fill in the missing data. 
 

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
  
  
  
  How to put the output into few busses
  Mux16(a=out0, b=notOut0, sel=no, out=out, out[15]=first, out[0..7]=lastHalf, out[8..15]=firstHalf);
  
  
  
DMux8Way
=================
Inputs: in, sel[3]
Outputs: a, b, c, d, e, f, g, h
Function: If sel=000 then {a=in, b=c=d=e=f=g=h=0}
                else if sel=001 then {b=in, a=c=d=e=f=g=h=0}
                else if sel=010 ...
                ...
                else if sel=111 then {h=in, a=b=c=d=e=f=g=0}.
				
Mux8Way16
==============				
 8-way 16-bit multiplexor:
 IN a[16], b[16], c[16], d[16],
       e[16], f[16], g[16], h[16],
 Function:
 * out = a if sel == 000
 *       b if sel == 001
 *       etc.
 *       h if sel == 111	

A: register that holds address 
 
1. Register Oriented 
     add r1, r2  #  
2.  Direct Addressing
     add r1, m[200] # r1 = r1 + memory 200 
3. Indirect Addressing 
     add r1, @a   #r1 = r1+memory a   #  
4  Immediate 
     add r1, 79   r1 = r1 +79 

 
