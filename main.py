#QuickNotes
#A note assignment program for CLI
import subprocess

class app():
    def __init__(self):
        #look for quicknote folder
        self.username = subprocess.check_output('whoami', universal_newlines=True)
        self.mainConfigFile = ''
        self.mainConfigData = ''
        #config varibles Defaults
        self.autoLogin = False
        self.accountName = ''
        #self.quickNotesDirectory = '/home/' + self.getUsername() + '/Documents/QuickNotes/'

    #setup
    def setup(self):
        directoryFound = self.findHomeDirectory()
        if directoryFound == True:
            self.loadMainConfig()
        else:
            self.createMainConfig()
        self.fetchUserName()

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
        self.mainConfigFile.write("autoLogin={}\naccountName={}\nquickNotesDirectory='/home/{}/Documents/QuickNotes/'".format(False,'', self.getUsername()))
        #self.loadMainConfig()

    def loadMainConfig(self):
        self.mainConfigFile = open('/home/{}/Documents/QuickNotes/.main.conf'.format(self.getUsername()), 'r')
        self.mainConfigData = self.mainConfigFile.readlines()
        self.autoLogin = self.mainConfigData[0].split('=')[1]
        self.accountName = self.mainConfigData[1].split('=')[1]
        self.quickNotesDirectory = self.mainConfigData[2].split('=')[1] #Needs to be eval
    

    #if there is config check for auto log in preference
    #ask for username
    def fetchUserName(self):
        accountName = ''
        if self.autoLogin == True:
            accountName = self.accountName
            self.loadUserConfig()
        else:
            #Replace this with UI call
            accountLoaded = False
            while accountLoaded == False:
                accountName = input("Enter Account Name: ")
                accountSearch = subprocess.call(['ls', '/home/{}/Documents/QuickNotes/{}/'.format(self.getUsername(), self.getAccountName()) ], stderr=subprocess.DEVNULL)
                if accountSearch != 0:
                    createAccount = input("No account found! Create account? ")
                    if createAccount == 'y':
                        accountLoaded = True
                        self.accountName = accountName
                        self.createUserConfig()
                    else: 
                        accountLoaded = False
                else:
                    self.accountName = accountName
                    accountLoaded = True
                    self.loadUserConfig()

    #check for/create user config
    def loadUserConfig(self):
        accountConfig = open('/home/{}/Documents/QuickNotes/{}/{}.conf'.format(self.getUsername(), self.getAccountName(), self.getAccountName()), 'r')


    def createUserConfig(self):
        subprocess.call(['mkdir', '/home/{}/Documents/QuickNotes/{}/'.format(self.getUsername(), self.getAccountName())])
        accountConfig = open('/home/{}/Documents/QuickNotes/{}/.{}.conf'.format(self.getUsername(), self.getAccountName(),self.getAccountName()), "w+")
        accountConfig.close()
    #get config set up varibles from user config and create app(user configs)


    

class userAccount():
    def __init__(self, userAccount):
        self.userAccount = userAccount
        self.accountDirectory = ''
        self.currentNotebook = ''
        self.currentTopic = ''
        self.userInput = ''
        self.previousInput = '||' #Have codeReader store current command here
        self.notebooks = [self.addNotebook('scrapeBook')]

    #Setup and configuration functions
    #add a set directory and cd to directory functions
    def establishDirectory(self):
        #
        return 0




    #get Functions
    def getUserAccount(self):
        return self.userAccount

    def getCurrentNotebook(self):
        return self.currentNotebook

    def getCurrentTopic(self):
        return self.currentTopic

    def getUserInput(self):
        return self.userInput

    def getPreviousInput(self):
        return self.previousInput

    #main functions

    def fetchUserInput(self):
        #Removes whitespace from beginning
        userNote = input("")
        self.userInput = userNote.lstrip()

    def codeReader(self, userNote, oldActionCode):
        assignmentCodesList = ['', '||', ';;', '..', '<<', '>>', ';>', ';/', '? ']
        actionCodeList = ['blank', 'notebook', 'topic', 'back', 'exit', 'addNotebook', 'addTopic', 'addSubTopic', 'ignore']
        #add try: if fail then must be a note
        try:
            assigmentNumber = assignmentCodesList.index(userNote[:2])
        except ValueError: 
            assigmentNumber = 8
        actionCodeName = actionCodeList[assigmentNumber]

        #check for double enter
        if actionCodeName == oldActionCode and actionCodeName == 'blank':
            actionCodeName = 'back'

        return actionCodeName

    def actionSelect(self, actionCodeName):
        #Uses the action code to call the correct function
        if actionCodeName == 'blank':
            action = self.addNote()
        elif actionCodeName == 'notebook':
            action = self.changeDirectory(self.userInput[2:].lstrip(), 'notebook') #Removes assigment code and any possible white space
        elif actionCodeName == 'topic':
            action = self.changeDirectory(self.userInput[2:].lstrip(), 'topic')
        elif actionCodeName == 'back':
            action = self.changeDirectory('..', 'back') #Triggers back function within function
        elif actionCodeName == 'exit':
            action = self.changeDirectory(self.notebooks[0], 'notebook')
        elif actionCodeName == 'addNotebook':
            action = self.addNotebook()
        elif actionCodeName == 'addTopic':
            action = self.addTopic()
        elif actionCodeName == 'addSubTopic':
            action = self.addSubTopic()
        elif actionCodeName == 'ignore':
            action = self.addNote(userNote=self.userInput)

        return action



    def changeDirectory(self, destination, directoryType):
        #Directory Type changes functionality
        return 'changeDirectory'


    def addNotebook(self):
        #creates folder in a directory and creates notebook object
        return 'AddNoteBook'

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





    

