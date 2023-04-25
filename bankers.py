def check(i, need , available , r):
    for j in range(r):
        if need[i][j] > available[j]:
            return False
    return True


#initialise
# p, r , need , allocate, maximum , available , sequence , visited , count
p = 5
r = 4
allocated = [[4, 0, 0, 1], [1, 1, 0, 0], [1, 2, 5, 4], [0, 6, 3, 3], [0, 2, 1, 2]]  # matrix of currently allocated resources
maximum = [[6, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [1, 6, 5, 3], [1, 6, 5, 6]]  # matrix of maximum resources each process can request
available = [3, 2, 1, 1]  # list of available instances of each resource
need = [[0 for i in range(r)] for j in range(p)]

sequence = [0]*p
visited = [0]*p

count = 0

for i in range(p):
    for j in range(r):
        need[i][j] = maximum[i][j] - allocated[i][j]

    
  
while count < p:
   for i in range(p):
        if not visited[i] and check(i, need , available , r):
            sequence[count] = i
            visited[i] = 1
            count += 1

            for j in range(r):
                available[j] += allocated[i][j]

# check if all processes executed successfully
if count < p:
    print('The system is unsafe')
else:
    print("This system is safe")
    print("The safe sequence is", sequence)
    print("The available resources are", available)