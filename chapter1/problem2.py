#use any external module
import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say('''Mucho Mai Akad Ke Taao Bhare
Jab Mojadiya Mein Paav Dhare
Jab Paav Dhare

Aaye Haye Najook Si Maum Ki Moorat Say
Bada Pathhar Dil Bartao Karey
Pathhar Dil Bartao Kare Bartao Karey

Uyi Amma Haye Haye Mai To Mar Gayi
Uyi Amma Mai To Toott Ke Vikhar Gayi
Uyi Amma Uyi Amma Uyi Amma

Uyi Amma Chhui Mui Se Hirniya''')
engine.runAndWait()