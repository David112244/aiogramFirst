import os
from os.path import join, dirname
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


def load_token(key):
    token_path = join(dirname(__file__), 'token.env')
    load_dotenv(token_path)
    return os.environ.get(key)


token = load_token('BOT_TOKEN')
bot = Bot(token)
dis = Dispatcher(bot)


@dis.message_handler(commands=['start'])
async def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Hello', callback_data='hello'))
    await bot.send_message(message.chat.id, 'Welcome to my first bot on aiogram!', reply_markup=markup)


@dis.message_handler(commands=['pay'])
async def person_pay(message):
    price = types.LabeledPrice(label='My first pay', amount=20 * 100)
    await bot.send_invoice(message.chat.id,
                           title='Table',
                           provider_token=load_token('PAY_TOKEN'),
                           currency='978',
                           prices=price,
                           description='It is my first pay bot',
                           payload='6356')


@dis.callback_query_handler()
async def callback(call):
    if call.data == 'hello':
        await call.message.answer('safdf')


executor.start_polling(dis)
