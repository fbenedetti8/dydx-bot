import requests
from decouple import config
from telegram import Update
from telegram.ext import *
from constants import STOP_PROGRAM





async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text="Bot activado por Telegram!"
  )
  

async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  STOP_PROGRAM = True
  await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text="El bot fue detenido con exito!"
  )
      
async def error_callback(update, context):
  print('Error en telegram!')
  await context.bot.send_message(
      chat_id=update.effective_chat.id,
      text="Error en telegram!"
  )


if __name__ == '__main__':
  bot_token = config("TELEGRAM_TOKEN")
  application = ApplicationBuilder().token(bot_token).build()

  application.add_handler(CommandHandler('start', start_command))
  application.add_handler(CommandHandler('exit', exit_command))
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
  
  
