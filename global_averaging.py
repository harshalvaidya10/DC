import numpy as np 

num_nodes = 5
data_size = 10
iterations = 1000
learning_rate  = 0.1

data = [np.random.rand(data_size) for i in range(num_nodes)]
print(data)

global_avg = [0]*data_size

for i in range(iterations):
    for j in range(num_nodes):
        local_avg = data[j]
        local_avg -= (local_avg - globa_avg)*learning_rate
        data[j] = local_avg
    globa_avg = np.mean(data, axis = 0)

print(global_avg)
