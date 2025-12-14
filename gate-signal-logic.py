def relay(input_signal):
    return input_signal  

def and_gate(a, b):
    return relay(a) and relay(b)  

def or_gate(a, b):
    return relay(a) or relay(b)   

print(and_gate(True, False))  
