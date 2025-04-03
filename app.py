from aiogram import executor

from handlers import dp
from utils.misc.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    # Notification of successful bot launch
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
