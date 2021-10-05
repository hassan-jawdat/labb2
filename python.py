import math

print("please Enter the length of many side of any side of a Cube in cm.")
side = int(input())

print("choose volume for either "
      "1- cube "
      "2- Tetrahedron. ")

while True:
    choose = int(input("please type 1 or 2 "))

    if choose == 1:
        volume = side ** 3
        print(f'volume for cube is {round(volume,2)} cm3')
        break

    elif choose ==2:
        volume = (side ** 3) / (6 * math.sqrt(2))
        print(f'Volume for tetrahedron is {round(volume,2)} cm3')
        break

    else:
        print("sorry, i did not understand that.")
        continue