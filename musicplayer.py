from tkinter import *
import pygame
import os
from PIL import Image, ImageTk  # Import the required PIL modules

class MusicPlayer:

    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        # Customize colors and fonts
        background_color = "#2C3E50"
        button_color = "#3498DB"
        text_color = "white"
        font_style = ("arial", 15, "bold")

        trackframe = LabelFrame(self.root, text="Song Track", font=font_style, bg=background_color, fg=text_color, bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("arial", 24, "bold"), bg=background_color, fg="#B0FC38").grid(row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.status, font=("arial", 24, "bold"), bg=background_color, fg="#B0FC38").grid(row=0, column=1, padx=10, pady=5)

        buttonframe = LabelFrame(self.root, text="Control Panel", font=font_style, bg=background_color, fg=text_color, bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        
        # Load and resize image files for buttons
        play_img = Image.open("play.png")
        play_img = play_img.resize((50, 50), Image.ANTIALIAS)  # Resize the image to fit the button frame
        play_img = ImageTk.PhotoImage(play_img)  # Convert to PhotoImage
        
        pause_img = Image.open("pause.png")
        pause_img = pause_img.resize((50, 50), Image.ANTIALIAS)
        pause_img = ImageTk.PhotoImage(pause_img)
        
        stop_img = Image.open("stop.png")
        stop_img = stop_img.resize((50, 50), Image.ANTIALIAS)
        stop_img = ImageTk.PhotoImage(stop_img)
        
        # Create image buttons and bind them to functions
        playbtn = Button(buttonframe, image=play_img, command=self.playsong, bg=background_color)
        playbtn.image = play_img  # Keep a reference to the image
        pausebtn = Button(buttonframe, image=pause_img, command=self.pausesong, bg=background_color)
        pausebtn.image = pause_img
        stopbtn = Button(buttonframe, image=stop_img, command=self.stopsong, bg=background_color)
        stopbtn.image = stop_img
        
        # Use pack with fill and expand options to make buttons take all available space
        playbtn.pack(side=LEFT, fill="both", expand=True, padx=10)
        pausebtn.pack(side=LEFT, fill="both", expand=True, padx=10)
        stopbtn.pack(side=LEFT, fill="both", expand=True, padx=10)

        songsframe = LabelFrame(self.root, text="Song Playlist", font=font_style, bg=background_color, fg=text_color, bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        scroll_y = Scrollbar(songsframe, orient=VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand=scroll_y.set, selectbackground=button_color, selectmode=SINGLE, font=("arial", 12, "bold"), bg=background_color, fg=text_color, bd=5, relief=GROOVE)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        os.chdir("mp3")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END, track)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("Playing.....")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set("Stopped......")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("Paused......")
        pygame.mixer.music.pause()

root = Tk()
MusicPlayer(root)
root.mainloop()
