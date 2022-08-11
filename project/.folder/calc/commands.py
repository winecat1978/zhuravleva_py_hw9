from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n\nДействия с рациональными числами\n/summation(sum)\n/deduction(min)\n/multiplication(mult)\n/division(div)\n/exponentiation(exp)')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}+{y} = {x+y}')

async def minus_command(update: Update, context: ContextTypes.DEFAULT_TYPE): 
    msg = update.message.text
    print(msg)
    items = msg.split() 
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}-{y} = {x-y}')

async def pow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):   
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}*{y} = {x*y}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}:{y} = {x/y}')

async def exponent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}^{y} = {x**y}')