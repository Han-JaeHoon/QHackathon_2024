n = 5 # length of feature vecture

temp_dev = qml.device("default.qubit", wires = n)

def embedding(params):
    n = (len(params) + 1) // 2
    for i in range(n):
        qml.Hadamard(i)
        qml.RZ(2.0 * params[i], i)
    
    for i in range(n - 1):
        qml.IsingZZ(2.0 * params[n + i] ,[i , i + 1])

@qml.qnode(temp_dev, interface="torch")
def fidelity(vec1, vec2):
    '''
        Args:
            vec1 : list, (2n - 1)개의 element로 이루어진 vector
            vec2 : list, (2n - 1)개의 element로 이루어진 vector
    '''
    embedding(vec1) # Phi(x1) circuit 적용
    qml.adjoint(embedding)(vec2) # Phi^t(x2) 적용
    return qml.probs()

def n_to_2n_1(vec): # 대충 n -> (2n -1) list로 변환하는 간이 함수. 테스트용
    return vec + vec[1:]

def cost_fn(x1, x2, y1, y2):
    '''
        Args:
            x1 : list, n개의 element로 이루어진 vector
            x2 : list, n개의 element로 이루어진 vector
            y1 : list, (2n - 1)개의 element로 이루어진 vector
            y2 : list, (2n - 1)개의 element로 이루어진 vector
    '''
    vec1 = n_to_2n_1(x1) ## n개의 feature로 이루어진 vector를 2n-1개의 vector로
    vec2 = n_to_2n_1(x2)

    result = fidelity(vec1, vec2)
    print(result)

x1 = [0.5] * 5
x2 = [0.5] * 5
cost_fn(x1, x2, [], [])