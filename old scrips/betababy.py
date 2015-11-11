print('Importing...')
import os
import sys
import sqlite3 as sql
from ttk import *
from tkinter import *
from tkinter import Button as TkButton
from tkinter import messagebox
from PIL.ImageTk import PhotoImage
print('Done.')

'''
retarded
'''

__author__ = 'retarded' 


class Player(object):

    '''player data container'''
        
    def __init__(self, slot):
        
        self.name = None
        self.character = None
        self.slot = slot
        self.kills = 0
        self.sds = 0
        self.games = 0
        #once all player classes have been instantiated,
        #have all player classes sync to create relative
        #kill variables
    
    def export(self):
        
        #export data to a file in the form of a dictionary
        pass

    def reportself(self):
        print('\nPlayer info:\nName = {}\nCharacter = {}'
              .format(self.name, self.character))

    def readytoplay(self):

        if self.name != None and self.character != None:
            return True
        else:
            return False
        
class Smash(Frame):

    
    '''the gooey bit'''

    
    def __init__(self, master):
        
        '''
        Initializes the gui by creating the main frame, calling the title
        screen and doing whatever background work.
        '''

        Frame.__init__(self, master)
        root.geometry('800x600+0+440')
        self.canvas = Canvas(master = self, cursor = 'hand1',
                             width = 800, height = 600)
        s = Style(root)
        s.configure('.', cursor = 'hand1')
        self.canvas.pack()
        self.datahandler(init = True)
        self.titlescreen()
        
        
    def datahandler(self, init = False):
        
        '''Consider wrapping this in a class external to the GUI.'''

        
        originalpath = os.getcwd()
        class smashcontainer:
            
            pass
        
        def databasesearch():
            # seach cwd for correct file, maybe use a custom extension
            # for convenience 
            # os.chdir('..') for wider search
            
            path = None
            for tuple in os.walk(os.getcwd()):
                for item in tuple[2]:
                    if item == 'smashdatabase.db':        
                        path = tuple[0]
                        return path


        def database_skeleton():
            
            print('Creating stat skeleton...')
            skeleton = ('CREATE TABLE basic(Name text, Kills int)',
                        """INSERT INTO basic VALUES ('Matt', 0),
                                                    ('Karel', 0),
                                                    ('Kevin', 0)""")              
            self.cur.execute(skeleton[0])
            self.cur.execute(skeleton[1])
            self.con.commit()
            print('Done.')

            
        def import_stats():
            
            pass


        if init:
            print('Looking for stats...')
            database_path = databasesearch()
            if not database_path:
                print('Stats not found.\n'\
                      'Creating stat database in {}...'.format(originalpath))
                self.con = sql.connect('smashdatabase.db')
                self.cur = self.con.cursor()
                database_skeleton()
            else:
                print('Stats found.')
                self.con = sql.connect('smashdatabase.db')
                self.cur = self.con.cursor()
      
        # to do:
        #   -prompt the user to find it themselves if autosearch fails or
        #    search with wider scope
        #   -create import functions for handling the demands of statdisplay
        #    and stat analysis
        
    def titlescreen(self):
        
        '''
        Main menu screen.
        Options:
            -display records
            -begin stat recording:
            -stat analysis
            -whatever
            -quit
        '''

        def button_highlight(event):
            event.widget.config(foreground = '#040D24',
                                background = '#FFCB00')
        def button_dehighlight(event):
            event.widget.config(foreground = '#C89632',
                                background = '#040D24')

        try: self.canvas.delete('all')
        except: pass
        
    
        self.titleimage = PhotoImage(file = 'titleimage.png')
        self.canvas.create_image((400, 300),
                                      image = self.titleimage)
        
        RecordingButton = TkButton(master = self,
                            text = 'Start Recording', cursor = 'hand1',
                            font = ('Helectiva', 20, 'bold'),
                            fg = '#C89632', bg = '#040D24', bd = 1,
                            command = self.playerselect)
        StatDisplayButton = TkButton(master = self,
                            text = 'Stat Display', cursor = 'hand1',
                            font = ('Helectiva', 20, 'bold'),
                            fg = '#C89632', bg = '#040D24', bd = 1,
                            command = self.statdisplay)
        AnalysisButton = TkButton(master = self,
                            text = 'Stat Analysis', cursor = 'hand1',
                            font = ('Helectiva', 20, 'bold'),
                            fg = '#C89632', bg = '#040D24', bd = 1,
                            command = self.statanalysis)
                                  
        RecordingButton.bind('<Enter>', button_highlight)
        StatDisplayButton.bind('<Enter>', button_highlight)
        AnalysisButton.bind('<Enter>', button_highlight)
        RecordingButton.bind('<Leave>', button_dehighlight)
        StatDisplayButton.bind('<Leave>', button_dehighlight)
        AnalysisButton.bind('<Leave>', button_dehighlight)
        
        self.canvas.create_window((322,186), window = RecordingButton,
                                  width = 323, height = 40)
        self.canvas.create_window((255,245), window = StatDisplayButton,
                                  width = 320, height = 40)
        self.canvas.create_window((204,308), window = AnalysisButton,
                                  width = 320, height = 41)

        #to do:
        #   -create a dynamic focus-based label in bottom text slot
        #   -maybe recreate the focus-based 'select-ball' on right of option
                                 
        
    def playerselect(self, init=True):
        '''
        A new toplevel screen or replacement canvas inside main_frame.
        Called before stat recording begins, used for selecting
        participating players/characters and handling related data.
        Meant to handle like normal melee game setup.
        '''

        try: self.canvas.delete('all')
        except Exception as ex: print(ex)
            
        #canvas cosmetics, image resourcing   
        self.backimage = PhotoImage(file = 'back.png')
        self.toggleon = PhotoImage(file = 'toggleon.png')
        self.toggleoff = PhotoImage(file = 'toggleoff.png')
        self.pselectbackground = PhotoImage(file = 'listboxbackground.png')
        self.p1coin = PhotoImage(file = 'p1coin.png')
        self.p2coin = PhotoImage(file = 'p2coin.png')
        self.p3coin = PhotoImage(file = 'p3coin.png')
        self.p4coin = PhotoImage(file = 'p4coin.png')
        self.coinlist = [self.p1coin, self.p2coin, self.p3coin, self.p4coin]

  
        def back():
            self.titlescreen()


        def namelist():
            
            '''Consider making namefill a method of a datahandler class.'''
            
            print('Trying to fill list with names.')
            self.cur.execute("""SELECT Name FROM basic""")
            namelist = [name for name in self.cur]
            for name in namelist:
                print(name[0])
            print('Done Trying.')
            return namelist
        
            
        def playercoin(self, event, player):

            def move_coin(event):
                self.canvas.move('p{}coin'.format(coinslot),
                                 event.x - 20, event.y - 20)

              
            def determine_character(event, player):
                # consider storing this grid info and grid arithmetic in
                # a separate module
                character_array = {
                    'dr. mario' : (45, 100), 'mario' : (125, 95),
                    'luigi': (205, 95), 'bowser' : (285, 95),
                    'peach': (365, 95), 'yoshi' : (445, 95),
                    'dk': (525, 95), 'falcon' : (610, 95),
                    'ganondorf' : (690, 100), 'falco' : (45, 175),
                    'fox' : (125, 170), 'ness' : (205,170),
                    'ice climbers' : (285, 170), 'kirby' : (365, 170),
                    'samus' : (445, 170), 'zelda' : (525, 170),
                    'link' : (610, 170), 'young link':(690, 175),
                    'pichu' : (130, 250), 'pikachu' : (205, 245),
                    'jigglypuff' : (285, 245), 'mewtwo' : (365, 245),
                    'game and watch' : (445, 245), 'marth' : (525, 245),
                    'roy' : (610, 250)}

                coin_x = coin.winfo_x() + 20
                coin_y = coin.winfo_y() + 20
                x = portrait_width = 70; y = portrait_height = 65
                for char in character_array.keys():
                    pivot = portrait_corner = character_array[char]
                    if coin_x >= pivot[0] and coin_x <= pivot[0] + x:
                        if coin_y >= pivot[1] and coin_y <= pivot[1] + y:
                            print('Selected {}'.format(char))
                            player.character = char
                            player.reportself()              

            coinslot = event.widget.slot
            print('Creating p{} coin.'.format(coinslot))
            coin_origin = ((event.widget.winfo_x() + 120,
                            event.widget.winfo_y()))
            coin = Label(self, borderwidth = 0,  cursor = 'hand1',
                              image = self.coinlist[coinslot - 1])
            coin.bind('<B1-Motion>', move_coin)
            coin.bind('<ButtonRelease-1>', lambda event:
                      determine_character(event, player))
            self.canvas.create_window(coin_origin,
                                      window = coin,
                                      tags = ('p{}coin'.format(coinslot),
                                              'p{}'.format(coinslot)))

            
        def nameselectbox(self, event, player):

            def nameupdate(event, player):
                player.name = namebox.get(int(namebox.curselection()[0]))
                player.reportself()
            
            xpos = event.widget.winfo_x() + 90
            ypos = event.widget.winfo_y() + 135
            namebox = Listbox(self,
                              bg = 'black', fg = 'white',
                              font = ('Helectiva', 15, 'bold'),
                              activestyle = 'dotbox',  cursor = 'hand1',
                              selectbackground = 'green',
                              selectforeground = 'black',
                              selectmode = SINGLE, takefocus = FALSE,
                              exportselection = False)
            namebox.bind('<<ListboxSelect>>',
                         lambda event: nameupdate(event, player))
            self.canvas.create_window((xpos, ypos),
                                      window = namebox,
                                      width = 160,  height = 210,
                                      tags = ('p{}box'
                                              .format(event.widget.slot),
                                              'p{}'
                                              .format(event.widget.slot)))
            namebox.focus()
            names = namelist()
            for name in names:
                namebox.insert(END, name[0])
            namebox.selection_clear(namebox.index(ACTIVE))
            
            player.reportself()
            
            #create name entry button
            #handle name selection/creation

        def playerbox(self, event, player):

            pass
        
        def buttontoggle(event):
            '''changes the image on the player toggle button'''
            
            if event.widget.var.get() == 0:
                event.widget.var.set(1)
                event.widget.config(image = self.toggleon)
                player = Player(button.slot)
                activeplayerlist[button.slot - 1] = player
                playerbox(self, event, player)
                nameselectbox(self, event, player)
                playercoin(self, event, player)
                    
            else:
                event.widget.var.set(0)
                event.widget.config(image = self.toggleoff)
                self.canvas.delete('p{}'.format(event.widget.slot))
                activeplayerlist[button.slot - 1].name = None
                activeplayerlist[button.slot -1].character = None
                activeplayerlist[button.slot -1] = None
            
        activeplayerlist= [None, None, None, None]
        #button widget creations
        backbutton = Button(self, cursor = 'hand1',
                            image = self.backimage, bd = 0, command = back)
        self.canvas.create_window((720, 65), window = backbutton)
        toggle_xpos = 90; toggle_ypos = 335
        for slot in range(1,5):
            toggle = BooleanVar(self)
            button = Checkbutton(self, indicatoron = False,
                                 bd = 0, cursor = 'hand1',
                                 image = self.toggleoff)
            button.var = toggle
            button.slot = slot
            button.bind('<Button-1>', buttontoggle)
            self.canvas.create_window((toggle_xpos, toggle_ypos),
                                      window = button,
                                      tag = 'p{}toggle'.format(slot))
            toggle_xpos += 175

        # this next block somehow fails if placed in resourcing block above
        self.pselectbackground = PhotoImage(file = 'playerselect.png')
        self.canvas.create_image((400,300), image = self.pselectbackground)
        
        #to do:
        #   -provide an option for adding a completely new player
        #   -instantiate player classes from given names
            
    def recordingscreen(self):
        
        '''Possibly integrate playerselection and recording.'''
        
        pass

    def statdisplay(self):

        '''Display session and all-time stats.'''

        pass

    def statanalysis(self):

        '''In depth analysis.'''

        pass

    def guiquit(self):

        '''Clean up and close.'''

        pass

    
if __name__ == '__main__':
    
    root = Tk()
    retardedlifeless = Smash(root)
    retardedlifeless.pack()
    root.mainloop()
           


##if __name__ == '__main__':
##    
##    try:
##        root = Tk()
##        retardedlifeless = Smash(root)
##        retardedlifeless.pack()
##        root.mainloop()
##        
##    except Exception as ex:
##        
##        print(ex)
##        input()
