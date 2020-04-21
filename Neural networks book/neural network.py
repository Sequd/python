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

        # w_i_j
        # w11 w21
        # w12 w22 etc
        # матрици весов связей wih (входной-скрытый)
        self.wih = (numpy.random.rand(self.hidden, self.input) - 0.5)

        # матрици весов связей who (скрытый-выходной)
        self.who = (numpy.random.rand(self.output, self.hidden) - 0.5)

        # self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        # self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # сигмоида в качестве функции активации
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    def train(self, input_list, target_list):
        """тренировка сети"""

        # преобразовать список входных значений в думерный массив
        inputs = numpy.array(input_list, ndmin=2).T
        target = numpy.array(target_list, ndmin=2).T

        # рассчитать входящие сигналы для скрытого слоя
        hidden_inputs = numpy.dot(self.wih, inputs)

        # рассчитать исходящие сигналы для скрытого слоя
        hidden_outputs = self.activation_function(hidden_inputs)

        # рассчитать входящие сигналы для выходного слоя
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # рассчитать исходящие сигналы для выходного слоя
        final_outputs = self.activation_function(final_inputs)

        # ошибка = целевое значение - фактическое значение
        output_errors = target - final_outputs

        # ошибка скрытого слоя - это ошибки output_errors,
        # распределенные пропорцианально весовым коэффицентам связей
        # и рекомбинированные на скрытых узлах
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # обновить весовые коэффициенты связей между скрытым и выходным слоями
        self.who += self.lr * numpy.dot(
            (output_errors * final_outputs * (1.0 - final_outputs)),
            numpy.transpose(hidden_outputs))

        # обновить весовые коэффициенты связей между входным и скрытым слоями
        self.wih += self.lr * numpy.dot(
            (hidden_outputs * hidden_outputs * (1.0 - hidden_outputs)),
            numpy.transpose(inputs))

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


input_number = 3
hidden_number = 3
output_number = 3
rate = 0.3

n = NeuralNetwork(input_number, hidden_number, output_number, rate)
final = n.query([1.0, 0.5, -1.5])
print(final)
