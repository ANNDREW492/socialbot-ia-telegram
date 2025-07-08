from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Crear cliente OpenAI con tu API Key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generar_respuesta(mensaje_usuario):
    """Genera respuesta real con GPT-3.5 Turbo"""
    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un asistente virtual de ventas que ayuda a los clientes a encontrar productos, "
                        "informarse sobre promociones y resolver dudas sobre sus compras."
                    )
                },
                {"role": "user", "content": mensaje_usuario}
            ],
            max_tokens=150,
            temperature=0.5,
        )

        mensaje_respuesta = respuesta.choices[0].message.content.strip()
        return mensaje_respuesta

    except Exception as e:
        return f"Error al generar la respuesta: {str(e)}"
