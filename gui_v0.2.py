# 1/27/25 Edited by Cameron, GUI v0.2
"""Changes made:
shoved all functions into a class "Window."

TO DO:
1) Main menu logo and background
2) Possible Timer
3) Replacement function for lambda instances
4) Other aesthetic edits
"""
import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self):
        self.main = tk.Tk("Note Rush")
        
    def game_over(self):
        game_over = tk.Toplevel(self.main,bg="red")
        game_over.title("Note Rush - Game over")
        game_over.geometry(f"{self.main.screen_width}x{self.main.screen_height}")

        replay_button = ttk.Button(game_over, text="PLAY AGAIN?", command=lambda:[self.game_window(), game_over.destroy()]).pack(padx=10,pady=10,ipadx=20,ipady=20)
        main_menu_button = ttk.Button(game_over, text="MAIN MENU", command=game_over.destroy).pack(padx=10, pady=10)
        quit_button = ttk.Button(game_over, text="QUIT", command=self.main.destroy).pack(padx=10, pady=10)
        
    def game_window(self):
        game_window = tk.Toplevel(self.main,bg="blue")
        game_window.title("Note Rush")
        game_window.geometry(f"{self.main.screen_width}x{self.main.screen_height}")

        play_button = ttk.Button(game_window, text="PLAYER", command=lambda:[self.game_over(),game_window.destroy()]).pack(padx=10,pady=10,ipadx=20,ipady=20) # lambda will need to be edited
        quit_button = ttk.Button(game_window, text="QUIT", command=game_window.destroy).pack(padx=10, pady=10)

    def start(self):
        self.main.screen_width = self.main.winfo_screenwidth()
        self.main.screen_height = self.main.winfo_screenwidth()
        self.main.geometry(f"{self.main.screen_width}x{self.main.screen_height}")
        self.main.window_name = self.main.title("Note Rush")
        
        self.main.text = ttk.Label(self.main, text="NOTE RUSH", anchor="n", font=25).pack(padx=5,pady=5,ipadx=10,ipady=10)
        self.main.play_button = ttk.Button(self.main, text="PLAY", command=self.game_window).pack(padx=10,pady=10,ipadx=20,ipady=20)
        self.main.quit_button = ttk.Button(self.main, text="QUIT", command=self.main.destroy).pack(padx=10,pady=10,ipadx=2,ipady=2)
        self.main.mainloop()

app = Window()
app.start()


