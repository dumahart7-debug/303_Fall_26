# Pair Exercise 3
# Student: Annabel Ezekiel-Hart
# Peer: Kritten Yleah




import datetime
import string


def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""

    for char in input_text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            encoded_text += alphabet[(index + shift) % 26]
        else:
            encoded_text += char

    return (alphabet, encoded_text)


def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ""

    for char in input_text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            decoded_text += alphabet[(index - shift) % 26]
        else:
            decoded_text += char

    return decoded_text


class BankAccount:
    def __init__(
        self,
        name="Rainy",
        ID="1234",
        creation_date=datetime.date.today(),
        balance=0
    ):
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future.")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount

        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print(self.balance)

    def view_balance(self):
        print(self.balance)


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        days_existing = (
            datetime.date.today() - self.creation_date
        ).days

        if days_existing < 180:
            print(self.balance)
            return

        if self.balance - amount < 0:
            print(self.balance)
            return

        self.balance -= amount
        print(self.balance)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.balance -= amount

        if self.balance < 0:
            self.balance -= 30

        print(self.balance)
