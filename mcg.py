while True:
    print("-----<MEMORY CARD GAME by- Janhavi Negi>-----".center(100, " "))
    print("<P> Play".center(100, " "))
    print("<I> Instructions".center(100, " "))
    print("<Q> Quit".center(100, " "))
    choice = input("Enter your choice \n <P> \n <I> \n <Q> \n")
    
    if choice in ("p", "P"):
        print("GAME IS RUNNING")
        import random
        L = ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
        ele = ["@", "&", "@", "!", "~", "$", "*", "%", "!", "^", "$", "&", "*", "~", "%", "^"]
        random.shuffle(ele)
        score = 0
        
        while True:
            y = ""
            for a, _ in enumerate(L):
                y += _ + "  "
                if (a + 1) % 4 == 0:
                    y += "\n"
                    
            for i in y.split("\n"):
                print(i.center(100))
            
            ch1 = int(input("Choose the first card: "))
            ch1 -= 1
            while L[ch1]== "_":
                print("-------you cannot choose once card again------- \n So choose again")
                ch1 = int(input("Choose the first card: "))
                ch1 -= 1
            
            card1 = ele[ch1]
            L[ch1] = card1
            
            y = ""
            for a, _ in enumerate(L):
                y += _ + "  "
                if (a + 1) % 4 == 0:
                    y += "\n"        
            for i in y.split("\n"):
                print(i.center(100))
            ch2 = int(input("Choose the second card: "))
            ch2 -= 1
            card2 = ele[ch2]
            while ch1 == ch2:
                print("-------You cannot choose the same card twice------- \n So choose again")
                ch2 = int(input("Choose the second card: "))
                ch2 -= 1
                card2 = ele[ch2]
            
            if card1 == card2:
                score += 1
                print(f"SCORE: {score}")
                L[ch1] = L[ch2] = "_"
                
                if L.count("#") == 0:
                    print("Congratulations! You've matched all the cards!")
                    break
            else:
                print("Try Again")
                L[ch1] = L[ch2] = "#"
                q = input("Do you want to quit the game? <Y/N> ")
                if q in ("y", "Y"):
                    break
    
    elif choice in ("i", "I"):
        print("These are instructions: ")
        print("To find the matching pair of cards from(1-16) \n \n   --->Choose the one card first \n \n   --->Choose the second card right after each other \n \n \n<If you match the cards pairs then your score will increased by one > \n \n \n <If you don't find the right pair , the cards will flip back and you can 'TRY AGAIN'>".center(200, " "))
        
    elif choice in ("q", "Q"):
        q = input("Do you really want to quit the game? <Y/N> ")
        if q in ("y", "Y"):
            break
        else:
            continue   
    else:
        print("INVALID")
