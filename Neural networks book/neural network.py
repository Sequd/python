import numpy


# определение класса нейроной сети
class NeuralNetwork:

    # инициализировать сеть
    def __init__(self, inputNodes, hiddenNodes, outputNodes, lerningRate):
        # задать кол-во узлов. входные, скрытые, выходные
        self.oNodes = outputNodes
        self.hNodes = hiddenNodes
        self.iNodes = inputNodes

        # коэффициент обучения
        self.lr = lerningRate

        # матрици весов связей wih (входной-скрытый)
        self.wih = (numpy.random.rand(self.hNodes, self.iNodes) - 0.5)

        # матрици весов связей who (скрытый-выходной)
        self.who = (numpy.random.rand(self.oNodes, self.hNodes) - 0.5)

    # тренировка сети
    def train(self):
        pass

    # опрос сети
    def query(self):
        pass


input = 3
hidden = 3
output = 3
rate = 0.3

n = NeuralNetwork(input, hidden, output, rate)

x = (numpy.random.rand(3, 3) - 0.5)
print(x)
