# Robot avoiding obstacles
number = int(input("How many obstacles must I avoid?"))
obstacles = 0
while obstacles < number:
    print("Obstacle avoided!")
    obstacles += 1
    print (f"...Done {obstacles} obstacles taken")
print ("All obstacles have been avoided!")