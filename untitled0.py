#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:00:43 2019

@author: rin35130
"""

import tkinter as tk
from random import randint
from tkinter import LabelFrame, Radiobutton, Entry


class Application(tk.Tk):
    name = 'Pocitani'
    

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=10)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Počítání pro ZŠ")
        self.lbl.pack()
        
        
        
        self.transakceVar = tk.StringVar()
        #self.transakceVar.trace('w', self.vypocet)
        
        self.transakceFrame = LabelFrame(self, text="Mat. operace",
                                         padx=5, pady=5)
        self.transakceFrame.pack()
#####        
        Radiobutton(self.transakceFrame, text="+",
                    variable=self.transakceVar, value='+',command=self.plus).pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text="-",
                    variable=self.transakceVar, value='-',command=self.minus).pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text="x",
                    variable=self.transakceVar, value='x',command=self.krat).pack(anchor=tk.W)
        Radiobutton(self.transakceFrame, text=":",
                    variable=self.transakceVar, value=':',command=self.deleni).pack(anchor=tk.W)
        self.transakceVar.set('+')
        
        
#####        
        
        
        #self.cisloA= LabelFrame(self, text="")
        #self.cisloA.pack()
        
        self.kurzFrame = LabelFrame(self, text="")
        self.kurzFrame.pack()
        
        
        
        #self.cisloA= Entry(self.kurzFrame, state="readonly")
        #self.cisloA.pack()
        
        
#####        

        self.vstup = Entry(self.kurzFrame)
        self.vstup.pack()
        self.vstup.focus_set()
#####
        
        self.tlacitko = tk.Button(self.kurzFrame, text=u"přečti", width=10, command=self.komand, font="ArialNarrow 10")
        self.tlacitko.pack()

        
#####   
        self.btn = tk.Button(self, text='Konec', command=self.quit)
        self.btn.pack()
    
    def plus(self):
        self.a= randint(0, 99)
        self.b= randint(0, 99)
        self.x= self.a+self.b
        print(self.a, "+", self.b, '=', self.x)
        return()
        
    def minus(self):
        self.a= randint(0, 99)
        self.b= randint(0, self.a)
        self.x= self.a-self.b
        print(self.a, "-", self.b, '=', self.x)
        return()
    def krat(self):
        self.a= randint(0, 9)
        self.b= randint(0, 9)
        self.x= self.a*self.b
        print(self.a,"x" , self.b, '=', self.x)
        return()
    def deleni(self):
        self.x= randint(0, 9)
        self.b= randint(1, 9)
        self.a= self.b*self.x
        print(self.a, ":", self.b, '=', self.x)
        return()
        
     
    def komand(self):
    
        print(self.x)
        print(self.vstup.get())
       # if self.x=="":
       #     print("žádný příklad")
       #     pass
       # else:
        if int(self.vstup.get())== self.x:
            print("výborně")
        else:
            print("Back to Kosinka")
    #def vypocet(self):
     #   operace = (self.plus, self.minus, self.krat, self.deleni)
      #  nahoda = randint(0, 3)
      #  funkce = operace[nahoda]
       # funkce()
      #  print()
      #  print(self.a, funkce.__name__, self.b, '=', self.x)            
       # if self.vysledek == self.x:
        #    print("ok")
        
    def quit(self, event=None):
        super().quit()
        
    
app = Application()
app.mainloop()