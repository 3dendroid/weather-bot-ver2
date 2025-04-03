import datetime

import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import OWM
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")
    await message.answer("Write me the name of the city and I will send you the weather report!")


@dp.message_handler()
async def get_weather_def(message: types.Message):
    code_to_emoji = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OWM}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_emoji:
            wd = code_to_emoji[weather_description]
        else:
            wd = "Look out the window, I don’t understand what kind of weather it is there!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"Weather in the city: {city}\nTemperature: {cur_weather}C° {wd}\n"
                            f"Humidity: {humidity}%\nPressure: {pressure} mmHg\nWind: {wind} m/s\n"
                            f"Sunrise: {sunrise_timestamp}\nSunset: {sunset_timestamp}\nDay length: {length_of_the_day}\n"
                            )
    except:
        await message.reply("\U00002620 Check the name of the city \U00002620")
