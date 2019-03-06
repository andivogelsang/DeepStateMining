class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, input):
        try:
            handler = self.handlers[self.startState]
            output = []
        except:
            raise InitializationError("must call .set_start() before .run()")
        #if not self.endStates:
        #   raise  InitializationError("at least one state must be an end_state")
    
        while True:
            (newState, output, input) = handler(input, output)
            if len(input)==0:
                break
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break 
            else:
                handler = self.handlers[newState.upper()] 
        return output


def idle_transitions(input,output):
    currentInput = input[0]  
    input =  input[1:] if len(input) > 1 else []
    if currentInput == "coin-5":
        newState = "Paid5"
    elif currentInput == "coin-10":
        newState = "Paid10"
    else:
        newState = "idle"
    output.append("")
    return (newState, output, input)

def paid5_transitions(input, output):
    currentInput = input[0]  
    input =  input[1:] if len(input) > 1 else []
    if currentInput == "tea":
        newState = "idle"
        output.append("cupOfTea")
    elif currentInput == "coffee":
        newState = "idle"
        output.append("return-5")
    elif currentInput == "coin-5":
        newState = "Paid10"
        output.append("")
    else:
        newState = "idle"
        output.append("")
    return (newState, output, input)

def paid10_transitions(input, output):
    currentInput = input[0]  
    input =  input[1:] if len(input) > 1 else []
    if currentInput == "tea":
        newState = "idle"
        output.append("cupOfTea, return-5")
    elif currentInput == "coffee":
        newState = "idle"
        output.append("cupOfCoffee")
    else:
        newState = "idle"
        output.append("")
    return (newState, output, input)

def getCVM():
    m = StateMachine()
    m.add_state("idle", idle_transitions)
    m.add_state("Paid5", paid5_transitions)
    m.add_state("Paid10", paid10_transitions)
    m.set_start("idle")
    return m