import numpy
import scipy.special
import matplotlib.pyplot as plt


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
        # self.wih = (numpy.random.rand(self.hidden, self.input) - 0.5)

        # матрици весов связей who (скрытый-выходной)
        # self.who = (numpy.random.rand(self.output, self.hidden) - 0.5)

        self.wih = numpy.random.normal(0.0, pow(self.input, -0.5),
                                       (self.hidden, self.input))
        self.who = numpy.random.normal(0.0, pow(self.hidden, -0.5),
                                       (self.output, self.hidden))

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


# кол-во входных, скрытых и выходных узлов
input_number = 784
hidden_number = 100
output_number = 10
rate = 0.3

n = NeuralNetwork(input_number, hidden_number, output_number, rate)

data_file = open("dataset/mnist_train.csv", 'r')
data_list = data_file.readlines()
data_file.close()

# тренеровка сети

epochs = 1

for _ in range(epochs):
    # перебрать все записи в тренеровочном наборе
    for record in data_list:
        all_values = record.split(',')
        # масштабировать и сместить входные данные
        inputs_data = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # создать целевые входные значения, все 0.01 кроме маркерного (0.99)
        targets = numpy.zeros(output_number) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs_data, targets)

# проверка сети


test_data_file = open("dataset/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# журнал оценок сети
scorecard = []
for record in test_data_list:
    all_values = record.split(',')
    correct_label = int(all_values[0])

    print(correct_label, "истеный маркер")

    # масштабировать и сместить входные значения
    inputs_data = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

    # опрос сети
    outputs = n.query(inputs_data)

    # наибольшый маркер
    label = numpy.argmax(outputs)
    print(label, "ответ сети")
    # присоеденить оценку ответа сети к таблице
    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)

print(scorecard)
scorecard_array = numpy.asarray(scorecard)
print("эффективность сети = ", scorecard_array.sum() / scorecard_array.size)
# image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
# plt.imshow(image_array, cmap='Greys', interpolation='None')
# plt.show()
# n.query()
