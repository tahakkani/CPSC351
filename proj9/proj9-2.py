#######################
#  Taha Hakkani
#  CPSC351
#  Python 3.7 (64-bit)
#######################

class DFA:
    def __init__(self, *args, **kwargs):
        self.Q = args[0]
        self.sigma = args[1]
        self.delta = args[2]
        self.q0 = args[3]
        self.F = args[4]
        self.currSt = args[3]
    def __reset(self):
        self.currSt = self.q0
    def __run(self, input):
        for x in input:
            if x in self.sigma:
                self.currSt = self.delta[self.currSt][x]
            else:
                print ("REJECT (string contains unrecognized elements)")
                return
        if self.currSt in self.F:
            print('ACCEPT\n')
        else:
            print('REJECT\n')


#states with vowels represent the 0 breaks between 1's 
#(A, E, I, O, U).
#Qi is state before the transition, Qj is the one after.
#R0, R1, R_ represent read 0, 1, and blank, respectively, from #tape.
#W represents write to tape.
#L and R are left and right.
#Z states represent '00' between transitions and final '000' at 
#the end.

states = {'A1', 'A2', 'A3', 'A4', 'Qi', 'E', 'R0', 'R1', 'R_', 'I', 'Qj', 'O', 'W0', 'W1', 'W_', 'U', 'L', 'R', 'Z1', 'Z2', 'Z3', 'X'}
sigma  = {'0','1'}
delta  = {'A1':   {'0':'A2',  '1':'X'  },
          'A2':   {'0':'A3',  '1':'X'  },
          'A3':   {'0':'A4',  '1':'X'  },
          'A4':   {'0':'X' ,  '1':'Qi' },
          'Qi':   {'0':'E' ,  '1':'Qi' },
          'E' :   {'0':'X' ,  '1':'R0' },
          'R0':   {'0':'I' ,  '1':'R1' },
          'R1':   {'0':'I' ,  '1':'R_' },
          'R_':   {'0':'I' ,  '1':'X'  },
          'I' :   {'0':'X' ,  '1':'Qj' },
          'Qj':   {'0':'O' ,  '1':'Qj' },
          'O' :   {'0':'X' ,  '1':'W0' },
          'W0':   {'0':'U' ,  '1':'W1' },
          'W1':   {'0':'U' ,  '1':'W_' },
          'W_':   {'0':'U' ,  '1':'X'  },
          'U' :   {'0':'X' ,  '1':'L'  },
          'L' :   {'0':'Z1',  '1':'R'  },
          'R' :   {'0':'Z1',  '1':'X'  },
          'Z1':   {'0':'Z2',  '1':'X'  },
          'Z2':   {'0':'Z3',  '1':'Qi' },
          'Z3':   {'0':'X' ,  '1':'X'  },
          'X' :   {'0':'X' ,  '1':'X'  }  }

start = 'A1'
accepts = {'Z3'}
UTM = DFA(states, sigma, delta, start, accepts)

while 1:
    str = input("Enter a string: ")
    if str == 'quit':
        break
    UTM._DFA__run(str)
    UTM._DFA__reset()


