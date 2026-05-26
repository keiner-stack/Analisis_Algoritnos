import streamlit as st
import random
import time

# ----------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ----------------------------------------

st.set_page_config(
    page_title="Sort & Search",
    page_icon="📊",
    layout="centered"
)

# ----------------------------------------
# ESTILOS
# ----------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#050816;
    color:white;
}

html, body, [class*="css"]{
    color:white;
    font-family:Arial;
}

h1,h2,h3{
    color:white;
}

.stTextInput input{
    background-color:#1e1e2f !important;
    color:white !important;
    border-radius:15px !important;
    height:55px;
    font-size:24px;
}

.stButton > button{
    background-color:transparent;
    color:white;
    border:1px solid #3b3b50;
    border-radius:15px;
    width:150px;
    height:70px;
    font-size:22px;
}

.stButton > button:hover{
    border:1px solid #00ffaa;
    color:#00ffaa;
}

.resumen{
    color:#38f2c2;
    font-size:50px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# ALGORITMOS DE ORDENAMIENTO
# ----------------------------------------

def burbuja(lista):

    n = len(lista)

    for i in range(n):

        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def insercion(lista):

    for i in range(1, len(lista)):

        actual = lista[i]

        j = i - 1

        while j >= 0 and lista[j] > actual:

            lista[j + 1] = lista[j]

            j -= 1

        lista[j + 1] = actual

    return lista


def mezcla(lista):

    return sorted(lista)

# ----------------------------------------
# ALGORITMOS DE BÚSQUEDA
# ----------------------------------------

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

# ----------------------------------------
# SESSION STATE
# ----------------------------------------

if "lista_ordenada" not in st.session_state:
    st.session_state.lista_ordenada = None

if "algoritmo_ordenamiento" not in st.session_state:
    st.session_state.algoritmo_ordenamiento = None

if "tiempo_orden" not in st.session_state:
    st.session_state.tiempo_orden = None

if "algoritmo_busqueda" not in st.session_state:
    st.session_state.algoritmo_busqueda = None

if "tiempo_busqueda" not in st.session_state:
    st.session_state.tiempo_busqueda = None

if "posicion" not in st.session_state:
    st.session_state.posicion = None

# ----------------------------------------
# TÍTULO
# ----------------------------------------

st.title("📊 SORT & SEARCH")

st.write("Ordenamiento • Búsqueda • Tiempo Real")

# ----------------------------------------
# PASO 1
# ----------------------------------------

st.header("1. ¿Cuál es el objetivo?")

objetivo = st.text_input(
    "Ingresa un número de 4 dígitos:",
    max_chars=4,
    placeholder="Ej: 1234"
)

# ----------------------------------------
# VALIDACIONES
# ----------------------------------------

valido = False

if objetivo:

    if not objetivo.isdigit():

        st.error("❌ Solo puedes ingresar números")

    elif len(objetivo) < 4:

        st.warning("⚠️ Debes ingresar exactamente 4 dígitos")

    elif len(objetivo) == 4:

        valido = True

        st.success(f"✅ Objetivo válido: {objetivo}")

# ----------------------------------------
# CONTINUAR SOLO SI ES VÁLIDO
# ----------------------------------------

if valido:

    objetivo = int(objetivo)

    lista = [random.randint(1000, 9999) for _ in range(10000)]

    st.divider()

    # ----------------------------------------
    # PASO 2
    # ----------------------------------------

    st.header("2. Elije el algoritmo de ordenamiento")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("Burbuja"):

            inicio = time.perf_counter()

            st.session_state.lista_ordenada = burbuja(lista.copy())

            st.session_state.tiempo_orden = (
                time.perf_counter() - inicio
            ) * 1000000

            st.session_state.algoritmo_ordenamiento = "Burbuja"

    with col2:

        if st.button("Inserción"):

            inicio = time.perf_counter()

            st.session_state.lista_ordenada = insercion(lista.copy())

            st.session_state.tiempo_orden = (
                time.perf_counter() - inicio
            ) * 1000000

            st.session_state.algoritmo_ordenamiento = "Inserción"

    with col3:

        if st.button("Mezcla"):

            inicio = time.perf_counter()

            st.session_state.lista_ordenada = mezcla(lista.copy())

            st.session_state.tiempo_orden = (
                time.perf_counter() - inicio
            ) * 1000000

            st.session_state.algoritmo_ordenamiento = "Mezcla"

    # ----------------------------------------
    # PASO 3
    # ----------------------------------------

    if st.session_state.lista_ordenada is not None:

        st.success(
            f"✅ {st.session_state.algoritmo_ordenamiento} completado"
        )

        st.divider()

        st.header("3. Elije el algoritmo de búsqueda")

        col4, col5 = st.columns(2)

        with col4:

            if st.button("Lineal"):

                inicio = time.perf_counter()

                st.session_state.posicion = busqueda_lineal(
                    st.session_state.lista_ordenada,
                    objetivo
                )

                st.session_state.tiempo_busqueda = (
                    time.perf_counter() - inicio
                ) * 1000000

                st.session_state.algoritmo_busqueda = "Lineal"

        with col5:

            if st.button("Binaria"):

                inicio = time.perf_counter()

                st.session_state.posicion = busqueda_binaria(
                    st.session_state.lista_ordenada,
                    objetivo
                )

                st.session_state.tiempo_busqueda = (
                    time.perf_counter() - inicio
                ) * 1000000

                st.session_state.algoritmo_busqueda = "Binaria"

    # ----------------------------------------
    # RESUMEN FINAL
    # ----------------------------------------

    if st.session_state.algoritmo_busqueda is not None:

        st.divider()

        st.header("🏆 Resumen Final")

        st.write("Ordenamiento")

        st.markdown(
            f'<p class="resumen">{st.session_state.algoritmo_ordenamiento}</p>',
            unsafe_allow_html=True
        )

        st.write(
            f"⏱ {st.session_state.tiempo_orden:,.1f} μs"
        )

        st.write("")

        st.write("Búsqueda")

        st.markdown(
            f'<p class="resumen">{st.session_state.algoritmo_busqueda}</p>',
            unsafe_allow_html=True
        )

        st.write(
            f"⏱ {st.session_state.tiempo_busqueda:,.1f} μs"
        )

        st.write("")

        if st.session_state.posicion != -1:

            st.success(
                f"🎯 Objetivo {objetivo} encontrado en la posición {st.session_state.posicion}"
            )

        else:

            st.error(
                f"❌ Objetivo {objetivo} no encontrado"
            )

        # ----------------------------------------
        # REINICIAR
        # ----------------------------------------

        if st.button("Reiniciar"):

            st.session_state.lista_ordenada = None
            st.session_state.algoritmo_ordenamiento = None
            st.session_state.tiempo_orden = None
            st.session_state.algoritmo_busqueda = None
            st.session_state.tiempo_busqueda = None
            st.session_state.posicion = None

            st.rerun()