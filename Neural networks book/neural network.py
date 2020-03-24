import numpy
import scipy.special


# определение класса нейроной сети
class NeuralNetwork:

    # инициализировать сеть
    def __init__(self, inputNodes, hiddenNodes, outputNodes, lerningRate):
        # задать кол-во узлов. входные, скрытые, выходные
        self.output = outputNodes
        self.hidden = hiddenNodes
        self.input = inputNodes

        # коэффициент обучения
        self.lr = lerningRate

        # матрици весов связей wih (входной-скрытый)
        self.wih = (numpy.random.rand(self.hidden, self.input) - 0.5)

        # матрици весов связей who (скрытый-выходной)
        self.who = (numpy.random.rand(self.output, self.hidden) - 0.5)

        # сигмоида в качестве функции активации
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    def train(self):
        """тренировка сети"""
        pass

    def query(self, inputs):
        """опрос сети"""
        # рассчитать входные сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)

        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)

        # расчитать входные сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # расчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


input = 3
hidden = 3
output = 3
rate = 0.3

n = NeuralNetwork(input, hidden, output, rate)
final = n.query([1.0, 0.5, -1.5])
print(final)
