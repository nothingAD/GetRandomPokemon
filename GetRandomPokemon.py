import asyncio
import aiohttp
import random
import urllib
import PySimpleGUI as sg

pname = ""


async def GetPokemon():
    async with aiohttp.ClientSession() as session:

        r = random.randint(1,1000)
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/' + str(r)
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            pname = str(pokemon["name"])

            backImg = pokemon["sprites"]["back_default"]
            frontImg = pokemon["sprites"]["front_default"]
            urllib.request.urlretrieve(backImg, "images/back.png")
            urllib.request.urlretrieve(frontImg, "images/front.png")

            print(pname)
            return pname.capitalize()


sg.theme('DarkPurple6') 

column = [  [sg.Text('GET A RANDOM POKEMON')],
            [sg.HorizontalSeparator(color="GREY")],
            [sg.Button("Get Pokemon")],
            [sg.Image(key="IMGF"), sg.Image(key="IMG") ],
            [sg.Text("", key="OUT")],
            [sg.Button('Close')] ]

layout = [  [sg.Column(column, element_justification='center') ]]


window = sg.Window('GET A POKEMON', layout, grab_anywhere=True, icon="images/Great-Ball.ico")

while True:
    event, values = window.read(timeout=10)
    if event == "Get Pokemon":
        window['OUT'].update(asyncio.run(GetPokemon()))
        window['IMG'].update(filename="images/back.png", visible=True)
        window['IMGF'].update(filename="images/front.png", visible=True)
        window.refresh()
    if event == sg.WIN_CLOSED or event == 'Close': 
        break
    

window.close()


