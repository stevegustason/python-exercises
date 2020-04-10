import random, os, sys

os.system("color 2F")

global chips
global play_again
chips=50
play_again="y"

class Starter:
    def __init__(self):
        self.card=("  ","0"," 2"," 3"," 4"," 5"," 6"," 7"," 8"," 9","10"," J"," Q"," K"," A")
        self.total_bet=0

    def blank_space(self):
        global chips
        print("")
        print("")        
        print("")
        print("")
        print("             ____  _            _    _            _    ")
        print("            |  _ \| |          | |  (_)          | |   ")
        print("            | |_) | | __ _  ___| | ___  __ _  ___| | __")
        print("            |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /")
        print("            | |_) | | (_| | (__|   <| | (_| | (__|   < ")
        print("            |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ ")
        print("                                   _/ |                ")
        print("                                  |__/                 ")
        print("")
        print("                                                          Chips:", chips)
        
        
    def main(self):
        global chips
        self.computer_card_1=random.randint(2,14)
        self.computer_card_2=random.randint(2,14)
        self.player_card_1=random.randint(2,14)
        self.player_card_2=random.randint(2,14)
        self.player_hit_1=random.randint(2,14)
        self.player_hit_2=random.randint(2,14)
        self.computer_hit_1=random.randint(2,14)
        self.computer_hit_2=random.randint(2,14)
        s.blank_space()
        ante=5
        chips -= ante
        print("5 chip ante taken...")
        print("                                                          Chips:", chips)
        print ("Dealer Cards:")
        print ("""              ___       ___ 
             | """+str(self.card[0])+"""|     | """+str(self.card[self.computer_card_2])+"""|       
             |___|     |___|""")
        print("")
        print ("Your Cards:")
        print ("""              ___       ___ 
             | """+str(self.card[self.player_card_1])+"""|     | """+str(self.card[self.player_card_2])+"""|       
             |___|     |___|""")
        print("")
        self.computer_total = 0
        self.player_total= 0
        self.choice_1=0
        self.choice_2=0
        self.comp_choice=0
        self.running_player_total=0
        ante=5
        chips -= ante
        
    def bet(self):
        global chips
        bet=eval(input("How much would you like to bet? "))
        self.total_bet=self.total_bet+bet

    def hit_choice(self):
        self.choice_1=input("Would you like to hit?(y/n) ")
        if self.choice_1==str("y"):
            s.blank_space()
            print ("Dealer Cards:")
            print ("""              ___       ___ 
             | """+str(self.card[0])+"""|     | """+str(self.card[self.computer_card_2])+"""|       
             |___|     |___|""")
            print("")
            print ("Your Cards:")
            print ("""              ___       ___       ___ 
             | """+str(self.card[self.player_card_1])+"""|     | """+str(self.card[self.player_card_2])+"""|     | """+str(self.card[self.player_hit_1])+"""|       
             |___|     |___|     |___|""")
            print("")
            s.ace_check_1()
            s.lose_check()
            #s.bet()

        else:
            self.player_hit_1=0
            self.player_hit_2=0
            
    def hit_choice_2(self):
        if self.choice_1==str("y") and self.running_player_total<22:
            self.choice_2=input("Would you like to hit again?(y/n) ")
            if self.choice_2=="y":
                pass
            else:
                self.player_hit_2=0
        else:
            pass

    def lose_check(self):
        global chips
        global play_again
        pc1=self.player_card_1
        pc2=self.player_card_2
        ph1=self.player_hit_1
        if pc1>10 and pc1<14:
            pc1=10
        if pc1==14:
            pc1=11
            
        if pc2>10 and pc2<14:
            pc2=10
        if pc2==14:
            pc2=11
            
        if ph1>10 and ph1<14:
            ph1=10
        if ph1==14:
            ph1=11

        self.running_player_total=pc1+pc2+ph1
        
        if self.running_player_total >21:
            print ("Bust!")
            print("Dealer wins...")
            print ("Computer: ", self.computer_total)
            print ("You: ", self.player_total)
            chips=chips-self.total_bet
            print("                                                          Chips:", chips)
            input("Press enter")
            s.lose()
            
        else:
            pass
        
    def total(self):
        cc1=self.computer_card_1
        cc2=self.computer_card_2
        pc1=self.player_card_1
        pc2=self.player_card_2
        ph1=self.player_hit_1
        ph2=self.player_hit_2
        ch1=self.computer_hit_1
        ch2=self.computer_hit_2
        if cc1>10 and cc1<14:
            cc1=10
        if cc1==14:
            cc1=11
            
        if cc2>10 and cc2<14:
            cc2=10
        if cc2==14:
            cc2=11
            
        if pc1>10 and pc1<14:
            pc1=10
        if pc1==14:
            pc1=11
            
        if pc2>10 and pc2<14:
            pc2=10
        if pc2==14:
            pc2=11
            
        if ph1>10 and ph1<14:
            ph1=10
        if ph1==14:
            ph1=11
            
        if ph2>10 and ph2<14:
            ph2=10
        if ph2==14:
            ph2=11
            
        if ch1>10 and ch1<14:
            ch1=10
        if ch1==14:
            ch1=11
            
        if ch2>10 and ch2<14:
            ch2=10
        if ch2==14:
            ch2=11
        self.computer_total = cc1+cc2
        self.player_total= pc1+pc2+ph1+ph2

        if self.computer_total>21:
            if cc1==11:
                cc1=1
            if cc1==11:
                cc2=1
            if ch1==11:
                ch1=1
            if ch2==11:
                ch2=1
        if self.player_total>21:
            if pc1==11:
                pc1=1
            if pc2==11:
                pc2=1
            if ph1==11:
                ph1=1
            if ph2==11:
                ph2=1

    def comp_hit(self):
        if self.computer_total<=16:
            self.comp_choice=1
            self.computer_hit_2=0
            self.computer_total+=self.computer_hit_1
            if self.computer_total<=16:
                self.comp_choice=2
                self.computer_total += self.computer_hit_2
            else:
                pass
        else:
            pass
                
    def ace_check_1(self):
        pc1=self.player_card_1
        pc2=self.player_card_2
        ph1=self.player_hit_1
        if pc1>10 and pc1<14:
            pc1=10
        if pc1==14:
            pc1=11
            
        if pc2>10 and pc2<14:
            pc2=10
        if pc2==14:
            pc2=11
            
        if ph1>10 and ph1<14:
            ph1=10
        if ph1==14:
            ph1=11

        running_total=pc1+pc2+ph1

        if self.running_player_total>21 and pc1==11:
            pc1=1
        if self.running_player_total>21 and pc2==11:
            pc2=1
        if self.running_player_total>21 and ph1==11:
            ph1=1
        

    def final_cards(self):
        if self.comp_choice==2:
            s.blank_space()
            print ("Dealer Cards:")
            print ("""              ___       ___       ___       ___ 
             | """+str(self.card[self.computer_card_1])+"""|     | """+str(self.card[self.computer_card_2])+"""|     | """+str(self.card[self.computer_hit_1])+"""|     | """+str(self.card[self.computer_hit_2])+"""|        
             |___|     |___|     |___|     |___|""")
            print("")
        
        elif self.comp_choice==1:
            s.blank_space()
            print ("Dealer Cards:")
            print ("""              ___       ___       ___ 
             | """+str(self.card[self.computer_card_1])+"""|     | """+str(self.card[self.computer_card_2])+"""|     | """+str(self.card[self.computer_hit_1])+"""|       
             |___|     |___|     |___|""")
            print("")
        
        elif self.comp_choice==0:
            s.blank_space()
            print ("Dealer Cards:")
            print ("""             ___       ___
            | """+str(self.card[self.computer_card_1])+"""|     | """+str(self.card[self.computer_card_2])+"""|
            |___|     |___|""")
            print("")


        if self.choice_1=="y" and self.choice_2=="n":
            print ("Your Cards:")
            print ("""              ___       ___       ___ 
             | """+str(self.card[self.player_card_1])+"""|     | """+str(self.card[self.player_card_2])+"""|     | """+str(self.card[self.player_hit_1])+"""|       
             |___|     |___|     |___|""")
            print("")
            
        elif self.choice_1=="n":
            print ("Your Cards:")
            print ("""              ___       ___
             | """+str(self.card[self.player_card_1])+"""|     | """+str(self.card[self.player_card_2])+"""|       
             |___|     |___|""")
            print("")
            
        elif self.choice_2=="y":
            print ("Your Cards:")
            print ("""              ___       ___       ___       ___ 
             | """+str(self.card[self.player_card_1])+"""|     | """+str(self.card[self.player_card_2])+"""|     | """+str(self.card[self.player_hit_1])+"""|     | """+str(self.card[self.player_hit_2])+"""|        
             |___|     |___|     |___|     |___|""")
            print("")

        else:
            print ("Your Cards:")
            print ("""              ___       ___        ___ 
             | """+str(self.card[self.player_card_1])+"""|     | """+str(self.card[self.player_card_2])+"""|     | """+str(self.card[self.player_hit_1])+"""|       
             |___|     |___|     |___|""")
            print("")

    def winner(self):
        global chips
        global play_again
        if self.player_total >21:
            print("Dealer wins...")
            print ("Computer: ", self.computer_total)
            print ("You: ", self.player_total)
            chips=chips-self.total_bet
            print("                                                          Chips:", chips)
            s.lose()
            play_again=input("Play again?(y/n) ")


        elif self.player_total<22 and self.computer_total >21:
            print("You Win!")
            print ("Computer: ", self.computer_total)
            print ("You: ", self.player_total)
            chips=chips+self.total_bet
            print("                                                          Chips:", chips)
            play_again=input("Play again?(y/n) ")
        
        elif self.computer_total>=self.player_total:     
            print("Dealer wins...")
            print ("Computer: ", self.computer_total)
            print ("You: ", self.player_total)
            chips=chips-self.total_bet
            print("                                                          Chips:", chips)
            s.lose()
            play_again=input("Play again?(y/n) ")
            
        elif self.player_total>self.computer_total:
            print("You Win!")
            print ("Computer: ", self.computer_total)
            print ("You: ", self.player_total)
            chips=chips+self.total_bet
            print("                                                          Chips:", chips)
            play_again=input("Play again?(y/n) ")

    def lose(self):
        global play_again
        if chips>0:
            pass
        else:
            print("")
            print("          _____                         ____      ")           
            print("         / ____|                       / __ \                ")
            print("        | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __") 
            print("        | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
            print("        | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ | ")  
            print("         \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_| ")
            print("")

            input()
            sys.exit()

while play_again=="y":
        s=Starter()
        s.main()
        s.bet()
        s.hit_choice()
        s.hit_choice_2()
        s.total()
        s.comp_hit()
        s.final_cards()
        s.winner()
