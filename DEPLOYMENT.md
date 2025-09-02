# 🚀 Guía de Despliegue de Magna

## 📋 Para Streamlit Cloud

### 1. Configurar Secretos en Streamlit Cloud

1. Ve a tu aplicación en [Streamlit Cloud](https://share.streamlit.io)
2. Haz clic en "Settings" (Configuración)
3. Ve a la sección "Secrets"
4. Agrega la siguiente configuración:

```toml
openai_api_key = "sk-proj-tu_api_key_real_aqui"
```

### 2. Variables de Entorno (Alternativa)

También puedes configurar la variable de entorno:
- `OPENAI_API_KEY` = tu_api_key_real

## 🏠 Para Uso Local

### 1. Clonar el Repositorio
```bash
git clone https://github.com/mariajoml/magnaAI.git
cd magnaAI
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar API Key
Crea el archivo `.streamlit/secrets.toml`:
```toml
openai_api_key = "sk-proj-tu_api_key_real_aqui"
```

### 4. Ejecutar la Aplicación
```bash
streamlit run streamlit_app.py
```

## 🔐 Seguridad

- ✅ El archivo `secrets.toml` está en `.gitignore`
- ✅ No se sube la API key al repositorio
- ✅ Configuración segura para producción

## 🌐 URLs

- **Local**: http://localhost:8501
- **Streamlit Cloud**: https://magnabot.streamlit.app
