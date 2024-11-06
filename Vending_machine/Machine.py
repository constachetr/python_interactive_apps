
import pyttsx3

class Voice_assist:
    def __init__(self, voice_index=0, rate=100):
        self.engine = pyttsx3.init()
        self.set_voice(voice_index)
        self.set_rate(rate)

    def set_voice(self, voice_index):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice_index].id)

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
voice_assist = Voice_assist(voice_index=1, rate=160)

class Machine:
    def list_food(self):
        food_msg = "Today's menu. Burgers, Sandwiches, and Croissants"
        print("1. Burgers\n2. Sandwiches\n3. Croissants\n\n4. Cancel")
        voice_assist.say(food_msg)

        food_choice = input("Enter your choice: ")

        if food_choice == "1":
            burger_msg = "You have chosen a Burger, \nThe price is $5.99!"
            print(burger_msg)
            voice_assist.say(burger_msg)
            pay_option_msg = "Choose the payment option"
            print("1. Card     2. Cash")
            voice_assist.say(pay_option_msg)
            pay_option= input("Option: ")

            if pay_option == "1":
                card_pay_msg = ("Please insert your card")
                voice_assist.say(card_pay_msg)
                card_pay = input("Card input >>>  ").lower()

                if card_pay == "card":
                    card_acc = "Card was accepted \n Enjoy your Burger!"
                    print(card_acc)
                    voice_assist.say(card_acc)
                else:
                    card_dec = "Card Declined"
                    voice_assist.say(card_dec)
            elif pay_option == "2":
                try:
                    cash_pay = float(input("Please insert $5.99: "))
                    if cash_pay < 5.99:
                        low_funds_msg = "Insufficient funds. Please insert $5.99."
                        print(low_funds_msg)
                        voice_assist.say(low_funds_msg)
                    elif cash_pay == 5.99:
                        acc_funds_msg = "Thank you! Payment accepted. Enjoy your Burger!"
                        print(acc_funds_msg)
                        voice_assist.say(acc_funds_msg)
                    else:
                        change = cash_pay - 5.99
                        change_msg = f"Thank you! Payment accepted. Your change is ${change:.2f}. Enjoy your Burger!"
                        print(change_msg)
                        voice_assist.say(change_msg)
                except ValueError:
                    cash_pay_inv = "Invalid amount. Please try again."
                    print(cash_pay_inv)
                    voice_assist.say(cash_pay_inv)

        elif food_choice == "2":
            sand_msg = "You have chosen a Sandwich, \nThe price is $4.69!"
            print(sand_msg)
            voice_assist.say(sand_msg)
            pay_option_msg = "Choose the payment option"
            print("1. Card     2. Cash")
            voice_assist.say(pay_option_msg)
            pay_option= input("Option: ")

            if pay_option == "1":
                card_pay_msg = ("Please insert your card")
                voice_assist.say(card_pay_msg)
                card_pay = input("Card input >>>  ").lower()

                if card_pay == "card":
                    card_acc = "Card was accepted \n Enjoy your Burger!"
                    print(card_acc)
                    voice_assist.say(card_acc)
                else:
                    card_dec = "Card Declined"
                    voice_assist.say(card_dec)
            elif pay_option == "2":
                try:
                    cash_pay = float(input("Please insert $4.69: "))
                    if cash_pay < 4.69:
                        low_funds_msg = "Insufficient funds. Please insert $4.69."
                        print(low_funds_msg)
                        voice_assist.say(low_funds_msg)
                    elif cash_pay == 4.69:
                        acc_funds_msg = "Thank you! Payment accepted. Enjoy your Sandwich!"
                        print(acc_funds_msg)
                        voice_assist.say(acc_funds_msg)
                    else:
                        change = cash_pay - 4.69
                        change_msg = f"Thank you! Payment accepted. Your change is ${change:.2f}. Enjoy your Sandwich!"
                        print(change_msg)
                        voice_assist.say(change_msg)
                except ValueError:
                    cash_pay_inv = "Invalid amount. Please try again."
                    print(cash_pay_inv)
                    voice_assist.say(cash_pay_inv)

        elif food_choice == "3":
            croiss_msg = "You have chosen a Croissant, \nThe price is $2.99!"
            print(croiss_msg)
            voice_assist.say(croiss_msg)
            pay_option_msg = "Choose the payment option"
            print("1. Card     2. Cash")
            voice_assist.say(pay_option_msg)
            pay_option= input("Option: ")

            if pay_option == "1":
                card_pay_msg = ("Please insert your card")
                voice_assist.say(card_pay_msg)
                card_pay = input("Card input >>>  ").lower()

                if card_pay == "card":
                    card_acc = "Card was accepted \n Enjoy your Croissant!"
                    print(card_acc)
                    voice_assist.say(card_acc)
                else:
                    card_dec = "Card Declined"
                    voice_assist.say(card_dec)
            elif pay_option == "2":
                try:
                    cash_pay = float(input("Please insert $2.99: "))
                    if cash_pay < 2.99:
                        low_funds_msg = "Insufficient funds. Please insert $2.99."
                        print(low_funds_msg)
                        voice_assist.say(low_funds_msg)
                    elif cash_pay == 2.99:
                        acc_funds_msg = "Thank you! Payment accepted. Enjoy your Croissant!"
                        print(acc_funds_msg)
                        voice_assist.say(acc_funds_msg)
                    else:
                        change = cash_pay - 2.99
                        change_msg = f"Thank you! Payment accepted. Your change is ${change:.2f}. Enjoy your Croissant!"
                        print(change_msg)
                        voice_assist.say(change_msg)
                except ValueError:
                    cash_pay_inv = "Invalid amount. Please try again."
                    print(cash_pay_inv)
                    voice_assist.say(cash_pay_inv)

        elif food_choice == "4":
            food_cancel = "Selection Cancelled"
            print(food_cancel)
            voice_assist.say(food_cancel)
        else:
            drink_invalid = "Invalid option"
            voice_assist.say(drink_invalid)


    def list_drink(self):
        drink_msg = "We have Cola, Sprite and Water available"
        print("1. Cola\n2. Sprite\n3. Water\n\n4. Cancel")
        voice_assist.say(drink_msg)

        drink_choice = input("Enter your choice: ")
        if drink_choice == "1":
            cola_msg = "You have chosen cola, \nThe price is $1.5!"
            print(cola_msg)
            voice_assist.say(cola_msg)
            pay_option_msg = "Choose the payment option"
            print("1. Card     2. Cash")
            voice_assist.say(pay_option_msg)
            pay_option= input("Option: ")

            if pay_option == "1":
                card_pay_msg = ("Please insert your card")
                voice_assist.say(card_pay_msg)
                card_pay = input("Card input >>>  ").lower()

                if card_pay == "card":
                    card_acc = "Card was accepted \n Enjoy your Cola!"
                    print(card_acc)
                    voice_assist.say(card_acc)
                else:
                    card_dec = "Card Declined"
                    voice_assist.say(card_dec)
            elif pay_option == "2":
                try:
                    cash_pay = float(input("Please insert $1.5: "))
                    if cash_pay < 1.5:
                        low_funds_msg = "Insufficient funds. Please insert $1.5."
                        print(low_funds_msg)
                        voice_assist.say(low_funds_msg)
                    elif cash_pay == 1.5:
                        acc_funds_msg = "Thank you! Payment accepted. Enjoy your Cola!"
                        print(acc_funds_msg)
                        voice_assist.say(acc_funds_msg)
                    else:
                        change = cash_pay - 1.5
                        change_msg = f"Thank you! Payment accepted. Your change is ${change:.2f}. Enjoy your Cola!"
                        print(change_msg)
                        voice_assist.say(change_msg)
                except ValueError:
                    cash_pay_inv = "Invalid amount. Please try again."
                    print(cash_pay_inv)
                    voice_assist.say(cash_pay_inv)


        elif drink_choice == "2":
            sprite_msg = "You have chosen Sprite, \nThe price is $1.5!"
            print(sprite_msg)
            voice_assist.say(sprite_msg)
            pay_option_msg = "Choose the payment option"
            print("1. Card     2. Cash")
            voice_assist.say(pay_option_msg)
            pay_option= input("Option: ")

            if pay_option == "1":
                card_pay_msg = ("Please insert your card")
                voice_assist.say(card_pay_msg)
                card_pay = input("Card input >>>  ").lower()

                if card_pay == "card":
                    card_acc = "Card was accepted \n Enjoy your Sprite!"
                    print(card_acc)
                    voice_assist.say(card_acc)
                else:
                    card_dec = "Card Declined"
                    voice_assist.say(card_dec)
            elif pay_option == "2":
                try:
                    cash_pay = float(input("Please insert $1.5: "))
                    if cash_pay < 1.5:
                        low_funds_msg = "Insufficient funds. Please insert $1.5."
                        print(low_funds_msg)
                        voice_assist.say(low_funds_msg)
                    elif cash_pay == 1.5:
                        acc_funds_msg = "Thank you! Payment accepted. Enjoy your Sprite!"
                        print(acc_funds_msg)
                        voice_assist.say(acc_funds_msg)
                    else:
                        change = cash_pay - 1.5
                        change_msg = f"Thank you! Payment accepted. Your change is ${change:.2f}. Enjoy your Sprite!"
                        print(change_msg)
                        voice_assist.say(change_msg)
                except ValueError:
                    cash_pay_inv = "Invalid amount. Please try again."
                    print(cash_pay_inv)
                    voice_assist.say(cash_pay_inv)

        elif drink_choice == "3":
            water_msg = "You have chosen Water, \nThe price is $1!"
            print(water_msg)
            voice_assist.say(water_msg)
            pay_option_msg = "Choose the payment option"
            print("1. Card     2. Cash")
            voice_assist.say(pay_option_msg)
            pay_option= input("Option: ")

            if pay_option == "1":
                card_pay_msg = ("Please insert your card")
                voice_assist.say(card_pay_msg)
                card_pay = input("Card input >>>  ").lower()

                if card_pay == "card":
                    card_acc = "Card was accepted \n Enjoy your Water!"
                    print(card_acc)
                    voice_assist.say(card_acc)
                else:
                    card_dec = "Card Declined"
                    voice_assist.say(card_dec)
            elif pay_option == "2":
                try:
                    cash_pay = float(input("Please insert $1: "))
                    if cash_pay < 1:
                        low_funds_msg = "Insufficient funds. Please insert $1.5."
                        print(low_funds_msg)
                        voice_assist.say(low_funds_msg)
                    elif cash_pay == 1:
                        acc_funds_msg = "Thank you! Payment accepted. Enjoy your Water!"
                        print(acc_funds_msg)
                        voice_assist.say(acc_funds_msg)
                    else:
                        change = cash_pay - 1
                        change_msg = f"Thank you! Payment accepted. Your change is ${change:.2f}. Enjoy your Water!"
                        print(change_msg)
                        voice_assist.say(change_msg)
                except ValueError:
                    cash_pay_inv = "Invalid amount. Please try again."
                    print(cash_pay_inv)
                    voice_assist.say(cash_pay_inv)
        elif drink_choice == "4":
            drink_cancel = "Selection Cancelled"
            print(drink_cancel)
            voice_assist.say(drink_cancel)
        else:
            drink_invalid = "Invalid option"
            voice_assist.say(drink_invalid)

#Initialize vending machine

vending_machine = Machine()

while True:
    display_message = "Please choose an option"
    print("Our Products")

    print("1. Food      2. Drinks   ")
    voice_assist.say(display_message)
    choice = input("\nOption: ")
    if choice == "1":
        vending_machine.list_food()
    elif choice == "2":
        vending_machine.list_drink()

    else:
        invalid_msg = "Invalid Choice. Please select again."
        print(invalid_msg)
        voice_assist.say(invalid_msg)



