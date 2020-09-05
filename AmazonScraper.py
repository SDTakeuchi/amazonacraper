import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.co.jp/FLEXISPOT-%E5%BA%A7%E4%BD%8D%E3%83%BB%E7%AB%8B%E4%BD%8D%E4%B8%A1%E7%94%A8%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%87%E3%82%B9%E3%82%AF-%E9%AB%98%E3%81%9512%E6%AE%B5%E9%9A%8E%E8%AA%BF%E7%AF%80%E4%BB%98-35%E3%82%A4%E3%83%B3%E3%83%81-%E3%83%96%E3%83%A9%E3%83%83%E3%82%AFM2B/dp/B01HTM9D4U/ref=pd_rhf_ee_s_bmx_1_20?_encoding=UTF8&pd_rd_i=B01HTM9D4U&pd_rd_r=0816bd08-0467-4292-b0fe-5805d6bd7a18&pd_rd_w=hK2ac&pd_rd_wg=DbwYF&pf_rd_p=8b48ead3-ccea-41f6-86cf-ad6867afbd43&pf_rd_r=N5Z53T2WQJQW514GMCPM&psc=1&refRID=N5Z53T2WQJQW514GMCPM"

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    converted_price = int(price[1:7].replace(',', ""))

    if(converted_price < 22500):
        send_mail()

    print(title.strip())
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    pwd = "*********"

    server.login('kuranku191952996@gmail.com', pwd)

    subject = "Price has fallen down!"
    body = "Check the amazon link https://www.amazon.co.jp/FLEXISPOT-%E5%BA%A7%E4%BD%8D%E3%83%BB%E7%AB%8B%E4%BD%8D%E4%B8%A1%E7%94%A8%E3%82%B9%E3%82%BF%E3%83%B3%E3%83%87%E3%82%A3%E3%83%B3%E3%82%B0%E3%83%87%E3%82%B9%E3%82%AF-%E9%AB%98%E3%81%9512%E6%AE%B5%E9%9A%8E%E8%AA%BF%E7%AF%80%E4%BB%98-35%E3%82%A4%E3%83%B3%E3%83%81-%E3%83%96%E3%83%A9%E3%83%83%E3%82%AFM2B/dp/B01HTM9D4U/ref=pd_rhf_ee_s_bmx_1_20?_encoding=UTF8&pd_rd_i=B01HTM9D4U&pd_rd_r=0816bd08-0467-4292-b0fe-5805d6bd7a18&pd_rd_w=hK2ac&pd_rd_wg=DbwYF&pf_rd_p=8b48ead3-ccea-41f6-86cf-ad6867afbd43&pf_rd_r=N5Z53T2WQJQW514GMCPM&psc=1&refRID=N5Z53T2WQJQW514GMCPM"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'kuranku191952996@gmail.com',
        'kuranku191952996@gmail.com',
        msg
    )

    print('Alright, email has just been sent.')

    server.quit()

while(True):
    check_price()
    time.sleep(3600)
