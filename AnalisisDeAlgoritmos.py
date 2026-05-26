import random
import bisect
import streamlit as st


# =========================
# CONFIGURACION PAGINA
# =========================

st.set_page_config(
    page_title="Sort & Search",
    page_icon="🔍",
    layout="centered"
)


# =========================
# TITULO
# =========================

st.title("🔍 Sistema de Búsqueda de Contraseñas")

st.write(
    "Esta aplicación genera contraseñas desordenadas, "
    "las ordena usando Merge Sort y realiza una búsqueda binaria."
)


# =========================
# GENERAR CONTRASEÑAS
# =========================

passwords = random.sample(range(10000), 10000)

passwords = [f"{n:04d}" for n in passwords]


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
# ORDENAMIENTO
# =========================

passwords = merge_sort(passwords)


# =========================
# ENTRADA USUARIO
# =========================

objetivo = st.text_input(
    "Ingrese una contraseña de 4 dígitos",
    placeholder="Ejemplo: 0456"
)


# =========================
# BOTON BUSCAR
# =========================

if st.button("Buscar contraseña"):

    if objetivo.isdigit() and len(objetivo) <= 4:

        objetivo = f"{int(objetivo):04d}"

        posicion = bisect.bisect_left(passwords, objetivo)

        if posicion < len(passwords) and passwords[posicion] == objetivo:

            st.success("Contraseña encontrada")

            st.write(f"🔑 Contraseña: {objetivo}")
            st.write(f"📍 Posición: {posicion + 1}")
            st.write("⚡ Método de búsqueda: Búsqueda Binaria")
            st.write("📚 Método de ordenamiento: Merge Sort")

        else:
            st.error("Contraseña no encontrada")

    else:
        st.warning("Ingrese solo números entre 0000 y 9999")