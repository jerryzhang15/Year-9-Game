import art
word=art.text2art("Welcome to My Game!")
print(word)


player =  input("What's your name? >")
print("Hello, "+player)
validInput = False
while validInput == False:
    introduction = input("Hello , this game is called The Proudest Blue. Would you like to learn how to play, Yes or No? > ")
    if "yes" in introduction.lower():
     print("The game you are playing right now is a text-based adventure game based the book The Proudest Blue. The goal of the game is to teach you about islamphobia. Try your hardest to make the kindest and best decisions and in turn you'll get lots of points!")
     validInput = True

    elif "no" in introduction.lower():
     print("Let's begin the fun right away!")
     validInput = True

    else:
        print("I can't do that")
        validInput = False
point = 0
print ("It is the first day of school, you get out of bed")



validInput = False
while validInput == False:
    command1 = input("Do you want to brush your teeth?")
    if "yes" in command1.lower():
        print("You have brushed your teeth with watermelon toothpaste and went downstairs to eat breakfast. +1point")
        point =+ 1
        validInput = True
    elif "ok" in command1.lower():
        print("You have brushed your teeth with watermelon toothpaste and went downstairs to eat breakfast. +1point")
        point += 1
        validInput = True
    elif "sure" in command1.lower():
        print("You have brushed your teeth with watermelon toothpaste and went downstairs to eat breakfast. +1point")
        point +=1
        validInput = True
    elif "no" in command1.lower():
        print("You went straight downstairs to eat breakfast but your breath smells horrible. 0points")
        point += 0
        validInput = True

    else:
     print ("I can't do that.")
     validInput = False


print(point)

print("Once your downstairs, you see your sister Amari wearing a deep blue clothe wrapped around her head.")
print("You are not sure what that is and is curious.")

validInput = False
while validInput == False:
    command2 = input("What do you ask her?(examples: what is that?, it's so ugly can you take it off?)")
    if "what" in command2.lower():

        print("She said that the scarf she's wearing is called a Hijab. It is apart of Muslim culture and defines her identity! 1point")
        point =+ 1
        validInput = True

    elif "why" in command2.lower():

        print("She said that the scarf she's wearing is called a Hijab. It is apart of Muslim culture and defines her identity! 1point")
        point =+ 1
        validInput = True

    elif "ugly"in command2.lower():

        print("Hey stop it! Don't disrespect our culture, it's very important to me, Amari yelled. -1point")
        point += -1
        validInput = True

    elif "off"in command2.lower():

        print("Hey stop it! Don't disrespect our culture, it's very important to me, Amari yelled. -1point")
        point += -1
        validInput = True
   
    else:
     print ("I can't do that.")
     validInput = False


print(point)


print("You have arrived at school and during lunch, a bully comes up to your sister")
print("The boy teases her and says 'why are you wearing a dirty mop on your head' and continues to make fun of her ")

validInput = False
while validInput == False:
    command3 = input("What are you going to do? 1. Ignore it  2. tell the bully to stop  3. tease her")
    if "ignore" in command3.lower():

        print("You continued to eat your lunch and ignored the bully. Your sister ran out of the lunch hall with tears dripping down her eyes. -1point")
        point =+ -1
        validInput = True

    elif "stop" in command3.lower():

        print("You told the bully to stop and what they are doing isn't cool. The bully sat down and stopped making fun of your sister. +2points")
        point =+ 2
        validInput = True

    elif "tease"in command3.lower():

        print("You told your sister Amari that her hijab was very ugly. She got very sad started crying. -2points ")
        point += -2
        validInput = True

    elif "fun"in command3.lower():

        print("You told your sister Amari that her hijab was very ugly. She got very sad started crying. -2points")
        point += -2
        validInput = True
   
    else:
     print ("I can't do that.")
     validInput = False

print(point)


if point < 1:
    validInput = False
    while validInput == False:
        command4 = input("Once you arrived home your mom is extremely mad at you and spanks you. What do you do? 1. Apologize  2. Hit your mom")
        if "apologize" in command4.lower():

            print("You told your mom that your extremely sorry and Amary forgives you. +1point")
            point =+ 1
            validInput = True

        elif "hit" in command4.lower():

            print("You threw a devious right hook to your mom and sent her to the hospital. You were disowned. -50points. THE END. YOU LOST.")
            point =+ -50
            validInput = True
        else:
            print ("I can't do that.")
            validInput = False

print(point)

if point == 1:
    print("You have made some mediocre choices. Not the best but still good. Congrats! The game is finished")

if point > 1:
    print("CONGRATS, you have made amazing decisions and beat the game. Hope you had fun!")