import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import smtplib
import datetime
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from playsound import playsound

Edict = {
    "jogendra": "rajendrakingsabar@gmail.com",
    "kishan": "sp87418845@gmail.com"
}


try:
    engine_pyttsx3 = pyttsx3.init('sapi5')
    voices = engine_pyttsx3.getProperty('voices')
    print("Available pyttsx3 voices:")
    female_voice = None
    for voice in voices:
        print(f"Voice: {voice.name}, ID: {voice.id}")
        if "Zira" in voice.name or "Hazel" in voice.name or "Female" in voice.name:
            female_voice = voice
            break
    if female_voice:
        engine_pyttsx3.setProperty('voice', female_voice.id)
        print(f"Selected female voice: {female_voice.name}")
    else:
        print("No female voice found, using default voice")
        engine_pyttsx3.setProperty('voice', voices[0].id)
    use_gtts = False
except Exception as e:
    print(f"pyttsx3 initialization failed: {e}")
    use_gtts = True

def speak(audio, use_gtts=use_gtts):
    """Speak the given audio string using gTTS or pyttsx3."""
    try:
        if use_gtts:
            tts = gTTS(text=audio, lang='en', tld='us')  
            temp_file = "temp_audio.mp3"
            tts.save(temp_file)
            playsound(temp_file)
            os.remove(temp_file)
        else:
            engine_pyttsx3.say(audio)
            engine_pyttsx3.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {e}")
        if use_gtts:
            print("Falling back to pyttsx3")
            engine_pyttsx3.say(audio)
            engine_pyttsx3.runAndWait()

def wishme():
    """Greet user based on time of day."""
    hour = int(datetime.datetime.now().hour)
    greeting = "Good morning" if 0 <= hour < 12 else "Good Afternoon" if 12 <= hour < 18 else "Good evening"
    speak(f"{greeting}. I am your voice-based email sender. Please say the name of the person.")

def list_microphones():
    """List available microphones using speech_recognition."""
    print("Available microphones:")
    mic_list = sr.Microphone.list_microphone_names()
    for i, mic in enumerate(mic_list):
        print(f"Device {i}: {mic}")
    return mic_list

def takecommand(max_retries=3):
    """Capture and recognize speech using speech_recognition."""
    r = sr.Recognizer()
    r.energy_threshold = 300  
    r.pause_threshold = 1.5   
    mic_list = list_microphones()
    mic_index = 0  

    try:
        with sr.Microphone(device_index=mic_index) as source:
            print(f"Using microphone: {mic_list[mic_index]}")
            for attempt in range(max_retries):
                try:
                    speak("Get ready to speak. Starting in one seconds.")
                    for i in range(1, 0, -1):
                        speak(str(i))
                        time.sleep(1)
                    speak("Speak clearly and loudly now.")
                    print(f"Attempt {attempt + 1}/{max_retries}: Listening for 10 seconds...")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source, timeout=10, phrase_time_limit=10)
                    print("Recognizing...")
                    text = r.recognize_google(audio, language='en-US')
                    print(f"Recognized: {text}")
                    return text.lower()
                except sr.WaitTimeoutError:
                    print("No speech detected within 10 seconds.")
                    speak("No speech detected. Try speaking louder or closer to the microphone.")
                except sr.UnknownValueError:
                    print("Could not understand audio.")
                    speak("Could not understand. Please say again.")
                except sr.RequestError as e:
                    print(f"Speech recognition error: {e}")
                    speak("Error with speech recognition service. Please try again.")
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    speak("Error capturing speech. Please try again.")
    except Exception as e:
        print(f"Microphone error: {e}")
        speak("Microphone error. Please check your audio device.")
        return None

    speak("Maximum retries reached. Skipping this step.")
    return None

def sendemail(to, content):
    """Send email to the specified address with the given content."""
    try:
        sender_email = "kishan734779@gmail.com" 
        sender_password = "reof mniu oodt mzyv"  

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to
        msg["Subject"] = "Voice-Based Email"
        msg.attach(MIMEText(content, "plain"))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to}")
        speak("Email sent successfully.")
        return True
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Incorrect email or password.")
        speak("Authentication failed. Please check your email credentials.")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
        speak("Failed to send email due to server issue.")
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        speak("Failed to send email. Please try again.")
        return False

if __name__ == "__main__":
    wishme()
    while True:
        try:
            name = takecommand()
            if name is None:
                continue
            if name == "exit":
                speak("Goodbye")
                break
            if name not in Edict:
                speak("Name not found in contacts. Please say another name.")
                continue

            email = Edict[name]
            speak(f"Say the message for {name}.")
            content = takecommand()
            if content is None or content.strip() == "":
                speak("No valid message provided. Please try again.")
                continue

            print(f"Sending email to: {email}")
            print(f"Message: {content}")
            sendemail(email, content)

        except Exception as e:
            print(f"Unexpected error: {e}")
            speak("An error occurred. Please try again.")