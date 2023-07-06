# Btd6-Auto-Farmer
This project was inspired by Linus Jansson's [btd6farmer](https://github.com/linus-jansson/btd6farmer)
## Installation
If you don't have Python and pip installed, please download and install them from the official [Python website.](https://www.python.org/)

Once that's done, run installRequirements.bat

If there are any issues with Pytesseract, check out [this guide](https://github.com/UB-Mannheim/tesseract/wiki)

## Running the bot

Open up bt6 and go to the home page. I'd recommend selecting obyn. Then run the game plan from the file.
I have an example set up however
it's incomplete and serves as an example. Any chimps or hard mode gameplans can be copied from youtube videos.
In order to stop the script you can close the game or just the script itself.

## Issues
If you have any issues with the script feel free to join my [discord](https://discord.gg/H4gvFZHCej) or add SkellXC

## Creating gameplans
Check out dcChimps to see how the file runs. Generally, each round would look like this:
```python
hero = monkeys.Monkey("hero",0.469921875,0.41203703703703703)
dart0 = monkeys.Monkey("dart",0.521484375,0.6166666666666667)
if correctRound(currentRound,previousRound,6):
    dart0.place()
    hero.place()
    dart0.upgrade("bottom",2)
```
