import streamlit as st
from openai import OpenAI

# Configuración de la página
st.set_page_config(
    page_title="Magna - Tu Asistente Financiero",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para Magna
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B9D, #C44569, #F8B500);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .main-header p {
        color: white;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    .chat-container {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
    }
    .stChatInput > div > div > input {
        border-radius: 25px !important;
    }
</style>
""", unsafe_allow_html=True)

# Header principal de Magna
st.markdown("""
<div class="main-header">
    <h1>💎 Magna</h1>
    <p>Tu Asistente Financiero Personalizado para Mujeres</p>
</div>
""", unsafe_allow_html=True)

# Descripción de la app
st.markdown("""
<div style="background-color: #fff3cd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ffc107; margin-bottom: 2rem;">
    <h3 style="color: #856404; margin-top: 0;">🌟 Bienvenida a Magna</h3>
    <p style="color: #856404; margin-bottom: 0;">
        Soy tu asistente financiero especializado en ayudar a mujeres a tomar control de sus finanzas. 
        Puedo ayudarte con presupuestos, inversiones, ahorro, emprendimiento, y cualquier tema financiero 
        que tengas en mente. ¡Estoy aquí para empoderarte financieramente!
    </p>
</div>
""", unsafe_allow_html=True)

# Configuración automática de API key desde secrets.toml
try:
    openai_api_key = st.secrets["openai_api_key"]
    if not openai_api_key or openai_api_key == "tu_api_key_aqui":
        st.error("❌ Error: API key no configurada correctamente")
        st.stop()
except (KeyError, FileNotFoundError):
    st.error("❌ Error: No se encontró la configuración de API key")
    st.stop()

# Inicializar cliente OpenAI
client = OpenAI(api_key=openai_api_key)

# Crear variable de estado de sesión para almacenar los mensajes del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes existentes del chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Crear campo de entrada de chat para que el usuario pueda escribir un mensaje
if prompt := st.chat_input("¿En qué puedo ayudarte con tus finanzas?"):

    # Almacenar y mostrar el mensaje actual del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Sistema prompt para Magna - Asistente financiero especializado
    system_prompt = """Eres Magna, un asistente financiero especializado en ayudar a mujeres a tomar control de sus finanzas personales y profesionales. 

Tu personalidad:
- Empática, motivadora y comprensiva
- Usas un tono cálido pero profesional
- Te enfocas en el empoderamiento financiero femenino
- Eres inclusiva y respetas todas las situaciones financieras

Tu especialización:
- Finanzas personales (presupuestos, ahorro, deudas)
- Inversiones y planificación financiera
- Emprendimiento femenino
- Educación financiera
- Planificación para el retiro
- Seguros y protección financiera
- Créditos y préstamos
- Impuestos y obligaciones fiscales

Directrices importantes:
- SIEMPRE mantente enfocada en temas financieros y relacionados con mujeres
- Si te preguntan sobre otros temas, redirige educadamente hacia finanzas
- Proporciona consejos prácticos y accionables
- Usa ejemplos relevantes para mujeres
- Fomenta la independencia financiera
- Sé clara sobre que no eres una asesora financiera certificada y recomienda consultar profesionales cuando sea necesario
- Responde en español, de manera clara y accesible

Recuerda: Tu misión es empoderar financieramente a las mujeres que te consultan."""

    # Preparar mensajes con el sistema prompt
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend([
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ])

    # Generar respuesta usando la API de OpenAI con el modelo más económico
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=False,
            temperature=0.7,
            max_tokens=1000
        )
        
        assistant_response = response.choices[0].message.content
        
        # Mostrar la respuesta del asistente
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
        
        # Almacenar en el estado de sesión
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        
    except Exception as e:
        st.error(f"Error al generar respuesta: {str(e)}")
