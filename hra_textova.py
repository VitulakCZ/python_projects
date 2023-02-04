answer = input("Q = Play City Empire. No God = exit game")
if answer == "Q":
  answer = input("1000 coins: A = castle for 750 coins, B = water Mill for 150 coins, C = house for 50 coins.")
  if answer == "A":
      answer = input("400 coins (+150 by castle): A = you don't have enough money for: upgrade castle for 550 coins, B = water Mill for 150 coins, C = house for 50 coins.")
      if answer == "A":
        print("you don't have enough money!!!!!")

      elif answer == "B":
          answer = input("430 coins (+150 by castle, +30 by water Mill): A = you don't have enough money for: upgrade castle for 550 coins, B = upgrade water Mill for 100 coins, C = house for 50 coins.")
          if answer == "A":
            print("you don't have enough money!!!!")
          elif answer == "B":
            answer = input("515 coins (+150 by castle, +60 by water Mill lvl.2): A = you don't have enough money for: upgrade castle for 550 coins, B = upgrade water Mill for 150 coins, C = house for 50 coins.")
            if answer == "A":
              print("you don't have enough money!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            elif answer == "B":
              answer = input("605 coins (+150 by castle, +90 by water Mill lvl.3): A = upgrade castle for 550 coins, B = upgrade water Mill for 250 coins, C = house for 50 coins.")
              if answer == "A":
                print("CASTLE lvl.1 -> CASTLE lvl.2")
                print("You researched a: mine")
                print("----------------------------")
                answer = input("445 coins (+300 by castle lvl.2, +90 by water Mill lvl.3): A = you don't have enough money for: upgrade castle for 750 coins, B = upgrade water Mill for 250 coins, C = house for 50 coins.")
              elif answer == "B":
                answer = input("630 coins (+150 by castle, +125 by water Mill lvl.4): A = upgrade castle for 550 coins, B = upgrade water Mill for 475 coins, C = house for 50 coins.")
                if answer == "A":
                  print("CASTLE lvl.1 -> CASTLE lvl.2")
                  print("You researched a: mines")
                  print("----------------------------")
                  answer = input("505 coins (+300 by castle lvl.2, +125 by water Mill lvl.4): A = you don't have enough money for: upgrade castle for 750 coins, B = upgrade water Mill for 475 coins, C = house for 50 coins, D = mines for 250 coins.")
                  if answer == "A":
                    print("you don't have enough money!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                  elif answer == "B":
                    answer = input("555 coins (+300 by castle lvl.2, +255 by water Mill lvl.5): A = you don't have enough money for: upgrade castle for 750 coins, B = you don't have enough money for: upgrade water Mill for 925 coins, C = house for 50 coins, D = mines for 250 coins.")
                  elif answer == "C":
                    answer = input("888 coins (+300 by castle lvl.2, +255 by water Mill lvl.5, +8 by house.): A = upgrade castle for 750 coins, B = you don't have enough money for: upgrade water Mill for 925 coins, C = upgrade house for 17 coins.")
                elif answer == "B":
                  answer = input("560 coins (+150 by castle, +255 by water Mill lvl.5): A = upgrade castle for 550 coins, B = you don't have enough money for: upgrade water Mill for 925 coins")
              elif answer == "C":
                answer = input("803 coins (+150 by castle, +90 by water Mill lvl.3, +8 by house): A = upgrade castle for 550 coins, B = upgrade water Mill for 250 coins, C = upgrade house for 17 coins.")
              
          elif answer == "C":
            answer = input("188 coins (+150 by castle, +30 by water Mill, +8 by house): A = you don't have enough money for: upgrade castle for 550 coins, B = upgrade water Mill for 150 coins, C = upgrade house for 17 coins.")

      elif answer == "C":
        answer = input("508 coins (+150 by castle, +8 by house): A = you don't have enough money for: upgrade castle for 550 coins, B = water Mill for 150 coins, C = upgrade house for 17 coins.")
        if answer == "A":
          print("you don't have enough money!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        elif answer == "B":
          answer = input("546 coins (+150 by castle, +8 by house, +30 by water Mill): A = you don't have enough money for: upgrade castle for 550 coins, B = upgrade water Mill for 100 coins, C = upgrade house for 17 coins.")
        elif answer == "C":
          answer = input("657 coins (+150 by castle, +16 by house lvl.2): A = upgrade castle for 550 coins, B = water Mill for 150, C = upgrade house for 34 coins.")


elif answer == "No God":
  print("OK XDDDDDDDDDD")
  answer = input("Do you really want to leave the game? Yes = yes, No = no.")
  if answer == "Yes":
    exit
  elif answer == "No":
    print("You shouldn't have left the game HAHAHAHAHAHA")
    answer = input("Click in cross!")

#mines is for 150 coins (+60 coins)
