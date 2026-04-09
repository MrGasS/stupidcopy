#STUPIDCOPY 0.1 (MOSTLY INCOMPLETE RIGHT NOW)
#S.E.M. Magrì
#https://github.com/MrGasS
#I'M NOT RESPONSIBLE OF ANYTHING IN CASE YOUR COMPUTER BLOWS UP LIKE YO MAMA WHEN SHE'S WITH ME
#latest update 9/10/2025

#import os #UNCOMMENT FOR FIREWORKS AND OTHER EXPLOSIONS
def pathchanger(): #questa funzione permette di cambiare le origini e le destinazioni, include processo di revisione
    def reviewpath():
        print(f'(O)rigin: {pathdict["dirpathorig"]}\n(D)estination: {pathdict["dirpathdest"]}\n{chosenopt} {pathdict["filepath"] if chosenopt == '(F)ile: ' else  'Type S or F for subdirectories or a single file.'}')
        reviewpaths = str(input(f'Are you sure about your choices? (Y)es/O/D/{'F' if chosenopt == '(F)ile: ' else 'S'}\n'))
        if len(reviewpaths) != 0 and reviewpaths.upper() == 'O':
            insertorigdir()
        if len(reviewpaths) != 0 and reviewpaths.upper() == 'D':
            insertdestdir()
        if len(reviewpaths) != 0 and reviewpaths.upper() == 'S' or reviewpaths.upper() == 'F':
            insertoptfile()
        if len(reviewpaths) != 0 and reviewpaths.upper() == 'Y':
            choicemaker()
        else:
            print("Please, make a choice\n")
            reviewpath()
    def insertorigdir(): #funzione per l'inserimento dell'origine
        origdir = str(input('\nDirectory origin path: '))
        pathdict.update({'dirpathorig':f'"{origdir}"'})
    def insertdestdir(): #funzione per l'inserimento della destinazione
        destdir = str(input('Directory destination path: '))
        pathdict.update({'dirpathdest':f'"{destdir}"'})
    def insertoptfile(): #funzione per l'inserimento dei file che ritorna chosenopt
        optfile = str(input('If you want to copy a single file, type filename+extension, otherwise left blank: '))
        if len(optfile) != 0:
            pathdict.update({'filepath':f'"{optfile}"'})
            chosenopt = '(F)ile: '
        else:
            subdirquest = str(input(f'Do you want to copy subdirectories? Y/N\n'))
            if len(subdirquest) != 0 and subdirquest.upper() == 'Y':
                    subdirquest2 = str(input(f'Including empty ones? Y/N\n'))
                    if len(subdirquest2) != 0 and subdirquest2.upper() == 'Y':
                        pathdict.update({'filepath':'/e'})
                        chosenopt = 'Copy (S)ubdirectories: yes, including empty ones.'
                    elif len(subdirquest2) != 0 and subdirquest2.upper() == 'N':
                        pathdict.update({'filepath':'/s'})
                        chosenopt = 'Copy (S)ubdirectories: yes, excluding empty ones.'
                    else:
                        print("Okay, I won't include any subdirectory.\n")
                        chosenopt = ''
            else:
                print("Okay, I won't include any subdirectory.\n")
                chosenopt = ''
        return chosenopt
    insertorigdir()
    insertdestdir()
    chosenopt = insertoptfile()
    reviewpath()

def optchanger(): #questa funzione permette di cambiare le opzioni di copia, include processo di revisione
    #ANCORA DA SCRIVERE
    def reviewopt():
        print('1null')
        reviewopts = str(input(f'Are you sure about your choices? ODSFY\n'))
        if len(reviewopts) != 0 and reviewopts.upper() == 'O':
            print('nullO')
        if len(reviewopts) != 0 and reviewopts.upper() == 'D':
            print('nullD')
        if len(reviewopts) != 0 and reviewopts.upper() == 'S' or reviewopts.upper() == 'F':
            print('nullSF')
        if len(reviewopts) != 0 and reviewopts.upper() == 'Y':
            print('nullY')
        else:
            print("Please, make a choice\n")
            reviewopt()
    reviewopt()

def choicemaker():
    while True:
        currentstring = f'robocopy {pathdict['dirpathorig']} {pathdict['dirpathdest']} {pathdict['filepath']}'
        print(f'\nCurrent string:\n{currentstring}')
        promptchoice= str(input("\nWhat do you want to do?\n1. Change paths\n2. Change options\n3. Run Robocopy\n4. Exit\nYour choice: "))
        if promptchoice != 0:
            if promptchoice[:1] == '1':
                userwantstocopyafile = pathchanger()
            if promptchoice[:1] == '2':
                optchanger()
            if promptchoice[:1] == '3':
                runchoice = str(input(f'\nYour current robocopy string is \n{currentstring}\nAre you sure to proceed? Y/N\n'))
                if len(runchoice) != 0:
                    if runchoice[:1].upper() == 'Y':
                        print(f'\n||||||||||||||||||||||\nESECUZIONE FITTIZIA DI \n{currentstring}\n||||||||||||||||||||||\n')#command check
                        #os.system(currentstring)#UNCOMMENT FOR FIREWORKS AND OTHER EXPLOSIONS
            if promptchoice[:1] == '4':
                exit()

def mainloop():
    print("\nStupidcopy v0.1\nA simple robocopy assistant\nWritten by MrGasS a.k.a. S.E.M.M. in 2025\n")
    choicemaker()

pathdict = {'dirpathorig':'>>PRESS 1 TO','dirpathdest':'DEFINE PATHS<<','filepath':''}
optdict = {'fileopt':'>>PRESS 2 TO','diropt':'DEFINE OPTIONS<<'}
mainloop()