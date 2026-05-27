import streamlit as st
import time

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Búsqueda y Ordenamiento",
    page_icon="🔵",
    layout="centered"
)

# =====================================================
# ESTILOS
# =====================================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to bottom, #071120, #0b1730);
}

html, body, [class*="css"]{
    color:white;
    font-family:Arial;
}

h1, h2, h3{
    color:white;
}

/* TITULO */

.main-title{
    font-size:55px;
    font-weight:bold;
    color:#60a5fa;
}

.sub-title{
    font-size:20px;
    color:#94a3b8;
}

/* INPUT */

.stTextInput input{
    background-color:#10233f !important;
    color:white !important;
    border-radius:15px !important;
    border:1px solid #2563eb !important;
    height:60px;
    font-size:24px;
}

/* BOTONES */

.stButton > button{
    background-color:#10233f;
    color:white;
    border:1px solid #2563eb;
    border-radius:15px;
    width:180px;
    height:70px;
    font-size:22px;
    transition:0.3s;
}

.stButton > button:hover{
    background-color:#2563eb;
    color:white;
    border:1px solid #60a5fa;
}

/* TARJETAS */

.card{
    background-color:#0f1c35;
    padding:25px;
    border-radius:20px;
    border:1px solid #1d4ed8;
    margin-top:20px;
}

/* TEXTO RESUMEN */

.resumen{
    color:#60a5fa;
    font-size:40px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# ALGORITMOS DE ORDENAMIENTO
# =====================================================

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

# =====================================================
# ALGORITMOS DE BÚSQUEDA
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
# SESSION STATE
# =====================================================

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

# =====================================================
# TITULO
# =====================================================

st.markdown(
    '<p class="main-title">🔵 Búsqueda y Ordenamiento</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">Sistema de análisis de algoritmos</p>',
    unsafe_allow_html=True
)

st.write("")

# =====================================================
# PASO 1
# =====================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("1️⃣ ¿Cuál es el objetivo?")

objetivo = st.text_input(
    "Ingresa un número de 4 dígitos",
    max_chars=4,
    placeholder="Ejemplo: 0001"
)

valido = False

if objetivo:

    if not objetivo.isdigit():

        st.error("❌ Solo puedes ingresar números")

    elif len(objetivo) < 4:

        st.warning("⚠️ Debes ingresar exactamente 4 dígitos")

    else:

        valido = True

        st.success(f"✅ Objetivo válido: {objetivo}")

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# CONTINUAR SOLO SI ES VALIDO
# =====================================================

if valido:

    lista = [str(i).zfill(4) for i in range(0, 10000)]

    # =====================================================
    # ORDENAMIENTO
    # =====================================================

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.header("2️⃣ Elige el algoritmo de ordenamiento")

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

    if st.session_state.lista_ordenada is not None:

        st.success(
            f"✅ {st.session_state.algoritmo_ordenamiento} completado"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # BUSQUEDA
    # =====================================================

    if st.session_state.lista_ordenada is not None:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("3️⃣ Elige el algoritmo de búsqueda")

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

        st.markdown('</div>', unsafe_allow_html=True)

    # =====================================================
    # RESUMEN FINAL
    # =====================================================

    if st.session_state.algoritmo_busqueda is not None:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("🏆 Resumen Final")

        st.write("")

        st.write("Ordenamiento")

        st.markdown(
            f'<p class="resumen">{st.session_state.algoritmo_ordenamiento}</p>',
            unsafe_allow_html=True
        )

        st.write(
            f"⏱ Tiempo Ordenamiento: {st.session_state.tiempo_orden:,.1f} μs"
        )

        st.write("")

        st.write("Búsqueda")

        st.markdown(
            f'<p class="resumen">{st.session_state.algoritmo_busqueda}</p>',
            unsafe_allow_html=True
        )

        st.write(
            f"⏱ Tiempo Búsqueda: {st.session_state.tiempo_busqueda:,.1f} μs"
        )

        st.write("")

        # =====================================================
        # SUMAR 1 A LA POSICIÓN
        # =====================================================

        if st.session_state.posicion != -1:

            posicion_real = st.session_state.posicion + 1

            st.success(
                f"🎯 Objetivo {objetivo} encontrado en la posición {posicion_real}"
            )

        else:

            st.error(
                f"❌ Objetivo {objetivo} no encontrado"
            )

        st.write("")

        # =====================================================
        # REINICIAR
        # =====================================================

        if st.button("🔄 Reiniciar"):

            st.session_state.lista_ordenada = None
            st.session_state.algoritmo_ordenamiento = None
            st.session_state.tiempo_orden = None
            st.session_state.algoritmo_busqueda = None
            st.session_state.tiempo_busqueda = None
            st.session_state.posicion = None

            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)