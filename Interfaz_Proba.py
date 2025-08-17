# streamlit_app.py
import streamlit as st

st.set_page_config(page_title="Resumen de Probabilidad", layout="wide")
st.title("📚 Resumen de Probabilidad - Ross")

# Sidebar con botones para cada tema
st.sidebar.title("Temas")
tema = st.sidebar.radio("Selecciona un tema:", [
    "Regla de multiplicación y suma",
    "Permutaciones",
    "Combinaciones",
    "Aplicaciones a problemas de probabilidad"
])

# Contenido de cada tema
if tema == "Regla de multiplicación y suma":
    st.header("Regla de multiplicación y suma")
    st.write("""
    - **Regla de multiplicación:** Si un evento puede ocurrir de `m` formas y otro de `n` formas, 
      entonces ambos ocurren en `m * n` formas.
    - **Regla de suma:** Si un evento puede ocurrir de `m` formas y otro (mutuamente excluyente) de `n` formas, 
      entonces uno u otro ocurre en `m + n` formas.
    """)
    
elif tema == "Permutaciones":
    st.header("Permutaciones")
    st.write(r"""
    - Permutaciones **sin repetición:** número de formas de ordenar `n` objetos distintos: `n!`
    - Permutaciones **con repetición:** si algunos objetos se repiten, dividir entre factorial de repeticiones
      \(`n! / (n1! * n2! * ... * nk!)`\)
    """)
    
elif tema == "Combinaciones":
    st.header("Combinaciones")
    st.write(r"""
    - **Sin repetición:** número de formas de elegir `k` elementos de `n` distintos: `C(n, k) = n! / (k! * (n-k)!)`
    - **Con repetición:** `C(n+k-1, k)` formas de elegir con reemplazo.
    """)
    
elif tema == "Aplicaciones a problemas de probabilidad":
    st.header("Aplicaciones a problemas de probabilidad")
    st.write("""
    - Usar las reglas de multiplicación y suma para contar resultados.
    - Aplicar permutaciones y combinaciones para calcular probabilidades de eventos.
    - Ejemplo: Probabilidad de obtener 2 caras al lanzar 3 monedas = `C(3,2)/2^3 = 3/8`.
    """)

st.markdown("---")
st.write("💡 Desarrollado con Streamlit para estudio interactivo de probabilidad.")
