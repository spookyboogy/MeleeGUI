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


class DataHandler(object):
    
    
    def __init__(self):
        
        self.originalpath = os.getcwd()
        
        print('\nLooking for stats...')
        self.database_path = self.databasesearch()
        if not self.database_path:
            print('Stats not found.\n'\
                  'Creating stat database in {}...'.format(self.originalpath))
            self.database_path = os.path.join(self.originalpath,
                                              'smashdatabase.db')
            self.con = sql.connect(self.database_path)
            self.cur = self.con.cursor()
            self.database_skeleton()
        else:
            print('Stats found.')
            self.con = sql.connect('smashdatabase.db')
            self.cur = self.con.cursor()        
        
 
    def databasesearch(self):
        # seach cwd for correct file, maybe use a custom extension
        # for convenience 
        # os.chdir('..') for wider search
        
        path = None
        for tuple in os.walk(os.getcwd()):
            for item in tuple[2]:
                if item == 'smashdatabase.db':        
                    path = tuple[0]
                    return path


    def database_skeleton(self):
        
        print('Creating stat skeleton...')
        skeleton = ('CREATE TABLE basic(Name text, Kills int)',
                    """INSERT INTO basic VALUES ('Matt', 0),
                                                ('Karel', 0),
                                                ('Kevin', 0)""")              
        self.cur.execute(skeleton[0])
        self.cur.execute(skeleton[1])
        self.con.commit()
        print('Done.')
        
    # to do:
    #   -prompt the user to find it themselves if autosearch fails or
    #       search with wider scope
    #   -create import functions for handling the demands of statdisplay
    #       and stat analysis

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
    
        print('\nPlayer report:\nSlot = {}\nName = {}\nCharacter = {}'
              .format(self.slot, self.name, self.character))

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
        self.datahandler = DataHandler()
        self.titlescreen()
       
        
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
                                 
        
    def playerselect(self):
        '''
        A new toplevel screen or replacement canvas inside main_frame.
        Called before stat recording begins, used for selecting
        participating players/characters and handling related data.
        Meant to handle like normal melee game setup.
        '''

        try: self.canvas.delete('all')
        except Exception as ex: print(ex)
            
        # canvas cosmetics, image resourcing
        # could be compressed
        # clean up portrait images
        self.backimage = PhotoImage(file = 'back.png')
        self.toggleon = PhotoImage(file = 'toggleon.png')
        self.toggleoff = PhotoImage(file = 'toggleoff.png')
        self.pselectbackground = PhotoImage(file = 'listboxbackground.png')
        self.nameboxpreimage = PhotoImage(file = 'nameboxpreimage.png')
        self.p1coin = PhotoImage(file = 'p1coin.png')
        self.p2coin = PhotoImage(file = 'p2coin.png')
        self.p3coin = PhotoImage(file = 'p3coin.png')
        self.p4coin = PhotoImage(file = 'p4coin.png')
        self.p1empty = PhotoImage(file = 'p1empty.png')
        self.p2empty = PhotoImage(file = 'p2empty.png')
        self.p3empty = PhotoImage(file = 'p3empty.png')
        self.p4empty = PhotoImage(file = 'p4empty.png')
        self.p1portrait = None; self.p2portrait = None
        self.p3portrait = None; self.p4portrait = None
        
        self.coinlist = [self.p1coin, self.p2coin, self.p3coin, self.p4coin]
        self.emptylist = [self.p1empty, self.p2empty, self.p3empty, self.p4empty]
        self.playerportraits = [self.p1portrait, self.p2portrait,
                                self.p3portrait, self.p4portrait]
        self.character_array = {
                    'dr mario' : (45, 100), 'mario' : (125, 95),
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
  
        def back():
            self.titlescreen()


        def namelist():
            
            '''Consider making namefill a method of a datahandler class.'''
            
            print('\nTrying to fill list with names...')
            self.datahandler.cur.execute("""SELECT Name FROM basic""")
            namelist = [name[0] for name in self.datahandler.cur]
            print('Done Trying.')
            return namelist
        
            
        def playercoin(togglebutton, player):
            
            
            def move_coin(event):

                determine_character(event, player)
                self.canvas.delete('p{}box'.format(coin.slot))
                coin.lift()
                self.canvas.move('p{}coin'.format(coin.slot),
                                 event.x - 20, event.y - 20)

              
            def determine_character(event, player):

                coin_x = coin.winfo_x() + 20
                coin_y = coin.winfo_y() + 20
                
                x = portrait_width = 70; y = portrait_height = 65
                
                charflag = False
                for char in self.character_array.keys():
                    pivot = portrait_corner = self.character_array[char]
                    if coin_x >= pivot[0] and coin_x <= pivot[0] + x:
                        if coin_y >= pivot[1] and coin_y <= pivot[1] + y:
                            charflag = True
                            toon = char
                            
                if not charflag:
                    self.playerportraits[coin.slot - 1] = None
                    player.character = None
                    self.canvas.delete('p{}portrait'.format(coin.slot))
                else:
                    if player.character == toon:
                        pass
                    else:
                        player.character = toon
                        player.reportself()
                        fighter = toon
                            

                try:
                    self.playerportraits[coin.slot -1] = PhotoImage(
                        file = str(fighter) + '.png')
                    
                    self.canvas.delete('p{}portrait'.format(coin.slot))

                    portrait = Label(self, bd = 0, highlightthickness = 0,
                                     cursor = 'hand1',
                                     image = self.playerportraits[coin.slot -1])
                    self.canvas.create_window((togglebutton.winfo_x() + 86,
                                               togglebutton.winfo_y() + 98),
                                              window = portrait,
                                              tags = ('p{}portrait'.format(coin.slot),
                                                      'p{}'.format(coin.slot)))
                    self.canvas.lift('namebutton')
                except:
                    pass

            coin_origin = ((togglebutton.winfo_x() + 120,
                            togglebutton.winfo_y()))
            
            coin = Label(self, borderwidth = 0,  cursor = 'hand2',
                              image = self.coinlist[togglebutton.slot - 1])
            coin.slot = togglebutton.slot
            print('\nCreating p{} coin.'.format(coin.slot))
            coin.bind('<B1-Motion>', move_coin)
            coin.bind('<ButtonRelease-1>', lambda event:
                      determine_character(event, player))
            self.canvas.create_window(coin_origin,
                                      window = coin,
                                      tags = ('p{}coin'.format(coin.slot),
                                              'p{}'.format(coin.slot)))
         
         
        def nameselectbox(self, togglebutton, namebutton, player):
            
            
            def nameupdate(player):
            
                print('\n\n Interest 2: \nplayer.slot = {}'.format(player.slot))
                
                selectedname = namebox.get(int(namebox.curselection()[0]))
                
                dupflag = None
                for slot in range(len(self.playerlist)):
                    if self.playerlist[slot] != None:
                        print('\nplayer != none!!!\nChecking name for dup...')
                        print('player name = {}'.format(player.name))
                        if self.playerlist[slot].name == selectedname:
                                print('dup name encountered')
                                dupflag = True
                        else:
                            pass
                    else:
                        pass
                
                if dupflag == True:
                    print('DUP DETECTED')
                    namebox.itemconfig(int(namebox.curselection()[0]),
                                       {'fg' : 'red'})
                else:
                    print('NO DUP DETECTED')
                    player.name = selectedname
                    player.reportself()
                    self.canvas.delete('p{}box'.format(togglebutton.slot))
                    
                    namebutton.config(text = player.name, font = ('Helectiva', 15))
            
            
            def nameregister():
                
                name = self.newnameentry.get()
                
                print('name = {}'.format(name))
                self.newnameentry.delete(0, END)
                
                if name in self.names:
                    print('name already taken')
                    messagebox.showinfo(title = 'Duplicate Name',
                    message = 'Name already exists, pick another')
                elif name == None or name == "''":
                    pass
                else:
                    self.datahandler.cur.execute("""INSERT INTO basic VALUES 
                                                 (?, ?)""", (name, 0))
                    self.datahandler.con.commit()
                    self.canvas.delete('p{}box'.format(togglebutton.slot))
                    namebutton.config(text = name, font = ('Helectiva', 15))
              
                
            
            
            def nameentry():
                
                self.newnameentry = Entry(self, text = 'NEW NAME ENTRY',
                bd = 0, bg = 'white', fg = 'black', font = ('Arial', 12))
                self.canvas.create_window((xpos + 89, ypos + 228), 
                width = 156, height = 23,
                window = self.newnameentry, tags = ('p{}'.format(togglebutton.slot),
                                            'p{}box'.format(togglebutton.slot)))
                self.newnameentry.bind('<Return>', lambda event: nameregister())
                savebutton = Button(self, text = 'Done',
                font = ('Arial', 9),
                highlightthickness = 0,
                command = nameregister)
                self.canvas.create_window((xpos + 150, ypos + 205),
                width = 37, height = 17,
                window = savebutton, tags = ('p{}box'.format(togglebutton.slot), 'p{}'.format(togglebutton.slot)))            
             
                self.newnameentry.focus()
            
            xpos = togglebutton.winfo_x()
            ypos = togglebutton.winfo_y()
            
            self.names = namelist()
            
            namebox = Listbox(self, bg = 'black', fg = 'white',
                              font = ('Helectiva', 15, 'bold'),
                              activestyle = 'dotbox',  cursor = 'hand1',
                              selectbackground = 'green',
                              selectforeground = 'black',
                              selectmode = SINGLE, takefocus = FALSE,
                              exportselection = False)
            namebox.bind('<<ListboxSelect>>',
                         lambda event: nameupdate(player))
            self.canvas.create_window((xpos + 88, ypos + 122),
                                      window = namebox,
                                      width = 160,  height = 190,
                                      tags = ('p{}box'
                                              .format(togglebutton.slot),
                                              'p{}'
                                              .format(togglebutton.slot)))
            if len(self.names) >= 8: 
                scrollbar = Scrollbar(self, 
                                      orient = VERTICAL, width = 4,
                                      bd = 0, highlightthickness= 0,
                                      command = namebox.yview)
                namebox.config(yscrollcommand = scrollbar.set)
                self.canvas.create_window((xpos + 164, ypos + 122),
                                          window = scrollbar,
                                          height = 190,
                                          tags = ('p{}'.format(togglebutton.slot),
                                                  'p{}scroll'
                                                  .format(togglebutton.slot),
                                                  'p{}box'
                                                  .format(togglebutton.slot)))
            else:
                pass
                
            newname = TkButton(self, text = 'NEW NAME ENTRY',
            bd = 0, bg = 'black', fg = 'white', font = ('Arial', 10),
            command = nameentry)
            
            self.canvas.create_window((xpos + 88, ypos + 228), 
                                        width = 156, height = 23,
                                        window = newname, 
                                        tags = ('p{}'
                                                .format(togglebutton.slot),'p{}box'
                                                .format(togglebutton.slot)))
           
            print('\nCurrent playerlist = {}'.format(self.playerlist))
            
            for slot in range(1, len(self.playerlist) + 1):
                print('slot = {}'.format(slot))
                if self.playerlist[slot -1] != None:
                    #there's a player
                    print('Check: player name = {}'.format(player.name))
                    
            for _name in self.names:
                namebox.insert(END, _name)
            
            print('\nInterest1: \n\nPlayer call... \n\nplayer = {}\nPlayer slot = {} \nPlayer name= {}\nPlayer char= {} \n\nCall Done.'.format(player, player.slot, player.name, player.character))
            
            
            namebox.focus()
            namebox.selection_clear(namebox.index(ACTIVE))
            
            player.reportself()
            

        def playerbox(event, player):
            
            togglebutton = event.widget
            
            bleh = Label(self, cursor = 'hand1',
                         highlightthickness = 0, bd = 0,
                         image = self.emptylist[togglebutton.slot -1])
            self.canvas.create_window((togglebutton.winfo_x() + 86,
                                       togglebutton.winfo_y() + 122),
                                      window = bleh,
                                      tags = ('p{}empty'.format(togglebutton.       slot),
                                             'p{}'.format(togglebutton.slot)))
            namebutton = TkButton(self, text = 'SELECT A NAME',
                                    compound = CENTER, bd = 0, fg = 'white',
                                    font = ('Arial Black', 8),
                                    highlightthickness = 0, cursor = 'hand2',
                                    highlightbackground = 'black',
                                    image = self.nameboxpreimage)
            namebutton.bind('<Button-1>',
                            lambda event:
                            nameselectbox(self, togglebutton, namebutton, player))
            self.canvas.create_window((togglebutton.winfo_x() + 90,
                                       togglebutton.winfo_y() + 185),
                                      window = namebutton,
                                      tags = ('namebutton',
                                              'p{}'.format(togglebutton.slot)))
            togglebutton.lift()
            print('\nTrying to raise p{}coin'.format(togglebutton.slot))
            self.canvas.tag_raise('p{}coin'.format(togglebutton.slot))
            
        def buttontoggle(event):
            '''changes the image on the player toggle button'''
            
            if event.widget.var.get() == 0:
                event.widget.var.set(1)
                event.widget.config(image = self.toggleon)
                player = Player(event.widget.slot)
                player.reportself()
                print('\nCreated a player in slot {}.'.format(event.widget.slot))
                self.playerlist[event.widget.slot - 1] = player
                
                playerbox(event, player)
                playercoin(event.widget, player)
                    
            else:
                event.widget.var.set(0)
                event.widget.config(image = self.toggleoff)
                self.canvas.delete('p{}'.format(event.widget.slot))
                print('\nPlayer removed from slot {}'.format(event.widget.slot))
                self.playerlist[event.widget.slot - 1].name = None
                self.playerlist[event.widget.slot - 1].character = None
                self.playerlist[event.widget.slot - 1] = None

                
        def gamestart():
            print('\nChecking for readiness...')
            if readycheck() == True:
                print('Ready.')
                # display the next screen
                self.recordingscreen()
            
            else:
                print('\nNot ready.')
                # pop up a message box or flash the buttons/coins
                # that require action
               
        def readycheck(quiet = False):
            
            activecount = 0
            readycount = 0
            
            if not quiet:
                print('\nCurrent players: ')
                
            for player in self.playerlist:
                if player != None:
                    activecount += 1
                    if not quiet:
                        player.reportself()
                    if player.readytoplay() == True:
                        readycount += 1
            
            if not quiet:
                print('\nActive count: {}'.format(activecount))
                print('Ready count: {}/{}'
                      .format(readycount,
                                                  activecount))
                                                  
            if activecount == readycount and activecount >= 2: 
                self.readytofight.config(image = self.readyimage)
                return True
            else:
                self.readytofight.config(image = self.notreadyimage)
                return False
                
            print('\nLeaving readycheck.')
            
            
        self.playerlist= [None, None, None, None]
        
        backbutton = Button(self, cursor = 'hand2',
                            image = self.backimage, bd = 0, command = back)
        self.canvas.create_window((720, 65), window = backbutton)
        
        toggle_xpos = 90; toggle_ypos = 335
        for slot in range(1,5):
            
            toggle = BooleanVar(self)
            button = Checkbutton(self, indicatoron = False,
                                 highlightthickness = 0,
                                 bd = 0, cursor = 'hand2',
                                 image = self.toggleoff)
            button.var = toggle
            button.slot = slot
            button.bind('<Button-1>', buttontoggle)
            self.canvas.create_window((toggle_xpos, toggle_ypos),
                                      window = button,
                                      tag = 'p{}toggle'.format(slot))
            toggle_xpos += 175

        self.readyimage = PhotoImage(file = 'readytofight.png')
        self.notreadyimage = PhotoImage(file = 'notreadytofight.png')
        self.readytofight = Button(self, bd = 0, highlightthickness = 0,
                              image = self.notreadyimage,
                              command = gamestart)                      
        self.canvas.create_window((110,55), window = self.readytofight)
        
        self.canvas.bind_all('<ButtonRelease-1>', 
        lambda event: readycheck(quiet = True))
        
    
        # this next block somehow fails if placed in resourcing block at top
        self.pselectbackground = PhotoImage(file = 'playerselect.png')
        self.canvas.create_image((400,300), image = self.pselectbackground)
          
        #to do:
        #   -make coins circular
        #   -database work:
        #       -player-relative stats
        #       -decide table structure
        
            
    def recordingscreen(self):
        
        '''Possibly integrate playerselection and recording.'''
        
        print('\nDisplaying Recording Screen...')
        
        #to do:
        #   -decide input layout
        #   -layout must be created dynamically,
        #       account for number of players, names, etc. 
        

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
