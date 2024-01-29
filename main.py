import asyncio
import logging
import os
import sys
import sqlite3 as sq
import database

import phases_file
import text_info
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from keyboard_menu import (keyboard_start, keyboard_food,
                           food_inkey, gr_inkey, keyboard_back, ht_inkey, ne_inkey, keyboard_ghi,
                           keyboard_excursion, keyboard_ex_gh, keyboard_ex_region, keyboard_ex_sity, keyboard_ghi_group,
                           keyboard_ghi_family, apart_inkey, keyboard_traffic, keyboard_func, keyboard_events,
                           events_inkey, keyboard_independ, keyboard_groupp, keyboard_kids, keyboard_corporate,
                           keyboard_start_admin, keyboard_admin)

load_dotenv()
dp = Dispatcher()
form_router = Router()
bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
# dbU = Database('gh.db')


db = sq.connect('gh.db', check_same_thread=False)
cur = db.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users ("
            "user_id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "username TEXT NOT NULL, "
            "first_name TEXT, "
            "last_name TEXT, "
            "active)"
            )

cur.execute('''CREATE TABLE IF NOT EXISTS items (
                i_id INTEGER PRIMARY KEY,
                anons TEXT,
                program TEXT,
                price TEXT
                )''')


# Меню старт
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{hbold(message.from_user.full_name)}</b>!", reply_markup=keyboard_start())
    await message.answer_photo(photo='https://cloud.mail.ru/public/xdao/LCa8qBbpi',
                               caption=text_info.text_start)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f"Вы вошли как администратор, выберите пункт для редактирования информации.",
                             reply_markup=keyboard_start_admin())
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # active =

    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:

        await message.answer(f"Привет, <b>{hbold(message.from_user.full_name)}</b>!", reply_markup=keyboard_start())
        await message.answer_photo(photo='https://cloud.mail.ru/public/xdao/LCa8qBbpi',
                                   caption=text_info.text_start)
        if message.from_user.id == int(os.getenv('ADMIN_ID')):
            await message.answer(f"Вы вошли как администратор, выберите пункт для редактирования информации.",
                                 reply_markup=keyboard_start_admin())
        # user_id = message.from_user.id,
        # username = message.from_user.username,
        # first_name = message.from_user.first_name,
        # last_name = message.from_user.last_name
        #
        # print(type(user_id))

        # cur.execute("INSERT INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)",
        #             (user_id, username, first_name, last_name))
        # db.commit()

    info = cur.execute("SELECT 1 FROM users WHERE user_id =='{key}'".format(key=user_id)).fetchone()
    if not info:
        cur.execute("INSERT INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)",
                    (user_id, username, first_name, last_name))
        db.commit()


# Первая строка меню
@dp.message(F.text.lower() == "грёза инфо")
async def ghi_handler(message: Message) -> None:
    await message.answer(f"Немного о нашем комплексе", reply_markup=keyboard_ghi())
    await message.answer_photo(photo='https://cloud.mail.ru/public/xdao/LCa8qBbpi',
                               caption=text_info.text_ghi)


@dp.message(F.text.lower() == "предложения группам")
async def gh_group_handler(message: Message) -> None:
    await message.answer(f"Если вас много!", reply_markup=keyboard_ghi_group())
    await message.answer_photo(photo='https://cloud.mail.ru/public/UD3H/tN36XHdTY',
                               caption=text_info.text_gh_group,
                               reply_markup=food_inkey)


@dp.message(F.text.lower() == "семейные предложения")
async def gh_family_handler(message: Message) -> None:
    await message.answer(f"Для всей семьи!", reply_markup=keyboard_ghi_family())
    await message.answer_photo(photo='https://cloud.mail.ru/public/hB3E/8Vpza5zTK',
                               caption=text_info.text_gh_family,
                               reply_markup=food_inkey)


# Думаем над сценарием реализации афиши
@dp.message(F.text.lower() == "афиша")
async def poster_handler(message: Message) -> None:
    cur.execute('SELECT anons FROM items WHERE i_id=?', (2066039829,))
    result = cur.fetchone()
    if result:
        anons = result[0]
    else:
        anons = "Афиша в разработке"
    await message.answer(f'Афиша на февраль', reply_markup=keyboard_back())
    await message.answer(anons, reply_markup=food_inkey)


@dp.message(F.text.lower() == "экскурсии")
async def excursion_handler(message: Message) -> None:
    await message.answer(f"Начнем Ваше путешествие!", reply_markup=keyboard_excursion())
    await message.answer_photo(photo='https://cloud.mail.ru/public/boWu/f6mrbrYYK',
                               caption=text_info.text_excursion)


@dp.message(F.text.lower() == "\"грёза хутор\"")
async def gh_handler(message: Message) -> None:
    await message.answer(f"Туристический комплекс \"Грёза Хутор!\"", reply_markup=keyboard_ex_gh())
    await message.answer_photo(photo='https://cloud.mail.ru/public/xdao/LCa8qBbpi',
                               caption=text_info.text_gh,
                               reply_markup=gr_inkey)


@dp.message(F.text.lower() == "по области")
async def region_handler(message: Message) -> None:
    await message.answer(f"Экскурсии по Калининградской области!", reply_markup=keyboard_ex_region())
    await message.answer_photo(photo='https://cloud.mail.ru/public/cr43/9H9TRjSeV',
                               caption=text_info.text_region,
                               reply_markup=ht_inkey)
    pass


@dp.message(F.text.lower() == "по калининграду")
async def sity_handler(message: Message) -> None:
    await message.answer(f"Экскурсии по Калининграду!", reply_markup=keyboard_ex_sity())
    await message.answer_photo(photo='https://cloud.mail.ru/public/1bdV/UWwPBTRju',
                               caption=text_info.text_sity,
                               reply_markup=ne_inkey)


@dp.message(lambda message: message.text.lower() in phases_file.phases_food)
async def food_handler(message: Message) -> None:
    await message.answer(f"Проголодались? Тогда вот наши подсказки", reply_markup=keyboard_food())
    await message.answer_photo(photo='https://cloud.mail.ru/public/6yhJ/qoeRNJRTE',
                               caption=text_info.text_food,
                               reply_markup=food_inkey)


@dp.message(F.text.lower() == "проживание")
async def services_handler(message: Message) -> None:
    await message.answer(f"Решили остановиться у нас, выбирайте варианты проживания!", reply_markup=keyboard_back())
    await message.answer_photo(photo='https://cloud.mail.ru/public/355p/Yhm9poTVZ',
                               caption=text_info.text_apart,
                               reply_markup=apart_inkey)


@dp.message(F.text.lower() == "чем заняться")
async def traffic_handler(message: Message) -> None:
    await message.answer(f"Что делать на территории комплекса? Выбирайте по душе!", reply_markup=keyboard_traffic())
    await message.answer_photo(photo='https://cloud.mail.ru/public/UD3H/tN36XHdTY',
                               caption=text_info.text_traffic,
                               reply_markup=apart_inkey)


@dp.message(F.text.lower() == "оборудование")
async def func_handler(message: Message) -> None:
    await message.answer(f"Оборудование", reply_markup=keyboard_func())
    await message.answer_photo(photo='https://cloud.mail.ru/public/355p/Yhm9poTVZ',
                               caption=text_info.text_func, )


@dp.message(F.text.lower() == "мероприятия")
async def events_handler(message: Message) -> None:
    await message.answer(f"Мероприятия комплекса", reply_markup=keyboard_events())
    await message.answer_photo(photo='https://cloud.mail.ru/public/LMoP/4GyEkCp3X',
                               caption=text_info.text_events,
                               reply_markup=events_inkey)


@dp.message(F.text.lower() == "самостоятельные маршруты")
async def independ_handler(message: Message) -> None:
    await message.answer(f"Гуляем сами", reply_markup=keyboard_independ())
    await message.answer_photo(photo='https://cloud.mail.ru/public/355p/Yhm9poTVZ',
                               caption=text_info.text_independ)


@dp.message(F.text.lower() == "группам")
async def groupp_handler(message: Message) -> None:
    await message.answer(f"Гуляем сами", reply_markup=keyboard_groupp())
    await message.answer_photo(photo='https://cloud.mail.ru/public/355p/Yhm9poTVZ',
                               caption=text_info.text_groupp)


@dp.message(F.text.lower() == "детские")
async def kids_handler(message: Message) -> None:
    await message.answer(f"Гуляем сами", reply_markup=keyboard_kids())
    await message.answer_photo(photo='https://cloud.mail.ru/public/355p/Yhm9poTVZ',
                               caption=text_info.text_kids)


@dp.message(F.text.lower() == "корпоративные")
async def corporate_handler(message: Message) -> None:
    await message.answer(f"Гуляем сами", reply_markup=keyboard_corporate())
    await message.answer_photo(photo='https://cloud.mail.ru/public/355p/Yhm9poTVZ',
                               caption=text_info.text_corporate)


@dp.message(F.text.lower() == "как к нам добраться?")
async def contact_handler(message: Message) -> None:
    await message.answer(f"Гуляем сами", reply_markup=keyboard_back())
    await message.answer_photo(photo='https://cloud.mail.ru/public/Nfxk/KiFDkAtp8',
                               caption=text_info.text_contact)


@dp.message(F.text.lower() == "админ-панель")
async def admin_handler(message: Message) -> None:
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f"Вы вошли как администратор, выберите пункт для редактирования информации.",
                             reply_markup=keyboard_admin())
    else:
        await message.reply('Я тебя не понимаю, воспользуйся кнопками для выбора позиции.',
                            reply_markup=keyboard_start())


@dp.message(F.text.lower() == "вернуться в начало")
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Начнем с начала", reply_markup=keyboard_start())
    await message.answer_photo(photo='https://cloud.mail.ru/public/xdao/LCa8qBbpi',
                               caption="Спасибо, что зашел к нам в гости!\n"
                                       "Здесь ты можешь выбрать чем заняться в выходные, "
                                       f"найти совет, куда отправиться в путешествие по Калининградской области.")


@dp.message(Command('newmessage'))
async def new_message(message: Message) -> None:
    if message.chat.type == 'private':
        if message.from_user.id == int(os.getenv('ADMIN_ID')):
            text = message.text[12:]
            # photo = message.photo
            users = cur.execute("SELECT user_id, active FROM users").fetchall()
            for user_id, active in users:
                try:
                    await bot.send_message(user_id, text)
                    print(active)
                    if active != 1:
                        cur.execute("UPDATE users SET active = ? WHERE user_id = ?", (0, user_id))
                except:
                    cur.execute("UPDATE users SET active = ? WHERE user_id = ?", (1, user_id))
            await bot.send_message(message.from_user.id, 'Сообщение отправлено')

        # @dp.message(Command('new_anons'))


# async def anons_text(message: Message) -> None:
#     if message.from_user.id == int(os.getenv('ADMIN_ID')):
#         new_anons = message.text.split(maxsplit=1)[1]
#         cur.execute('INSERT INTO items (i_id, anons) VALUES (?, ?)', (message.from_user.id, new_anons))
#         db.commit()
#         await message.answer('Афиша успешно обновлена!')
#     else:
#         await message.answer('У вас нет прав для этой операции!')
#
#
# @form_router.message(Form.name)
# async def process_name(message: Message, state: FSMContext) -> None:
#     await state.update_data(name=message.text)
#     await state.set_state(Form.like_bots)
#     await message.answer(f"Текст афиши заменен на: {html.quote(message.text)}", reply_markup=keyboard_admin())
#     await show_summary(message=message)
#
#
# async def show_summary(message: Message, data: Dict[str, Any]) -> None:
#     name = data["name"]
#     text = f"Текст афиши заменен на: {html.quote(name)}"
#     await message.answer(text=text)


@dp.message()
async def empty_handler(message: Message) -> None:
    await message.reply('Я тебя не понимаю, воспользуйся кнопками для выбора позиции.', reply_markup=keyboard_start())


async def main() -> None:

    # dp.include_router(form_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
