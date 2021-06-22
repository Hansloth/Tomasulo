# Tomasulo Algorithm

Implementing Tomasulo Algorithmr with Python

### To run the code:

>* Step1: Create an code.txt.
>* Step2: Read the Default setting.
>* Step3: Run!

### Default setting:

>* set up initial parameters in the main.
>* All letters must be uppercase.
>* Do not allow empty line.
>* ### Dispatch: 
>- [x] ADD,ADDI: one cycle
>- [X] SUB,SUBI: one cycle
>- [X] MUL,DIV:  one cycle

>* ### Same-cycle:
>* Issue -> Dispatch: NO!
>* Capture -> Dispatch: NO!
>* Issue -> Capture: YES!
>* Issue/Result in RAT: YES!

### Input:
    ADDI F1, F2, 1
    SUB F1, F3, F4
    DIV F1, F2, F3
    MUL F2, F3, F4
    ADD F2, F4, F2
    ADDI F4, F1, 2
    MUL F5, F5, F5
    ADD F1, F4, F4
   
### Output:
    CYCLE:  1
         __ RF __
     F1  |  0  |
     F2  |  2  |
     F3  |  4  |
     F4  |  6  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |  RS1  |
     F2  |    |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |  +  |  2  |  1  | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

        _______________________
     RS4  |    |    |    | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

    code_for_exe:  [['/', 'F1', 'F2', 'F3'], ['*', 'F2', 'F3', 'F4'], ['+', 'F2', 'F4', 'F2'], ['+', 'F4', 'F1', 2], ['*', 'F5', 'F5', 'F5'], ['+', 'F1', 'F4', 'F4']]

    CYCLE:  2
        __ RF __
     F1  |  3  |
     F2  |  2  |
     F3  |  4  |
     F4  |  6  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |  RS2  |
     F2  |    |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |    |    |    | 
     RS2  |  -  |  4  |  6  | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( RS1 )  3

        _______________________
     RS4  |    |    |    | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

    code_for_exe:  [['*', 'F2', 'F3', 'F4'], ['+', 'F2', 'F4', 'F2'], ['+', 'F4', 'F1', 2], ['*', 'F5', 'F5', 'F5'], ['+', 'F1', 'F4', 'F4']]

    CYCLE:  3
        __ RF __
     F1  |  -2  |
     F2  |  2  |
     F3  |  4  |
     F4  |  6  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |  RS4  |
     F2  |    |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |    |    |    | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( RS2 )  -2

        _______________________
     RS4  |  /  |  2  |  4  | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

    code_for_exe:  [['+', 'F2', 'F4', 'F2'], ['+', 'F4', 'F1', 2], ['*', 'F5', 'F5', 'F5'], ['+', 'F1', 'F4', 'F4']]

    CYCLE:  4
        __ RF __
     F1  |  0.5  |
     F2  |  2  |
     F3  |  4  |
     F4  |  6  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |    |
     F2  |  RS5  |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |    |    |    | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

        _______________________
     RS4  |    |    |    | 
     RS5  |  *  |  4  |  6  | 
        -----------------------

    BUFFER: ( RS4 )  0.5

    code_for_exe:  [['+', 'F4', 'F1', 2], ['*', 'F5', 'F5', 'F5'], ['+', 'F1', 'F4', 'F4']]

    CYCLE:  5
        __ RF __
     F1  |  0.5  |
     F2  |  24  |
     F3  |  4  |
     F4  |  6  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |    |
     F2  |  RS1  |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |  +  |  6  |  24  | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

        _______________________
     RS4  |    |    |    | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( RS5 )  24

    code_for_exe:  [['*', 'F5', 'F5', 'F5'], ['+', 'F1', 'F4', 'F4']]

    CYCLE:  6
        __ RF __
     F1  |  0.5  |
     F2  |  30  |
     F3  |  4  |
     F4  |  6  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |    |
     F2  |    |
     F3  |    |
     F4  |  RS2  |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |    |    |    | 
     RS2  |  +  |  0.5  |  2  | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( RS1 )  30

        _______________________
     RS4  |    |    |    | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

    code_for_exe:  [['+', 'F1', 'F4', 'F4']]

    CYCLE:  7
        __ RF __
     F1  |  0.5  |
     F2  |  30  |
     F3  |  4  |
     F4  |  2.5  |
     F5  |  8  |
        --------

        __ RAT __
     F1  |    |
     F2  |    |
     F3  |    |
     F4  |    |
     F5  |  RS4  |
        ---------

        __ RS _________________
     RS1  |    |    |    | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( RS2 )  2.5

        _______________________
     RS4  |  *  |  8  |  8  | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

    code_for_exe:  []

    CYCLE:  8
        __ RF __
     F1  |  0.5  |
     F2  |  30  |
     F3  |  4  |
     F4  |  2.5  |
     F5  |  64  |
        --------

        __ RAT __
     F1  |  RS1  |
     F2  |    |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |  +  |  2.5  |  2.5  | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

        _______________________
     RS4  |    |    |    | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( RS4 )  64

    code_for_exe:  []

    CYCLE:  9
        __ RF __
     F1  |  5.0  |
     F2  |  30  |
     F3  |  4  |
     F4  |  2.5  |
     F5  |  64  |
        --------

        __ RAT __
     F1  |    |
     F2  |    |
     F3  |    |
     F4  |    |
     F5  |    |
        ---------

        __ RS _________________
     RS1  |    |    |    | 
     RS2  |    |    |    | 
     RS3  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  

        _______________________
     RS4  |    |    |    | 
     RS5  |    |    |    | 
        -----------------------

    BUFFER: ( empty )  
