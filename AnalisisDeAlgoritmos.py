import streamlit as st
import random
import time
import pandas as pd
import plotly.express as px


# =====================================================
# CONFIGURACION PAGINA
# =====================================================

st.set_page_config(
    page_title="Analizador de Algoritmos",
    page_icon="🧠",
    layout="wide"
)


# =====================================================
# ESTILOS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

div.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.resultado {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# TITULO
# =====================================================

st.title("🧠 Analizador de Algoritmos")

st.write(
    "Comparación entre algoritmos de ordenamiento "
    "y búsqueda."
)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("⚙️ Configuración")


cantidad = st.sidebar.slider(
    "Cantidad de datos",
    100,
    10000,
    1000
)


ordenamiento = st.sidebar.selectbox(
    "Algoritmo de Ordenamiento",
    [
        "Bubble Sort",
        "Insertion Sort",
        "Merge Sort"
    ]
)


busqueda = st.sidebar.selectbox(
    "Algoritmo de Búsqueda",
    [
        "Lineal",
        "Binaria"
    ]
)


# =====================================================
# GENERAR DATOS
# =====================================================

datos = random.sample(range(cantidad * 10), cantidad)

datos = [f"{n:04d}" for n in datos]


# =====================================================
# ALGORITMOS ORDENAMIENTO
# =====================================================

def bubble_sort(lista):

    lista = lista.copy()

    for i in range(len(lista)):

        for j in range(0, len(lista) - i - 1):

            if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def insertion_sort(lista):

    lista = lista.copy()

    for i in range(1, len(lista)):

        clave = lista[i]

        j = i - 1

        while j >= 0 and clave < lista[j]:

            lista[j + 1] = lista[j]

            j -= 1

        lista[j + 1] = clave

    return lista


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


# =====================================================
# ALGORITMOS BUSQUEDA
# =====================================================

def busqueda_lineal(lista, objetivo):

    for i in range(len(lista)):

        if lista[i] == objetivo:

            return i

    return -1


def busqueda_binaria(lista, objetivo):

    izquierda = 0

    derecha = len(lista) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:

            return medio

        elif lista[medio] < objetivo:

            izquierda = medio + 1

        else:

            derecha = medio - 1

    return -1


# =====================================================
# ENTRADA USUARIO
# =====================================================

objetivo = st.text_input(
    "🔑 Ingrese una contraseña",
    placeholder="Ejemplo: 0456"
)


# =====================================================
# BOTON EJECUTAR
# =====================================================

if st.button("🚀 Ejecutar Análisis"):

    if objetivo.isdigit():

        objetivo = f"{int(objetivo):04d}"


        # ==========================================
        # ORDENAMIENTO
        # ==========================================

        inicio_ordenamiento = time.time()

        if ordenamiento == "Bubble Sort":

            datos_ordenados = bubble_sort(datos)

        elif ordenamiento == "Insertion Sort":

            datos_ordenados = insertion_sort(datos)

        else:

            datos_ordenados = merge_sort(datos)

        fin_ordenamiento = time.time()

        tiempo_ordenamiento = (
            fin_ordenamiento - inicio_ordenamiento
        )


        # ==========================================
        # BUSQUEDA
        # ==========================================

        inicio_busqueda = time.time()

        if busqueda == "Lineal":

            posicion = busqueda_lineal(
                datos_ordenados,
                objetivo
            )

        else:

            posicion = busqueda_binaria(
                datos_ordenados,
                objetivo
            )

        fin_busqueda = time.time()

        tiempo_busqueda = (
            fin_busqueda - inicio_busqueda
        )


        # ==========================================
        # RESULTADOS
        # ==========================================

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "⏱️ Tiempo Ordenamiento",
                f"{tiempo_ordenamiento * 1000:.4f} ms"
            )

        with col2:

            st.metric(
                "🔍 Tiempo Búsqueda",
                f"{tiempo_busqueda * 1000:.4f} ms"
            )

        with col3:

            if posicion >= 0:

                st.metric(
                    "📍 Posición",
                    posicion + 1
                )

            else:

                st.metric(
                    "📍 Posición",
                    "No encontrada"
                )


        # ==========================================
        # TABLA
        # ==========================================

        st.subheader("📊 Resultados")

        df = pd.DataFrame({

            "Algoritmo Ordenamiento": [ordenamiento],

            "Algoritmo Búsqueda": [busqueda],

            "Tiempo Ordenamiento": [tiempo_ordenamiento],

            "Tiempo Búsqueda": [tiempo_busqueda]

        })

        st.dataframe(df)


        # ==========================================
        # GRAFICA
        # ==========================================

        grafica = pd.DataFrame({

            "Proceso": [
                "Ordenamiento",
                "Búsqueda"
            ],

            "Tiempo": [
                tiempo_ordenamiento,
                tiempo_busqueda
            ]

        })

        fig = px.bar(
            grafica,
            x="Proceso",
            y="Tiempo",
            title="Comparación de Tiempos"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.warning(
            "Ingrese solo números"
        )