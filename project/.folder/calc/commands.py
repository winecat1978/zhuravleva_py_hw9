from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Базовые команды:\n/Hi(Привет!)\n/Time(Который час?)\n/Help(Помоги!)\n\nДействия с рациональными числами:\nСумма(/sum)\nРазность(/min)\nУмножение(/mult)\nДеление(/div)\nВозведение в степень(/exp)\n\n\
Действия с комплексными числами:\nПример ввода: 1 2 3 4 -> 1+2j и 3+4j\nСумма(/c_sum)\nРазность(/c_min)\nУмножение(/c_mult)\nДеление(/c_div)')

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
    await update.message.reply_text(f'{x} : {y} = {x/y}')

async def exponent_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 4324
    x = float(items[1])
    y = float(items[2])
    await update.message.reply_text(f'{x}^{y} = {x**y}')

async def complex_sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a}+{b} = {a+b}')

async def complex_min_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a}-{b} = {a-b}')

async def complex_mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a}*{b} = {a*b}')

async def complex_div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split() # /sum 123 4324
    print(items)
    a = complex(float(items[1]),float(items[2]))
    b = complex(float(items[3]),float(items[4]))
    await update.message.reply_text(f'{a} : {b} = {a/b}')