import tkinter as tk
import playsound as ps

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
    tk.exit()
screen.geometry('900x400')

Text = tk.Label(screen, text="Play Detective Conan music").pack(pady=20)
Play = tk.Button(screen, text="Play Detective conan music", command=play).pack(pady =20)
Plays = tk.Button(screen, text="Play Detective conan sad music", command=plays).pack(pady =20)
Playss = tk.Button(screen, text="Play Naruto music", command=playss).pack(pady =20)
Exit = tk.Button(screen, text="Exit", command=Exit).pack(pady=5)   
screen.mainloop()
