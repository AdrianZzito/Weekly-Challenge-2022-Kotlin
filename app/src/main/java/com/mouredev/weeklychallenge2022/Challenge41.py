
"""
 * Reto #41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 """

def calculo_ohm(V, R, I):
    try:

        # Calculo Voltaje
        if V == None:
            calculo_V = (R * I)
            return print(calculo_V)

        # Calculo Resistencia
        elif R == None:
            calculo_R = (V / I)
            return print(calculo_R)

        # Calculo Corriente
        elif I == None:
            calculo_I = (R / I)
            return print(calculo_I)
        
    except TypeError:
        print("Invalid Values")

if __name__ == "__main__":

    # Introduce aqui los valores (V, I, R)
    calculo_ohm(None, 5, 6)
