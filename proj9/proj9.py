#######################
#  Taha Hakkani
#  CPSC351
#  Python 3.7 (64-bit)
#######################

class TuringMachine:
    def __init__(self, *args, **kwargs):
        self.Q = args[0]
        self.sigma = args[1]
        self.gamma = args[2]
        self.delta = args[3]
        self.q0 = args[4]
        self.qa = args[5]
        self.qr = args[6]
        self.currSt = args[4]
        self.currElem = 1
    def reset(self):
        self.currSt = self.q0
        self.currElem = 1
    def run(self, str):
        #this loop checks if any elements of the input are not in the alphabet
        for a in str:
            if a not in alpha:
                self.display(False)
                return
        str = list('_' + str + '_') #turn string into a list
        reject, accept = False, False    #keeps track of iwf machine hits an accept/reject state
        while not (accept or reject):   # while not in an accept or reject state:
            trans = delta[self.currSt][str[self.currElem]]  #trans is the 3-tuple rule retreieved from delta
            str[self.currElem] = trans[1]   # transform the string as specified by trans
            self.currSt = trans[0]      #move state in machine
            self.currElem = self.currElem + trans[2]    #move tape head either left or right
            if self.currSt == 'r':
                reject = True
                self.display(accept)
            elif self.currSt == 'a':
                accept = True
                self.display(accept)
    def display(self, acpt):
        if acpt:
            print('accept')
        else:
            print('reject')



states = {'j', 'k', 'l', 'm', 'n', 'a', 'r'} #accept and reject is a and r
alpha = {'0'}
tapeAlpha = {'X','_', '0'}
#delta organized as nested dictionaries. 
#Outer dictionary uses current state as key for inner dictionary
#Inner dictionaries use current element on the tape as a key to a unique delta transition
#Delta transitions organized as 3-tuples, blanks encoded here as underscore,
#L/R movements on tapehead encoded as either 1 (R) or -1 (L)
delta = {'j':       {'_':('r', '_', 1),  'X':('r', 'X', 1),  '0':('k', '_', 1)},
         'k':       {'_':('a', '_', 1),  'X':('k', 'X', 1),  '0':('l', 'X', 1)},
         'l':       {'_':('n', '_',-1),  'X':('l', 'X', 1),  '0':('m', '0', 1)},
         'm':       {'_':('r', '_', 1),  'X':('m', 'X', 1),  '0':('l', 'X', 1)},
         'n':       {'_':('k', '_', 1),  'X':('n', 'X',-1),  '0':('n', '0',-1)}   }

start = ('j')
accept = {'a'}
reject = {'r'}
myTMachine = TuringMachine(states, alpha, tapeAlpha, delta, start, accept, reject)


while 1:
    str = input("Enter a string: ")
    if str == 'quit':
        break
    myTMachine.run(str)
    myTMachine.reset()
    
