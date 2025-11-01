# for count in range(0, 3, 1):
#     for number in range(0, 10, 1):
#         print(f"{number} |", end="")

# Display a grid of ASCII emoji
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))

for i in range(rows):
    for j in range(columns):
        print(":)", end=" ")
    print()