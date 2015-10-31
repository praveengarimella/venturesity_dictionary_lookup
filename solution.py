# Praveen Garimella's solution to the dictionary problem posted on venturesity code challenge.
# TODO: The solution is naive.

def lookup(word):
  with open ("wordsEn.txt", "r") as myfile:
      data=myfile.read()
      if data.find(word + "\r\n") == -1:
        return False
      return True

word = raw_input('Enter your input:')
if lookup(word):
  print "String is a valid word."
else:
  print "The string is not a valid word."