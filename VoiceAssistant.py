88thprint("\n\n")
print("\t\tHie!! -- I am your Voice Asistant\n\n")

import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return "None"
        
    return query

def main():
    speak("Hello, how can I assist you today?")
    
    while True:
        query = listen().lower()
        
        if 'hello' in query:
            speak("Hello! How are you?")
        elif 'fine and you' in query:
            speak("I am also fine. Now tell me how can i help you")
        elif 'who are you' in query:
            speak("I am your voice assistant.")
        elif 'what is your name' in query:
            speak("my name is _________")
        elif 'how do you work' in query:
            speak("Just I listen your voice and give answer to you.")
        elif 'ok thank you' in query or 'bye' in query:
            speak("ok Goodbye have a nice day!   bbye")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()

print("\n\n")
