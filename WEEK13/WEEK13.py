# 04/14/2026  Honour Okhavhe CIS106


# 1. Prompt the user for a number which will represent the number of items in a list.
# Then use a for loop to add that many integers to the list. Display the list.
num_items = int(input("Enter the number of items for the list: "))
my_list = []
for i in range(num_items):
    num = int(input(f"Enter integer {i+1}: "))
    my_list.append(num)
print("\n1. Initial list:", my_list)

# 2. Insert the score of 99 at position 1 within the list. Display the updated list.
my_list.insert(1, 99)
print("2. List after inserting 99 at position 1:", my_list)

# 3. Replace the value of 99 with the value 100. Display the updated list.
# (Since we just inserted 99 at index 1, we can replace index 1 directly)
my_list[1] = 100 
print("3. List after replacing 99 with 100:", my_list)

# 4. Create a second list with the values 500, 600, 700, 800, 900. Display this list.
# Extend the first list with this second list. Display the first list.
second_list = [500, 600, 700, 800, 900]
print("4. Second list:", second_list)
my_list.extend(second_list)
print("   First list after being extended:", my_list)

# 5. Remove the value 800 from the first list. Display the first list.
my_list.remove(800)
print("5. List after removing 800:", my_list)

# 6. Remove the third item from the first list. Display the first list.
# (The third item corresponds to index 2 in Python)
my_list.pop(2)
print("6. List after removing the third item:", my_list)

# 7. Create a list of grades: grades = ["A", "B", "C", "A", "A", "C"]
grades = ["A", "B", "C", "A", "A", "C"]
print("7. Grades list created:", grades)

# 8. Display a count of the number of A grades.
print("8. Count of 'A' grades:", grades.count("A"))

# 9. Display the index (position) of the first B grade.
print("9. Index of the first 'B' grade:", grades.index("B"))

# 10. Look for grade of F in the grades list. Display a message that F is not in the list.
# (Do not let the code generate an error).
if "F" not in grades:
    print("10. F is not in the list.")

# 11. Clear (but do not delete) the second list of integers. Display the list.
second_list.clear()
print("11. Second list after clearing:", second_list)

# 12. Delete the second list. Try to display it. 
del second_list
print("12. Deleting second_list...")
try:
    print(second_list)
except NameError as e:
    print("    Error expected and caught:", e)

# 13. Create a list of players in this order ("Rizzo", "Davis", "Baez", "Happ", "Bryan")
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print("13. Players list:", players)

# 14. Sort the list of players. Display the sorted list.
players.sort()
print("14. Sorted players list:", players)

# 15. Make a copy of the list of players called players2. Display players2.
players2 = players.copy()
print("15. players2 (copy of players):", players2)

# 16. Reverse the order of players2. Display players, then display players2.
players2.reverse()
print("16. Original players list:", players)
print("    Reversed players2 list:", players2)