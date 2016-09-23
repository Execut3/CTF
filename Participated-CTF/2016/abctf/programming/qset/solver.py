from interpreter import *

# i0 x i1
# o1 -> counter with value of i0
#program = 'f1/f1 i0,f1 i0/f0 i0,f0 i0/i0'
#program = 'x/i0,y/i1,x y/x yy o0,f1/f1 i0,f1 i0/f0 i0,f0 i0/i0,y/yy'
#program = 'a b c/i0 c,/c,i0 b d/a d,/d, c d/i1, /i0,o0/b b'
program = 'a b c/i0 c,/c,i0 b d/a d,/d, c d/i1, /i0,o0/b b'
interpret(program, [3,2])



