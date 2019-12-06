#######################
#  Taha Hakkani
#  CPSC351
#  Python 3.7 (64-bit)
#######################

class DPDA:
    def __init__(self, *args, **kwargs):
        self.Q = args[0]
        self.sigma = args[1]
        self.gamma = args[2]
        self.delta = args[3]
        self.q0 = args[4]
        self.F = args[5]
        self.currSt = args[4]
        self.stack = ['']
    def __reset(self):
        self.currSt = self.q0
        self.stack = ['']
    #input: a string to be determined if it is in the language
    #output: prints Accept or Reject
    def __read(self, input):
        for a in input:
            noMoves = False #noMoves lets the while loop know 
            while True:
                if not self.executeMove(a):
                    if not self.executeMove(''):
                        noMoves = True   #this break needs to break the for loop
                        break
                    continue    #this hits when e transition happens
                break   #this break exits while loop so that we can continue to next character
            if noMoves:
                break
        if input:   #this happens only if the string is null. Allows for final e transition before determining input
            self.executeMove('')
        if self.currSt in self.F:
            print('ACCEPT\n')
        else:
            print('REJECT\n')
    #input: char is next character to be read, either an element of alphabet or e
    #output: returns boolean indicating wether or not a move was made
    def executeMove(self, char):
        worked = False
        for k in self.delta:
            if k[0] == self.currSt and  k[1] == char:
                if k[2] == self.stack[-1]:
                    self.stack.pop()
                elif not k[2] == '':
                    continue
                self.currSt = self.delta[k][0]
                if not self.delta[k][1] == '':
                    self.stack.append(self.delta[k][1])
                worked = True
                break
            else:
                continue
        return worked


states = {'A', 'B', 'C', 'D', 'R'}
alpha = {'0','1'}
stackAlpha = {'0', '1', '$'}
delta = {('A', '', ''):('B', '$'),
         ('B', '0', ''):('B', '0'),
         ('B','1', '0'):('C', ''),
         ('C','1', '0'):('C', ''),
         ('C','1', '$'):('R', ''),
         ('C', '0', '0'):('R', ''),
         ('C', '0', '$'):('R', ''),
         ('C','', '$'):('D', '')}
start = 'A'
accepts = {'D', 'A'}
myDPDA = DPDA(states, alpha, stackAlpha, delta, start, accepts)

cont = True
while cont:
    testString = input("Please enter a string to be tested by the PDA: ")
    myDPDA._DPDA__read(testString)
    myDPDA._DPDA__reset()
    choice = input("Continue? (y/n): ")
    if choice == 'n': cont = False