def tower_of_hanoi(n, source, auxiliary, target):
    # Base case
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    
    # Move n-1 disks from source to auxiliary, using target as auxiliary
    tower_of_hanoi(n-1, source, target, auxiliary)
    
    # Move the remaining disk from source to target
    print(f"Move disk {n} from {source} to {target}")
    
    # Move n-1 disks from auxiliary to target, using source as auxiliary
    tower_of_hanoi(n-1, auxiliary, source, target)
tower_of_hanoi(3, 'A', 'B', 'C')