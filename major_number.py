Rep = int(input("How many number you want to choose?: "))

count = 0
numbers = []

while count < Rep:
    x = int(input("Choose number: "))
    numbers.append(x)
    count += 1

print("You have choose: ", numbers)

numbers.sort() 

print("Now let's sort them: ", numbers)
major_number = numbers[-1] #the last number in list numbers
print("The major number is: ", major_number)