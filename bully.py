def bully(total, detect, failed):
    high_priority_machines = [i for i in range(detect + 1 , total + 1) if i != failed]
    print(f"Machine {detect} sends message to {high_priority_machines}")

    while len(high_priority_machines) > 0:
        sender = high_priority_machines[0]
        high_priority_machines.pop(0)
        print(f"Machine {sender} sends election message to {high_priority_machines}")
        for machine in high_priority_machines:
            print(f"Machine {machine} sends OK message to {sender}")

    print(f"Machine {sender} is elected as the new co-ordiantor")


bully(7, 2, 5)