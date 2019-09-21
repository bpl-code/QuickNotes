#QuickNotes
#A note assignment program for CLI
import os

class app():
    def __init__(self, userAccount):
        self.userAccount = userAccount #Create a folder based on this and save config file
        self.accountDirectory = ''
        self.currentNotebook = ''
        self.currentTopic = ''
        self.userInput = ''
        self.previousInput = '||' #Have codeReader store current command here
        self.notebooks = [self.addNotebook('scrapeBook')]

    #Setup and configuration functions
    #add a set directory and cd to directory functions



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





    

