import pyttsx3 #pip install pyttspx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import requests
import tkinter as tk
#import PIL.Image
#import pyautogui
#import pywhatkit as kit
import json
from tkinter import *
from requests import get
from pywikihow import search_wikihow
from googlesearch import search
from PIL import ImageTk, Image
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5') #for a windows Speech api 
voices = engine.getProperty('voices')
 #print(voices[1].id)
engine.setProperty('voice', voices[0].id)


#new code for gui
#os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
                            
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.5
        
        print("listen threshold")
        # audio = r.listen(source)
        audio = r.listen(source, phrase_time_limit = 5)
        print("got audio")

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
     # if 1:
                query = takeCommand().lower()
            
                # Logic for executing tasks based on query
                #-----------------------------Wikipedia Searching----------------------------------------#
                if 'search for' in query:
                    speak('Searching Wikipedia...')
                    query = query.replace("search for", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                #-------------------------IP Address----------------------#
                elif 'ip address' in query:
                    ip=get('https://api.ipify.org').text
                    print(ip)
                    speak(f'Your IP Address Is {ip}')   

                elif 'show about' in query:
                    speak('Going Through....')
                    query=query.replace("show about","")
                    googlesearch=requests.get("https://www.google.com/search?q="+query)
                    soup=BeautifulSoup(googlesearch.text,'html.parser')
                    result=soup.select('.r a')
                    for link in result [:5]:
                        actual=link.get('href')
                        webbrowser.open('https://google.com/'+actual) 
                
                #-----------------------------Opening Google----------------------------------------#
                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")    




                #-----------------------------Opening Stackoverflow----------------------------------------#
                elif 'open stack overflow' in query:
                    webbrowser.open("https://stackoverflow.com/")  
                
                #----------------------------Take Screen Shot-----------------------------------------------------#
                elif 'screenshot' in query:
                    speak("Please Tell Me The Name For The Screen Shot")
                    name=takeCommand()
                    speak("Plaese Hold The Screen Fow Few Seconds I Am Just Taking Screen Shot")
                    img=pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("Done Sir")

                #-----------------------------Wikipedia Searching Using Wikihow----------------------------------------#
                elif 'how to' in query:
                    query=query.replace("how to","")
                    max_results=1
                    how_to=search_wikihow(query,max_results)
                    assert len(how_to) ==1
                    how_to[0].print()
                    speak(how_to[0].summary)
            
                #---------------------------Temperature-----------------------------------------------------------#
                elif 'temperature' in query:
                    query1=query
                    query=query.replace("temperature","")
                    url=f"https://www.google.com/search?q={query}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_="vk_bk TylWce")
                    print(temp)
                    speak(f"current {query1} is {temp}")
                #---------------------------Play Music------------------------------------------------------------#
                elif 'play music' in query:
                    webbrowser.open("https://gaana.com/")

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print(strTime)    
                    speak(f"Sir, the time is {strTime}")
                    

                elif 'play game' in query:
                    codePath = "D:\\Valo\\Riot Games\\Riot Client\\RiotClientServices.exe"
                    os.startfile(codePath)

                elif 'open code' in query:
                    codePath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                    os.startfile(codePath)


