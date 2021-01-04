from tkinter import *

from XO import XO


class Controller:
    def __init__(self):
        self.numOfClicks = 0
        self.symbol = ""
        self.root = Tk()
        self.xo = XO()
        self.root.title("tic tac toe")
        self.symbolTexts = []
        self.buttonList = []
        for i in range(9):
            self.symbolTexts.append(StringVar())
            self.symbolTexts[i].set("")

        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[0], command=lambda: self.click(0),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[1], command=lambda: self.click(1),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[2], command=lambda: self.click(2),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[3], command=lambda: self.click(3),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[4], command=lambda: self.click(4),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[5], command=lambda: self.click(5),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[6], command=lambda: self.click(6),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[7], command=lambda: self.click(7),relief="sunken", padx=40, pady=40))
        self.buttonList.append(
            Button(self.root, textvariable=self.symbolTexts[8], command=lambda: self.click(8),relief="sunken", padx=40, pady=40))
        for i in range(9):
            if i < 3:
                self.buttonList[i].grid(row=1, column=i)
            elif i < 6:
                self.buttonList[i].grid(row=2, column=i - 3)
            else:
                self.buttonList[i].grid(row=3, column=i - 6)
        self.root.mainloop()

    def reset(self):
        self.xo = XO()
        self.numOfClicks = 0
        for i in range(9):
            self.buttonList[i]["state"] = NORMAL
            self.symbolTexts[i].set("")
        self.buttonList[0]['command'] = lambda: self.click(0)
        self.buttonList[1]['command'] = lambda: self.click(1)
        self.buttonList[2]['command'] = lambda: self.click(2)
        self.buttonList[3]['command'] = lambda: self.click(3)
        self.buttonList[4]['command'] = lambda: self.click(4)
        self.buttonList[5]['command'] = lambda: self.click(5)
        self.buttonList[6]['command'] = lambda: self.click(6)
        self.buttonList[7]['command'] = lambda: self.click(7)
        self.buttonList[8]['command'] = lambda: self.click(8)

