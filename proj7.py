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
    def __read(self, input):
        for x in input:
            if x in self.sigma:
                self.currSt = self.delta[(self.currSt,x)]
            else:
                print ("REJECT (string contains unrecognized elements)")
                return

        if self.currSt in self.F:
            print('ACCEPT\n')
        else:
            print('REJECT\n')



states = {'A', 'B', 'C', 'D'}
sigma = {'0','1'}
delta = {('A','0'):'D',
         ('A','1'):'B',
         ('B','0'):'C',
         ('B','1'):'C',
         ('C','0'):'D',
         ('C','1'):'B',
         ('D','0'):'D',
         ('D','1'):'D'}
start = 'A'
accepts = {'A','B','C'}
myDFA = DFA(states, sigma, delta, start, accepts)

cont = True
while cont:
    testString = input("Please enter a string to be tested by the DFA: ")
    myDFA._DFA__read(testString)
    myDFA._DFA__reset()
    choice = input("Continue? (y/n): ")
    if choice == 'n':
        cont = False


