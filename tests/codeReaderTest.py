import main

#Test new assignment
print(main.codeReader("||notebook", None))

#Test duplicate assignment of non-enterKey
print(main.codeReader("||notebook", "||textbook"))

#Test duplicate enterKey
print(main.codeReader('', 'blank'))

#Test enterKey with non enterkey
print(main.codeReader('', "||"))

