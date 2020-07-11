# bot.py
import csv
import os, sys
import random
import requests
#import selenium.webdriver
#-------------------------------------------------
from discord.ext import commands
from yahoo_fin import stock_info as si


#from bs4 import BeautifulSoup
#from dotenv import load_dotenv

#--------------------------------------------------

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def user_reader():
    with open('pricealert.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
       


def user_writer(x,y):
      with open('pricealert.csv', 'a') as csv_write:
            csv_writer = csv.writer(csv_write)
            csv_writer.writerow([x, y])
            


bot = commands.Bot(command_prefix='!')


@bot.command(name='IV'.lower())
async def IVInput(ctx, a: float, b: float, c: float):
    await ctx.send(a + b + c)
    


@bot.command(name='pricealert'.lower())
async def PriceAlert(ctx, stock_choice, price_alert: float, stock_storage=[]):
        await ctx.send("Price alert has been set")
        user_writer(stock_choice, price_alert)     


with open('pricealert.csv', 'r') as csv_f:
     csv_read = csv.reader(csv_f)

for w, c in p.items():
        csv_read.writerow(w + c)




bot.run('NzI5NDM2MjAyMTc1ODIzOTEz.XwI6mg.aZLKgHXomns73iz4Hkx9xS8ShZQ')


#driver = selenium.webdriver.PhantomJS(execute_path='Users/User\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\selenium\webdriver\phantomjs')
#driver.headless()
#driver.get('https://finance.yahoo.com/quote/(%d)/history?p=(%d)' %user_reader.csv_reader)


#url = 'https://finance.yahoo.com/quote/A?p=A'
#page = requests.get(url)     
#soup = BeautifulSoup(page.content, "html.parser")
#stock_price1 = soup.find(id={"data-reactid", "34"})
#stock_price = soup.find(id="quote-market-notice").find_parent().find("span").text

#print(stock_price1)
#print(stock_price)



                 


