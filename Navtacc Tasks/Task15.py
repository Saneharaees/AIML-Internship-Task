s = ["Geeks", "for", "Geeks"]

# using for loop with list of strings
for i in s:
    print(i)

    s = "Geeks"
for i in s:
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in 'geeksforgeeks':

    if i == 'e' or i == 's':
        continue
    print(i)

for i in 'geeksforgeeks':

    # break the loop as soon it sees 'e'
    # or 's'
    if i == 'e' or i == 's':
        break

print(i)

for i in 'geeksforgeeks':
    pass
print(i)

for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print (i, j)

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)