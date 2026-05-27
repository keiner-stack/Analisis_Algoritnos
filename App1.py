from flask import Flask, render_template, request
import random
import bisect

app = Flask(__name__)


# =========================
# MERGE SORT
# =========================

def merge_sort(lista):

    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2

    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):

    resultado = []

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):

        if izquierda[i] < derecha[j]:

            resultado.append(izquierda[i])
            i += 1

        else:

            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# =========================
# RUTA PRINCIPAL
# =========================

@app.route("/", methods=["GET", "POST"])

def inicio():

    resultado = None

    if request.method == "POST":

        objetivo = request.form["password"]

        passwords = random.sample(range(10000), 10000)

        passwords = [f"{n:04d}" for n in passwords]

        passwords = merge_sort(passwords)

        posicion = bisect.bisect_left(passwords, objetivo)

        if posicion < len(passwords) and passwords[posicion] == objetivo:

            resultado = f"Contraseña encontrada en posición {posicion + 1}"

        else:

            resultado = "Contraseña no encontrada"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)