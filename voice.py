import pyttsx3
import speech_recognition as sr
import smtplib
import datetime

Edict = {
    "nk sir": "nk_iet@yahoo.co.in",
    "anup": "anupkumarpuraini@gmail.com",
    "sumit":"sumitkrpaswan321@gmail.com",
    "rohit":"joges427@gmail.com",
    "kisan":"kisan734779@gmail.com"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am voice based email sender, tell me the name of person")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        name = r.recognize_google(audio, language='en-in')
        print(f"User: {name}\n")
    except Exception as e:
        print("Say that again please...")    
        return "none"
    return name.lower()  

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('anup705031@gmail.com', 'femtowhfnjbwttkd')  
    server.sendmail('anup705031@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        try:
            name = takecommand()
            if name == "none":
                continue
            if name not in Edict:
                speak("Name not found in contacts. Please try again.")
                continue
            email = Edict[name]
            speak("Okay, what is the message?")
            content = takecommand()
            print("Content: ", content)
            sendemail(email, content)
            speak("Email has been sent")
            break
        except Exception as e:
            print(e)
            speak("Email was not sent, please try again")