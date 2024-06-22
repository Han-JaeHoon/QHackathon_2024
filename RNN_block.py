import pennylane as qml
class RNN_block:
    def __init__(self, input_size):
        self.input_size = input_size

    
    def embedding(self, params):
        n = self.input_size
        for i in range(n):
            qml.Hadamard(i)
            qml.RZ(2.0 * params[:,i], i)
        
        for i in range(n - 1):
            qml.IsingZZ(2.0 * params[:,n + i] ,[i , i + 1])
    
    def ansatz(self, params, all_entangled = False):
        # Length of Params : 3 * num_qubit
        n = self.input_size
        for i in range(n):
            qml.RX(params[3 * i], i)
            qml.RY(params[3 * i + 1], i)
            qml.RZ(params[3 * i + 2], i)
        for i in range(n - 1):
            qml.CNOT([i, i + 1])
        if all_entangled:
            qml.CNOT([n - 1, 0])
            
class RNN_block_noise:
    def __init__(self, input_size):
        self.input_size = input_size

    
    def embedding(self, params):
        n = self.input_size
        for i in range(n):
            qml.Hadamard(i)
            qml.RZ(2.0 * params[:,i], i)
        
        for i in range(n - 1):
            qml.IsingZZ(2.0 * params[:,n + i] ,[i , i + 1])
            qml.DepolarizingChannel(0.02, wires=[i]) 
            qml.DepolarizingChannel(0.02, wires=[i + 1]) 
            qml.BitFlip(0.02, wires=[i])
            qml.BitFlip(0.02, wires=[i + 1])
    def ansatz(self, params, all_entangled = False):
        # Length of Params : 3 * num_qubit
        n = self.input_size
        for i in range(n):
            qml.RX(params[3 * i], i)
            qml.RY(params[3 * i + 1], i)
            qml.RZ(params[3 * i + 2], i)
        for i in range(n - 1):
            qml.CNOT([i, i + 1])
            qml.DepolarizingChannel(0.02, wires=[i]) 
            qml.DepolarizingChannel(0.02, wires=[i + 1]) 
            qml.BitFlip(0.02, wires=[i])
            qml.BitFlip(0.02, wires=[i + 1])
        if all_entangled:
            qml.CNOT([n - 1, 0])