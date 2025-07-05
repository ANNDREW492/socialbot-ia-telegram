from openai import OpenAI

client = OpenAI()

MODO_SIMULADO = True  # cambiar a False para usar la API real

def generar_respuesta(mensaje_usuario):
    """Genera respuesta simulada o real, según el modo"""
    if MODO_SIMULADO:
        # simulacion
        return f"(Simulado) Has dicho: {mensaje_usuario}"
    else:
        # Respuesta real con OpenAI API
        try:
            respuesta = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "eres un asistente de testeo que solo busca validar que el cliente tenga una buena experiencia con el producto."},
                    {"role": "user", "content": mensaje_usuario}
                ],
                max_tokens=50,
                temperature=0.5,
            )

            mensaje_respuesta = respuesta.choices[0].message.content.strip()
            return mensaje_respuesta

        except Exception as e:
            return f"Error al generar la respuesta: {str(e)}"
