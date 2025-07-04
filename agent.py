import openai
import os
from dotenv import load_dotenv

# Cargar claves desde .env
load_dotenv()

# Configurar API Key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")


def generar_respuesta(mensaje_usuario):
    """Genera respuesta con GPT-3.5 Turbo"""
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "eres un asistente de testeo que solo busca validar que el cliente tenga una buena experiencia con el producto."},
                {"role": "user", "content": mensaje_usuario}
            ],
            max_tokens=150,
            temperature=0.5,
        )

        mensaje_respuesta = respuesta['choices'][0]['message']['content'].strip()
        return mensaje_respuesta

    except Exception as e:
        return f"Lo siento, no pude responder en este momento. Por favor, intenta más tarde."
