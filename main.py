#QuickNotes
#A note assignment program for CLI

def codeReader(userNote):
    assignmentCode = None
    if userNote[:2] == '||':
        assignmentCode = 'notebook'

    return assignmentCode