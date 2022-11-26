import tkinter as tk
import time
import random
import matplotlib.pyplot as mlt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import matplotlib.pyplot as plt







class Matplotwin:
    def __init__(self):
        numballdata = {'Name': ['username'],
                       'Balls': [16]
                       }
        dataf = DataFrame(numballdata, columns=['Name', 'Balls'])
        root = tk.Tk()

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
        dataf = dataf[['Name', 'Balls']].groupby('Name').sum()
        dataf.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Title of the graph')

class classs():
    def __init__(self):
        self.numballs = 0
        self.humanremover = 5
        self.winner = ""
        self.xnum = 0
        self.username = ""
        self.numballs = 0
        self.number2 = 0
        self.number3 = 0
        self.input=''



        self.root = tk.Tk()
        self.root.title("Game")
        self.placeholder=""
        self.root.geometry("600x500")
        self.text=""
        self.Place = tk.Text(self.root, height=3, width=5)
        self.Titleprint = tk.Label(self.root, text="Let's play a game!")
        self.Titleprint.config(font=("Courier", 18))
        self.Printans = tk.Label(self.root, text="\n\n\n\nWhat do you want your username to be?\n\n\n")
        self.Printans.config(font=("Courier", 16))
        self.b1 = tk.Button(self.root, text="Make my selection", command=lambda: self.getinput())
        self.b2 = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.b3 = tk.Button(self.root, text="Show graphs", command=lambda: self.new_window(Matplotwin))
        self.Titleprint.pack()
        self.Printans.pack()
        self.Place.pack()
        self.b1.pack()
        self.b3.pack()
        self.b2.pack()

        self.Place.insert(tk.END, self.placeholder)


    def new_window(self, _class):
            _class()

    def changeText(self,text):
        self.text=text
        self.Printans['text'] = "\n\n\n\n"+ self.text +"\n\n\n"

    def getinput(self):
        self.input = self.Place.get(1.0, "end-1c")

    def strategy(self, number):
        if number > 9:
            local = random.randrange(1, 5)
            return local
        elif number <= 9 and number > 5:
            local = number - 5
            return local
        elif number == 5:
            local = random.randrange(1, 5)
            return local
        else:
            return number


    def asknumbballs(self):
        numballs=self.numballs
        while numballs < 15:
            self.changeText("Please enter the number of balls, must be 15 or higher: \n")
            numballs=int(self.getinput)
            self.numballs = numballs
        return self.numballs

    def another(self):



        self.root.mainloop()







    def __str__(self):
        return "The winner is " + self.username

def main():
    '''The main() function--used to call all other functions.'''
    testing=classs()
    testing.another()

if __name__ == '__main__':
    main()  # calls the main() function


