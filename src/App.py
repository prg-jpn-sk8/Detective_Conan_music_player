import tkinter as tk
import playsound as ps
from random import *

screen = tk.Tk()
screen.title('Detective Conan music')
screen.iconphoto(False, tk.PhotoImage('icons/icon.png'))


def play():
        ps.playsound('music/DetectiveConan.mp3', False)
def plays():
    ps.playsound('music/DetectiveConanSad.mp3', False)
def playss():
    ps.playsound('music/naruto-war-music.mp3', False) 
def Exit():
    exit()
screen.geometry('900x400')
def playsss():
        list = ["music/DetectiveConan.mp3", "music/DetectiveConanSad.mp3", "music/naruto-war-music.mp3"]
        music = choice(list)
        ps.playsound(music , False)
Text = tk.Label(screen, text="Play Detective Conan music").pack(pady=10)
Play = tk.Button(screen, text="Play Detective conan music", command=play).pack(pady =15)
Plays = tk.Button(screen, text="Play Detective conan sad music", command=plays).pack(pady =15)
Playss = tk.Button(screen, text="Play Naruto music", command=playss).pack(pady = 15)
Playsss= tk.Button(screen, text="random-loop", command=playsss).pack(pady =15)
Exit = tk.Button(screen, text="Exit", command=Exit).pack(pady=5)   
screen.mainloop()
