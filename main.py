# ClassDiscordBot.py

# _______________________________________________________________________________________________________________________________
# Imports
import os
import sys
import asyncio

import discord
import requests
import time
import pyautogui
import webbrowser
import subprocess
import json
import selenium

# From
from tinydb.operations import delete
from subprocess import Popen
from tinydb import TinyDB, Query
from discord.ext import commands
from tinydb import where
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# _______________________________________________________________________________________________________________________________
# ('1c3ac85653a4ea41078bd57a8faeb9c62af816d9')


bot = commands.Bot(command_prefix="!")

cryptoDB = TinyDB('Crypto.json')
stockDB = TinyDB('Stocks.json')
jsonCDB = TinyDB('crypto_jsondump.json')
jsonSDB = TinyDB('stock_jsondump.json')


class Main():
    print("Bot has started")

    # Stores users input into tinydb. crypto choice and price_alert are variables inputed by the user

    @bot.command(name="cpa".lower())
    async def crypto_price_alert(ctx, crypto_choice: str, crypto_price_alert: float):
        cryptoDB.insert({'ticker': crypto_choice, 'lastprice': crypto_price_alert})
        await ctx.send("Price has been set")

    # Stores users input into tinydb. stock choice and price_alert are variables inputed by the user
    @bot.command(name="spa".lower())
    async def price_alert(ctx, stock_choice: str, price_alert: float):
        try:
            stockDB.insert({'stock': stock_choice, 'price': price_alert})
            await ctx.send("Price alert has been set")
        except:
            await ctx.send("Price alert was not set")
    #a simple test to return users input
    @bot.command(name='test'.lower())
    async def test(ctx, arg):
        await ctx.send(arg)

    # !run commands start the process of checking anything in a database and applying those checks to a url that
    # requests a stock info using the tiingo api

    @bot.command(name="run".lower())
    async def restapi_request(ctx):
        perc_ans = 0

        sleeper = True
        while True:

            dict_crypto = [r['ticker'] for r in cryptoDB]
            dict_crypto_price = [n['lastprice'] for n in cryptoDB]

            for line in dict_crypto:
                print(line)
                test = str(line[0:])
                result = test.strip("''[]()")
                url = "https://api.tiingo.com/tiingo/crypto/top?tickers=%s&token" \
                      "=1c3ac85653a4ea41078bd57a8faeb9c62af816d9" % result
                headers = {
                    'Content-Type': 'application/json'
                }
                requestResponse = requests.get(
                    url, headers=headers)
                print(requestResponse.json())
                last_price = requestResponse.json()[0]["topOfBookData"][0]["lastPrice"]
                ticker = requestResponse.json()[0]["ticker"]

                jsonCDB.insert({"ticker": ticker, "lastprice": last_price})

            #  for line2 in dict_crypto_price:
            #      price = Query()
            #      cryptoDB.search(price.count < last_price)

            msg = await bot.wait_until_ready()
            if msg == "!cpa" or msg == "!spa" or "!c":
                break

            dict_stock = [l['stock'] for l in stockDB]
            for line in dict_stock:

                print(line)
                toString = str(line[0:])
                removeChracaters = toString.strip("''[]()")
                url = "https://api.tiingo.com/iex/?tickers=%s&token" \
                      "=1c3ac85653a4ea41078bd57a8faeb9c62af816d9" % removeChracaters
                headers = {
                    'Content-Type': 'application/json'
                }

                requestResponse = requests.get(
                    url, headers=headers)

                print(requestResponse.json())

                last_price2 = requestResponse.json()[0]["last"]
                ticker2 = requestResponse.json()[0]["ticker"]

                jsonSDB.insert({"ticker": ticker2, "lastprice": last_price2})
                msg = await bot.wait_until_ready()
                if msg == "!cpa" or msg == "!spa" or "!c":
                    break
                time.sleep(3)
    #a way to find the position of the mouse_x and mouse_y cords
    @bot.command(name="x".lower())
    async def test(ctx):
        while True:
            p = pyautogui.position()
            print(p)
    # opens up tradingview to grab a screenshot
    @bot.command(name="c".lower())
    async def crypto_price_alert(ctx, stock: str, tf):
        PATH = 'C:/Users/Ethan/Downloads/chromedriver_win32/chromedriver.exe'
        no_gui = webdriver.ChromeOptions()
        no_gui.add_argument('--headless')
        file_name = 'file.jpg'
       # location = 'C:/Users/Ethan/Desktop/PycharmProjects/pythonProject/file.jpg'
        driver = webdriver.Chrome(PATH)

        print("Started screenshot")
        try:
            driver.maximize_window()
            driver.get("https://www.tradingview.com/chart")
            #time.sleep(5)
           # driver.find_element_by_id("header-toolbar-intervals").click()

           # tf_list = ['1s', '5s', '15s', '30s', '1m', '3m', '5m', '15m', '45m', '1h', '2h', '3h', '4h', '1d', '1w']

           # for i in tf_list:
           #     if tf != i:
           #         await ctx.send("Please use a value timeframe")
           #         driver.quit()
           #     else:
           #         pass

            #tf_list = ['5m', '15m', '30m', '1H','4H', '1D']
            #index = str('[' + str(int(tf_list.index(tf)) + 1) + ']')
            #driver.find_element_by_id("header-toolbar-intervals" + index).click()
        except:
            driver.quit()

       # delete_file = os.path.join(location, file_name)
       # os.remove(delete_file)
        time.sleep(3)

        element = driver.find_element_by_class_name("layout__area--center")
        element.screenshot(file_name)
        await ctx.send(file=discord.File(r'C:\Users\Ethan\Desktop\PycharmProjects\pythonProject\file.jpg'))

        driver.quit()
    # link = driver.find_elements_by_class_name("//*[class=label-2IihgTnv]/div").get_attribute("value")

    # test = driver.find_element_by_class_name("close-3kPn4OTV").click()
    # print(screenshot)

    # print(test)
    # return link


bot.run('Add API here')
# 
