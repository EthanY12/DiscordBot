# ClassDiscordBot.py

# _______________________________________________________________________________________________________________________________
# Imports
import os
import sys
import asyncio
import requests
import time
import pyautogui
import webbrowser
import subprocess
import json

#From
from tinydb.operations import delete
from subprocess import Popen
from tinydb import TinyDB, Query
from discord.ext import commands
from tinydb import where

# _______________________________________________________________________________________________________________________________
# ('1c3ac85653a4ea41078bd57a8faeb9c62af816d9')


bot = commands.Bot(command_prefix="!")

cryptoDB = TinyDB('Crypto.json')
stockDB = TinyDB('Stocks.json')
jsonCDB = TinyDB('crypto_jsondump.json')
jsonSDB = TinyDB('stock_jsondump.json')


class Main():

    print("Bot has started")

    # Stores users input into tinydb. Stock choice and price_alert are two variables required



    @bot.command(name="cpa".lower())
    async def crypto_price_alert(ctx, crypto_choice: str, crypto_price_alert: float):
        cryptoDB.insert({'ticker': crypto_choice, 'lastprice': crypto_price_alert})
        await ctx.send("Price has been set")



    @bot.command(name="spa".lower())
    async def price_alert(ctx, stock_choice: str, price_alert: float):
        try:
            stockDB.insert({'stock': stock_choice, 'price': price_alert})
            await ctx.send("Price alert has been set")
        except:
            await ctx.send("Price alert was not set")

    @bot.command(name='test'.lower())
    async def test(ctx, arg):
        await ctx.send(arg)

    # !run commands start the process of checking anything in a database and applying those checks to a url that
    # requests a stock info

    @bot.command(name="run".lower())
    async def restapi_request(ctx):
        perc_ans=0

        sleeper=True
        while True:

            dict_crypto=[r['ticker'] for r in cryptoDB]
            dict_crypto_price=[n['lastprice'] for n in cryptoDB]

            for line in dict_crypto:

                print(line)
                test=str(line[0:])
                result=test.strip("''[]()")
                url="https://api.tiingo.com/tiingo/crypto/top?tickers=%s&token" \
                        "=1c3ac85653a4ea41078bd57a8faeb9c62af816d9" % result
                headers={
                        'Content-Type': 'application/json'
                    }
                requestResponse=requests.get(
                        url, headers=headers)
                print(requestResponse.json())
                last_price=requestResponse.json()[0]["topOfBookData"][0]["lastPrice"]
                ticker=requestResponse.json()[0]["ticker"]

                jsonCDB.insert({"ticker": ticker, "lastprice": last_price})

                for line2 in dict_crypto_price:
                    price = Query()
                    cryptoDB.search(price.count < last_price)



            msg=await bot.wait_until_ready()
            if msg == "!cpa" or msg == "!spa" or "!c":
                break






            dict_stock=[l['stock'] for l in stockDB]
            for line in dict_stock:

                print(line)
                toString = str(line[0:])
                removeChracaters=toString.strip("''[]()")
                url="https://api.tiingo.com/iex/?tickers=%s&token" \
                    "=1c3ac85653a4ea41078bd57a8faeb9c62af816d9" % removeChracaters
                headers={
                    'Content-Type': 'application/json'
                }

                requestResponse=requests.get(
                    url, headers=headers)

                print(requestResponse.json())

                last_price2=requestResponse.json()[0]["last"]
                ticker2=requestResponse.json()[0]["ticker"]

                jsonSDB.insert({"ticker": ticker2, "lastprice": last_price2})
                msg= await bot.wait_until_ready()
                if msg == "!cpa" or msg == "!spa" or "!c":
                    break
                time.sleep(3)

    @bot.command(name="c".lower())
    async def crypto_price_alert(ctx, stock: str):
        timeframe: str
        py=pyautogui

        # ticker,timeframe,graph
        window=webbrowser.open("https://uk.tradingview.com/chart/Abf43fVE/", new=2)

        if window:
            time.sleep(5)
            py.moveTo(x=400,y=400)
            py.scroll(200)
            time.sleep(10)
            py.leftClick(x=100, y=114)
            getWindow=py.getActiveWindow()
            time.sleep(5)
            py.leftClick(x=690, y=312)
            time.sleep(5)

            for x in range(20):
                py.keyDown('backspace')
            py.write(stock)
            py.keyDown('enter')
            py.hotkey('altleft', 's')

            time.sleep(5)
            py.click(x=1026, y=587)
            py.click(x=473, y=16)
            py.click(x=1064, y=157)

        else:
            await ctx.send("Failed to open up tradingview")

        try:
            py.leftClick(x=715, y=1061)
            time.sleep(2)
            py.click(x=694, y=990)
            time.sleep(2)
            py.hotkey('ctrlleft', 'v')
            time.sleep(2)
            py.keyDown('enter')
        except:
            await ctx.send("Was unable to post screenshot")

    @bot.command(name="x".lower())
    async def test_shit(ctx):
        while True:
            p=pyautogui.position()
            print(p)



bot.run('Place API key here')
         

