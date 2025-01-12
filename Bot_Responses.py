import random
from PIL import Image
from discord import File

file = "C:\\Users\\vince\OneDrive\\Desktop\\orange_mustang.jpg"
im = Image.open(file)

def get_response(user_input):
    lowered = user_input.lower()
    #randomNum = 
    commandsList = ["roll", "hello", "commands", "trigid", "invtrigid", "rps"] # "attack", ]
    rps = ["Rock", "Paper", "Scissors"]
    if lowered == "":
        return "Well, you're awfully silent..."
    elif "hello" in lowered:
        return "Hello there!"
    elif "roll" in lowered:
        return f"```You rolled: {random.randint(1, 6)}```"
    elif "rps" in lowered:
        return random.choice(rps)
    elif "commands" in lowered:
        return commandsList
    elif "pic" in lowered:
        with open("C:\\Users\\vince\\OneDrive\\Desktop\\orange_mustang.jpg", 'rb') as image:
            temp = File(image)
            return temp
    elif "invtrigid" in lowered:
        with open("C:\\Users\\vince\\OneDrive\\Desktop\\Discord_Bot_Pics\\Trig_Inverse_Derivatives.jpg", 'rb') as image:
            temp = File(image)
            return temp
    elif "trigid" in lowered:
        with open("C:\\Users\\vince\\OneDrive\\Desktop\\Discord_Bot_Pics\\Trig_Derivatives.png", 'rb') as image:
            temp = File(image)
            return temp
    elif "google" in lowered:
        return "https://www.google.com"
    else:
        return random.choice(["Does not compute...", "I don't understand.", "Did you mean to say 'roll'?"])

def Get_Token():
    with open("C:\\Users\\vince\\OneDrive\\Desktop\\Programming Sutff\\Discord_Bot\\GSU_Math_Bot.txt", 'r') as TOKEN:
        TokenStr = TOKEN.readline().strip()
        return TokenStr