print("Hallo, Welt!")
string_1 = "Hello "
string_2 = "World!"
print(string_1 + string_2)

result = (string_1 + string_2 + " ") * 4
print(result)

product = 4 * 4
quotient = 32 / 4
# bad = 32 / 0            # ZeroDivisionError: division by zero


a = 4
b = 0
try:
    result = a/b
except ZeroDivisionError:
    result="durch null"

print(result)


print(product)
print(quotient)