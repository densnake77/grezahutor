from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard_start():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Грёза инфо")
    builder.button(text=f"Афиша")
    builder.button(text=f"Экскурсии")
    builder.button(text=f"Питание")
    builder.button(text=f"Проживание")
    builder.button(text=f"Чем заняться")
    builder.button(text=f"Группам")
    builder.button(text=f"Как к нам добраться?")
    builder.adjust(3, 3, 2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_start_admin():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Грёза инфо")
    builder.button(text=f"Афиша")
    builder.button(text=f"Экскурсии")
    builder.button(text=f"Питание")
    builder.button(text=f"Проживание")
    builder.button(text=f"Чем заняться")
    builder.button(text=f"Группам")
    builder.button(text=f"Как к нам добраться?")
    builder.button(text=f"Админ-панель")
    builder.adjust(3, 3, 3)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_food():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Вернуться в начало")
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_back():
    builder = ReplyKeyboardBuilder()
    # builder.button(text=f"Назад")
    builder.button(text=f"Вернуться в начало")
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_apart():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Индивидуальные экскурсии")
    builder.button(text=f"Туры по области")
    builder.button(text=f"Остановиться у нас")
    builder.button(text=f"Что-то еще")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2, 2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_ghi():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Предложения группам")
    builder.button(text=f"Семейные предложения")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_ghi_group():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Семейные предложения")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_ghi_family():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Предложения группам")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_excursion():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"\"Грёза хутор\"")
    builder.button(text=f"По области")
    builder.button(text=f"По Калининграду")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(3, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_ex_gh():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"По области")
    builder.button(text=f"По Калининграду")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_ex_region():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"\"Грёза хутор\"")
    builder.button(text=f"По Калининграду")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_ex_sity():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"\"Грёза хутор\"")
    builder.button(text=f"По области")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_traffic():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Экскурсии")
    builder.button(text=f"Оборудование")
    builder.button(text=f"Мероприятия")
    builder.button(text=f"Самостоятельные маршруты")
    builder.button(text=f"Афиша")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(3, 3, 2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_func():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Экскурсии")
    builder.button(text=f"Мероприятия")
    builder.button(text=f"Самостоятельные маршруты")
    builder.button(text=f"Афиша")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(3, 3, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_events():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Экскурсии")
    builder.button(text=f"Оборудование")
    builder.button(text=f"Самостоятельные маршруты")
    builder.button(text=f"Афиша")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(3, 3, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_independ():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Экскурсии")
    builder.button(text=f"Оборудование")
    builder.button(text=f"Мероприятия")
    builder.button(text=f"Афиша")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(3, 3, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_groupp():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Детские")
    builder.button(text=f"Корпоративные")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_kids():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Корпоративные")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_corporate():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f"Детские")
    builder.button(text=f"Вернуться в начало")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант ниже')


def keyboard_admin():
    builder = ReplyKeyboardBuilder()
    builder.button(text=f'Заменить афишу')
    builder.button(text=f'Заменить мероприятия')
    builder.button(text=f'Заменить питание')
    return builder.as_markup(resize_keyboard=True, input_field_placeholder='Выберите вариант для замены текста')


food_inkey = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Заказать',
                             url='https://t.me/grezahutor'),
        InlineKeyboardButton(text='Подробнее',
                             url='https://grezahutor.ru/')
    ]
])

gr_inkey = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подробнее',
                             url='https://grezahutor.ru/')
    ]
])

ht_inkey = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подробнее',
                             url='http://hobbitur.ru/')
    ]
])

ne_inkey = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подробнее',
                             url='http://narodexcursovod.ru/')
    ]
])

apart_inkey = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Забронировать',
                             url='https://grezahutor.ru/')
    ]
])

events_inkey = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Подробнее',
                             url='https://grezahutor.ru/')
    ]
])
