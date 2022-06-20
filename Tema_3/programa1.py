print('Hola, bienvenido al programa de cálculo de masa corporal')

print('Introduce tu peso en kg')
peso = int(input("peso: "))

print('Introduce tu estatura')
estatura = float(input("estatura: "))

IMC=peso//estatura**2
res_redondeo = round(IMC, 4)

print('Tu índice de masa corporal es: ', res_redondeo)
