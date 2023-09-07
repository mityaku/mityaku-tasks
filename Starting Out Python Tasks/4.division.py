num = int(input("Enter an integer: "))
divisor = int(input("Enter a divisor: "))

times = num // divisor
remainder = num % divisor

print(f"{divisor} divides {num} {times} times with a remainder of {remainder}.")
