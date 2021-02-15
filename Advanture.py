# this is a plain text advanture game

#global error var
errStr="Please enter valid Char/Words."



def niceending():
    docLive = input().upper()
    while (docLive != "YES" and docLive != "NO"):
        print(errStr)
        docLive = input().upper()

    if docLive == "YES":
        print("You chose yes. Are you really going to believe him? Maybe he is the one who makes you trapped in this body. You never think about this? OK, after all. Congratulation. You reach the BEST ending. You get out the jail without becoming a murderer, and you have a peaceful and happy life with the cute doctor. THE END")

    else:
        print("You chose no. You leave the doctor. You spend five years tracking down a project called \"LongLive\", which includes an experiment that switches the memory of persons in order to find the truth of people's self-identity. Ironically, you find out the doctor is in charge of this experiment. One night, you approach the doctor, confront him. He admits everything. NOW, you are the one holding the gun, what would you do? By the way, he said, he doesn't regret it because he met you. (please enter \"KILL\" to kill, and \"LEAVE\" to leave)")
        badDoctor = input().upper()
        while (badDoctor != "KILL" and badDoctor != "LEAVE"):
            print(errStr)
            badDoctor = input().upper()

        if badDoctor == "KILL":
            print("You chose to kill. You put a bullet into the heart of the doctor. He didn't suffer. THE END. ")

        else:
            print("You chose to leave. You find all the people who involve in the project, who manipulated your life. You kill them all but the doctor. You know you can never pull the trigger. You never meet him again. \n 60 years later, you come to his funeral with a white flower, just like an old friend. THE END. ")


def badending():
    lifeChoice = input().upper()
    while (lifeChoice != "LEAVE" and lifeChoice != "STAY"):
        print(errStr)
        lifeChoice = input().upper()

    if lifeChoice == "LEAVE":
        print("You chose to leave. Are you really don't care about who is behind your tragedy? Are you really never worry about them come after you again? Well, lucky you. They never find you. Although you have a difficult start you have a life in a foreign land. THE END.")

    else:
        print("You chose to stay. But too many people are coming after you. On a rainy day, your body has been found in a little valley. THE END.")

         
def guard():
    print("But, you encounter a guard who seems to know the real doctor, and hence he is walking towards you. Turning back to hide from the guard or kill the guard just like you killed the doctor, WHICH would you choose? (please enter \"H\" for hiding or \"KILL\")")
    
    gua = input().upper()
    while (gua != "H" and gua != "KILL"):
        print(errStr)
        gua = input().upper()

    if gua == "H":
        print("You choose to hide. BAD choice. The guard didn't find you. But, he found the doctor who you killed. High alert raises, and you don't have the key to pass the last gate. So, they found you. They take you back to the cell and charge you with murder. FAIL.")

    else:
        print("You chose to kill the guard. Poor guard, lucky you. You get the key from the guard to open the last gate. You get out the jail. SUCCESS? Innocent you become a bloody murderer. uh, I won't call it a true victory. You have your freedom now, although it full of chasing and killing. You found a way to leave the country, but, in this way, you can never go back. Would you leave? Or, would you stay to find why your memory was manipulated? (please enter \"LEAVE\" or \"STAY\")")
        badending()



def doctor():
    docKill = input().upper()
    while(docKill != "KILL" and docKill != "KIDNAP"):
        print(errStr)
        docKill = input().upper()
    
    if docKill == "KILL":
        print("You chose to kill the doctor. You successfully disguise to a doctor and use doctor's name card pass two doors. NOW, you are only one door away from freedom.")
        guard()
        
    
    else:
        print("You chose to kidnap the doctor. The Doctor makes you pass two doors, but he doesn't have access to the last gate. He listened to your story and seems to believe in you. He suggests you go to his office, and he promises he has a way to get you out. NOW, are you going to believe this cute doctor? (Please enter \"B\" as believe and \"N\" as not believe)")
        docBelieve = input().upper()
        while (docBelieve != "B" and docBelieve != "N"):
            print(errStr)
            docBelieve = input().upper()

        if docBelieve == "B":
            print("You chose to believe the doctor. Interesting, you believe someone who you kidnaped. Anyway, you went to the office with him.  He injects some medicine into you, hence triggers the medical parole. As he promised, he gets you out the jail. In the hospital, you can easily kill the guard and gain freedom. But, the doctor asks you to wait for few more days. Would you wait? Or, would you handle it in your way, I mean, Kill for freedom. (please, enter \"WAIT\" or \"KILL\")")

            docStay = input().upper()
            while (docStay != "WAIT" and docStay != "KILL"):
                print(errStr)
                docStay = input().upper()

            if docStay == "WAIT":
                print("You chose to wait. The doctor never fails you. He false your death, and switches you with a corp. NOW, you are free. The doctor asks you to live with him. Temporarily, you assume. Are you going to live the doctor or not? (please enter \"YES\" or \"NO\")")
                niceending()

            else:
                print("You chose to kill. You don't think you can fully trust the doctor. You have your freedom now, although it full of chasing and killing. You found a way to leave the country, but, in this way, you can never go back. Would you leave? Or, would you stay to find why your memory was manipulated? (please enter \"LEAVE\" or \"STAY\")")
                badending()

        else:
            print("You chose to not believe the doctor. You knock out the doctor and put his cloth on. You wonder around the last gate.")
            guard()







def main():
    """
    this is taking charge of the flow of the game.
    collecting input and throwing errors
    input is not case-sensetive

    """

    
    print("Welcome to plain text advanture game.\n\n")
    print(" You wake up in a jail cell with other's memory. You feel dizzy, so you look at your hand. You are pretty sure this is not your body. You want to get out the jail and find out why. Luckily, somehow, you know the floor plan of this jail. It is a tiny jail, only three doors away from the outside world. And, this body is an absolute killing machine. \n The cell is not locked, so you got out in the hallway. There is a window on the right end of the hallway. And, you heard some crowd noise from the left. WHICH direction are you going to choose? (Please enter \"L\" or \"R\")")
    hallway = input().upper()
    while (hallway != "L" and hallway != "R"):
        print(errStr)
        hallway = input().upper()


    if hallway == "L":
        print("You chose to go left. Just around the corner, you see a doctor who notices you and walks to you. NOW, you can choose to kill the doctor or kidnap the doctor. WHICH would be your choice? (please enter \"KILL\" or \"KIDNAP\")")
        doctor() # it leads to same dirction with some other choice, so combine them using a functioin

    else:
        print("You chose to go right. Just around the corner, you see a guard. The guard sees you too, so he walks toward you. Just by watching him walking, your body spontaneously knows how to kill him. NOW, are you going to kill him or turning around and avoid him? (please enter \"KILL\" or \"AVOID\")")
        guard = input().upper()
        while (guard != "KILL" and guard != "AVOID"):
            print(errStr)
            guard = input().upper()
        
        if guard == "KILL":
            print("You chose to kill the guard. It was really easy for you, but, the doctor at another end of the hallway sees your action. He triggers the high alert, all the guard is now coming to you. However, most of them are in the outer area. So, you can choose to chase and kill the doctor, then disguise as the doctor to lose the guard, or keep running using the guard's card to pass the doors and kill everyone on your way. WHICH would you choose? (please enter \"D\" for kill doctor and \"R\" for keep running)")
            docKill = input().upper()
            while (docKill != "D" and docKill != "R"):
                print(errStr)
                docKill = input().upper()
            
            if docKill == "D":
                print("You chose to kill the doctor. You successfully disguise to a doctor and use doctor's name card pass two doors. NOW, you are only one door away from freedom. But, you encounter a guard who seems to know the real doctor, and hence he is walking towards you. Turning back to hide from the guard or kill the guard, WHICH would you choose? (please enter \"H\" for hiding or \"KILL\")")
                guardkill = input().upper()
                while (guardkill != "H" and guardkill != "KILL"):
                    print(errStr)
                    guardkill = input().upper()

                if guardkill == "H":
                    print("You chose to hide. BAD choice. You already killed two people, why stop now? Since the high alert, the guard is super careful. The guard noticed the blood spot on your shoe. He shot you, then they got you back to your cell. FAIL.")

                else:
                    print("You chose to kill the guard. Poor guard, lucky you. You get the key from the guard to open the last gate. You get out the jail. SUCCESS? Innocent you become a bloody murderer. uh, I won't call it a true victory. You have your freedom now, although it full of chasing and killing. You found a way to leave the country, but, in this way, you can never go back. Would you leave? Or, would you stay to find why your memory was manipulated? (please enter \"LEAVE\" or \"STAY\")")
                    badending()


            else:
                print("You chose to keep running. As a killing machine, you successfully killed everyone who tries to block your way to freedom. You get out the jail. SUCCESS? Innocent you become a bloody murderer. uh, I won't call it a true victory. You have your freedom now, although it full of chasing and killing. You found a way to leave the country, but, in this way, you can never go back. Would you leave? Or, would you stay to find why your memory was manipulated? (please enter \"LEAVE\" or \"STAY\")")
                badending()
        
        else:
            print("You chose to avoid the guard. luckily, he didn't pay too much attention to you. You keep walking, just around the corner, you see a doctor who notices you and walks to you. NOW, you can choose to kill the doctor or kidnap the doctor. WHICH would be your choice? (please enter 'KILL' or 'KIDNAP')\"")
            doctor()
            







main()