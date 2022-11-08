from create_bot import dp, bot

from db.create_db import create_db

from FSM.user_profile import profile_router
from FSM.user_language import language_router
from FSM.admin.send import send_router
from FSM.simp import simp_router

import handlers.users
import handlers.admin

if __name__ == "__main__":
    # Запуск бота
    dp.include_router(profile_router)
    dp.include_router(language_router)
    dp.include_router(simp_router)
    dp.include_router(send_router)
    create_db()
    dp.run_polling(bot, skip_updates=True)
