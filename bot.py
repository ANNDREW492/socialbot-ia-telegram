import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from agent import generar_respuesta

# Cargar claves desde .env
load_dotenv()

# Obtener el token del bot de Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Función de inicio /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu asistente de prueba. ¿En qué puedo ayudarte hoy?")

# Función para manejar mensajes normales
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje_usuario = update.message.text
    respuesta = generar_respuesta(mensaje_usuario)
    await update.message.reply_text(respuesta)


def main():
    # Crear la aplicación del bot
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Comando /start
    app.add_handler(CommandHandler("start", start))
    # Mensajes de texto normales
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    # Iniciar el bot
    print("Bot iniciado... Esperando mensajes.")
    app.run_polling()


if __name__ == "__main__":
    main()
