Prompt1: Using python, define a GameLogic class with a calculate_score static method and roll_dice static method. The calculate_score method have a parameter that requires a tuple of integers that represents a dice roll, the output from calculate_score should be an integer representing the roll’s score according to the rules of the game farkle. The roll_dice method should have an input of an integer between 1-6 and the output should be a tuple with random values between 1 and 6. The length of the output tuple for roll_dice should match the input argument.



~~~python
#Importing random module 
import random


#initializing/ define the GameLogic class
class GameLogic:
#telling python its static method 
    @staticmethod
    
    #define the calculate score method
    def calculate_score(dice_roll):
        #This line uses a list comprehension to generate a list of the number of times each value (1 to 6) appears in the dice_roll tuple. The count method is used to count the number of occurrences of each value in the tuple.
        dice_counts = [dice_roll.count(i) for i in range(1, 7)]
        #This line initializes a variable "score" to keep track of the total score for the dice roll.
        score = 0
        #This line starts a for loop that iterates over the list of dice counts.
        for count in dice_counts:
            #This line checks if the count for the current value is greater than or equal to 3.
            if count >= 3:
                
                              
            #This line adds the appropriate score for the current value based on the count. If the count is equal to 3, the score is count * 100. If the count is greater than 3, the score is count * 100 * 2.
             if count == 3:
                    score += (count * 100) if count == 3 else (count * 100 * 2)
                else:
                    score += (count * 100 * 2)
                    
                    
            #This line adds the score for values with a count greater than 0 but less than 3. The score is count * 100.       
            elif count > 0:
                score += (count * 100)
        #This line returns the total score for the dice roll.
        return score

    
    #This line defines the roll_dice method as a static method of the GameLogic class. The num_dice parameter is the number of dice to roll.
    @staticmethod
    def roll_dice(num_dice):
        
        
        #This line uses a generator expression to generate a tuple of num_dice random integers between 1 and 6. The randint method from the random module is used to generate the random integers, and the tuple function is used to convert the generator expression to a tuple. The _ in for _ in range(num_dice) is a common Python convention for a throwaway variable.
        return tuple(random.randint(1, 6) for _ in range(num_dice))

~~~












Prompt2:Change calculate_score method  single 5s are worth 50, single 1s are worth 100

~~~python

    @staticmethod
    def calculate_score(dice_roll):
        dice_counts = [dice_roll.count(i) for i in range(1, 7)]
        score = 0
        #allows for the assignment of two different variable during each iteration of the for loop, i = index value and count = the value at i 
        for i, count in enumerate(dice_counts):
            if count >= 3:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)
                else:
                    score += (count * 100 * (i + 1))
                    
            #this adds 100 for 1s and 50 for 5s         
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)
        
        return score


~~~

Prompt3:change calculate_score method so three of a kind of 1s equals 1000 and three of a kind of 5s equals 500 and the score for each doubles with every extra time that number was rolled 

~~~python

        for i, count in enumerate(dice_counts):
            
            if count >= 3:
                #next four lines of code account for values of 1 and 5 when count is greater than or equal to 3 
                if i == 0:
                    score += (1000 * (2 ** (count - 3)))
                elif i == 4:
                    score += (500 * (2 ** (count - 3)))
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)
~~~

note: 

