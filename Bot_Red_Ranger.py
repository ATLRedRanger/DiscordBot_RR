from discord import Intents, Client, Message, File
import Bot_Responses as bot
from PIL import Image


#STEP 1: BOT SETUP
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)
#im = File("C:\\Users\\vince\\OneDrive\\Desktop\\orange_mustang.jpg")

#STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message, user_message):

    print(f"{message.author.id}")
    

    if not user_message:
        print("Message was empty because intents were not enabled")
        return
    
    if user_message[0] == ">":
        user_message = user_message[1:]

        try:
            response = bot.get_response(user_message)
            if (type(response) == File):
                await message.channel.send(file = response)
            else:
                await message.channel.send(response)

        except Exception as e:
            print(e)
#STEP 3: HANDLING BOT STARTUP
@client.event
async def on_ready():
    print(f"{client.user} is now running!")
    return None


#STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message):
    userName = str(message.author)
    userMessage = message.content
    channel = str(message.channel)
    if message.author == client.user:
        return
    
    print(f"[{channel}] {userName}: '{userMessage}'")
    await send_message(message, userMessage)
    return None

def main():
    client.run(token=bot.Get_Token())
    print(bot.Set_Token())
    return None

if __name__ == "__main__":
    main()