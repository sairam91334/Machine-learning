
n = int(input("Enter a positive integer: "))


print("\nNumbers from 1 to", n, "using a for loop:")
for i in range(1, n + 1):
    print(i)


sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1

print("\nThe sum of all numbers from 1 to", n, "is:", sum_numbers)
