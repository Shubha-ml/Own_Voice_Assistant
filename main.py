import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tom' in command:
                command = command.replace('tom', '')
                print(command)
    except:
        pass
    return command


def run_tom():
    command = take_command()
    print(command)
    if 'play video' in command:
        vsong = command.replace('play video', '')
        talk('playing ' + vsong)
        kit.playonyt(vsong)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        kit.playonyt(song)
    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        result = command.replace('who is', '')
        info = wikipedia.summary(result, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        result = command.replace('what is', '')
        info = wikipedia.summary(result, 1)
        print(info)
        talk(info)
    elif "open google" in command:
        result = command.replace('open google', '')
        info = kit.search(result)
        talk('Gooogle is Openning..')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk('Welcome')
        exit()
    else:
        talk('Please say again')


while True:
    run_tom()
