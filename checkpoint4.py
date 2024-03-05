
import math
# exercise 1
my_list = ["hola", "kaixo", "hello", "salut"]
my_tuple = ("nombre", "apellido", "edad", "genero")
my_float = 15.60
my_integer = 33
my_decimal = 33.3456789
my_diccionary = {
    "nombre1": "david",
    "nombre2": "ivan",
    "nombre3": "alaia",
    "nombre4": "alicia"
}
print(my_list)
print(my_tuple)
print(my_float)
print(my_integer)
print(my_decimal)
print(my_diccionary)

# exercise 2
my_round_number = math.ceil(my_float)
print(my_round_number)

# exercise 3
my_square_number = math.sqrt(my_float)
print(my_square_number)

#exercise 4

print(my_diccionary["nombre1"])

# exercise 5

print(my_tuple[1])

# exercise 6

my_list.append("halo")
print(my_list)

# exercise 7

my_list[0] = "holita"
print(my_list)

# exercise 8

my_list.sort()
print(my_list)

# exercise 9

my_new_tuple = my_tuple + ("domicilio",)
print(my_new_tuple)
 