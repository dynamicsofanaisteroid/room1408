import time

# Intro sequence
print("You enter Room 1408 with the dry skepticism Mike Enslin has always had for haunted hotel rooms.")
time.sleep(2)
print("You expected nothing more than a few creaky pipes, maybe a hotel employee moaning through the vents.")
time.sleep(2)
print("But as the door closes behind you, you feel a shiver chase your spine.")
time.sleep(2)
print("Time to look around.")
time.sleep(1)

# Game state tracking
actions_completed = {
    "tear_paper": False,
    "eat_chocolates": False,
    "look_at_phone": False,
    "look_out_window": False,
    "pull_curtain": False
}

# Room navigation map
room_transitions = {
    "main": {"north": "window", "east": "bathroom", "west": "bedroom", "south": "lounge"},
    "window": {"south": "main"},
    "bathroom": {"west": "main"},
    "bedroom": {"east": "main"},
    "lounge": {"north": "main"}
}

current_room = "main"

def scene_progress_check():
    return all([
        actions_completed["tear_paper"],
        actions_completed["eat_chocolates"],
        actions_completed["look_at_phone"]
    ])

# Main game loop
while True:
    command = input("\nWhat do you want to do? ").strip().lower()

    if command == "look":
        if current_room == "main":
            print("\nYou are stood in an elegant, old-fashioned hotel room.")
            print("To your north is a window, the curtains billowing softly in the breeze.")
            print("To your east is the bathroom, where Olin implied the maid had gone insane (yeah, right).")
            print("To your west is the bedroom, where two hotel chocolate wrappers now lie empty on the pillow." if actions_completed["eat_chocolates"] else "To your west is the bedroom, where you can see two hotel chocolates have been left for you on the pillow.")
            print("To your south is the lounge, where a quaint old rotary telephone sits on the sideboard.")
        elif current_room == "bathroom":
            paper_desc = "a torn toilet paper roll" if actions_completed["tear_paper"] else "a toilet paper roll"
            curtain_desc = "with the curtain open" if actions_completed["pull_curtain"] else "with the curtain drawn"
            print(f"You enter the bathroom. No ghoulies in here, yet. There is {paper_desc}, a bath {curtain_desc}, and a tap.")
        elif current_room == "bedroom":
            chocolates_desc = "Two empty wrappers" if actions_completed["eat_chocolates"] else "The chocolates"
            print(f"You step into the bedroom. {chocolates_desc} rest on the pillow like bait. The painting above the bed continues to brood.")
        elif current_room == "lounge":
            print("The rotary phone sits silently, almost smugly.")
        elif current_room == "window":
            print("The window yawns open, cold air spilling into the room. Beyond it, the city flickers.")

    elif command in ["north", "east", "west", "south"]:
        if command in room_transitions.get(current_room, {}):
            current_room = room_transitions[current_room][command]
            if current_room == "window":
                print("You approach the open window. The Dolphin's view overlooks the blur of taxi cabs far below, at a drop that makes your stomach clench. Opposite there is an apartment building, with one dark window opposite.")
            elif current_room == "bathroom":
                print("You enter the bathroom. No ghoulies in here, yet. There is a toilet paper roll, a bath with the curtain drawn, and a tap.")
            elif current_room == "bedroom":
                if actions_completed["eat_chocolates"]:
                    print("You step into the bedroom. A depressive painting of a schooner at sea glowers above the headboard. Two empty chocolate wrappers are on the pillow, mocking you with their lack of sugary promise.")
                else:
                    print("You step into the bedroom. A depressive painting of a schooner at sea glowers above the headboard. The chocolates nestle on the pillow like little teeth in wraps of green hotel paper.")
                print("You step into the bedroom. A depressive painting of a schooner at sea glowers above the headboard. The chocolates nestle on the pillow like little teeth in wraps of green hotel paper.")
            elif current_room == "lounge":
                print("You walk into the lounge. The rotary phone sits there in silent judgement.")
            elif current_room == "main":
                print("You return to the main room, the eerie calm swallowing your footsteps.")
        else:
            print("You can't go that way.")

    # Bathroom interactions
    elif current_room == "bathroom":
        if command == "tear paper":
            actions_completed["tear_paper"] = True
            print("You tear a piece of toilet paper. Satisfying.")
        elif command == "look at toilet paper":
            if actions_completed["tear_paper"]:
                print("A toilet paper roll, now torn.")
            else:
                print("It's a roll of toilet paper. What were you expecting?")
        elif command == "take toilet paper":
            print("Nah. You're good.")
        elif command == "use tap":
            print("The tap provides a stream of perfectly mild water, then trickles to a stop.")
        elif command == "look at bath":
            if actions_completed["pull_curtain"]:
                print("A claw-footed creation. The curtain is drawn, revealing nothing.")
            else:
                print("A claw-footed creation. The curtain is pulled, masking what lies beyond.")
        elif command == "take bath":
            print("Nah. You're good.")
        elif command == "pull curtain":
            actions_completed["pull_curtain"] = True
            print("The rings on the rail rattle, revealing...nothing. Mike is mildly disappointed.")

    # Bedroom interactions
    elif current_room == "bedroom":
        if command == "eat chocolates":
            actions_completed["eat_chocolates"] = True
            print("You scoff both the hotel chocolates. Pure sugar on the tongue, then gone.")
        elif command == "look at chocolates":
            if actions_completed["eat_chocolates"]:
                print("Two empty wrappers lie on the pillow.")
            else:
                print("Two chocolates rest on the pillow, wrapped in neat green foil.")
        elif command == "take chocolates":
            print("You could... or you could just eat them.")

    # Lounge interaction
    elif command == "look at phone" and current_room == "lounge":
        actions_completed["look_at_phone"] = True
        print("You stare at the rotary phone. It seems to hum with static energy.")

    # Window interaction
    elif command == "look out window" and current_room == "window":
        actions_completed["look_out_window"] = True
        if scene_progress_check():
            print("You lean out the window, enjoying the night air...until the frame SLAMS down, as if yanked by an invisible, gleeful hand. You jerk back, but not quick enough - your hand catches between the frame, exploding with pain, blood gushing lazily down your knuckles. The radio flares into life in the same second. The Carpenters. 'We've only just begun....''.\n--- SCENE TWO BEGINS ---")
            break
        else:
            print("You lean out the window... but something feels off. You pull back. Best to check out the rest of the room, before sampling the city air.")

    elif command == "take":
        print("Take what?")

    elif command == "help":
        print("--- HELP ---")
        print("Welcome, stranger, to Room 1408. You were warned not to enter. You came anyway. Time to play.")
        print("This game utilizes simple commands to explore and interact with the environment.")
        print("Available command types:")
        print("- look : observe your current location")
        print("- look at <object> : examine an object")
        print("- take <object> : attempt to take something")
        print("- use <object> : interact with certain objects")
        print("- directional movement: north, south, east, west")
        print("- quit : What do you think happens? You end up, back where you started, again. There's no leaving Room 1408. Not before your time.")
        print("Try to observe everything...not all is what it seems. Don't be so certain that what you've taken won't reappear again...or that the door you entered leads where you think.")

    elif command == "quit":
        print("You decide you've had enough of Room 1408. You reach for the doorknob...it's broken. Was it broken when you came in? Who knows. You can't leave. But you do find yourself, standing exactly where you started. Right back at the beginning again. We've only just begun.")
        break

    else:
        print("I don't understand that command. Try looking around or interacting with something in the room.")
