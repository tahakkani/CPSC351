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
    def __read(self, input):
        for x in input:
            print(self.currSt, " ", self.stack, "\n")
            #check to see if there are any e-transitions in current state, if yes, then fire them up, skip to next statement
            self.checkForETransitions()
            for k2 in self.delta:
                if k2 == (self.currSt, x, ''):
                    self.currSt = self.delta[k2][0]
                    if not self.delta[k2][1] == '':
                        self.stack.append(self.delta[k2][1])
                    more = False
                    break
                if k2 == (self.currSt, x, self.stack[len(self.stack) - 1]):
                    self.currSt = self.delta[k2][0]
                    self.stack.pop()
                    if not self.delta[k2][1] == '':
                        self.stack.append(self.delta[k2][1])
                    more = False
                    break
        self.checkForETransitions()
        if self.currSt in self.F:
            print('ACCEPT\n')
        else:
            print('REJECT\n')
    def checkForETransitions(self):
        more = True #more keeps track of if there might be any more e-transitions for the current state
        while more:
            more = False
            for k in self.delta:
                if k == (self.currSt, '', self.stack[len(self.stack) - 1]):
                    self.currSt = self.delta[k][0]
                    if not self.delta[k][1] == '':
                        self.stack.append(self.delta[k][1])
                    more == True
                    break




states = {'A', 'B', 'C', 'D'}
alpha = {'0','1'}
stackAlpha = {'0', '1', '$'}
delta = {('A', '', ''):('B', '$'),
         ('B', '0', ''):('B', '0'),
         ('B','1', '0'):('C', ''),
         ('C','1', '0'):('C', ''),
         ('C','', '$'):('D', '')}
start = 'A'
accepts = {'D'}
myDPDA = DPDA(states, alpha, stackAlpha, delta, start, accepts)

cont = True
while cont:
    testString = input("Please enter a string to be tested by the PDA: ")
    myDPDA._DPDA__read(testString)
    myDPDA._DPDA__reset()
    choice = input("Continue? (y/n): ")
    if choice == 'n' or 'N': cont = False