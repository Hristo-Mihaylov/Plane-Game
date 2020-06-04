from tkinter import Tk, Canvas, PhotoImage, Button, Label, Toplevel
from random import randint
import time
import _assessment2


def new_game():
    _assessment2.init()


def restart_game():
    global canvas1, canvas2
    canvas1.pack_forget()
    text_restart1 = canvas2.create_text(400, 235,
                                        text="If you want to restart the game, press <Shift R>.",
                                        font="Times 20 italic bold")
    btn_back = Button(canvas2, width="35", height="3",
                      text="Back", bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=lambda: back_to_menu())
    btn_back.place(x=500, y=400)
    canvas2.pack()


def leaderboard():
    global canvas1, canvas7
    canvas1.pack_forget()
    canvas7.create_text(400, 35, text="Leaderboard",
                        font="Times 40 italic bold")
    global lead_list
    lead_list = list()
    with open("leader_board.txt", "r") as file:
        lead_list = file.readlines()
        for i in range(5):
            canvas7.create_text(400, 170+i*40, text=str(i+1)+". " + lead_list[i],
                                font="Times 20 italic bold")
    btn_back = Button(canvas7, width="35", height="3",
                      text="Back", bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=lambda: back_to_menu())
    btn_back.place(x=500, y=400)
    canvas7.pack()


def how_to_play():
    global canvas1, canvas3
    canvas1.pack_forget()
    text_1 = canvas3.create_text(400, 35,
                                 text="Your main aim is to avoid the obstacles and the clouds.",
                                 font="Times 20 italic bold")
    text_2 = canvas3.create_text(400, 105,
                                 text="Every star you collect is worth 10 points.",
                                 font="Times 20 italic bold")
    text_3 = canvas3.create_text(400, 175,
                                 text="On every 50 points, the game gets harder. Good luck!",
                                 font="Times 20 italic bold")
    btn_back = Button(canvas3, width="35", height="3",
                      text="Back", bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=lambda: back_to_menu())
    btn_back.place(x=500, y=400)
    canvas3.pack()


def boss_key():
    global canvas1, canvas6
    canvas1.pack_forget()
    text_boss = canvas6.create_text(400, 200,
                                    text="For boss key, press <b>",
                                    font="Times 20 italic bold")
    btn_back = Button(canvas6, width="35", height="3",
                      text="Back", bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=lambda: back_to_menu())
    btn_back.place(x=500, y=400)
    canvas6.pack()


def cheat_codes():
    global canvas1, canvas4
    canvas1.pack_forget()
    text_4 = canvas4.create_text(400, 35,
                                 text="Press <cheat> to slow down the obstacles.",
                                 font="Times 20 italic bold")
    text_5 = canvas4.create_text(400, 105,
                                 text="Press <harder> to speed up the game.",
                                 font="Times 20 italic bold")
    text_6 = canvas4.create_text(400, 175,
                                 text="Press <s> to increase the speed of the plane.",
                                 font="Times 20 italic bold")

    btn_back = Button(canvas4, width="35", height="3",
                      text="Back", bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=lambda: back_to_menu())
    btn_back.place(x=500, y=400)
    canvas4.pack()


def settings():
    global canvas1, canvas5
    canvas1.pack_forget()
    text_up_down = canvas5.create_text(400, 25,
                                       text="Move the plane using the <Up> and <Down> keys",
                                       font="Times 20 italic bold")
    text_pause = canvas5.create_text(400, 95,
                                     text="If you want to pause the game, press <p>.",
                                     font="Times 20 italic bold")
    text_unpause = canvas5.create_text(400, 165,
                                       text="If you want to unpause the game, press <u>.",
                                       font="Times 20 italic bold")
    text_restart = canvas5.create_text(400, 235,
                                       text="If you want to restart the game, press <Shift R>.",
                                       font="Times 20 italic bold")
    text_quit = canvas5.create_text(400, 305,
                                    text="If you want to quit the game, press <q>.",
                                    font="Times 20 italic bold")
    btn_back = Button(canvas5, width="35", height="3", text="Back",
                      bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=lambda: back_to_menu())
    btn_back.place(x=500, y=400)
    canvas5.pack()


def exit_game():
    root.destroy()


def back_to_menu():
    global canvas1, canvas2, canvas3, canvas4, canvas5, canvas6
    canvas2.pack_forget()
    canvas3.pack_forget()
    canvas4.pack_forget()
    canvas5.pack_forget()
    canvas6.pack_forget()
    canvas7.pack_forget()
    canvas1.pack()


def main_menu():
    global canvas1, canvas2, canvas3, canvas4, canvas5, canvas6, canvas7
    welcome_text = canvas1.create_text(400, 40,
                                       text="Welcome to Unknown Skies!",
                                       font="Times 35 italic bold",
                                       fill="black")
    btn_new_game = Button(canvas1, width="35", height="3",
                          text="New Game", bg="#cafafe",
                          borderwidth=2, relief="solid",
                          command=new_game)
    btn_new_game.place(x=100, y=170)
    btn_restart_game = Button(canvas1, width="35", height="3",
                              text="Restart game", bg="#cafafe",
                              borderwidth=2, relief="solid",
                              command=restart_game)
    btn_restart_game.place(x=100, y=240)
    btn_leaderboard = Button(canvas1, width="35", height="3",
                             text="Leaderboard", bg="#cafafe",
                             borderwidth=2, relief="solid",
                             command=leaderboard)
    btn_leaderboard.place(x=100, y=310)
    btn_settings = Button(canvas1, width="35", height="3",
                          text="Settings", bg="#cafafe",
                          borderwidth=2, relief="solid",
                          command=settings)
    btn_settings.place(x=400, y=310)
    btn_how_to_play = Button(canvas1, width="35", height="3",
                             text="How to play", bg="#cafafe",
                             borderwidth=2, relief="solid",
                             command=how_to_play)
    btn_how_to_play.place(x=100, y=380)
    btn_boss_key = Button(canvas1, width="35", height="3",
                          text="Boss Key", bg="#cafafe",
                          borderwidth=2, relief="solid",
                          command=boss_key)
    btn_boss_key.place(x=400, y=170)
    btn_cheat_codes = Button(canvas1, width="35", height="3",
                             text="Cheat codes", bg="#cafafe",
                             borderwidth=2, relief="solid",
                             command=cheat_codes)
    btn_cheat_codes.place(x=400, y=240)
    btn_exit_game = Button(canvas1, width="35", height="3",
                           text="Quit game", bg="#cafafe",
                           borderwidth=2, relief="solid",
                           command=exit_game)
    btn_exit_game.place(x=400, y=380)
    btn_back = Button(canvas1, width="35", height="3",
                      text="Back", bg="#cafafe",
                      borderwidth=2, relief="solid",
                      command=back_to_menu)


root = Tk()
root.configure(background="#e6ffff")
root.title("M E N U")
root.geometry("800x500")
global background
background = PhotoImage(file="sky1.png")
global canvas1
canvas1 = Canvas(root, width=800, height=500)
canvas1.configure(background="#f0f0f0")
canvas1.pack()
global canvas2
canvas2 = Canvas(root, width=800, height=500)
canvas2.configure(background="#f0f0f0")
global canvas3
canvas3 = Canvas(root, width=800, height=500)
canvas3.configure(background="#f0f0f0")
global canvas4
canvas4 = Canvas(root, width=800, height=500)
canvas4.configure(background="#f0f0f0")
global canvas5
canvas5 = Canvas(root, width=800, height=500)
canvas5.configure(background="#f0f0f0")
global canvas6
canvas6 = Canvas(root, width=800, height=500)
canvas6.configure(background="#f0f0f0")
global canvas7
canvas7 = Canvas(root, width=800, height=500)
canvas7.configure(background="#f0f0f0")
main_menu()
root.mainloop()
