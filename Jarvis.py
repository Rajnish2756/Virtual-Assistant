from tkinter import *
from tkinter import messagebox,ttk
import tkinter,sqlite3
from PIL import Image, ImageTk, ImageSequence
import wolframalpha
import pyttsx3
import datetime, calendar
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import base64


def jarvisFunc():
    class App:
        def __init__(self, parent):
            self.parent = parent
            self.canvas = Canvas(parent, width=600, height=600)
            self.canvas.pack()
            self.sequence = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(Image.open('Peter.gif'))]
            self.image = self.canvas.create_image(300,300, image=self.sequence[0])
            self.animate(1)
        def animate(self, counter):
            self.canvas.itemconfig(self.image, image=self.sequence[counter])
            self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

    numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
    a = {'name':'your email'}
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    window = Tk()
    window.configure(bg="Black")

    global var
    global var1

    var = StringVar()
    var1 = StringVar()

    password=base64.b64decode("NjEwNTQ0QGdtYWls").decode('utf-8')

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def sendemail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('akshaychaturvedi544@gmail.com', password) # email id - use any email id whose security/privacy is off
        server.sendmail('akshaychaturvedi544@gmail.com', to, content)
        server.close()

    def getDate():
        
        now = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()]# e.g. Monday
        monthNum = now.month
        dayNum = now.day
        month_names = ['January', 'February', 'March', 'April', 'May',
           'June', 'July', 'August', 'September', 'October', 'November',   
           'December']
        ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', 
                          '7th', '8th', '9th', '10th', '11th', '12th',                      
                          '13th', '14th', '15th', '16th', '17th', 
                          '18th', '19th', '20th', '21st', '22nd', 
                          '23rd', '24th', '25th', '26th', '27th', 
                          '28th', '29th', '30th', '31st']
       
        return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

    username="Sir"
    ainame="Jarvis 1.o"
    def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            var.set(f"Good Morning {username}") #Name - your Name
            window.update()
            speak(f"Good Morning {username}")
        elif hour >= 12 and hour <= 18:
            var.set(f"Good afternoon {username}")
            window.update()
            speak(f"Good afternoon {username}")
        else:
            var.set(f"Good evening {username}")
            window.update()
            speak(f"Good evening {username}")
        speak(f"Myself {ainame} How may I help you sir") #BotName - Give a name to your assistant

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            var.set("Listening...")
            window.update()
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 400
            audio = r.listen(source)
        try:
            var.set("Recognizing...")
            window.update()
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            var.set(f"{username}, Can you repeat the command please?")
            window.update()
            speak(f"{username}, Can you repeat the command please?")
            return "None"
        
        var1.set(query)
        window.update()
        return query

    def takeEmail():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            var.set("Listening...")
            window.update()
            print("Listening...")
            r.pause_threshold = 1
            r.energy_threshold = 400
            audio = r.listen(source)
        try:
            var.set("Recognizing...")
            window.update()
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            var.set(f"{username}, Can you repeat the command please?")
            window.update()
            speak(f"{username}, Can you repeat the command please?")
            return "None"
        
        var1.set(query)
        window.update()
        z=query.replace(" ","")
        return z.replace("attherate","@")
    
    def play():
        global count
        btn2['state'] = 'disabled'
        btn0['state'] = 'disabled'
        btn1.configure(bg = 'orange')
        if count==0:
            wishme()
        count=1
        while True:
            btn1.configure(bg = 'orange')
            query = takeCommand().lower()
            if 'thank you' in query:
                var.set(f"It was Pleasure Helping You {username}")
                btn1.configure(bg = '#5C85FB')
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                window.update()
                speak(f"It was Pleasure Helping You {username}")
                window.destroy()

            elif 'wikipedia' in query:
                if 'open wikipedia' in query:
                    webbrowser.open('wikipedia.com')
                else:
                    try:
                        speak("searching wikipedia")
                        query = query.replace("according to wikipedia", "")
                        results = wikipedia.summary(query, sentences=1)
                        speak("According to wikipedia")
                        var.set(results)
                        window.update()
                        speak(results)
                        var.set("Task Completed")
                        window.update()
                    except Exception as e:
                        var.set(f"sorry {username}, could not find any result")
                        window.update()
                        speak(f"sorry {username}, could not find any result")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif 'open youtube' in query:
                var.set('opening Youtube')
                window.update()
                speak('opening Youtube')
                webbrowser.open("youtube.com")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif 'open coursera' in query:
                var.set('opening coursera')
                window.update()
                speak('opening coursera')
                webbrowser.open("coursera.com")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif 'open google' in query:
                var.set('opening google')
                window.update()
                speak('opening google')
                webbrowser.open("google.com")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif 'hello' in query:
                var.set('Hello Sir')
                window.update()
                speak("Hello Sir")
                            
            elif 'open stack overflow' in query:
                var.set('opening stack overflow')
                window.update()
                speak('opening stack overflow')
                webbrowser.open('stackoverflow.com')
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif ('play music' in query) or ('change music' in query):
                var.set('Here are your favorites')
                window.update()
                speak('Here are your favorites')
                os.startfile("https://www.youtube.com/watch?v=z8y8UZMQaLo")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break 

            elif 'the time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                var.set("Sir the time is %s" %strtime)
                window.update()
                speak("Sir the time is %s" %strtime)

    ##        elif 'the date' in query:
    ##            strdate = datetime.datetime.today().strftime("%d %m %y")
    ##            var.set("Sir today's date is %s" %strdate)
    ##            window.update()
    ##            speak("Sir today's date is %s" %strdate)
            elif 'the date' in query:
                var.set(getDate())
                window.update()
                speak(getDate())

            elif 'can you do for me' in query:
                var.set('I can do multiple tasks for you sir. tell me whatever you want to perform sir')
                window.update()
                speak('I can do multiple tasks for you sir. tell me whatever you want to perform sir')

            elif 'old are you' in query:
                var.set("I am just born but surely able to help you sir")
                window.update()
                speak("I am just born but surely able to help you sir")

            elif 'open media player' in query:
                var.set("opening VLC media Player")
                window.update()
                speak("opening V L C media player")
                path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player.lnk" #Enter the correct Path according to your system
                os.startfile(path)
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif 'your name' in query:
                var.set(f"Myself {ainame} Sir")
                window.update()
                speak(f'myself {ainame} sir')

            elif 'who creates you' in query:
                var.set('My Creator is Shivanshu and Rajnish')
                window.update()
                speak('My Creator is Shivanshu and Rajnish')

            elif 'say hello' in query:
                var.set(f'Hello Everyone! My self {ainame}')
                window.update()
                speak(f'Hello Everyone! My self {ainame}')

            elif 'open chrome' in query:
                var.set("Opening Google Chrome")
                window.update()
                speak("Opening Google Chrome")
                path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk" #Enter the correct Path according to your system
                os.startfile(path)
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif 'send email' in query:
                try:
                    var.set("What should I say")
                    window.update()
                    speak('what should I say')
                    content = takeCommand()
                    var.set('please give me reciever email id')
                    window.update()
                    speak('please give me reciever email id')
                    
                    to = takeEmail()
                    
                    var.set(f"sending email to {to}")
                    window.update()
                    var.set(f'confirm send email to {to}')
                    window.update()
                    speak(f'confirm send email to {to}')
                    confirm=takeCommand()
                    if 'yes' in confirm:
                        sendemail(to, content)
                        var.set('Email has been sent')
                        window.update()
                        speak('Email has been sent')
                    elif 'no' in confirm:
                        var.set('email sending cancelled')
                        window.update()
                        speak('email sending cancelled')
                    
                except Exception as e:
                    print(e)
                    var.set("Sorry Sir! I was not able to send this email")
                    window.update()
                    speak('Sorry Sir! I was not able to send this email')
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break
                    
            elif "open python" in query:
                var.set("Opening Python Idle")
                window.update()
                speak('Opening Python Idle')
                os.startfile('C:\\Users\Rajnish Chanchal\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\IDLE (Python 3.8 64-bit)') #Enter the correct Path according to your system
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break
            
            elif "write a note" in query:
                var.set('What should i write,sir')
                window.update()
                speak("What should i write, sir")
                note = takeCommand()
                file = open('jarvis.txt', 'a')
                var.set('Sir, should i include time')
                window.update()
                speak("Sir, Should i include time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(f"{note}\n")
                    var.set('done sir')
                    window.update()
                    speak('done sir')
                else:
                    file.write(note)
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break
                    
            elif "show notes" in query:
                var.set('Showing Notes')
                window.update()
                speak("Showing Notes")
                file = os.startfile("C:\\Users\Rajnish Chanchal\AppData\Local\Programs\Python\Python38\jarvis.txt") 
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif "calculate" in query: 
                 
                try:
                    app_id = "V7KLV6-Y5GQ54UQR7"
                    client = wolframalpha.Client(app_id)
                    indx = query.lower().split().index('calculate') 
                    query = query.split()[indx + 1:] 
                    res = client.query(' '.join(query)) 
                    answer = next(res.results).text
                    var.set(f"The answer is {answer}")
                    window.update()
                    speak(f"The answer is {answer}")
                    btn2['state'] = 'normal'
                    btn0['state'] = 'normal'
                except:
                    var.set("No result")
                    window.update()
                    speak("No result")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break
            
            elif "what is" in query or "who is" in query:
                app_id = "V7KLV6-Y5GQ54UQR7"
                client = wolframalpha.Client(app_id)
                res = client.query(query)
                 
                try:
                    var.set(f"{next(res.results).text}")
                    window.update()
                    speak(f"{next(res.results).text}")
                    var.set("Task Completed")
                    window.update()
                except StopIteration:
                    var.set("No results")
                    window.update()
                    speak("No result")
                btn2['state'] = 'normal'
                btn0['state'] = 'normal'
                break

            elif "shutdown" in query:
                var.set("Pleasure helping you sir!")
                window.update()
                speak("Pleasure helping you sir!")
                window.destroy()
                
            elif "horoscope" in query:
                var.set("I ain't an astrologer but I do know \n everything will be fine in the end.")
                
                window.update()
                speak("I am not an astrologer but I do know everything will be fine in the end.")


    label2 = Label(window, textvariable = var1, bg = '#FAB60C')
    label2.config(font=("Courier", 20))
    var1.set('User Command will show here')
    label2.pack()

    label1 = Label(window, textvariable = var, bg = '#ADD8E6')
    label1.config(font=("Courier", 20))
    var.set('Welcome')
    label1.pack()

    window.title('JARVIS')

    app=App(window)

    btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
    btn0.config(font=("Courier", 12))
    btn0.pack()
    btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
    btn1.config(font=("Courier", 12))
    btn1.pack()
    btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
    btn2.config(font=("Courier", 12))
    btn2.pack()

    window.mainloop()
    


def login():
    #--------------------------------------------------------------------------------------------------------------
    #create the window and add size and title to it
    windo = Tk()
    windo.geometry("800x500+300+100")
    #set size permanently   #or you can use window.resizabld(false, false)
    windo.minsize(800, 500)
    windo.maxsize(1600, 800)
    windo.title("USER LOGIN")
    windo.iconbitmap("lock_v2W_icon.ico")

    #---------------------------------------------------------------------------------------------------------------
    #first get the picture then save it in pic and set as background
    image = Image.open("blueBG.jpg")
    pic = ImageTk.PhotoImage(image)
    #build pic and add it to window
    label0 = Label(image = pic)
    label0.pack(fill = BOTH, expand = 'yes')
    count=0

    #-------------------------------------------------------------------------------------------------------------
    #functions for the buttons to perform
    def loggin():
        users = {'User': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
        username = userName.get()
        Pass = password.get()
        count=0
        if username in users :
            if (users[username] == Pass):
                label4 = Label(windo, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
                label4.place(x = 0, y = 400)
                windo.destroy()
                jarvisFunc()
                
                
            else:
                label4 = Label(windo, text = ("Incorrect User/Password")  ,width = 25, font = ("arial", 15, "bold"))
                label4.place(x = 200, y = 400)

        else:
            label4 = Label(windo, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

    #----------------------------------------------------------------------------------------------------------------
    #first lable
    label1 = Label(windo, text = " Prove Identity ", fg = "black", font = ("new times roman", 40, "bold"))
    label1.place(x = 200, y = 15)

    label2 = Label(windo, text = "User Name :", font = ("arial", 16, "bold"))
    label2.place(x = 110, y = 150)

    userName = StringVar()
    textBox1 = Entry(windo, textvar = userName, width = 30, font = ("arial", 16, "bold"))
    textBox1.place(x = 290, y = 150)

    label3 = Label(windo, text = "Password :", font = ("arial", 16, "bold"))
    label3.place(x = 116, y = 250)

    password = StringVar()
    textBox2 = Entry(windo, textvar = password, width = 30, font = ("arial", 16, "bold"),show='*')
    textBox2.place(x = 290, y = 250)

    button1 = Button(windo, text = "   LOGIN   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 16, "bold"), command = loggin)
    button1.place(x = 335, y = 340)

    #display window
    windo.mainloop()
count=0
login()

