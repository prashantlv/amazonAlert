import requests
from bs4 import BeautifulSoup
import smtplib      # simple mail transfer protocol

url = 'https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=sr_1_4?keywords=boat&qid=1582823584&sr=8-4'

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
dprice = 500
def check_price():
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:5])

    if converted_price < dprice :
        send_mail()
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender@mail', 'password')         # need to allow less secure app for google
    subject = 'Price fell down below Rs.400 !!!'
    body = 'Check this out, Hurry !!!  link https://www.amazon.in/boAt-BassHeads-100-Headphones-Black/dp/B071Z8M4KX/ref=sr_1_4?keywords=boat&qid=1582823584&sr=8-4'

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'sender@mail',
        'receiver@mail',
        msg
    )

    print("Email has been sent successfully.")
    print("Hurry !!! check your wishlist now. ")

    server.quit()

check_price()
