import requests
import json
import gtts
import playsound

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=ea4714e5af924e5596353315230606&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
text = f"The current weather in {city} is {w} degree celcius"
sound = gtts.gTTS(text, lang="en")
sound.save('temp.mp3')
playsound.playsound('temp.mp3')


