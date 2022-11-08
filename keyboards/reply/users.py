from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
button_cancel = KeyboardButton(text="/отмена")

button_ru = KeyboardButton(text="ru")
language_kb = ReplyKeyboardMarkup(keyboard=[[button_ru,button_cancel]],resize_keyboard=True)

button_male = KeyboardButton(text="Парень")
button_female = KeyboardButton(text="Девушка")
gender_kb = ReplyKeyboardMarkup(keyboard=[[button_male, button_female],[button_cancel]],resize_keyboard=True)

button_guys = KeyboardButton(text="Парни")
button_girls = KeyboardButton(text="Девушки")
like_kb = ReplyKeyboardMarkup(keyboard=[[button_guys, button_girls],[button_cancel]],resize_keyboard=True)

button_like = KeyboardButton(text="👎")
button_dlike = KeyboardButton(text="👍")
button_report = KeyboardButton(text="/report")
ldr = ReplyKeyboardMarkup(keyboard=[[button_like, button_dlike],[button_report]],resize_keyboard=True)

button_edit_profile = KeyboardButton(text="/edit_profile")
button_myprofile = KeyboardButton(text="/myprofile")
button_start = KeyboardButton(text="/start")
button_ankets = KeyboardButton(text="/ankets")
button_change_language = KeyboardButton(text="/change_language")
command_kb = ReplyKeyboardMarkup(keyboard=[[button_edit_profile,button_myprofile],
                                           [button_ankets,button_start],
                                           [button_change_language,button_cancel]], resize_keyboard=True)
