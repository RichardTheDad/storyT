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
    print(f"\nTerrified of the beasts you run abandoning your {Sibling}. As you bolt tripping throughout the forest you hear the screams of your {Sibling} as thier flesh be torn from bone. ")


