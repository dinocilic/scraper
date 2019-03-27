#!/usr/bin/python3
import requests as req
from requests import ConnectionError
import time, sys
from bs4 import BeautifulSoup

class GetChoice():
    print(""" 
        Welcome to the Scraper.
        Please make sure the url is in the right format.
        Example http/s://example.com 

            Thank you. '-_-'
    """)

    def __init__(self):
        self.get_choice()

    def get_choice(self):
        self.url = input("> Url: ")
        
        if "http://" not in self.url and "https://" not in self.url:
            print("\n> Please enter a valid url.")
            self.get_choice()
        else:
            print("\n> Preparing to scrape.\n")
            pass

        print(""" 
        > What would you like me to scrape? 
            1) Links
            2) Text
            3) Full Content
        """)
        try:
            choice = input("> Select an option: ")
        except SyntaxError as err:
            print(err)
        else:
            if choice == "1":
                print("> Scraping links from " + self.url + "\n> Please wait...\n")
                self.get_links()      
            elif choice == "2":
                print("> Scraping text from " + self.url + "\n> Please wait...\n")
                self.get_text()
            elif choice == "3":
                print("> Scraping full content from " + self.url + "\n> Please wait...\n")
                self.get_content()
            else:
                print("Wrong input!")
                self.get_choice()
    
    def get_links(self):
        try:
            response = req.get(self.url)
        except ConnectionError:
            print("\n> Website does not exist. Enter a valid url.\n")
            self.get_choice()
        else:
            soup = BeautifulSoup(response.text,'lxml')
            file = open("links-" + time.strftime("%a-%H:%M") + ".txt" , "wb")
            links = soup.find_all('a')
            for link in links:
                href = link.get('href') + "\n"
                if "http" in href:
                    file.write(href.encode())
            file.close()

            print("Links are scraped and stored as links-" + time.strftime("%a-%H:%M") + ".txt.")

    def get_text(self):
        try:
            response = req.get(self.url)
        except ConnectionError:
            print("\n> Website does not exist. Enter a valid url.\n")
            self.get_choice()
        else:
            soup = BeautifulSoup(response.text,'lxml')
            text = soup.get_text()

            file = open("website_text-" + time.strftime("%a-%H:%M") + ".txt" , "w")
            file.write(text)
            file.close()

            print("Text has been scraped and stored as website_text-" + time.strftime("%a-%H:%M") + ".txt.")

    def get_content(self):
        try:
            response = req.get(self.url)
        except ConnectionError:
            print("\n> Website does not exist. Enter a valid url.\n")
            self.get_choice()
        else:
            soup = BeautifulSoup(response.text, 'lxml')  
            with open("index-" + time.strftime("%a-%H:%M") + ".html", "w") as file:
                file.write(soup.prettify())
                file.close()
                
            print("\n> Content has been scraped and stored as index-" + time.strftime("%a-%H:%M") + ".html!")


GetChoice()