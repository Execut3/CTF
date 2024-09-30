## donut [100 pts]

**Category:** Web
**Solves:** 109

## Description
I don't like Jessica and she has donuts on her two pegs (1 and 2). Can you move all those donuts onto my third peg please??

I don't like Jessica and she has donuts on her two pegs (1 and 2). Can you move all those donuts onto my third peg please??

### Solution

Checking the connection we'll see:
```bash
$ nc challs.pwnoh.io 13434
           |
          -|-
           |
       ----|----
           |

           |
           |
        ---|---
           |
      -----|-----
           |
     ------|------
           |
    -------|-------
           |
  ---------|---------
           |

           |
           |
         --|--
           |
   --------|--------
           |
 ----------|----------
           |

Enter the stack number you would like to move a donut from (1, 2 or 3):
1
Enter the stack number you would like to move this donut to (1, 2 or 3):
2

```

It seem there are three stacks each containing some donuts. that we can move any upper donut from one stack to anothers.

It's hanoi towers problem with N items.
I used quite a time to solve it. most of the current implementation of it is for 3 items, but found this repo working find for 10 items:

https://github.com/daturkel/pynoi

And did some twists one it.

The final payload is in `source.py` file.
It tries to get the data received from server, convert it to format of 
`[[1,2], [3, 4, 5], [6, 9, 10, 7, 8]]`
and feed in the function to calculate steps to solve the hanoi in this format
`[source, destinaion]` for example `[1, 2]` means move topest item from stack1 to stack2.

and running it after almost 1000 iterations got me the flag:
```bash
$ python solve.py


Connected to server challs.pwnoh.io on port 13434
           |
         --|--
           |
        ---|---
           |
    -------|-------
           |
  ---------|---------
           |
 ----------|----------
           |

           |
           |
          -|-
           |
       ----|----
           |
     ------|------
           |
   --------|--------
           |

           |
           |
      -----|-----
           |

Enter the stack number you would like to move a donut from (1, 2 or 3):

972. (1,2): [[6, 3, 2], [5, 4, 1], [10, 9, 8, 7]]
973. (1,3): [[6, 3], [5, 4, 1], [10, 9, 8, 7, 2]]
974. (2,3): [[6, 3], [5, 4], [10, 9, 8, 7, 2, 1]]
975. (1,2): [[6], [5, 4, 3], [10, 9, 8, 7, 2, 1]]
976. (3,1): [[6, 1], [5, 4, 3], [10, 9, 8, 7, 2]]
977. (3,2): [[6, 1], [5, 4, 3, 2], [10, 9, 8, 7]]
978. (1,2): [[6], [5, 4, 3, 2, 1], [10, 9, 8, 7]]
979. (1,3): [[], [5, 4, 3, 2, 1], [10, 9, 8, 7, 6]]
980. (2,3): [[], [5, 4, 3, 2], [10, 9, 8, 7, 6, 1]]
981. (2,1): [[2], [5, 4, 3], [10, 9, 8, 7, 6, 1]]
982. (3,1): [[2, 1], [5, 4, 3], [10, 9, 8, 7, 6]]
983. (2,3): [[2, 1], [5, 4], [10, 9, 8, 7, 6, 3]]
984. (1,2): [[2], [5, 4, 1], [10, 9, 8, 7, 6, 3]]
985. (1,3): [[], [5, 4, 1], [10, 9, 8, 7, 6, 3, 2]]
986. (2,3): [[], [5, 4], [10, 9, 8, 7, 6, 3, 2, 1]]
987. (2,1): [[4], [5], [10, 9, 8, 7, 6, 3, 2, 1]]
988. (3,1): [[4, 1], [5], [10, 9, 8, 7, 6, 3, 2]]
989. (3,2): [[4, 1], [5, 2], [10, 9, 8, 7, 6, 3]]
990. (1,2): [[4], [5, 2, 1], [10, 9, 8, 7, 6, 3]]
991. (3,1): [[4, 3], [5, 2, 1], [10, 9, 8, 7, 6]]
992. (2,3): [[4, 3], [5, 2], [10, 9, 8, 7, 6, 1]]
993. (2,1): [[4, 3, 2], [5], [10, 9, 8, 7, 6, 1]]
994. (3,1): [[4, 3, 2, 1], [5], [10, 9, 8, 7, 6]]
995. (2,3): [[4, 3, 2, 1], [], [10, 9, 8, 7, 6, 5]]
996. (1,2): [[4, 3, 2], [1], [10, 9, 8, 7, 6, 5]]
997. (1,3): [[4, 3], [1], [10, 9, 8, 7, 6, 5, 2]]
998. (2,3): [[4, 3], [], [10, 9, 8, 7, 6, 5, 2, 1]]
999. (1,2): [[4], [3], [10, 9, 8, 7, 6, 5, 2, 1]]
1000. (3,1): [[4, 1], [3], [10, 9, 8, 7, 6, 5, 2]]
1001. (3,2): [[4, 1], [3, 2], [10, 9, 8, 7, 6, 5]]
1002. (1,2): [[4], [3, 2, 1], [10, 9, 8, 7, 6, 5]]
1003. (1,3): [[], [3, 2, 1], [10, 9, 8, 7, 6, 5, 4]]
1004. (2,3): [[], [3, 2], [10, 9, 8, 7, 6, 5, 4, 1]]
1005. (2,1): [[2], [3], [10, 9, 8, 7, 6, 5, 4, 1]]
1006. (3,1): [[2, 1], [3], [10, 9, 8, 7, 6, 5, 4]]
1007. (2,3): [[2, 1], [], [10, 9, 8, 7, 6, 5, 4, 3]]
1008. (1,2): [[2], [1], [10, 9, 8, 7, 6, 5, 4, 3]]
1009. (1,3): [[], [1], [10, 9, 8, 7, 6, 5, 4, 3, 2]]
1010. (2,3): [[], [], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
solved in 1010 steps

Final state of stacks:
Stack A: []
Stack B: []
Stack C: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
index 1
[2, 3]
b'Enter the stack number you would like to move this donut to (1, 2 or 3):\n'
b'           |\n\n           |\n           |\n         --|--\n           |\n        ---|---\n           |\n    -------|-------\n           |\n\n           |\n           |\n          -|-\n           |\n       ----|----\n           |\n      -----|-----\n           |\n     ------|------\n           |\n   --------|--------\n           |\n  ---------|---------\n           |\n ----------|----------\n           |\n\nEnter the stack number you would like to move a donut from (1, 2 or 3):\n'
index 2
[3, 1]
b'Enter the stack number you would like to move this donut to (1, 2 or 3):\n'
b'           |\n          -|-\n           |\n\n           |\n           |\n         --|--\n           |\n        ---|---\n           |\n    -------|-------\n           |\n\n           |\n           |\n       ----|----\n           |\n      -----|-----\n           |\n     ------|------\n           |\n   --------|--------\n           |\n  ---------|---------\n           |\n ----------|----------\n           |\n\nEnter the stack number you would like to move a donut from (1, 2 or 3):\n'
index 3
[1, 2]
b'Enter the stack number you would like to move this donut to (1, 2 or 3):\n'
b'           |\n\n           |\n           |\n          -|-\n           |\n         --|--\n           |\n        ---|---\n           |\n    -------|-------\n           |\n\n           |\n           |\n       ----|----\n           |\n      -----|-----\n           |\n     ------|------\n           |\n   --------|--------\n           |\n  ---------|---------\n           |\n ----------|----------\n           |\n\nEnter the stack number you would like to move a donut from (1, 2 or 3):\n'

```

And finaly the flag will apear.