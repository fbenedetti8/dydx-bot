import requests
from decouple import config
from telegram import Update
from telegram.ext import *
from constants import STOP_PROGRAM



# start 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  STOP_PROGRAM.clear()
  await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text="Bot activado por Telegram!"
  )

# Finalizar programa
async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  STOP_PROGRAM.set()
  await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text="Detenido bot ..."
  )
      
# Mensaje de error
async def error_callback(update, context):
  print('Error en telegram!')
  await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text="Error en telegram!"
  )


# Escuchar Comandos de telegram
def listen_telegram_messages():
  bot_token = config("TELEGRAM_TOKEN")
  application = ApplicationBuilder().token(bot_token).build()

  application.add_handler(CommandHandler('start', start_command))
  application.add_handler(CommandHandler('stop', stop_command))
  application.add_error_handler(error_callback)

  application.run_polling()


# Send Message
def send_message(message):
  bot_token = config("TELEGRAM_TOKEN")
  chat_id = config("TELEGRAM_CHAT_ID")
  url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
  res = requests.get(url)
  if res.status_code == 200:
    return "sent"
  else:
    return "failed"
  
  
