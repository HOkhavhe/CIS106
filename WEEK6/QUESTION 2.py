04/15/26   Honour Okhavhe CIS106-001



# Problem 2: Display numbers from a custom start, stop, and increment [cite: 6, 7]

start_val = int(input("Enter the start value: "))
stop_val = int(input("Enter the stop value: "))
increment_val = int(input("Enter the increment value: "))

current_val = start_val

# Use a while loop structure 
while current_val <= stop_val:
    print(current_val)
    current_val += increment_val
