popu_x = 70000
popu_y = 180000

anos = 0
while (popu_x<popu_y):
    popu_x += popu_x * 0.035
    popu_y += popu_y * 0.015
    anos += 1

print(f"Quantidade anos: {anos}")
print(f"População x: {popu_x:.0f}")
print(f"População y: {popu_y:.0f}")