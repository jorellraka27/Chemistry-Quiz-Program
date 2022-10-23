import random

import os
import os.path
#menu inspiration from numeracybuilder.py
#(group) menu
def m2():
 
 print("\n")
 menu2 = """
Element's group menu
------------------------------------
Please select an option below:
1. Element's group list
2. Finding element's group
3. Finding element's group (quiz)
4. Exit
------------------------------------"""
 print(menu2)
 s2 = input('Enter your selection [1 - 4]:')
 if(s2 == '1'):
        m21()
 elif(s2 == '2'):
       m22()
 elif(s2 == '3'):
     m23()
 elif(s2 == '4'):
       main()
 else:
     print('invalid option, try')
     m2()


#displaying list inspiration from grok learning
#element group list (group) 
def m21():
 print("\n")

 alkalimetal = ["lithium","sodium","potasium", "rubidium","cesium", "francium"]
 alkalineearth = ["beryllium" , "magnesium" , "calcium" , "strontium", "barium", "radium"]
 transitionmetal = ["scandium","titanium","vanadim","chromium","manganese","iron","cobalt","nickel","copper","zinc","yttrium","zirconium","platinum","gold","mercury","rutherfordium","dubnium","seaborgium","bohrium","hassium","meitnerium","ununbium","niobium","iridium","molybdenum","technetium","ruthenium","rhodium","palladium","silver","cadmium","hafnium","tantalum","tungsten","rhenium","osmium"]
 basicmetal = ["aluminum","gallium","indium","tin","thallium","lead","bismuth","ununtrium"]
 semimetal = ["boron","silicon","germanium","arsenic","antimony","tellurium","polonium"]
 nonmetal = ["hydrogen","carbon","nitrogen","oxygen","phosphorus","sulfur","selenium"]
 halogen = ["fluorine","chlorine","bromine","iodine","astatine"]
 noblegas = ["helium","neon","argon","krypton","xenon","radon","oganesson"]
 lanthanide = ["lanthanum","Cerium ","Praseodymium","Neodymium","Promethium","Samarium","Europium ","Gadolinium","Terbium","Dysprosium ","Holmium ","Erbium ","Thulium","Ytterbium","Lutetium"]
 acticide= ["actinium","thorium","protactinium","uranium","neptunium","plutonium","americium","curium","berkelium","californium","einsteinium","fermium","mendelevium","nobelium","lawrencium"]
 
 menu21 = """

Please select an option below:
1. alkalimetal
2. alkalineearth
3. transitionmetal
4. basicmetal
5. semimetal
6. nonmetal
7. halogen
8. noblegas
9. lanthanide
10. acticide
11. Exit
-------------------------------------------------------"""
 print(menu21)
 s21 = input('Enter your selection [1 - 5]:')
 no= -1#variable that calls the strings(element) in the list
 nl=0 #show the number order of the elements displayed
 if s21 == "1":
   print("alkalimetal:")
   for el in alkalimetal:
    no=no+1
    nl=nl+1
    print(nl,alkalimetal[no])
    
 elif s21 =="2":
   print("alkalineearth:")
   for el in alkalineearth:
    no=no+1
    nl=nl+1
    print(nl,alkalineearth[no])
    
 elif s21 =="3":
   print("transitionmetal:")
   for el in transitionmetal:
    no=no+1
    nl=nl+1
    print(nl,transitionmetal[no])
 elif s21 =="4":
   print("basicmetal:")
   for el in basicmetal:
    no=no+1
    nl=nl+1
    print(nl,basicmetal[no])
 elif s21 =="5":
   print("semimetal:")
   for el in semimetal:
    no=no+1
    nl=nl+1
    print(nl,semimetal[no])
 elif s21 =="6":
   print("nonmetal:")
   for el in nonmetal:
    no=no+1
    nl=nl+1
    print(nl,nonmetal[no])
 elif s21 =="7":
   print("halogen:")
   for el in halogen:
    no=no+1
    nl=nl+1
    print(nl,halogen[no])
 elif s21 =="8":
   print("noblegas:")
   for el in noblegas:
    no=no+1
    nl=nl+1
    print(nl,noblegas[no])
 elif s21 =="9":
   print("lanthanide:")
   for el in lanthanide:
    no=no+1
    nl=nl+1
    print(nl,lanthanide[no])
 elif s21 =="10":
   print("acticide:")
   for el in acticide:
    no=no+1
    nl=nl+1
    print(nl,acticide[no])
 elif s21 =="11":
    m2()
 else:
  print(" invalid option")
 print("\n")
 m21()

#element finding group (group) 
def m22():
 print("\n")

 alkalimetal = {"lithium","sodium","potasium", "rubidium","cesium", "francium"}
 alkalineearth = {"beryllium" , "magnesium" , "calcium" , "strontium", "barium", "radium"}
 transitionmetal = {"scandium","titanium","vanadim","chromium","manganese","iron","cobalt","nickel","copper","zinc","yttrium","zirconium","platinum","gold","mercury","rutherfordium","dubnium","seaborgium","bohrium","hassium","meitnerium","ununbium","niobium","iridium","molybdenum","technetium","ruthenium","rhodium","palladium","silver","cadmium","hafnium","tantalum","tungsten","rhenium","osmium"}
 basicmetal = {"aluminum","gallium","indium","tin","thallium","lead","bismuth","ununtrium"}
 semimetal = {"boron","silicon","germanium","arsenic","antimony","tellurium","polonium"}
 nonmetal = {"hydrogen","carbon","nitrogen","oxygen","phosphorus","sulfur","selenium"}
 halogen = {"fluorine","chlorine","bromine","iodine","astatine"}
 noblegas = {"helium","neon","argon","krypton","xenon","radon","oganesson"}
 lanthanide = {"lanthanum","Cerium ","Praseodymium","Neodymium","Promethium","Samarium","Europium ","Gadolinium","Terbium","Dysprosium ","Holmium ","Erbium ","Thulium","Ytterbium","Lutetium"}
 acticide= {"actinium","thorium","protactinium","uranium","neptunium","plutonium","americium","curium","berkelium","californium","einsteinium","fermium","mendelevium","nobelium","lawrencium"}

 print("press enter(without putting input) to exit")

 print("\n")
 a= input("enter element name: ")

 while a:#allow the user to exit by pressing enter without input

  if a in alkalimetal:
      print("alkali metal")
  elif a in alkalineearth:
      print("alkaline earth")

  elif a in transitionmetal:
      print("transition metal")

  elif a in basicmetal:
      print("basic metal")
 
  elif a in semimetal:
      print("semimetal")

  elif a in nonmetal:
      print("nonmetal")

  elif a in halogen:
      print("halogen")
  elif a in noblegas:
      print("noble gas") 
  elif a in lanthanide:
      print("lanthanide")
  elif a in acticide:
      print("acticide")
  else:
      print("No element")
  a= input("enter element formula: ")
 
 main()
#group quiz
def m23():

 
 print("\n")

 alkalimetal = ["lithium","sodium","potasium", "rubidium","cesium", "francium"]
 alkalineearth = ["beryllium" , "magnesium" , "calcium" , "strontium", "barium", "radium"]
 transitionmetal = ["scandium","titanium","vanadim","chromium","manganese","iron","cobalt","nickel","copper","zinc","yttrium","zirconium","platinum","gold","mercury","rutherfordium","dubnium","seaborgium","bohrium","hassium","meitnerium","ununbium","niobium","iridium","molybdenum","technetium","ruthenium","rhodium","palladium","silver","cadmium","hafnium","tantalum","tungsten","rhenium","osmium"]
 basicmetal = ["aluminum","gallium","indium","tin","thallium","lead","bismuth","ununtrium"]
 semimetal = ["boron","silicon","germanium","arsenic","antimony","tellurium","polonium"]
 nonmetal = ["hydrogen","carbon","nitrogen","oxygen","phosphorus","sulfur","selenium"]
 halogen = ["fluorine","chlorine","bromine","iodine","astatine"]
 noblegas = ["helium","neon","argon","krypton","xenon","radon","oganesson"]
 lanthanide = ["lanthanum","Cerium ","Praseodymium","Neodymium","Promethium","Samarium","Europium ","Gadolinium","Terbium","Dysprosium ","Holmium ","Erbium ","Thulium","Ytterbium","Lutetium"]
 acticide= ["actinium","thorium","protactinium","uranium","neptunium","plutonium","americium","curium","berkelium","californium","einsteinium","fermium","mendelevium","nobelium","lawrencium"]
# To collect all the strings in all of the list into one list
 totel= alkalimetal + alkalineearth + transitionmetal + basicmetal+ semimetal+ nonmetal+halogen +lanthanide +acticide

 l = """
 1. alkalimetal
 2. alkalineearth
 3. transitionmetal
 4. basicmetal
 5. semimetal
 6. nonmetal
 7. halogen
 8. noblegas
 9. lanthanide
 10. acticide
 Enter group number:"""
 q2 = 0
 p= 0
 nq=0
 while q2 < 9:
  nq=nq+1
  c = random.randint(0,104)#getting random number to display random element base on their array
  q2 = q2+1
  print(str(nq)+".) "+"which group",totel[c],"belongs to?")
  answ = input(l)


  if answ == "1":
   if totel[c] in alkalimetal:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "2":
   if totel[c] in alkalineearth:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "3":
   if totel[c] in transitionmetal:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "4":
   if totel[c] in basicmetal:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "5":
   if totel[c] in semimetal:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "6":
   if totel[c] in nonmetal:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "7":
   if totel[c] in halogen:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  elif answ == "8":
   if totel[c] in noblegas:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")

  elif answ == "9":
   if totel[c] in lanthanide:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")

  elif answ == "10":
   if totel[c] in acticide:
      print("your correct")
      p = p + 1
   else:
      print("your wrong")
  else:
      print("invalid option")
 del totel[c] 
 name2= input("what is your name?")
 print("nice try",name2,"score is",str(p)+"/10")

 fscore = open("scores2.txt","a")#create a text file for storing data
 fscore.write(str(p)+"\n")#entering the score into the text file
 fscore.close()
 lname = open("name2.txt","a")
 lname.write(str(name2)+"\n")
 lname.close()
 con= input("press y to restart/press space to exit")
 if con.lower() == "y":
    m23()
    
 else:
   m2()

#(quiz)
 #feedback: hard to read the code(ira)(classmate)

def m1():
 import random
 print("\n")

 point=0
 q=-1
 mq=["The tiniest particle is: ","An atom have a proton, nuetron and: ","The body of theory which explains the physical properties of matter in terms of the motions of its constituent particles: ","State where its particle far apart and move freely: ","State where its particle are close together (touching) but they are able to move/slide/flow past each other: ","The state where particles are pack together, do not move, only vibrate: ","The number of electrons in the outer shell is called: ","In the periodic table, atoms with the same valence are place in one: ","Bonds between metal and non metal: ","Bonds between non metal and non metal: "]
 ma=["atom","electron","kinetic theory","gas","liquid","solid","valence","group","ionic bond","covalent bond"]
 i=0
 j=9
 n=0
 while q < 9:
    b = random.randint(i,j)
    j=j-1
    q = q+1
    n= n+1
    print("question",n)
    a = input(mq[b])
   
    if a.lower() == ma[b]:
     
     print('well done')
     print("\n")
     point = point+1
     del mq[b]#we dont want any question to repeat, so we remove the answered questions off the list
     del ma[b]
#deleting item in list inspiration from https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python
    else:
     print('correct answer is '+ma[b]+' ,try again!!!')
     print("\n")
     

     del mq[b]
     del ma[b]
 name= input("what is your name?")
 print("nice try",name," your score is",str(point)+"/10")
 lscore = open("scores1.txt","a")
 lscore.write(str(point)+"\n")
 lscore.close()
 lname = open("name1.txt","a")
 lname.write(str(name)+"\n")
 lname.close()
 
 con= input("press y to restart/press space to exit")
 if con.lower() == "y":
    m1()
    
 else:
    main()

def m3():
 help =""" About Chemistry program 1.0

Welcome to chemistry program 1.0, this program is simply built to help senior
students to gain basic knowledge of the chemistry subject and also remember
each elements’group in the periodic table.



This program is divided into 2 sections:
the basic knowledge quiz and Finding elements’ group section.







Basic knowledge quiz

The basic knowledge skill helps user to test their knowledge on chemistry.
Ten random questions will appeared on the screen, one at a time. Then user will need
to enter the correct answer with correct spelling, without worrying about the
cases. After completing the 10 questions, user’s score will be displayed on the screen.









Finding elements’ group

Users can do 3 things in the element’s group section which are
1. Element's group list
2. Finding element's group (guide)
3. Finding element's group (quiz)






Element's group list

The element’s group list section will show the selections of
groups of elements that the user is interested in. The program
will then displayed the list of elements in the selected group.




Finding element's group (guide)

Finding element's group (guide) section allows user to gain
information on which group an element belongs to efficiently.
Just by entering an element name in the program, the program will
then display the group name of the entered element.






Finding element's group (quiz)

Finding element's group (quiz) helps user to memorise
which group elements belongs to by testing the with 10 random questions.
The program will display one random element, then user need to select the
correct group the displayed element belongs to.
A score will be given once the user complete the test."""
 
 print(help)
 helpinput= input("press space to exit")
 if input :
     main()
 else:
     m3()
#scoremenu
#saving score inspiration from numeracyBuilder.py and https://stackoverflow.com/questions/4450144/easy-save-load-of-data-in-python
def m4():
 scoremenu = """

-------------------------------------------------------
Please select an option below:

1. Basic knowledge quiz 
2. Finding element's group
3. Exit
-------------------------------------------------------"""
 print(scoremenu)
 scorein = input('Enter your selection [1 - 2]:')
 if(scorein == '1'):
        s1()
 elif(scorein == '2'):
       s2()
 elif(scorein == '3'):
       main()

 else:
     print('invalid option, try again')
     m4()

#Basic knowledge quiz scores
def s1():
 show= open("scores1.txt").read().split('\n')# collect the strings from the file and converting them to list
 name1= open("name1.txt").read().split('\n')
 nl=0
 no=-1
 print("Score History in Basic knowledge quiz")
 for sc in show:
   no=no+1
   nl=nl+1
   print(str(nl)+".",name1[no],":",show[no])

 s1input= input("press space to exit")
 if input :
     m4()
 else:
     s1()

#Finding element's group scores

def s2():
 show2= open("scores2.txt").read().split('\n')#saving score inspiration from numeracyBuilder.py and https://stackoverflow.com/questions/4450144/easy-save-load-of-data-in-python

 name2= open("name2.txt").read().split('\n')
 no=-1
 nl=0
 print("Score History in Basic knowledge quiz")
 for sc in show2:
   no=no+1
   nl=nl+1
   print(str(nl)+".",name2[no],":",show2[no])
 s1input= input("press space to exit")
 if input :
     m4()
 else:
     s1()
#main menu
def main():
 print("\n")

 menu = """
Main Menu
-------------------------------------------------------
Please select an option below:

1. Basic knowledge quiz
2. Finding element's group
3. Help
4. score
-------------------------------------------------------"""
 print(menu)
 s = input('Enter your selection [1 - 4]')

 if(s == '1'):
        m1()
 elif(s == '2'):
       m2()
 elif(s == '3'):
       m3()
 elif(s == '4'):
       m4()
 else:
     print('invalid option, try again')
     main()
print('Welcome to Chemistry program 1.0')
main()
