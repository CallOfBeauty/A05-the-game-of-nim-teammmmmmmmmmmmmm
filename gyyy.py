###################################################################
# Author: Dimitrios Ntentia and Rodolfo Alvarado
# Username: ntentiad, alvaradoreyesr2
#
# Assignment: Final Project: The Nim Gitters
#
# Purpose: This program is designed for the user to play a fun game with the computer.
#
####################################################################################
import tkinter as tk
import msvcrt as m
from threading import Thread
import time
import random
import matplotlib.pyplot as mlt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import os

inputlist = []  # global list needed to be imported for the graphs


class Matplotwin:
    def __init__(self, inputlist):
        counter = 0
        username = inputlist[0]
        Totalballs = int(inputlist[1])
        del inputlist[:2]
        inputlist = [int(item) for item in inputlist]
        Tempcompballs = [inputlist[even] for even in range(len(inputlist)) if even % 2 == 1]
        print(Tempcompballs)
        for i in Tempcompballs:
            counter += i
        Computerballs = counter
        counter = 0
        Tempuserdata = [inputlist[odd] for odd in range(len(inputlist)) if odd % 2 == 0]
        print(Tempuserdata)
        for i in Tempuserdata:
            counter += i
        Userdata = counter
        counter = 0
        newroot = tk.Tk()

        totaldata = {"": ["Total"], "Balls": [Totalballs]}
        computerdata = {"": ["computer"], "Balls": [Computerballs]}
        userdata = {"": [username], "Balls": [Userdata]}

        totalframe = DataFrame(totaldata, columns=["", "Balls"])
        compframe = DataFrame(computerdata, columns=["", "Balls"])
        userframe = DataFrame(userdata, columns=["", "Balls"])

        totalfig = mlt.Figure(figsize=(5, 4), dpi=80)
        compfig = mlt.Figure(figsize=(5, 4), dpi=80)
        userfig = mlt.Figure(figsize=(5, 4), dpi=80)

        addtotfig = totalfig.add_subplot(111)
        addcompfig = compfig.add_subplot(111)
        adduserpfig = userfig.add_subplot(111)

        totalbar = FigureCanvasTkAgg(totalfig, newroot)
        compbar = FigureCanvasTkAgg(compfig, newroot)
        userbar = FigureCanvasTkAgg(userfig, newroot)

        totalbar.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        compbar.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        userbar.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        totalframe = totalframe[['', 'Balls']].groupby('').sum()
        compframe = compframe[['', 'Balls']].groupby('').sum()
        userframe = userframe[['', 'Balls']].groupby('').sum()

        totalframe.plot(kind='bar', legend=True, ax=addtotfig)
        compframe.plot(kind='bar', legend=True, ax=addcompfig)
        userframe.plot(kind='bar', legend=True, ax=adduserpfig)

        addtotfig.set_title("Graph showing the total Number of Balls")
        addcompfig.set_title("Graph showing Number of Balls chosen by the computer")
        adduserpfig.set_title("Graph showing Number of Balls chosen by " + username)


class interface(object):
    def __init__(self, inputlist):
        self.question = "What is your username?"
        self.input = ""
        self.root = tk.Tk()
        self.inputlist = inputlist
        self.compchoice = 0

        self.numballs = 0
        self.humanremover = 5
        self.winner = ""
        self.stage = 1

    def maketkinter(self):
        self.root.title("Game")
        self.root.geometry("800x500")
        self.root.subtitle = tk.Label(self.root, text="Let's Play a game!")
        self.root.subtitle.config(font=("Courier", 20))
        self.root.question = tk.Label(self.root, text="\n\n\n\n" + self.question + "\n\n\n")
        self.root.question.config(font=("Courier", 16))
        self.root.textbox = tk.Text(self.root, height=2, width=10)

        self.root.btnsubmit = tk.Button(self.root, text="Submit", command=self.Btn_clicked)
        self.root.btnexit = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.root.btngraphs = tk.Button(self.root, text="Show graphs", command=lambda: self.new_window(Matplotwin))

        self.root.subtitle.pack()
        self.root.question.pack()
        self.root.textbox.pack()
        self.root.btnsubmit.pack()
        self.root.btngraphs.pack()
        self.root.btnexit.pack()
        self.root.mainloop()

    def new_window(self, _class):
        _class(inputlist=self.inputlist)

    def Btn_clicked(self):
        self.getinput()
        self.loop_Num()

    def changequestion(self):
        self.root.question["text"] = "\n\n\n\n" + self.question + "\n\n\n"
        self.root.question.pack()

    def getinput(self):
        self.input = self.root.textbox.get("1.0", "end-1c")
        self.inputlist.append(self.input)
        print(self.inputlist)

    def strategy(self):
        numballs = int(self.numballs)
        if numballs > 9:
            local = random.randrange(1, 5)
            return local
        elif numballs <= 9 and numballs > 5:
            local = numballs - 5
            return local
        elif numballs == 5:
            local = random.randrange(1, 5)
            return local
        elif numballs < 5:
            local = numballs
            return local


    def loop_Num(self):
        if len(inputlist) == 1:
            self.question = "How many Total balls do you wanna chose?(15 and above)"
            self.changequestion()
            self.stage = self.stage + 1
        elif self.stage == 2:
            try:
                if int(inputlist[1]) < 15:
                    inputlist.pop()
                    self.question = "The Input does not meeting the requirements\nPlease input a number greater than 15"
                    self.changequestion()
                else:
                    self.numballs = inputlist[1]
                    self.compchoice = self.strategy()
                    self.numballs = int(inputlist[1]) - int(self.compchoice)
                    self.question = "The computer chose " + str(self.compchoice) + "\n \nThere are " + str(
                        self.numballs) + " balls left\n\nHow many balls do you wanna remove:"
                    self.changequestion()
                    self.stage = self.stage + 1
                    inputlist.append(self.compchoice)
            except Exception:
                inputlist.pop()
                self.question = "The Input is not Valid, please input a number greater than 15"
                self.changequestion()

        elif self.stage == 3:
            try:
                k = inputlist.pop()
                int(k)
                inputlist.append(k)
                if int(k) > 4 or int(k) < 1:
                    inputlist.pop()
                    self.question = "Please make a selection between 1 and 4"
                    self.changequestion()
                else:
                    self.numballs=self.numballs-int(k)
                    self.compchoice = self.strategy()
                    self.numballs=self.numballs+int(k)
                    if int(k) >= int(self.numballs):
                        self.question = "THE WINNER is " + str(inputlist[0])
                        self.changequestion()
                    elif int(self.compchoice) == (int(self.numballs)-int(k)):
                        inputlist.append(self.compchoice)
                        self.question = "The computer chose " + str(
                            self.compchoice) + "\n There are no balls left.\n THE WINNER is computer"
                        self.changequestion()
                    else:
                        self.numballs = int(self.numballs) - int(self.compchoice)-int(k)
                        self.question = "The computer chose " + str(self.compchoice) + "\n \nThere are " + str(
                            self.numballs) + " balls left\n\nHow many balls do you wanna remove:"
                        self.changequestion()
                        inputlist.append(self.compchoice)

            except Exception:
                inputlist.pop()
                self.question = "The Input is not Valid\n\nPlease input a number greater than 0 and smaller than 5"
                self.changequestion()


def main():
    Parent = interface(inputlist)
    Parent.maketkinter()


def sound():
    file = "music.mp3"
    os.system("mpg123 " + file)


if __name__ == '__main__':
    main()
  #  Thread(target=main).start()
   # Thread(target=sound).start()

