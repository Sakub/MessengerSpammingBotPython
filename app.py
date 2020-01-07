from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os

class MessengerBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.bot = webdriver.Firefox(executable_path='PATH TO GECKODRIVER.EXE')
        self.selectingPerson()

    def login(self, person):
        bot = self.bot

        bot.get(f'https://www.messenger.com/login.php?next=https%3A%2F%2Fwww.messenger.com%2Ft%2F{person}')
        print('Loading page...')
        time.sleep(3)
        emailInput = bot.find_element_by_name('email')
        passInput = bot.find_element_by_name('pass')
        emailInput.clear()
        passInput.clear()
        emailInput.send_keys(self.email)
        passInput.send_keys(self.password)
        passInput.send_keys(Keys.RETURN)
        self.clearScreen()
        print('Loading page...')
        time.sleep(15)
        self.clearScreen()
        self.message()

    def message(self):
        try:
            howMuchMessagesToSend = int(input('How much messages do u wanna send? '))
        except ValueError:
            print('Error! Try again!')
            self.message()
        bot = self.bot
        messageInput = bot.find_element_by_xpath("//div[contains(@class,'_5rpu') and @role='combobox']")
        for index in range(howMuchMessagesToSend):
            word = random.choice(list(open('messages.txt')))
            messageInput.send_keys(word + Keys.RETURN)
            print(f'Message sent: {word}')
        print(f'Sent {index + 1} message(s)')
        self.sendAgain()

    def sendAgain(self):
        try:
            userChoice = int(input('Do you wanna spam again? 1 - yes, 0 - no '))
        except ValueError:
            print('Error! Try again!')
            self.sendAgain()
        else:
            if userChoice > 1 or userChoice < 0:
                print('Error! Try again!')
                self.sendAgain()
            else:
                if userChoice == 0:
                    exit()
                else:
                    self.clearScreen()
                    self.message()
    def selectingPerson(self):
        listOfIds = ['put', 'here', 'messenger', "id's",'Custom id']
        for idIndex, id in enumerate(listOfIds):
            print(f'{idIndex}. {id}')
        try:
            userChoice = int(input('Select a person which gonna be spammed: '))
        except ValueError:
            print('Error! Try again!')
            self.selectingPerson()
        else:
            if userChoice > int(len(listOfIds)) - 1 or userChoice < 0:
                print('Error! Try again!')
                self.selectingPerson()
            else:
                if userChoice == int(len(listOfIds)) -1:
                    person = input('Write a custom id: ')
                else:
                    person = listOfIds[userChoice]
                self.login(person)
    def clearScreen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

skbBot = MessengerBot('your facebook email', 'your facebook password')
