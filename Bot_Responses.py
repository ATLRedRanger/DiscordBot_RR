import random
from PIL import Image
from discord import File

file = "C:\\Users\\vince\OneDrive\\Desktop\\orange_mustang.jpg"
im = Image.open(file)

def get_response(user_input):
    lowered = user_input.lower()
    #randomNum = 
    commandsList = ["roll", "hello", "commands", "trigid", "invtrigid", "rps", "intro"] # "attack", ]
    icebreakers = ["Would you rather have invisibility or flight?\n", "If you could bring back any fashion trend, what would it be?\n",
                    "Coffee or tea?\n", "What's your favorite breakfast cereal?\n", "What sport would you compete in if you were in the Olympics?\n",
                      "What is your favorite TV show?\n", "What two things do you consider yourself to be very good at?\n",
                        "What is your favorite movie?\n", "What is your favorite book?\n", "What movie can you rewatch over and over again?\n", "What's your dream car?\n",
                        "What's your favorite color?\n", "What's your favorite video game?\n", "Who's your favorite music artist?\n"]
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
    elif "intro" in lowered:
        introQs = random.choices(icebreakers, k = 3)
        questions = introQs[0] + introQs[2] + introQs[1]
        return questions
    else:
        return random.choice(["Does not compute...", "I don't understand.", "Did you mean to say 'roll'?"])

def Get_Token():
    with open("C:\\Users\\vince\\OneDrive\\Desktop\\Programming Sutff\\Discord_Bot\\GSU_Math_Bot.txt", 'r') as TOKEN:
        TokenStr = TOKEN.readline().strip()
        return TokenStr