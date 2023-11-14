#input an integer from the user
num = int(input("Enter an integer: "))

#initializes an empty list to store factors
factors = []

#finds and stores the factors
for i in range(2, num + 1):
    if num % i == 0:
        factors.append(i)

#prints the factors
print("Factors of", num, "are:", factors)
