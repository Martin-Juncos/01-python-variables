# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
# name = input('¿Cuál es tu nombre? ')
# age = input('¿Cuántos años tienes? ')
# print(name)
# print(age)

# Cambiamos su tipo
name = age
age = "Brais"
print('name', name)
print('age', age)

# ¿Forzamos el tipo?
# address: str = "Mi dirección"
# print(type(address))
# print(len(address))
# address = True
# print(type(address))
# address = 5
# print(type(address))
# address = 1.2
# print(type(address))
