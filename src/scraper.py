#! /Users/jonathan/anaconda/bin/python
import smtplib
from time import sleep
from urllib2 import urlopen
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        pass

    def scrap(self):
        while True:
            html = urlopen("http://www.apple.com/uk/shop/browse/home/specialdeals/ipad/ipad_mini_3/wi_fi")
            bs_obj = BeautifulSoup(html)
            added = False
            for i in bs_obj.findAll("h3"):
                for j in i.find("a"):
                    if "64GB - Space Grey" in j:
                        added = True
                        break

            if added:
                print("Found!")
                self.send_email()
            else:
                print("Sleeping!")
                sleep(300)

    @staticmethod
    def send_email():
        sender = "jonathan.carlton@hotmail.com"
        receivers = ["jonathan.carlton@hotmail.com"]
        message = """
            From: jonathan.carlton@hotmail.com
            To: jonathan.carlton@hotmail.com
            Subject: It's in stock!

            The iPad is in stock, here is a quick link:
            http://www.apple.com/uk/shop/browse/home/specialdeals/ipad/ipad_mini_3/wifi
        """

        f = open("file")
        pw = f.readline()

        try:
            s = smtplib.SMTP("smtp.live.com", 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login("jonathan.carlton@hotmail.com", pw)
            s.sendmail(sender, receivers, message)
            s.quit()
            print("Sent!")
        except smtplib.SMTPException:
            print("Error!")


Scraper().scrap()