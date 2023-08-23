print("Before the story begins fill out the questions and be sure to hit enter to submit them.")

FamilyName = input("\nPick a family name:  ")
HighElfName = input("\nEnter the name of your elf:  ")
HighElfGender = input("\nEnter the gender of your elf:  ")
Weapon = input("\nWhat wepon will you use:  ")
Sibling = input("\nDo you have a brother or a sister:  ")


print(f"\nYou are a {HighElfGender} Elf apart of the distinguished {FamilyName} family. Your name is {HighElfName} and your family is in a crisis, your {Sibling} has run away from home.")
print(f"\nYou set out to find your {Sibling}. You caught wind that your {Sibling} is heading to the enchanted forest, While giving chase you spot your {Sibling} and they are surounded by feral boars. ")

Choice1 = input(f"\nWill you save your {Sibling} or will you abandoned them - y to save, n to abandon: ")
while Choice1.lower() not in ["y", "n"]:
    Choice1 = input("invalid value enter y or n:  ")
if Choice1.lower() == "y":
    print(f"\nYou run twords your {Sibling} brandishing your {Weapon} and you slay the feral beasts. You grab your {Sibling} and head off. ")
elif Choice1.lower() == "n":
    print(f"\nTerrified of the beasts you run abandoning your {Sibling}. As you bolt tripping throughout the forest you hear the screams of your {Sibling} as their  flesh be torn from the bone. ")

#choice 2 good ending
if Choice1.lower() == "y":
    print(f"\nNow with your startled {Sibling} held tightly in your arms will you head home or will you stay within the forest captivated by its beauty.")
Choice2 = input("head home y, say in the forest n:  ")
while Choice2.lower() not in ["y","n"]:
    Choice2 = input("invalid value enter y or n:  ")
if Choice2.lower() =="y":
    print(f"\nYou head home with your {Sibling} thinking how great it will be to finaly head home after the long day.")

#choice 2 bad ending
if Choice1.lower() == "n":
    print(f"\nYou hang your head in shame at your cowardice. Will you head home or will you stay within the forest to ashamed to show your face to your parents.")
Choice2 = input("head home y, say in the forest n:  ")
while Choice2.lower() not in ["y","n"]:
    Choice2 = input("invalade value enter y or n:  ")
if Choice1.lower() == "n":
    print(f"\nYou head home to accept your punishment from your parents with a heavy heart.")