# Contador Binario:
# Escriban un programa que, usando un ciclo, cuente desde 0 hasta 15 y muestre cada número en su representación binaria.
# Extensión: Utilicen un retardo (por ejemplo, con time.sleep) para simular el conteo de un circuito.
import time

def concatenar_ceros(rs): # Funcion para rellenar cifras 0 al numero binario
    while len(rs) < 4:
        rs = "0" + rs
    return rs

def conversor_binario(i): 
    if i == 0:
        print(f"{i}: 0000")  # Maneja el caso especial para 0
    else:
        resto_string = ""  # Variable para almacenar el binario
        numero = i
        while numero > 0:  # Convierte el número a binario
            resto = numero % 2  # Obtiene el resto
            resto_string = str(resto) + resto_string  # Agrega el dígito al inicio
            numero = numero // 2  # Divide entre 2
        resto_string = concatenar_ceros(resto_string) # Asegura que tenga 4 dígitos
        print(f"{i}: {resto_string}")

for i in range(16):
    conversor_binario(i)
    time.sleep(0.5)  # Pausa de 0.5 segundo
