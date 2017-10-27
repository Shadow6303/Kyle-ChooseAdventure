def introduction():
    print "ABBY LOVE THE ADVENTURER"
    print "The year is 1815, welcome to London, England, the largest city in the world.  It is a beautiful December day and you are about to be born."
    print
    boy_girl()


def boy_girl():

    print "Would you like to be a boy or a girl?"
    print "Type b for boy or g for girl."
    answer = raw_input()
    if answer == "g":
        print "girl"
        rich_poor()
    else:
        print"boy"
        obscurity()


def obscurity():
    print "You are born in the slums of the huge eastern section of London.  Your life is short and hard and you die in obscurity."


def rich_poor():
    print "Your parents name you Ada, would you like to be rich or poor?"
    print "Type r for rich or p for poor."
    answer = raw_input()
    if answer == "r":
        poetry_science()
    else:
        obscurity()


def poetry_science():
    print "Ada you are a lucky girl your mother is the wealthy aristocrat Anne Isabella Noel Byron, 11th Baroness Wentworth and Baroness Byron.  "
    "\nYour father is the famous poet Lord Byron!  "
    "\nHe is the most famous poet of the romantic period and his magnum opus was Don Juan.  "
    print "Would you like to follow in your fathers footsteps or listen to your mother and pursue math and science?"
    print "Type p for poetry or m for math and science."
    answer = raw_input()
    if answer == "m":
        love_babbage()
    else:
        aristocrat()


def aristocrat():
    print "Enjoy your life as an English aristocrat, you will write poetry, paint, entertain and you will have a deep passion for horses."


def love_babbage():
    print "Ada you have just turned 17 and you are brilliant and rich.  At a lavish party you meet lots of aristocrats who want your attention.  Would you like to fall love with one of the rich suitors or are you more interested in a small working mechanical device?"
    print "Type l for love or d for device."
    answer = raw_input()
    if answer == "d":
        difference_engine()
    else:
        aristocrat()


def difference_engine():
    print "You find the machine and the man Charles Babbage fascinating; he is a mathematician and an inventor.  He has built a machine called the Difference Engine.  It is a large machine of gears and cranks that can calculate and print the answers to complicated polynomial equations."
    print "Babbage offers you the opportunity to learn more, would you like to study the Difference Engine?"
    print "Type y for yes or n for n."
    answer = raw_input()
    if answer == "y":
        horse_translate()
    else:
        aristocrat()


def horse_translate():
    print "His next project is much larger and more complicated computing project called the Analytical Engine."
    "\nThe Analytical Engine is never built but you immerse yourself in the plans of the this fantastic machine.  "
    "\nThe best description of the engine is in French and someone needs to translate it into English.  " \
    "\nYou find yourself in a dilemma, you love to ride horse and you love the Analytical Engine, unfortunately you do not have time for both."
    print "Would you like to ride your horse or translate the plans?"
    print "Type h for horse or t for translate."
    answer = raw_input()
    if answer == "t":
        history()
    else:
        aristocrat()


def history():
    print "Not only do you translate the article you also add extensive notes of your own.  Your article contains statements that show you to be a visionary with a deeply modern perspective.  You speculate that the Engine 'might act upon other things besides numbers... the Engine might compose elaborate and scientific pieces of music of any degree of complexity or extent'."
    print "The idea of a machine that could manipulate symbols in accordance with rules and that number could represent entities other than quantity mark the fundamental transition from calculation to computation. You were the first to explicitly articulate this notion and you surpass even Babbage in your understanding of the future of computing. You are know as the 'prophet of the computer age' and you go down in history has the first computer programmer!"
    print "Well done!!"


introduction()