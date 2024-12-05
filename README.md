# Welcome to Adrian Nelson's and Aidan Chin's colloborative ECE 371 Intro to Security Repository
This is meant as way to remotely access and share code as we complete each project. These projects are being done with the DE1SOC Altera FPGA Board. 

This code is written in a few different languages such as: Python, C, Verilog, and VHDL

# Lab1: Buffer Overflow Demonstration
* Using two adjecent memory spaces of 9 memory addresses for student ID numbers, show how buffer overflow can show you data that was not intended to be shared. 
* ex: Getting rid of a NULL terminator '\0' in C using a scanf() command without the "%9s" limiter.

# Lab2: RSA and DES Demonstration
* implementing RSA to encrypt a DES key and using it to encrypt and decrypt an image.

# Lab3: Encrypted Chat Demonstration
* using RSA and DES to achieve 1 way encrypted chat between 2 machines

# Lab4: Random Number generation implemted using Verilog and VHDL
* using verilog we implemented a psuedo-random number generator that was verfied through Intel Quartus Model Sim v16.0
* using vhdl we implemented a true-random number generator that was verfied on the DE1-SoC board
