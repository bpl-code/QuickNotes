#QuickNotes
#A note assignment program for CLI
import subprocess

class app():
    def __init__(self):
        #look for quicknote folder
        self.username = subprocess.check_output('whoami', universal_newlines=True)
        self.mainConfigFile = ''
        self.mainConfigData = ''
        self.currentSession = None
        #config varibles Defaults
        self.autoLogin = False
        self.accountName = ''
        self.quickNotesDirectory = '/home/{}/Documents/QuickNotes/'.format(self.getUsername())
        self.accountDirectory = ''
    #setup
    def setup(self):
        directoryFound = self.findHomeDirectory()
        if directoryFound == True:
            self.loadMainConfig()
        else:
            self.createMainConfig()
        self.fetchAccountDetails()
        self.createAccountSession()

    #Get Functions

    def getUsername(self):
        username = self.username.rstrip()
        return username

    def getAutoLogin(self):
        return self.autoLogin

    def getAccountName(self):
        return self.accountName
    
    def getQuickNotesDirectory(self):
        return self.quickNotesDirectory

    def getAccountDirectory(self):
        return self.accountDirectory

    #Main Functions
        
    def findHomeDirectory(self):
        #look for home directory
        result = subprocess.call(['ls', '/home/{}/Documents/QuickNotes/'.format(self.getUsername())], stderr=subprocess.DEVNULL)
        if result == 0:
            return True
        else:
            #if none build folder
            subprocess.call(['mkdir', '/home/{}/Documents/QuickNotes/'.format(self.getUsername())], stderr=subprocess.DEVNULL)
            return False
            

    def createMainConfig(self):
        self.mainConfigFile = open('/home/{}/Documents/QuickNotes/.main.conf'.format(self.getUsername()), 'w+')
        self.mainConfigFile.write("autoLogin={}\naccountName={}\nquickNotesDirectory={}".format(False,'', self.getQuickNotesDirectory()))
        #self.loadMainConfig()

    def loadMainConfig(self):
        self.mainConfigFile = open('/home/{}/Documents/QuickNotes/.main.conf'.format(self.getUsername()), 'r')
        self.mainConfigData = self.mainConfigFile.readlines()
        self.autoLogin = self.mainConfigData[0].split('=')[1]
        self.accountName = self.mainConfigData[1].split('=')[1]
        self.quickNotesDirectory = self.mainConfigData[2].split('=')[1] #Needs to be eval
        print(self.autoLogin)
        print(self.accountName)
        print(self.quickNotesDirectory)
    

    
    def fetchAccountDetails(self):
        #Checks for autolog in setting in main.conf
        accountName = ''
        if self.autoLogin == True:
            accountName = self.accountName
            self.loadUserConfig()
        else:
            #Replace this with UI call
            accountLoaded = False
            while accountLoaded == False:
                accountName = input("Enter Account Name: ")
                accountSearch = subprocess.call(['ls', '/home/{}/Documents/QuickNotes/{}/'.format(self.getUsername(), accountName) ], stderr=subprocess.DEVNULL)
                if accountSearch != 0:
                    createAccount = input("No account found! Create account? ")
                    if createAccount == 'y':
                        accountLoaded = True
                        self.accountName = accountName
                        self.accountDirectory = '{}{}'.format(self.getQuickNotesDirectory(), self.getAccountName())
                        self.createUserConfig()
                    else: 
                        accountLoaded = False
                else:
                    self.accountName = accountName
                    self.accountDirectory = '{}{}'.format(self.getQuickNotesDirectory(), self.getAccountName())
                    accountLoaded = True
                    self.loadUserConfig()

    #check for/create user config
    def loadUserConfig(self):
        accountConfig = open('{}/.{}.conf'.format(self.getAccountDirectory(), self.getAccountName()), 'r')
        #Read line of config and eval class creation line

    def createUserConfig(self):
        subprocess.call(['mkdir', '{}'.format(self.getAccountDirectory())])
        accountConfig = open('{}/.{}.conf'.format(self.getAccountDirectory() ,self.getAccountName()), "w+")
        accountConfig.write("userAccount({},{})".format(self.getAccountName(),self.getAccountDirectory()))

    def createAccountSession(self): 
        #Creates session - the part of the programs that manages notebooks and notes
        self.currentSession = userAccount(self.getAccountName(),self.getAccountDirectory(), self.getQuickNotesDirectory())

    

#UserAccount Class a class that holds notebook objects etc




    

class userAccount():
    def __init__(self, userAccountName, accountDirectory, homeDirectory):
        #Config Settings
        self.userAccountName = userAccountName
        self.homeDirectory = homeDirectory 
        self.accountDirectory = accountDirectory
        self.notebooks = []

        #Session Settings
        self.currentDirectory = accountDirectory
        self.setup()

        #App objects
        self.currentNotebook = ''
        self.currentTopic = ''
        self.currentUserInput = ''
        self.previousUserInput = '||' #Have codeReader store current command here


    #Setup and configuration functions
    def setup(self):
        #Add if loaded check and bypass create scrapbook if loaded 
        self.addNotebook('scrapeBook') #Creates the basic scrapbook where unassigned notes go 

    #get Functions
    def getUserAccountName(self):
        return self.userAccountName

    def getNotebooks(self):
        return self.notebooks

    def getCurrentNotebook(self):
        return self.currentNotebook

    def getCurrentTopic(self):
        return self.currentTopic

    def getUserInput(self):
        return self.currentUserInput

    def getPreviousInput(self):
        return self.previousInput

    def getCurrentDirectory(self):
        return self.currentDirectory
    

    #main functions
    def fetchUserInput(self):
        #Removes whitespace from beginning
        userNote = input("")
        self.userInput = userNote.lstrip()

    def codeReader(self, userNote, oldAssigmentCode):
        assignmentCodesList = {'':'blank', '||':'notebook', ';;':'topic', '..':'back', '<<':'exit', '>>':'addNotebook', ';>':'addTopic', ';/':'addSubTopic', '? ':'ignore'}
        #add try: if fail then must be a note
        try:
            assigmentCodeName = assignmentCodesList[userNote[:2]]
        except ValueError: 
            assigmentCodeName = 'ignore'

        #check for double enter
        if assigmentCodeName == oldAssigmentCode and assigmentCodeName == 'blank':
            assigmentCodeName = 'back'

        return assigmentCodeName

    def actionSelect(self, assigmentCodeName):
        #Uses the action code to call the correct function
        if assigmentCodeName == 'blank':
            action = self.addNote()
        elif assigmentCodeName == 'notebook':
            action = self.changeDirectory(self.userInput[2:].lstrip(), 'notebook') #Removes assigment code and any possible white space
        elif assigmentCodeName == 'topic':
            action = self.changeDirectory(self.userInput[2:].lstrip(), 'topic')
        elif assigmentCodeName == 'back':
            action = self.changeDirectory('..', 'back') #Triggers back function within function
        elif assigmentCodeName == 'exit':
            action = self.changeDirectory(self.notebooks[0], 'notebook')
        elif assigmentCodeName == 'addNotebook':
            action = self.addNotebook()
        elif assigmentCodeName == 'addTopic':
            action = self.addTopic()
        elif assigmentCodeName == 'addSubTopic':
            action = self.addSubTopic()
        elif assigmentCodeName == 'ignore':
            action = self.addNote(userNote=self.userInput)

        return action

#Action functions

    def changeDirectory(self, destination, directoryType):
        #Directory Type changes functionality
        if directoryType == 'back':
            directory = self.getCurrentDirectory().split('/')
            directoryBack = directory.pop()
            newDirectory = '/'.format(directoryBack)
            return newDirectory
        elif directoryType == 'exit':
            self.currentDirectory = self.homeDirectory
        elif directoryType == 'addNotebook' or directoryType == 'addTopic' or directoryType == 'addSubTopic':
            self.currentDirectory = self.homeDirectory

            



    def addNotebook(self, notebookName):
        #creates folder in a directory and creates notebook object
        newNotebookDirectory = '{}/{}'.format(self.getCurrentDirectory(), notebookName)
        subprocess.call(['mkdir', newNotebookDirectory])
        self.currentDirectory = newNotebookDirectory
        newNotebook = notebook(notebookName, self.getCurrentDirectory())
        self.notebooks.append(newNotebook)
        self.currentNotebook = newNotebook

        
        

    def addTopic(self):
        currentNoteBook = self.getCurrentNotebook() 
        currentTopic = self.getCurrentTopic()

        return 'addTopic'

    def addSubTopic(self):
        currentNoteBook = self.getCurrentNotebook() 
        currentTopic = self.getCurrentTopic()

        return 'addSubTopic'

    def addNote(self, userNote="\n"):
        currentNoteBook = self.getCurrentNotebook() 
        currentTopic = self.getCurrentTopic()
        return 'addNote'

class notebook():
    def __init__(self, notebookName, directory):
        self.notebookName = notebookName
        self.topics = []
        self.directory = ''

        #get functions

    def getNotebookName(self):
        return self.notebookName





    

