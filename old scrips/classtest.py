import os
import sys
import sqlite3 as sql
from ttk import *
from tkinter import *
from tkinter import Button as TkButton
from tkinter import messagebox
from PIL.ImageTk import PhotoImage



playerlist = []

class player(object):

    def __init__(self, slot):

        self.slot = slot

    
for slot in range(1,5):
    
    p = player(slot)
    playerlist.append(p)


print(playerlist)
