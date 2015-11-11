def datahandler(self):
        
        '''rewrite this to use sqlite3'''

        originalpath = os.getcwd()
        
        def createdatabase():

            skeleton = "'Smash Records'\n"\
                       "players = {'matt':{}, 'karel':{}}"
            os.chdir(originalpath)
            with open(skeleton, 'a+') as fout:
                fout.write('Smash Records\nTherest...')
                self.database = os.path.join(os.getcwd(),'smashstats.py')
            
        def databasesearch():
            # seach cwd for correct file, maybe use a custom extension
            # for convenience 
            # os.chdir('..') for wider search
            
            path = None
            for tuple in os.walk(os.getcwd()):
                for item in tuple[2]:
                    if item == 'smashstats.py':        
                        path = tuple[0]
                        return path
                    
        try:
            print('Importing Stats...')
            import smashstats
            print('Imported.')
        except: 
            print('Failed to import,\nsearching filesystem...')
            path = databasesearch()
            if not path:
                print('Stats not found.\n'\
                      'Creating stat database in ', originalpath)
                createdatabase()        
            else:
                print('found it')
                sys.path.append(path)
                try:
                    import smashstats
                except:
                    print('actually didnt find it? creating a new one..')
                    createdatabase()
                
        # # prompt the user to find it themselves if autosearch fails or
        # # create a new database
        # # set a flag for database: exists / doesn't exist?
        # # import the records for player initialization and display purposes
