servers = int(input("Enter number of servers: "))
processes = int(input("Enter number of processes: "))

def rrlb(servers, processes):
    lst = []
    for i in range(processes):
        lst.append((i%servers)+1)

    for i in range(servers):
        print(f"Server {i + 1} has {lst.count(i + 1)} processes")



while True:
    rrlb(servers, processes)
    choice = int(input("\n1. Add server\n2. remove server\n3. add process\n4. remove process\n5. exit\n"))
    if choice == 1:
        servers += 1
    elif choice == 2:
        servers -= 1
    elif choice == 3:
        processes += 1
    elif choice == 4:
        processes -= 1
    else:
        break