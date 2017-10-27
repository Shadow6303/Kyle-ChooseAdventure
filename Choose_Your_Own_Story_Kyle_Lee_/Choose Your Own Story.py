import time
import random
import webbrowser

def privateschool():
    print("Good choice!")
    time.sleep(1)
    print("Jeff's parents are very supportive of his decision, and Jeff is excited to attend his new school")
    time.sleep(4)
    print("9 years later...")
    time.sleep(3)
    print("Jeff has just finished high school and is choosing which college to attend.")
    time.sleep(4)
    print("All these years later, Jeff thinks he made a great decision to move to Harvard Westlake."
          "\n On his SAT, he got a perfect score and graduated Valedictorian.")
    time.sleep(5)
    print("Jeff was accepted into every college he applied to, but he is deciding between 2."
          "\nThe two are Stanford and Harvard. Jeff is once again, torn between which of the 2 he should attend.")
    gcollege = int(input("Should Jeff attend 1(Stanford) or 2(Harvard)?"))
    if gcollege == 1:
        Stanford()

    elif gcollege == 2:
        Harvard()

    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(3)
        print("The end...")

def publicschool():
    print("Jeff really wants to attend private school, but he feels that it is a more financially sound decision"
          " for him to stay at his current school")
    time.sleep(5)
    print("9 years later...")
    time.sleep(3)
    print("After all these years, Jeff regrets his decision to stay at South Pas. "
          "\nHe graduated an average student. "
          "\nHe is deciding which college to attend, but he was only accepted into 2. "
          "\nThe 2 colleges are Deep Springs College(DSC) "
          "\nand Alaska Career College(ACC)")

    tcollege  = int(input("Should Jeff attend 1.(DSC) or 2.(ACC)?"))



    if tcollege == 1:
        DeepSpringsCollege()
    elif tcollege == 2:
        AlaskaCareerCollege()
    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(3)
        print("The end...")

def choose(grass):
    if grass == 1:
        print("Jeff's Last Day...")
        time.sleep(3)
        print("One day, Jeff was picking up the droppings of his favorite bull, Shamba. Then, suddenly, out of nowhere,"
              "\n Shamba comes charging at Jeff, sending him flying 50 feet. He was pronounced dead at the scene.")
        time.sleep(6)
        print("The end")
    elif grass == 2:
        print("Good Choice")
        time.sleep(2)
        print("DragonSlayer wasn't fit for Jeff anyways. He is more fit to become DungeonKeeper.")
        time.sleep(4)
        print("This is why Jeff became DungeonKeeper, who takes care of the rooms.")
        time.sleep(3)
        print("One day, Jeff was cleaning somebody named Shamba's room.")
        time.sleep(3)
        print("While cleaning, he found a gun in Shamba's closet, and didn't know what to do.")
        time.sleep(4)
        print("Thoughts were racing through his mind. Should he pretend nothing happened? Should he tell the administrators?")
        time.sleep(3)
        print("A few minutes later, while Jeff was contemplating, Shamba came in, finding Jeff with his gun. "
              "\nShamba took out his spare gun and shot Jeff 3 times to the heart.")
        time.sleep(5)
        print("Jeff was pronounced dead at the scene.")
        time.sleep(3)
        print("The end...")
    else:
        print("You chose something wrong and guided Jeff in the wrong direction.")
        time.sleep(3)
        print("The next day, Jeff thought about his life, and realized how bad it was, so he killed himself.")

def Stanford():
    print("Great decision! Jeff has been vying to go to Stanford for several years!")
    time.sleep(5)
    print("Freshman Year...")
    time.sleep(3)
    print("Jeff is having a great time at Stanford! Jeff chose to major in Business Management, and was the only"
          " applicant accepted into the most elite fraternity on the campus, Alpha One. "
          "He also has straight A's, and is excelling in his business class.")
    time.sleep(10)
    print("Sophomore Year...")
    time.sleep(3)
    print("Jeff is excelling in his studies. He is on track to be able to finish college this year!"
          "After that, Jeff will move onto business school, and then will be on his way to becoming a billionaire!")
    time.sleep(6)
    print("Jeff has just finished college...")
    time.sleep(3)
    print("Because Jeff excelled, and set new records in his business class at Stanford, "
          "\nJeff is now considered a powerhouse in the business world. "
          "\nHe is highly sought after, and has received a scholarship offer to every one of his dream schools.")
    time.sleep(10)
    print("After hours of thought, Jeff has narrowed his choice to 2 "
          "The 2 business schools are Harvard Business School and the Stanford Graduate School of Business. ")

    bschool = int(input("Should Jeff attend 1.(Harvard Business School) or 2.(Stanford Graduate School of Business)?"))
    if bschool == 1:
        HarvardBusinessSchool()
    elif bschool == 2:
        StanfordGradSchool()

def Harvard():
    print("Great decision! Jeff has been vying to go to Harvard for several years!")
    time.sleep(5)
    print("Freshman Year...")
    time.sleep(3)
    print("Jeff decided to major in business management. "
          "\nJeff is struggling at Harvard.  "
          "\nEven though he was once Valedictorian, at Harvard he feels like an idiot.")
    time.sleep(9)
    print("Sophomore Year...")
    time.sleep(3)
    print("Jeff is struggling even more than the year before. "
          "\nJeff feels useless, and his college studies are costing his absurd amounts of money "
          "\nBecause of this, Jeff decides to buy a gun and shoot himself.")
    time.sleep(8)
    print("The end")

def AlaskaCareerCollege():
    print("Jeff is depressed that he was only accepted into 2 colleges, but he feels ACC is a great choice! "
          "\nJeff has heard great information about Alaska, and is psyched to finally move there! ")
    time.sleep(8)
    print("On top of that, ACC is known for their great business program!")
    time.sleep(5)
    print("Freshman Year...")
    time.sleep(3)
    print("It's going great for Jeff during his Freshman Year!"
          "\nOut of the 100 freshman, Jeff soon became the coolest guy on campus!"
          "\nHalfway into his freshman year, Jeff was invited by his friend, an Alaskan native named Shamba, "
          "\n to go bear hunting for Winter Break. Shamba said 'Because the bears are in hi-bear-nation, they will be"
          "\n easy pickings.")
    time.sleep(12)
    print("The day of the hunt...")
    time.sleep(3)
    print("'Shamba! There's one over there!' Jeff exclaimed! As Jeff got closer and closer to the bear,"
          "\n his heart started to race. Even though the bear was sleeping, it was the most exhilarating experiences"
          "\n of Jeff's life. Shamba said, 'Take a shot Jeff.' Jeff then lifted his gun, and took a shot."
          "\n It flew right past the bear. After this, the bear woke up and saw Jeff. Jeff, frozen in fear, "
          "\n could not move. The bear then attacked, and killed Jeff, but luckily, Shamba got away.")
    time.sleep(10)
    print("The end")
    bear = "https://i.ytimg.com/vi/Kgl0daD6j2U/maxresdefault.jpg"
    time.sleep(2)
    webbrowser.open(bear)

def DeepSpringsCollege():
    print("Jeff is depressed that he was only accepted into 2 colleges, but he feels DSC is a great choice! "
          "\nJeff has heard great information about the college, and is psyched to finally move there!"
          "\n On top of that, DSC is one of the most exclusive colleges in the U.S., and tuition is covered by DSC.")
    time.sleep(6)
    print("On top of that, DSC is known for their outdoor lifestyle, and has less than 30 students!")
    time.sleep(5)
    print("Freshman Year...")
    time.sleep(3)
    print("It's going great for Jeff during his Freshman Year!"
          "\nOut of the 30 students, Jeff soon became the coolest guy on campus!"
          "\nHalfway into his freshman year, Jeff was elected DragonSlayer, a student body position!"
          "\nOne of the most critical jobs of DragonSlayer is to take care of the bulls.")
    time.sleep(8)
    dumb = int(input("Should Jeff 1.(Become DragonSlayer) or 2.(Decline the offer)?"))
    choose(dumb)

def HarvardBusinessSchool():
    print("Great Choice")
    time.sleep(3)
    print("Jeff is ecstatic to go to Harvard Business School(HBS)."
          "\n Because of this, Jeff posted a racy image to his thousands of followers on Facebook, Instagram, and more.")
    time.sleep(7)
    print("Harvard soon found out about these racy photos, and revoked Jeff's admission.")
    time.sleep(5)
    print("Jeff soon found out about this, and took his modified nerf gun, and killed himself.")
    time.sleep(5)
    print("The end")

def StanfordGradSchool():
    print("Great Choice!")
    time.sleep(3)
    print("Jeff has been vying to go to Stanford for Business School his whole life!")
    time.sleep(5)
    print("Freshman Year...")
    time.sleep(5)
    print("As always, Jeff is doing well at Stanford Business School."
          "\nFrom the first day, the teachers noticed his particular skillset, and put him in more advanced classes."
          "\nBecause Jeff is excelling, Jeff's teachers advised him to go immediately into business as a rising star."
          "\nThis would make him highly sought after in the business world.")
    time.sleep(8)
    print("After Freshman Year...")
    time.sleep(4)
    print("Jeff decided to take his teachers' advice and go directly into the business world.")
    time.sleep(5)
    print("Jeff already has offers to several major companies. He has been noticed by world powerhouses, "
          "\n including Apple, Samsung, Coca-Cola, Microsoft, Nestle, and Ford.")
    time.sleep(8)
    print("There are 3 ways Jeff can go into business.")
    carvsother = int(input("Should Jeff 1.(Become CEO of a Business) 2.(Go into stock?) or 3.(Start his own Business?)"))
    if carvsother == 1:
        CEO()
    elif carvsother == 2:
        Stock()
    elif carvsother == 3:
        business()
    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(3)
        print("The end...")

def business():
    print("Great choice!")
    time.sleep(3)
    print("Jeff has been wanting to start a business from day 1.")
    time.sleep(5)
    print("Because of this, Jeff decided to start an Electronics brand called Typhoon.")
    time.sleep(5)
    print("Jeff decided to team up with a famous engineer, Alex Seaver, and design a phone.")
    time.sleep(5)
    print("Phone design finished, ready for production...")
    time.sleep(5)
    print("The phone is fast and beautiful. "
          "\nIt is 5 times faster than any Iphone, and has an 8k camera."
          "\nAlso, is made of titanium with carbon fiber and gold accents.")
    time.sleep(7)
    print("Typhoon is blowing up! "
          "\nThe phones have been noticed by many celebrities, and Typhoon is selling millions per day!")
    time.sleep(5)
    print("And with a base price of 1,000, Typhoon is selling billions worth of phones per day.")
    time.sleep(3)
    print("10 years later...")
    time.sleep(3)
    print("Typhoon has since released a computer line called Spyder, and several new phones."
          "\nOn top of that, they have become a world renowned brand, with public stock!")
    time.sleep(7)
    print("Because of this, Typhoon is the most valuable brand on Earth, being worth 5 trillion dollars!")
    time.sleep(5)
    print("Because of this, Jeff is now the most valuable man on Earth with a net worth of 1.46 trillion dollars!")
    time.sleep(5)
    print("You win!")
    time.sleep(2)
    trillionaire = "https://uncrate.com/p/2017/01/bel-air-mansion-9.jpg"
    webbrowser.open(trillionaire)

def Stock():
    print("Great Choice!")
    time.sleep(3)
    print("During Jeff's schooling at Stanford Business School, he set a new record for stock simulation!")
    time.sleep(5)
    print("Jeff has heard about 2 new up and coming companies. When he invests in stocks, he usually invests in 1"
          "\n up and coming company, and 1 established company. The 2 up and coming companies are Tesla and Shake Shack.")
    time.sleep(6)
    print("The estalished companies are Apple and Starbucks. Jeff likes to invest in one category."
          "\nThis is why Jeff is deciding whether he should invest in electronics or food.")
    invest = int(input("Should Jeff invest in 1(Apple and Tesla) or 2(Starbucks and Shake Shack)"))
    if invest == 1:
        electronics()
    elif invest == 2:
        food()
    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(5)
        print("The end...")

def electronics():
    print("Great choice!")
    time.sleep(3)
    print("Jeff has always been a firm believer of innovation, which is why he invested in electronics.")
    time.sleep(3)
    print("He is optimistic about the CEO of Tesla, Elon Musk, who started PayPal and SpaceX."
          "\nAlso, with the new Iphone X coming out, Jeff expects Apple stock to skyrocket.")
    time.sleep(4)
    print("Because of this, Jeff has decided to take a small loan of a 25 million dollars, and invest it directly into Apple and Tesla")
    time.sleep(3)
    print("Although, Jeff does not know when he should sell his stocks.")
    wait = int(input("How long should Jeff wait to sell his stock?(Up To 10)"))
    if wait <= 3:
        sure = (input("Are you sure you want to sell the stocks? They are at an all time high, but they could rise. 1 means yes, 2 means wait a few more years."))
        if sure == 1:
            print("Great Choice!")
            time.sleep(3)
            print("The Tesla Model 3 is becoming more commercialized, and the Iphone X sells out instantly.")
            time.sleep(5)
            print("The stocks have since multiplied their value by 15.")
            time.sleep(3)
            print("Jeff is worth about 750 million, but...")
            time.sleep(3)
            print("Because Jeff was such a firm believer in Apple in Tesla, they decided to give him the rest of the money he needed to be a billionaire.")
            time.sleep(5)
            print("You win")
            time.sleep(3)
            billionaire = "https://uncrate.com/p/2017/01/bel-air-mansion-9.jpg"
            webbrowser.open(billionaire)
        elif sure == 2:
            print("Jeff realized that after hitting their high, the stocks were beginning to fall, so he sold them.")
            time.sleep(3)
            print("Because of this, Jeff was able to retire comfortably with a net worth of 500 million."
                  "\nIt's a large amount, but not the billion Jeff was looking for.")
            time.sleep(5)
            print("Jeff retired comfortably, but was never able to become a billionaire.")
            time.sleep(3)
            print("The end")
    elif wait > 3 and  wait <= 5:
        print("Great financial decision!")
        time.sleep(3)
        print("Jeff realized that after hitting their high, the stocks were beginning to fall, so he sold them.")
        time.sleep(3)
        print("Because of this, Jeff was able to retire comfortably with a net worth of 500 million."
              "\nIt's a large amount, but not the billion Jeff was looking for.")
        time.sleep(5)
        print("Jeff retired comfortably, but was never able to become a billionaire.")
        time.sleep(3)
        print("The end...")
    elif wait > 5 and wait <= 10:
        print("Jeff waited far too long to sell his stock, and lost all of his money.")
        time.sleep(5)
        print("Because of this, Jeff decided to become a janitor, and stayed a janitor until his death.")
        time.sleep(5)
        print("The end...")
    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(3)
        print("The end...")

def food():
    print("Jeff is a firm believer in Shake Shack and McDonalds. To support his stock, he eats Shake Shack and McDonalds every day.")
    foodie = int(input("How long should Jeff wait to sell his stocks?"))
    long = random.randrange(1,foodie)
    time.sleep(3)
    print("Unfortunately, during his ", long, "th year, Jeff's stock fell. Jess got incredibly stressed."
          "\nWith Jeff's combination of an unhealthy diet and stress, he died.")
    print("The end...")

def CEO():
    print("Great Choice!")
    time.sleep(3)
    print("You have several offers from great companies, but the biggest ones are Apple and Samsung.")
    comp = int(input("Would you like to become CEO of 1.(Apple) or 2.(Samsung)?"))
    if comp == 1:
        Apple()
    elif comp == 2:
        Samsung()
    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(3)
        print("The end...")

def Apple():
    print("Great Choice!")
    time.sleep(3)
    print("Apple is paying you 30 million per year plus bonuses. You could easily retire if you want.")
    time.sleep(3)
    pie = int(input("How many years should Jeff work at Apple?(Up to 10)"))
    if pie == 10:
        print("Great choice!")
        time.sleep(3)
        print("Jeff can now retire comfortably and buy all the things he ever wanted."
              "\n On top of that, at Apple, Jeff tripled the annual revenue. Now, he is a billionaire!")
        time.sleep(5)
        print("You win!")
        time.sleep(2)
        work = "https://uncrate.com/p/2017/01/bel-air-mansion-9.jpg"
        webbrowser.open(work)
    elif pie < 3:
        print("Unfortunately, since Jeff was so new to managing a large scale company, Apple went bankrupt.")
        time.sleep(3)
        print("The end...")
    elif pie > 3 and pie < 10:
        print("That is a great financial move."
              "\nJeff made enough money to retire comfortably, but not enough to be a billionaire.")
        print("The end")
    elif pie > 10:
        print("Jeff got so tired of working at Apple that he killed himself. Should've listened to the rules...")
        time.sleep(5)
        print("The end...")

def Samsung():
    print("Jeff is ecstatic to start working at Samsung!")
    time.sleep(3)
    print("At Samsung, Jeff will be making 100 million per year plus bonuses, over 3 times Apple!"
          "\n In one year, he can make more than enough money to buy everything he's ever wanted!")
    time.sleep(5)
    bad = int(input("How many years should Jeff work at Samsung before he retires?"))
    worse = random.randrange(1, bad)
    time.sleep(3)
    print("Unfortunately, during Jeff's ", worse, "th year of working at Samsung, sales plummeted."
          "\nBecause of this, Jeff decided to take his own life.")
    time.sleep(5)
    print("The end...")

def main():
    print("This is a story about Jeff. Jeff is 9 years old and wants to become a billionaire one day. "
          "\nHis brother, Taylor, and his parents Matt and Kim think he is being ambitious, but he wants "
          "to prove them wrong. You will be joining him on his adventure.")

    time.sleep(3)

    print("Welcome to Jeff's Journey to Becoming a Billionaire!")
    time.sleep(3)

    print("Right now, Jeff is attending a horrible public school called South Pasadena Elementary, which he feels "
          "\nis really holding him back.")

    time.sleep(2)
    print("Jeff recently applied to Harvard Westlake and was accepted."
          "\nThe only thing holding him back is his parent's financial situation."
          "\nThis is why Jeff is torn between attending Harvard Westlake, which would present great new opportunities,"
          "\nor staying at South Pasadena Elementary.")
    school = int(input("Should Jeff 1.(transfer to Harvard Westlake) or 2.(Stay at trashy South Pasadena Elementary)?"))

    if school == 1:
        privateschool()
    elif school == 2:
        publicschool()
    else:
        print("That's not a valid choice. Because you didn't follow the rules, Jeff got murdered.")
        time.sleep(3)
        print("The end...")

main()

