import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return number
        if number % 2 == 0:
            return
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return
            return number
        return number
        
for i in range (1,151):
    print(is_prime(i))