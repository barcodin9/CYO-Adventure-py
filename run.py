print('''Your friend Hannah has been missing for 3 weeks now. 
      Gone, vanished without a trace. 
      You missed a call from her tonight, 3 weeks after she disappeared, she sounded scared and frantic.
      She said "I've been taken, I don't know where I am, I have shared my location with you, 
      please help..." then there was a bang and scream before the line went dead.

      You went to the police, but they didn't pay it any mind. It's your job to find her.
      
      You have tracked her phone to the old hotel about 40 miles north of town, it hasn't moved in several days.
      
      As you pull up to the location in your car, a sense of dread makes your stomach
      churn, what will you find? is she even still alive? will I be walking into a trap?..
      
      You get out of your car, walk up to the entrance, put your hand on the large, bronze door handle
      and you pause..\n''')
QAnswer = input("Are you ready to enter the abandoned hotel? (y/n)\n")

if QAnswer.lower().strip() == "y":

    print('''You push open the large front door of the hotel, the floor creaks under your foot as you step inside.
          The air runs cold, it is eerily quiet. No wind, no rustling of the trees, no animals can be heard.''')

    answer = input('''Directly in front of you are 2 doors, one is red, one is blue. 
                   You're unsure of where to go, but false bravery pushes you forward. 
                   Which door will you choose?\n''').lower().strip()
    if answer == "red":
        print('''As you walk through the red door it slams behind you! 
            You are immediately greeted by a foul smell, the room is pitch black.\n''')
    elif answer == "blue":
        print("As you walk through blue door, it slams behind you! you have entered a long narrow hallway.\n")
    else:
        print("You turn around and leave the hotel, abandoning your friend, shame on you.")
        

else:
    print("You have chosen to abandon your friend.") 
    