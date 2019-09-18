#QuickNotes
#A note assignment program for CLI

#Remember to .lstrip() all inputs!!!!!
        
def codeReader(userNote, oldActionCode):
    assignmentCodesList = ['', '||', ';;', '..', '<<']
    actionCodeList = ['blank', 'notebook', 'topic', 'back', 'exit']
    assigmentNumber = assignmentCodesList.index(userNote[:2])
    actionCodeName = actionCodeList[assigmentNumber]

    #check for double enter
    if actionCodeName == oldActionCode && actionCodeName == 'blank':
        actionCode = 'back'

    return actionCode

    

    

