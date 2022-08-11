from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import *

app = ApplicationBuilder().token('5552127770:AAHt_ib8rm6AjOqcErAxZdjBqr57jJaegLU').build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("min", minus_command))
app.add_handler(CommandHandler("mult", pow_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("exp", exponent_command))
print("server start")
app.run_polling()