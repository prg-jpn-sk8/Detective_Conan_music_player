import tkinter as tk
import playsound as ps

screen = tk.Tk()
screen.title('Detective Conan music')
screen.iconphoto(False, tk.PhotoImage('icons/icon.png'))

def play():
    ps.playsound('music/DetectiveConan.mp3', False) 
def Exit():
    exit()
screen.geometry('900x400')



Text = tk.Label(screen, text="Play Detective Conan music").pack(pady=40)
Play = tk.Button(screen, text="Play Detective conan", command=play).pack(pady =20)
Exit = tk.Button(screen, text="Exit", command=Exit).pack(pady=50)
screen.mainloop()