# 🚀 Deploy de Magna en Vercel

## 📋 Pasos para Deploy en Vercel

### 1. **Deploy desde Vercel Dashboard (Recomendado)**

1. Ve a [vercel.com](https://vercel.com)
2. Haz clic en **"New Project"**
3. **Importa tu repositorio** `mariajoml/magnaAI`
4. **Configura las variables de entorno:**
   - `OPENAI_API_KEY` = tu_api_key_real
5. **Deploy** automáticamente

### 2. **Configuración de Variables de Entorno en Vercel**

En el dashboard de Vercel:
1. Ve a tu proyecto
2. **Settings** → **Environment Variables**
3. Agrega:
   - **Name:** `OPENAI_API_KEY`
   - **Value:** tu_api_key_real_de_openai
   - **Environment:** Production, Preview, Development

### 3. **Archivos de Configuración Incluidos**
- ✅ `vercel.json` - Configuración de Vercel
- ✅ `config.py` - Manejo de configuración

## 🌐 **URLs de Acceso**
- **Producción:** `https://magna-ai.vercel.app` (o tu dominio personalizado)
- **Preview:** URLs automáticas para cada push

## 🔄 **Actualizaciones Automáticas**
- Cada push a `main` → Deploy automático
- Pull requests → Preview automático

## ⚠️ **Consideraciones**
- Vercel tiene límites de tiempo de ejecución
- Streamlit puede tener limitaciones en serverless

## 🎯 **Alternativas Recomendadas**
1. **Railway** - Excelente para Streamlit
2. **Render** - Muy fácil de usar
3. **Heroku** - Clásico y confiable
