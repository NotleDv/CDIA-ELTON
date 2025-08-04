popu_x = 70.000
popu_y = 180.000

anos = 0
while (popu_x<popu_y):
    popu_x += popu_x**0.035
    anos += 1

print(f"Quantidade anos: {anos}")
print(f"População x: {popu_x}")
print(f"População y: {popu_y}")