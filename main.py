points = 0


def scene1():
  import time
  global points

  print("You are MILO, the best big orange kitty ever. Your favorite things in the whole world are snacks, naps, and cuddles with your human JULIA. Today you awake from your nap to find that your food ball was empty and your human JULIA is no where to be seen! No time to waste! Let's start looking for JULIA (and maybe some food too)") 
  time.sleep(5)
  print("\n You walk into the BEDROOM and look around the room. You see your scratcher and a fishy toy with catnip. It's no time for games though! \n It doesn't seem like there's any good snacks around. Just JULIA's crummy M&Ms. No JULIA either. \n You do notice a tan lump on the bed. How should you approach it?") 
  time.sleep(5)
  print("\n Enter: CAUTIOUSLY or POUNCE?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='CAUTIOUSLY'):
      print("\n You cautiously approach the lump on the bed. When you get close you realize its your kitty friend IGGY taking a nap. You gently lick the top of his head and he stretches, sticking out his little paws. He gives you some licks back and jumps off the bed. ")
      time.sleep(5)
      print("\n JULIA isn't here so let's check the next room.")
      ans = 'correct'
      points += 1
    elif (choice.upper()=='POUNCE'):
      print("\n You swifty leap on to the bed right next to the lump. Suddenly the lump jumps up and hisses! Before you know it you're tangled up with another ball of fur and you and the mystery lump begin thrashing around the bed. All the freshly cleaned pillows are knocked down in front of the litter box. The mystery lump turned out to be your friend IGGY that you scared.")
      time.sleep(5)
      print("\n JULIA isn't here so let's check the next room.")
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(3)


def scene2():
  import time
  global points

  print("\n You enter JULIA's OFFICE. The sun is shining on her sparkly nail polishes reflecting all 3 colors of the rainbow onto the wall. So pretty. Still no signs of JULIA.") 
  time.sleep(5)
  print("\n While you're scratching the post of your cat tree you notice a curtain start to move. Suddenly something leaps out out from it! \n Quick! How do you react? ") 
  time.sleep(5)
  print("Enter: FLEE or HOLD?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='HOLD'):
      print("\n Whatever was behind the curtain leaps towards you! But you're a big kitty and you're not afraid of anything! (Well, sometimes.) The creature stops right in front of you and starts sniffing you. It's just IGGY's mommy, YUFFIE. You sniff YUFFIE back and give her a headbutt. She must be in a good mood because she reciprocates! ")
      time.sleep(5)
      print("Still no JULIA though. Let's head downstairs and look.")
      ans = 'correct'
      points += 1
    elif (choice.upper()=='FLEE'):
      print("\n Whatever was behind the curtain leaps towards you! You get scared and try to flee, but get caught! The creature bites your butt as you try to escape. Ouch! You look back and it's IGGY's mommy, YUFFIE. After she bites you, YUFFIE runs under the bed and hides. She's such a grump. ")
      time.sleep(5)
      print("Still no JULIA though. Let's head downstairs and look.")
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(5)
  

def scene3():
  import time
  global points

  print("\n You head downstairs to the LIVING ROOM. You try to call out to JULIA but no answer. How rude. You see your empty food ball next to a lone piece of cat food. You rush over to gobble it up! Now you're really hungry." ) 
  time.sleep(5)
  print("\n JULIA usually has something yummy on her dinner tray... Should you go check it out? ") 
  time.sleep(3)
  print("Enter: SEARCH or IGNORE?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='IGNORE'):
      print("\n You take a look at the tray from a different angle and see a lot of clutter, but no snacks. You decide against jumping up on the tray. You don't want to knock everything off and make a loud, scary noise! ")
      time.sleep(5)
      print("Too bad you still can't find JULIA. Maybe she'll be in the next room?")
      ans = 'correct'
      points += 1
    elif (choice.upper()=='SEARCH'):
      print("\n Without a second thought you jump up onto the tray. Unfortunately, you forgot that you're too heavy and the tray flips over instantly! JULIA's PS5 controller and T.V. remote slam on the floor and the remote slides under the couch that you safely land on. Lucky! JULIA wont be too happy when she can't find her stuff though... ")
      time.sleep(5)
      print("Too bad you still can't find JULIA. Maybe she'll be in the next room?")
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(5)

def scene4():
  import time
  global points

  print("\n Still hungry, you decide to search the KITCHEN for some snacks. You find a few more pieces of food along the way and gobble them up. Good thing you're a messy eater or you might have starved to death! When you enter the KITCHEN you catch an intoxicating scent. You know it can only be one thing. Chicken nuggs!!!") 
  time.sleep(5)
  print("\n You spy the box on the counter, half open revealing those tasty, meaty bites. You know JULIA would be upset if she found out you stole some. But they smell so good! Should you jump up and eat them or leave them be? ") 
  time.sleep(5)
  print("Enter: DISREGARD or PILLAGE?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='DISREGARD'):
      print("\n You know you aren't supposed to go up on the counter to steal food, and you're a good kitty. You decide it's not worth stealing any nuggs and leave them alone. Maybe JULIA will reward you for being so well behaved when you finally find her. She loves when her kitties are being good. ")
      time.sleep(5)
      print("It doesn't seem like JULIA is anywhere around the house... There's no where else to look so you sit by the back door and look out, waiting. Hopefully you see JULIA soon.")
      time.sleep(5)
      ans = 'correct'
      points += 1
    elif (choice.upper()=='PILLAGE'):
      print("\n You know you aren't supposed to go up on the counter to steal food, but nuggs are worth being a naughty kitty! After hopping onto the counter you begin working on getting the box open. It's a bit of a struggle, but finally you get it open all the way! When you try to pull one out you accidentally knock all the rest on the floor. Oh well. ")
      time.sleep(5)
      print("You start to eat the nugg but realize it's got breading all over it. Gross! You eat half the nugg and leave the rest on the counter. ")
      time.sleep(5)
      print("It doesn't seem like JULIA is anywhere around the house... There's no where else to look so you sit by the back door and look out, waiting. Hopefully you see JULIA soon.")
      time.sleep(5)
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(3)



def scene5():
  import time
  
  range1 = range(2, 4, 1)
  
  if points <= 1:
    print('You stare out the backdoor waiting forever for JULIA. Finally, you hear the back gate creek open and see JULIA and NICK step through. NICK opens the door and JULIA steps in. \n "Were you all good kities?" JULIA asks.')
    time.sleep(5)
    print("JULIA looks around the house and sees the mess that was made and isn't happy. She looks down at you and says ")
    print('"MILO, I am very disappointed in you. You were very bad today."')
    time.sleep(5)
    print('JULIA lets out a brief sigh...') 
    time.sleep(5)
    print('\n "But I still love you my naughty boy..." \n JULIA picks you up and gives you a big kiss on the head. \n THE END')
  
  
  elif points in range1:
    print('You stare out the backdoor waiting a long while for JULIA. Finally, you hear the back gate creek open and see JULIA and NICK step through. NICK opens the door and JULIA steps in. \n "Were you all good kities?" JULIA asks.')
    time.sleep(5)
    print("JULIA looks around the house and smiles. She looks down at you and says ")
    print('"You were a good boy today, werent you MILO?"')
    time.sleep(5)
    print('JULIA picks you up and gives you a big kiss on the head.') 
    time.sleep(5)
    print('\n "I love you my big boy." \n JULIA grabs a bag of treats and gives you a yummy piece of salmon. Now you have your JULIA and snacks! Good job! \n THE END')
  
  
  elif points == 4:
    print('You stare out the backdoor waiting a short while for JULIA. Finally, you hear the back gate creek open and see JULIA and NICK step through. NICK opens the door and JULIA steps in. \n "Were you all good kities?" JULIA asks.')
    time.sleep(5)
    print("JULIA looks around the house and smiles. She looks down at you and says ")
    print('"You were a very good kitty MILO! Such a good boy!"')
    time.sleep(5)
    print('JULIA picks you up and gives you a big kiss on the head and squeezes you tight.') 
    time.sleep(5)
    print('\n "I love you my big boy. You are the best kitty. \n JULIA grabs 3 bowls and a packet of wet food treats. You, IGGY, and YUFFIE all get delicious pumpkin and chicken treats for being so good while JULIA and NICK were away. What a good day; you are a very happy and content cat. \n THE END')

    
  


ans2 = 'incorrect'
def game():
  global ans2
  while ans2 == 'incorrect':
    scene1()
    scene2()
    scene3()
    scene4()
    scene5()
    print('Play Again? YES or NO')
    choice2 = input()
    if (choice2.upper() == 'YES'):
      ans2 = 'incorrect'
    elif (choice2.upper() == 'NO'):
      ans2 == 'correct'
      print('Fin.')
      break
    else:
      print("\n Please enter valid choice from above")

#def hub():
  anchor = 'INCORRECT'
  print(f'Which room do you want to search? ', (rooms) )
  selc = (input().upper())

  while anchor == 'INCORRECT':
    if selc == 'BEDROOM':
      anchor == 'CORRECT'
      scene1()
    elif selc == 'OFFICE':
      anchor == 'CORRECT'
      scene2()
    elif selc == 'LIVING ROOM':
      anchor == 'CORRECT'
      scene3()
    elif selc == 'KITCHEN':
      anchor == 'CORRECT'
      scene4
    else:
      print('Select a valid choice')

game()













points = 0


def scene1():
  import time
  global points

  print("You are MILO, the best big orange kitty ever. Your favorite things in the whole world are snacks, naps, and cuddles with your human JULIA. Today you awake from your nap to find that your food ball was empty and your human JULIA is no where to be seen! No time to waste! Let's start looking for JULIA (and maybe some food too)") 
  time.sleep(5)
  print("\n You walk into the BEDROOM and look around the room. You see your scratcher and a fishy toy with catnip. It's no time for games though! \n It doesn't seem like there's any good snacks around. Just JULIA's crummy M&Ms. No JULIA either. \n You do notice a tan lump on the bed. How should you approach it?") 
  time.sleep(5)
  print("\n Enter: CAUTIOUSLY or POUNCE?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='CAUTIOUSLY'):
      print("\n You cautiously approach the lump on the bed. When you get close you realize its your kitty friend IGGY taking a nap. You gently lick the top of his head and he stretches, sticking out his little paws. He gives you some licks back and jumps off the bed. ")
      time.sleep(5)
      print("\n JULIA isn't here so let's check the next room.")
      ans = 'correct'
      points += 1
    elif (choice.upper()=='POUNCE'):
      print("\n You swifty leap on to the bed right next to the lump. Suddenly the lump jumps up and hisses! Before you know it you're tangled up with another ball of fur and you and the mystery lump begin thrashing around the bed. All the freshly cleaned pillows are knocked down in front of the litter box. The mystery lump turned out to be your friend IGGY that you scared.")
      time.sleep(5)
      print("\n JULIA isn't here so let's check the next room.")
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(3)


def scene2():
  import time
  global points

  print("\n You enter JULIA's OFFICE. The sun is shining on her sparkly nail polishes reflecting all 3 colors of the rainbow onto the wall. So pretty. Still no signs of JULIA.") 
  time.sleep(5)
  print("\n While you're scratching the post of your cat tree you notice a curtain start to move. Suddenly something leaps out out from it! \n Quick! How do you react? ") 
  time.sleep(5)
  print("Enter: FLEE or HOLD?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='HOLD'):
      print("\n Whatever was behind the curtain leaps towards you! But you're a big kitty and you're not afraid of anything! (Well, sometimes.) The creature stops right in front of you and starts sniffing you. It's just IGGY's mommy, YUFFIE. You sniff YUFFIE back and give her a headbutt. She must be in a good mood because she reciprocates! ")
      time.sleep(5)
      print("Still no JULIA though. Let's head downstairs and look.")
      ans = 'correct'
      points += 1
    elif (choice.upper()=='FLEE'):
      print("\n Whatever was behind the curtain leaps towards you! You get scared and try to flee, but get caught! The creature bites your butt as you try to escape. Ouch! You look back and it's IGGY's mommy, YUFFIE. After she bites you, YUFFIE runs under the bed and hides. She's such a grump. ")
      time.sleep(5)
      print("Still no JULIA though. Let's head downstairs and look.")
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(5)
  

def scene3():
  import time
  global points

  print("\n You head downstairs to the LIVING ROOM. You try to call out to JULIA but no answer. How rude. You see your empty food ball next to a lone piece of cat food. You rush over to gobble it up! Now you're really hungry." ) 
  time.sleep(5)
  print("\n JULIA usually has something yummy on her dinner tray... Should you go check it out? ") 
  time.sleep(3)
  print("Enter: SEARCH or IGNORE?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='IGNORE'):
      print("\n You take a look at the tray from a different angle and see a lot of clutter, but no snacks. You decide against jumping up on the tray. You don't want to knock everything off and make a loud, scary noise! ")
      time.sleep(5)
      print("Too bad you still can't find JULIA. Maybe she'll be in the next room?")
      ans = 'correct'
      points += 1
    elif (choice.upper()=='SEARCH'):
      print("\n Without a second thought you jump up onto the tray. Unfortunately, you forgot that you're too heavy and the tray flips over instantly! JULIA's PS5 controller and T.V. remote slam on the floor and the remote slides under the couch that you safely land on. Lucky! JULIA wont be too happy when she can't find her stuff though... ")
      time.sleep(5)
      print("Too bad you still can't find JULIA. Maybe she'll be in the next room?")
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(5)

def scene4():
  import time
  global points

  print("\n Still hungry, you decide to search the KITCHEN for some snacks. You find a few more pieces of food along the way and gobble them up. Good thing you're a messy eater or you might have starved to death! When you enter the KITCHEN you catch an intoxicating scent. You know it can only be one thing. Chicken nuggs!!!") 
  time.sleep(5)
  print("\n You spy the box on the counter, half open revealing those tasty, meaty bites. You know JULIA would be upset if she found out you stole some. But they smell so good! Should you jump up and eat them or leave them be? ") 
  time.sleep(5)
  print("Enter: DISREGARD or PILLAGE?")
  
  choice = input()
  ans = 'incorrect'
  while (ans=='incorrect'):
    if (choice.upper()=='DISREGARD'):
      print("\n You know you aren't supposed to go up on the counter to steal food, and you're a good kitty. You decide it's not worth stealing any nuggs and leave them alone. Maybe JULIA will reward you for being so well behaved when you finally find her. She loves when her kitties are being good. ")
      time.sleep(5)
      print("It doesn't seem like JULIA is anywhere around the house... There's no where else to look so you sit by the back door and look out, waiting. Hopefully you see JULIA soon.")
      time.sleep(5)
      ans = 'correct'
      points += 1
    elif (choice.upper()=='PILLAGE'):
      print("\n You know you aren't supposed to go up on the counter to steal food, but nuggs are worth being a naughty kitty! After hopping onto the counter you begin working on getting the box open. It's a bit of a struggle, but finally you get it open all the way! When you try to pull one out you accidentally knock all the rest on the floor. Oh well. ")
      time.sleep(5)
      print("You start to eat the nugg but realize it's got breading all over it. Gross! You eat half the nugg and leave the rest on the counter. ")
      time.sleep(5)
      print("It doesn't seem like JULIA is anywhere around the house... There's no where else to look so you sit by the back door and look out, waiting. Hopefully you see JULIA soon.")
      time.sleep(5)
      ans = 'correct'
      points += 0
    else:
      print("\n Please enter valid choice from above")
      choice = input()
  time.sleep(3)



def scene5():
  import time
  
  range1 = range(2, 4, 1)
  
  if points <= 1:
    print('You stare out the backdoor waiting forever for JULIA. Finally, you hear the back gate creek open and see JULIA and NICK step through. NICK opens the door and JULIA steps in. \n "Were you all good kities?" JULIA asks.')
    time.sleep(5)
    print("JULIA looks around the house and sees the mess that was made and isn't happy. She looks down at you and says ")
    print('"MILO, I am very disappointed in you. You were very bad today."')
    time.sleep(5)
    print('JULIA lets out a brief sigh...') 
    time.sleep(5)
    print('\n "But I still love you my naughty boy..." \n JULIA picks you up and gives you a big kiss on the head. \n THE END')
  
  
  elif points in range1:
    print('You stare out the backdoor waiting a long while for JULIA. Finally, you hear the back gate creek open and see JULIA and NICK step through. NICK opens the door and JULIA steps in. \n "Were you all good kities?" JULIA asks.')
    time.sleep(5)
    print("JULIA looks around the house and smiles. She looks down at you and says ")
    print('"You were a good boy today, werent you MILO?"')
    time.sleep(5)
    print('JULIA picks you up and gives you a big kiss on the head.') 
    time.sleep(5)
    print('\n "I love you my big boy." \n JULIA grabs a bag of treats and gives you a yummy piece of salmon. Now you have your JULIA and snacks! Good job! \n THE END')
  
  
  elif points == 4:
    print('You stare out the backdoor waiting a short while for JULIA. Finally, you hear the back gate creek open and see JULIA and NICK step through. NICK opens the door and JULIA steps in. \n "Were you all good kities?" JULIA asks.')
    time.sleep(5)
    print("JULIA looks around the house and smiles. She looks down at you and says ")
    print('"You were a very good kitty MILO! Such a good boy!"')
    time.sleep(5)
    print('JULIA picks you up and gives you a big kiss on the head and squeezes you tight.') 
    time.sleep(5)
    print('\n "I love you my big boy. You are the best kitty. \n JULIA grabs 3 bowls and a packet of wet food treats. You, IGGY, and YUFFIE all get delicious pumpkin and chicken treats for being so good while JULIA and NICK were away. What a good day; you are a very happy and content cat. \n THE END')

    
  


ans2 = 'incorrect'
def game():
  global ans2
  while ans2 == 'incorrect':
    scene1()
    scene2()
    scene3()
    scene4()
    scene5()
    print('Play Again? YES or NO')
    choice2 = input()
    if (choice2.upper() == 'YES'):
      ans2 = 'incorrect'
    elif (choice2.upper() == 'NO'):
      ans2 == 'correct'
      print('Fin.')
      break
    else:
      print("\n Please enter valid choice from above")

#def hub():
  anchor = 'INCORRECT'
  print(f'Which room do you want to search? ', (rooms) )
  selc = (input().upper())

  while anchor == 'INCORRECT':
    if selc == 'BEDROOM':
      anchor == 'CORRECT'
      scene1()
    elif selc == 'OFFICE':
      anchor == 'CORRECT'
      scene2()
    elif selc == 'LIVING ROOM':
      anchor == 'CORRECT'
      scene3()
    elif selc == 'KITCHEN':
      anchor == 'CORRECT'
      scene4
    else:
      print('Select a valid choice')

game()













