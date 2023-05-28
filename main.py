import requests
import json
build = ["a1.0"]
game_on = True
print("Super USB " + build[0])
games = json.loads(requests.get("http://raw.githubusercontent.com/NightFreddys/SuperUSBDATA/main/games.json").text)
def name(id):
    return games["names"][int(id)-1]
print('"help" For shell help.')
while game_on:
    prompt = input("SuperUSB> ")
    if prompt=="help":
        print('"list" For the game list.\n"help" To prompt this message.\n"start" To start a game.')
    if prompt=="list":
        for x in games["ids"]:
            print("Id: " + str(x) + ", Name: " + name(x))
        print('Use the game id to launch the game with "start"\n(Example: start\n1)')
    if prompt=="start":
        idprompt = input("Id?> ")
        appload = requests.get("http://raw.githubusercontent.com/NightFreddys/SuperUSBDATA/main/" + str(idprompt) + ".py").text
        exec(appload)
    if prompt=="exit":
        game_on = False