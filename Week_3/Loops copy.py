# Robot removing apples from a box
number = int(input("How many apples should I remove? "))
removed_apples = 0
while removed_apples < number:
    print("Removed apple.")
    removed_apples += 1
    print (f"...Done {removed_apples} apples taken")
print ("All apples has been removed!")