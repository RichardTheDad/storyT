print("As the tale unfolds, remember to complete the questions provided below. Don't forget to press enter once you've filled them out.")

KeepPlaying = "yes"
while KeepPlaying.lower() == "yes":


    FamilyName = input("\nPick a family name:  ")

    HighElfName = input("\nEnter the name of your elf:  ")

    HighElfGender = input("\nWhat is the gender of your elf Male or female:  ")
    while HighElfGender.lower() not in ["male","female"]:
        HighElfGender = input("\nPlease enter male or female:  ")

    Weapon = input("\nWhat wepon will you use:  ")

    Sibling = input("\nDo you have a brother or a sister:  ")
    while Sibling.lower() not in ["brother","sister"]:
        Sibling = input(f"\nPlease enter brother or sister:  ")

    

    print(f"\nIn a realm where the luminescent High Elves dwell, you are one such elf belonging to the esteemed lineage of House {FamilyName}.")
    print(f"\nWith a name as illustrious as {HighElfName}, your family's standing is beyond compare.")
    print(f"\nHowever, the tranquility of your noble abode is shattered as a crisis befalls your household your very own {Sibling} has vanished into the unknown.")
    print(f"\nWith determination in your heart, you embarked on a quest to locate your {Sibling}. Rumors had reached you that your {Sibling} was journeying toward the mystical enchanted forest.")
    print(f"\nAs you pursued their trail, a glimpse of your {Sibling} came into view, but to your dismay, they were encircled by a pack of wild boars.")
    Choice1 = input(f"\nWill you save your {Sibling} or will you abandoned them  y to save, n to abandon: ")
    while Choice1.lower() not in ["y", "n"]:
        Choice1 = input("invalid value enter y or n:  ")
    if Choice1.lower() == "y":
        print(f"\nYou run twords your {Sibling} brandishing your {Weapon} and you slay the feral beasts. You grab your {Sibling} and head off. ")
    elif Choice1.lower() == "n":
        print(f"\nTerrified of the beasts you run abandoning your {Sibling}. As you bolt tripping throughout the forest dropping your {Weapon}.")
        print(f"\nYou hear the screams of your {Sibling} as their  flesh be torn from the bone.")

    

    #choice 2 y y
    if Choice1.lower() == "y":
        print(f"\nNow with your startled {Sibling} held tightly in your arms will you head home or will you stay within the forest captivated by its beauty.")
    Choice2 = input("head home y, say in the forest n:  ")
    while Choice2.lower() not in ["y","n"]:
        Choice2 = input("invalid value enter y or n:  ")
    if Choice2.lower() =="y" and Choice1.lower() =="y":
        print(f"\nYou head home with your {Sibling} thinking how great it will be to finaly head home after the long day.")

    

    #choice 2 n y
    if Choice1.lower() == "n":
        print(f"\nYou hang your head in shame at your cowardice. Will you head home or will you stay within the forest to ashamed to show your face to your parents.")
    while Choice2.lower() not in ["y","n"]:
        Choice2 = input("invalade value enter y or n:  ")
    if Choice1.lower() == "n" and Choice2.lower() == "y":
        print(f"\nYou head home to accept your punishment from your parents with a heavy heart.")


    

    #Choice 2 y n
    if Choice1.lower() == "y" and Choice2.lower() == "n":
        print(f"\nNow that your focus is lifted from your {Sibling} you notice that the forest looks incredible. You decide to live within the forest with your {Sibling} to save them from your family.")

    

    #Choice n n
    if Choice1.lower() == "n" and Choice2.lower() == "n":
        print(f"\nAshamed to face your parents due to your failure to bring back your {Sibling} you decide to live within the forest.")



    #story end 1
    if Choice1.lower() == "y" and Choice2.lower() == "y":
        print(f"\nAfter a long journey, you and your {Sibling} arrive back home. The warm embrace of your parents envelops both of you, filling the air with a sense of belonging. ")
        print(f"\nWith the family united once again, a newfound strength binds them together, forging an unbreakable bond.")


    #story end 2
    if Choice1.lower() == "y" and Choice2.lower() == "n":
        print(f"\nAfter a period of longing, you are at last reunited with your {Sibling}. As you embrace, you sense the depth of fear that has taken hold of them. ")
        print(f"\nThe {FamilyName} family, to which you both belong, is grappling with a tumultuous scandal that has shaken its very foundation.")
        print(f"\nFaced with these trying circumstances, a decision crystalizes in your mind you and your {Sibling} choose to seek solace in the heart of a captivating forest.")
        print(f"\nAmidst the beauty of nature, you hope to find a new beginning, far from the troubles that have befallen your family.")

    
    #story end 3
    if Choice1.lower() == "n" and Choice2.lower() == "y":
        print(f"\nThe tragic passing of your {Sibling} weighs heavily on your heart, burdening you with remorse for not being there when they needed you.")
        print(f"\nAfter a period of deep contemplation, you gather your thoughts and make your way back home, ready to confront whatever consequences your parents might impose upon you.")

    

    #story end 4 
    if Choice1.lower() == "n" and Choice2.lower() == "n":
        print(f"\nConsumed by shame for your inability to rescue your {Sibling} and burdened by overwhelming guilt, you opt to seclude yourself within the depths of the forest.")
        print(f"\nHere, you contemplate embracing the same fate that befell your {Sibling}.")


    KeepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while KeepPlaying.lower() not in ["yes", "no"]:
            KeepPlaying = input(f"\nEnter yes or no:  ")