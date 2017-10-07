from timeit import default_timer
from math import ceil, sqrt


# funkcia na zapisovanie cisla do suboru
def add_number_to_file(num, file):
    f = open(file, "a+")
    f.write(str(num) + "\n")
    f.close


# funkcia ktora urcuje ci je cislo prvocislo alebo nie
def is_prime(num):
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2, int(ceil(sqrt(num)))):
        if num % i == 0:
            return False
    return True


# funkcia ktora skusi ci je cislo prvocislo a az potom ho zapise na zvoleny subor
def add_prime_to_file(num, file):
    if is_prime(num):
        add_number_to_file(num, file)
    else:
        print"Number is not prime"


# cas
start = default_timer()
add_prime_to_file(151, "file.txt")
add_prime_to_file(50, "file.txt")
# print is_prime(13)
print "Execution takes " + str(default_timer() - start) + " seconds"
