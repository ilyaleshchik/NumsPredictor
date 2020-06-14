import numpy as np
import scipy.special
import matplotlib.pyplot



class NN:
    def __init__(self, InputNodes, OutputNodes, HiddenNodes, LearningRate):
        self.InputNodes = InputNodes
        self.OutputNodes = OutputNodes
        self.HiddenNodes = HiddenNodes
        self.RATE = LearningRate
        self.wInHid = np.random.normal(0.0, pow(self.HiddenNodes, -0.5), (self.HiddenNodes, self.InputNodes))
        self.wHidOut = np.random.normal(0.0, pow(self.OutputNodes, -0.5), (self.OutputNodes, self.HiddenNodes))
        self.ActivationFunc = lambda x: scipy.special.expit(x)

    def Training(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        hidden_inputs = np.dot(self.wInHid, inputs)
        hidden_outputs = self.ActivationFunc(hidden_inputs)

        final_inputs = np.dot(self.wHidOut, hidden_outputs)
        final_outputs = self.ActivationFunc(final_inputs)

        error = targets - final_outputs
        hidden_errors = np.dot(self.wHidOut.T, error)

        self.wHidOut += self.RATE * np.dot((error * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.wInHid += self.RATE * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

    def Query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_inputs = np.dot(self.wInHid, inputs)
        hidden_outputs = self.ActivationFunc(hidden_inputs)

        final_inputs = np.dot(self.wHidOut, hidden_outputs)
        final_outputs = self.ActivationFunc(final_inputs)

        return final_outputs

    def GetWeights(self):
        print(self.wInHid)
        print(self.wHidOut)


# input_nodes = 784
# output_nodes = 10
# hiden_nodes = 200
# learning_rate = 0.1


# Network = NN(input_nodes, output_nodes, hiden_nodes, learning_rate)



# trainig_data = open("mnist_train.csv", 'r')
# trainig_list = trainig_data.readlines()
# trainig_data.close()


# print(len(trainig_list))


# ers = int(input("Count of eres: "))

# for e in range(ers):
#     k = 1
#     for data in trainig_list:
#         print('pretesting on' ,  e + 1, 'era on ', k, 'test')
#         all_vals = data.split(',')

#         inputs = (np.asfarray(all_vals[1:]) / 255.0 * 0.99) + 0.01
#         tragets = np.zeros(output_nodes) + 0.01
#         tragets[int(all_vals[0])] = 0.99
#         Network.Training(inputs, tragets)
#         k += 1



# test_data = open("mnist_test.csv", 'r')
# test_list = test_data.readlines()
# test_data.close()


# scored = []



# for test in test_list:
#     test_vals = test.split(',')
#     correct = int(test_vals[0])
#     inputs = (np.asfarray(test_vals[1:]) / 255.0 * 0.99) + 0.01
#     res = Network.Query(inputs)
#     ans = np.argmax(res)

#     print("The network answer is", ans)

#     if(ans == correct):
#         scored.append(1)
#     else:
#         scored.append(0)


# scored = np.asarray(scored)

# print("The persent of truth answers is", scored.sum() / scored.size * 100 ,'%')

# Network.GetWeights()