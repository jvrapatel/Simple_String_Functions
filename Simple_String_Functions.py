print ("\n")
print ("MINUSCULE OR MAJUSCULE CASE")

phrase = "Liverpool Football Club"
print (phrase.lower())
print (phrase.upper())
print ("\n")

print ("CHECK THE CASE OF SENTENCE")
phrase = ("liverpool")
print(phrase.isupper())
print(phrase.islower())
print ("\n")

print ("USING TWO FUCTIONS")
phrase = ("liverpool")
print (phrase.upper().isupper())
print ("\n")

print ("LENGTH OF STRING")
phrase = "Liverpool Football Club"
print (len(phrase))
print ("\n")

print ("FIND AN INDEX")
phrase = ("liverpool")
print (phrase[2])
print (phrase.index("i"))
print(phrase.replace("liverpool", "You'll Never Walk Alone"))
