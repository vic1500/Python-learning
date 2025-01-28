import random as rand

for i in range(10):
    print(rand.randint(10, 20))

members = ["Mosh", "Mary", "Bob", "John"]
print(rand.choice(members))