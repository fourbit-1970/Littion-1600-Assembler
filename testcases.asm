       0:          RK TP CIE       $01             ; 01 ok Test case from manual
       1:          AC+14A  JC+fff  $02             ; 02 ok Add with Cary and Jump conditional
       2:          LA+7  NN  RK  SK  $03           ; 03 ok Test case with 4 opcodes
       3:          NN NN NN NN $04                 ; 04 ok Test case with four 8-bit opcodes
       4:          AC+14A  JC+fff  $05             ; 05 ok Test case with two 16-bit opcodes
       5:          AC+14A  RK TP $06               ; 06 ok Test case with one 16-bit opcode and two 8-bit opcodes
       6:          RK TP AC+14A $07                ; 07 ok Test case with two 8-bit opcodes and one 16-bit opcode
       7:          RK AC+14A $08                   ; 08*flag warning halt Test case with one 8-bit opcode and one 16-bit opcode
       8:          AC+14A RK $09                   ; 09*flag warning halt Test case with one 16-bit opcode and one 8-bit opcode
       9:          RK $0A                          ; 10*flag warning halt Test case with one 8-bit opcode
       $A:         AC+14A $0B                      ; 11*flag warning halt Test case with one 16-bit opcode
       $b:         RK TP CIE $0C                   ; 12 ok Test case with two 8-bit and a 16-bit opcodes
       12:         AC+14A JC+fff JM+fff $0D        ; 13*flag abort 'too many cmd' Test case with three 16-bit opcodes
       13:         RK+7 TP+7 CIE+7 SK+7 $0E        ; 14*flag abort 'invalid operands' Test case with four 8-bit opcodes and operands
       $E:         AC+14A JC+fff JM+fff LI+fff $0F ; 15*flag abort 'too many cmd' Test case with four 16-bit opcodes and operands
       $F:         RK+7 TP+7 CIE+7 $10             ; 16*flag abort 'invalid operands' Test case with three 8-bit opcodes and operands
       16:         AC+14A JC+fff JM+fff $11        ; 17*flag abort 'too many cmd' Test case with three 16-bit opcodes and operands
       17:         RK+7 $12                        ; 18*flag abort 'invalid operands' Test case with one 8-bit opcode and operands
       18:         AC+14A $13                      ; 19*flag warning halt Test case with one 16-bit opcode and operands
       19:         RK+7 TP+7 $14                   ; 20*flag abort invalid operands  Test case with two 8-bit opcodes and operands
       20:         AC+14A JC+fff $15               ; 21 ok Test case with two 16-bit opcodes and operands
       21:         AC+14A RK TP $16                ; 22 ok Test case with one 16-bit opcode and two 8-bit opcodes and operands
       22:         RK TP AC+14A $17                ; 23 ok Test case with two 8-bit opcodes and one 16-bit opcode and operands
       23:         RK AC+14A $18                   ; 24*flag warning halt Test case with one 8-bit opcode and one 16-bit opcode and operands
       24:         AC+14A RK $19                   ; 25*flag warning halt Test case with one 16-bit opcode and one 8-bit opcode and operands
       25:         INVALID $1A                     ; 26*flag warning halt Test case with invalid opcodes
       26:         RK+INVALID $1B                  ; 27*flag abort 'invalid operands' Test case with invalid operands
       27:         RK TP CIE SK RK $1C             ; 28*flag abort 'too many' cmd Test case with too many opcodes
       28:         RK TP CIE                       ; 29*flag abort 'no offset' Test case with missing next address
                                                ; 30 ok Test case with blank lines
                                                ; 31 ok Test case with comments
       31:         RK TP CIE $1D                   ; 32 ok Test case with comments on lines with code
       32:         TESTLABEL: RK TP CIE $1E        ; 33 ok Test case with labels
       33:         TESTLABEL2: RK TP CIE $1F       ; 34 ok Test case with labels at the beginning of the code
       34:         RK TP CIE $20                   ; 35 ok Test case with labels at the end of the code
       35:         RK TP CIE TESTLABEL3: $21       ; 36*flag abort 'invalid syntax' Test case with labels in the middle of the code
       36:         1234: RK TP CIE $22             ; 37 ok Test case with labels that are numbers
       37:         TESTLABEL4: RK TP CIE $23       ; 38 ok Test case with labels that are duplicated
       38:         TESTLABEL4: RK TP CIE $24       ; 39*flag warning 'lable' Test case with labels that are duplicated
