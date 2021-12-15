import sys
Words = {'Python':'Object Oriented Programming Language','R': 'Interpreted Language','HTML':'Markup Language','Jump':'move suddenly and quickly in a specified way.'}
class Dictionaries:
  def __init__(self,Wording):
    self.Dictionary = Wording
    #self.Option = input('What option do you want? 1.Search 2.Add 3.Exit')
    #self.Option = " "
    #Options = input()
    #consider using while loops maybe as it can help with repeatablility and storage of words especially for add_words()
  
    while True:
      Option = input('What option do you want? 1.Search 2.Add 3.Exit')
      if Option == '1':
        self.find_word()
      if Option == '2':
        self.add_word()
        print(self.Dictionary)
      if Option == '3':
        sys.exit(0)
        #self.exiting()
  
  def find_word(self):
      DictWord = input('What word is it you want?')
      for key,value in self.Dictionary.items():
        DictWord = DictWord.upper()
        if DictWord == key.upper():
          print(self.Dictionary[key])
      else:
        print('Word not found')


  def add_word(self):
      NewWord = input('NewWord: ')
      NewWordDef = input('Meaning: ')

      if NewWord in self.Dictionary.keys():
        sys.exit(0)
        
      while not NewWord.isalpha():
        #if NewWord in self.Dictionary.keys():
          #  print('no')
        NewWord = input('NewWord: ')
        NewWordDef = input('Meaning: ')
      self.Dictionary.update({NewWord:NewWordDef})
      return self.Dictionary

      #if NewWord in self.Dictionary.items():
        #self.Dictionary.pop(NewWord)

  #def exiting(self):
   # sys.exit(0)


Dicting = Dictionaries(Words)
Dicting.find_word()
print(Dicting.add_word())
#Dicting.exiting()
#print(Dicting.options())

