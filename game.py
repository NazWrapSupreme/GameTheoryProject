import numpy as np
from pandas import *
from sympy import Symbol
from sympy.solvers import solve
import random 

class gameTheory:

    
   def RandomMode(row, col):
       counter = 1
       Player1Strategy = list()
       print("------------------------------------")
       print ("Player: Player 1's strategies")
       print ("{", end="")
       for n in range(row):
           Player1Strategy.append("A"+ str(counter))
           print ("A", counter, sep ="", end="")
           print (" ", end="")
           counter = counter + 1
       print ("}")
      
       print("------------------------------------")
       print ("\n")
       print("------------------------------------")
       print("Player: Player 1's payoffs")
       Player1PayOff = np.random.randint(-99,99, (row,col))      
       Player1Temp = [[str(y) for y in x] for x in Player1PayOff]

       Player1DataFrame = DataFrame(Player1PayOff)
       print (Player1DataFrame)
       counter = 1
       print("------------------------------------")
       print("\n")
       print("------------------------------------")
       print ("Player: Player 2's strategies")
       print ("{", end="")
       Player2Strategy = list()
       for m in range(col):
           Player2Strategy.append("B"+ str(counter))
           print ("B", counter, sep ="", end="")
           print (" ", end="")
           counter = counter + 1
       print ("}")


       print("------------------------------------")
       print ("\n")
       print("------------------------------------")
       print("Player: Player 2's payoffs")
       Player2PayOff = np.random.randint(-99,99, (row,col))
       Player2Temp = [[str(y) for y in x] for x in Player2PayOff]
       Player2DataFrame = DataFrame(Player2PayOff)

       print (Player2DataFrame)
       print("------------------------------------")
       print ("\n")

       Gambit = np.array([zip(a,b) for a,b in zip(Player1PayOff,Player2PayOff)])
       tempGambit = np.array([zip(k,l) for k,l in zip(Player1Temp,Player2Temp)])
       L = list(Gambit)
       TempL = list(tempGambit)
       print("=======================================")
       print("Display Normal Form")
       print("=======================================")
       display1 = DataFrame(L)
       display1.index = Player1Strategy
       display1.columns = Player2Strategy
       print(display1)
       mystring = ""

       for c in range(col):
           max = np.max(Player1PayOff[:,c])
           nash1 = np.argmax(Player1PayOff[:,c])
           Player1Temp[nash1][c] = 'H'
          
     
       for r in range(row):
           max = np.max(Player2PayOff[r,:])
           nash2 = np.argmax(Player2PayOff[r,:])
           Player2Temp[r][nash2] = 'H'

       print ("\n")
       print("=======================================")   
       print("Nash Pure Equilibrium Locations:")
       print("=======================================")
       Nash = DataFrame(TempL)
       Nash.index = Player1Strategy
       Nash.columns = Player2Strategy
       print (Nash)
       print("\n")

       IsnashEq = False
       for row in Nash.itertuples():
           for col in range(col):              
               if(getattr(row, Nash.columns[col]) == ('H', 'H')):
                   (r,c) = (row.Index, Nash.columns[col])
                   (n1, n2) = (r,c)
                   IsnashEq = True
                   print ("Nash Equilibrium(s): ", (r, c))
      
       print("\n")
       belief1 = np.round(np.random.dirichlet(np.ones(col),size=1), decimals = 2)
       belief1 = belief1.reshape(-1)

       expPay1 = list()
       expSum = 0
       check = 0
    
       brSum1 = list()
       maxPlayer1PayOff = np.round(Player1PayOff[0][0] * belief1[0], decimals=2)
       maxRow = ""
       for r in range(row):
           for c in range(col):
                calc = np.round(Player1PayOff[r][c] * belief1[c], decimals= 2) 
                if(check != col):
                    expSum = calc + expSum
                    check+= 1
                if(check == col):
                    brSum1.append(round(expSum, 2))
                    expSum = 0
                    check = 0

                expPay1.append(calc)
       index  = np.argmax(brSum1)
       maxRow = Nash.index[index]
       belief2 = np.round(np.random.dirichlet(np.ones(row),size=1), decimals = 2)
       belief2 = belief2.reshape(-1)
       print("---------------------------------------------")
       print("Player1 Expected Payoffs with Player 2 Mixing")
       print("---------------------------------------------")
       
       for var in range(row):
            print("U(" + Player1Strategy[var] + ",", belief1, "=", brSum1[var])
       print("\n")
    
       print("-------------------------------------------")
       print("Player1 Best Response with Player 2 Mixing")
       print("-------------------------------------------")
       print("BR", belief1, "= {",maxRow,  "}")
       print("\n")


       expPay2 = list()
       brSum2 = list()
       expSum = 0
       check = 0
       maxPlayer2PayOff = np.round(Player2PayOff[0][0] * belief2[0], decimals=2)
       for c in range(col):
           for r in range(row):
                calc = np.round(Player2PayOff[r][c] * belief2[r], decimals= 2) 
                if(check != row):
                    expSum = calc + expSum
                    check+= 1
                if(check == row):
                    brSum2.append(round(expSum, 2))
                    expSum = 0
                    check = 0
                expPay2.append(calc)

       print("---------------------------------------------")
       print("Player2 Expected Payoffs with Player 1 mixing")
       print("---------------------------------------------")
       
       for v in range(col):
            print("U(" + Player2Strategy[v] + ",", belief2, "=", brSum2[v])
       print("\n")
       index2 = np.argmax(brSum2)
       maxCol = Nash.columns[index2]

       
       print("-------------------------------------------")
       print("Player2 Best Response with Player 1 mixing")
       print("-------------------------------------------")
       print("BR", belief2, "= {", maxCol, "}")
       print("\n")

       mixedPlayer1PayOff = 0
       mixedPlayer2PayOff = 0
       for r1 in range(row):
           mixedPlayer1PayOff = (brSum1[r1] * belief2[r1]) + mixedPlayer1PayOff
           mixedPlayer2PayOff = (brSum2[r1] * belief1[r1]) + mixedPlayer2PayOff

       

       print("------------------------------------------------------")
       print("Player 1 & 2 Expected Payoffs with both Player Mixing")
       print("-------------------------------------------------------")
       print("Player 1 -> U", belief2, ",",belief1, "=", round(mixedPlayer1PayOff,2))
       print("Player 2 -> U", belief2, ",",belief1, "=", round(mixedPlayer2PayOff,2))
       print("\n")

       if(row == 2 and col == 2):

            if(IsnashEq):
                print("------------------------------------------------------")
                print("Nash Pure Equilibrium Location")
                print("-------------------------------------------------------")
                print (Nash)
                print("-------------------------------------------------------")
                print("Nash Equilibriums: ", (n1,n2))
                print("\n")
                print("----------------------------------------------")
                print("Player 1 & 2 Indifferent Mix Probabilities")
                print("----------------------------------------------")
                print("Normal Form has Pure Strategy Equilibrium\n")
            else:
                print("------------------------------------------------------")
                print("Player 1 & 2 Indifferent Mix Probabilities")
                print("-------------------------------------------------------")
                q = Symbol('q')
                p = Symbol('p')
                firstEq = solve(q * Player1PayOff[0][0] + (1-q) * Player1PayOff[0][1] - (q * Player1PayOff[1][0] + (1-q) * Player1PayOff[1][1]))
                dec1 = round(float(firstEq[0]), 2)
                diff1 = round(1-dec1 ,2)
                secondEq = solve(p * Player2PayOff[0][0] + (1-p) * Player2PayOff[1][0] - (p * Player2PayOff[0][1] + (1-p) * Player2PayOff[1][1]))
                dec2 =  round(float(secondEq[0]), 2)
                diff2 = round(1-dec2 ,2)

                print ("Player 1 probability of strategies (" + Player1Strategy[0] + ") =", dec1)
                print ("Player 1 probability of strategies (" + Player1Strategy[1] + ") =", diff1)
                print ("Player 2 probability of strategies (" + Player2Strategy[0] + ") =", dec2)
                print ("Player 2 probability of strategies (" + Player2Strategy[1] + ") =", diff2)
                print("\n")
                print("------------------------------------------------------")
                print("Nash Pure Equilibrium Location")
                print("-------------------------------------------------------")
                print (Nash)
                print("-------------------------------------------------------")
                print ("Nash Equilibrium(s): None\n")
            

   def payOffManual(row, col):
        counter = 1
        Player1Strategy = list()
        for n in range(row):
           Player1Strategy.append("A"+ str(counter))
           counter+=1
        Player2Strategy = list()
        list1 = list()
        counter = 1
        for j in range(col):
            Player2Strategy.append("B"+ str(counter))
            counter+=1
        manualPay1 = np.empty((row,col), object)
        for x in range(row):
            for y in range(col):
                print("Enter payoff for (", Player1Strategy[x], ", ", Player2Strategy[y], ") = ", end="")
                manualPay1[x,y] = tuple(map(str,input().split(',')))
        normForm = DataFrame(manualPay1)
        normForm.index = Player1Strategy
        normForm.columns = Player2Strategy
        #manualPay1 = manualPay1.reshape(-1)
        # Player1Temp = [[tuple(int(y) for y in x) for x in manualPay1]]
        # print("Temp", Player1Temp)
        print(manualPay1)
        max1 = 0
        max2 = 0

        for n in range(row):
            max1 = 0 
            for m in range(col):
                x,y = manualPay1[n,m]
                newV = int(x)
                if(newV > max1):
                    max1 = newV
                    

               
        print(max1)
        print("=======================================")
        print("Display Normal Form")
        print("=======================================")
        print(normForm)
        print("\n")
        


        print("=======================================")   
        print("Nash Pure Equilibrium Locations:")
        print("=======================================")


        nashEqExists = False
        for row in normForm.itertuples():
           for col in range(col):              
               if(getattr(row, normForm.columns[col]) == ('H', 'H')):
                   (r,c) = (row.Index, normForm.columns[col])
                   (n1, n2) = (r,c)
                   nashEqExists = True
                   print ("Nash Equilibrium(s): ", (r, c))
        
   





