from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import *

app = ApplicationBuilder().token('5552127770:AAHt_ib8rm6AjOqcErAxZdjBqr57jJaegLU').build()

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("Time", time_command))
app.add_handler(CommandHandler("Help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("min", minus_command))
app.add_handler(CommandHandler("mult", pow_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("exp", exponent_command))
app.add_handler(CommandHandler("c_sum", complex_sum_command))
app.add_handler(CommandHandler("c_min", complex_min_command))
app.add_handler(CommandHandler("c_mult", complex_mult_command))
app.add_handler(CommandHandler("c_div", complex_div_command))
print("server start")
app.run_polling()