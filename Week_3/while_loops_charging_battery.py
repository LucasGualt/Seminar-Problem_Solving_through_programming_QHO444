# Robot avoiding bars
number = int(input("How many bars should be charged?"))
bars = 0
while bars < number:
    print("Charging:", " ".join ("█" * bars))
    bars += 1
    print (f"")
print ("The battery is fully charged!")