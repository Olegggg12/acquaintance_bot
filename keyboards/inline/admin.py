from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

send_all_button = InlineKeyboardButton(text="Отправить сообщение всем", callback_data="send_all_button")
ban_user_button = InlineKeyboardButton(text="Забанить пользователя", callback_data="ban_user_button")

inline_admin_kb = InlineKeyboardMarkup(inline_keyboard=[
                                                        [send_all_button],
                                                        [ban_user_button]
                                                       ])
