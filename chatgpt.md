# ChatGPT prompts and responses

## Prompt 1
- PROMPT: Using python, define a GameLogic class with a calculate_score static method and roll_dice static method. The calculate_score method have a parameter that requires a tuple of integers that represents a dice roll, the output from calculate_score should be an integer representing the roll’s score according to the rules of the game farkle. The roll_dice method should have an input of an integer between 1-6 and the output should be a tuple with random values between 1 and 6. The length of the output tuple for roll_dice should match the input argument.

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

## Prompt 2
- PROMPT: Change calculate_score method  single 5s are worth 50, single 1s are worth 100

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0
    
    # ***NEW***
    # allows for the assignment of two different variable during each iteration of the for loop, i = index value and count = the value at i 
    for i, count in enumerate(dice_counts):
        if count >= 3:
            if i == 0:
                score += (count * 100)
            elif i == 4:
                score += (count * 50)
            else:
                score += (count * 100 * (i + 1))
        # ***NEW***            
        # this adds 100 for 1s and 50 for 5s         
        elif count > 0:
            if i == 0:
                score += (count * 100)
            elif i == 4:
                score += (count * 50)
        
    return score
~~~

## Prompt 3
- PROMPT: change calculate_score method so three of a kind of 1s equals 1000 and three of a kind of 5s equals 500 and the score for each doubles with every extra time that number was rolled 

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0
    
    for i, count in enumerate(dice_counts):
        if count >= 3:
            # ***NEW***
            # next four lines of code account for values of 1 and 5 when count is greater than or equal to 3 
            if i == 0:
                score += (1000 * (2 ** (count - 3)))
            elif i == 4:
                score += (500 * (2 ** (count - 3)))
            # ***NOTE***
            # ChatGPT deleted code here used for scoring three of a kind for numbers other than 1 and 5, this will need to be added back in
        elif count > 0:
            if i == 0:
                score += (count * 100)
            elif i == 4:
                score += (count * 50)
    return score
~~~

## Prompt 4
- PROMPT: Change the calculate_score method to account for the fact that three of a kind for numbers other than 1 and 5 are equal to 100 times whatever the number is, and it doubles with every extra occurrence of that number

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0

    for i, count in enumerate(dice_counts):
        if count >= 3:
            if i == 0:
                score += (1000 * (2 ** (count - 3)))
            elif i == 4:
                score += (500 * (2 ** (count - 3)))
            # ***NEW***
            # else statement added to account for numbers other than
            else:
                score += (100 * i * (2 ** (count - 3)))
                # ***NOTE***
                # tests currently not passing due to the fact that i = the index and not the actual number on the dice i needs to equal i + 1
        elif count > 0:
            if i == 0:
                score += (count * 100)
            elif i == 4:
                score += (count * 50)

    return score
~~~

## Prompt 5
- PROMPT: The last result had a slight when using i to multiply it needs to have 1 added to it to make it equal to the number it actually corresponds to on the dice. please fix this.

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0

    for i, count in enumerate(dice_counts):
        if count >= 3:
            if i == 0:
                score += (1000 * (2 ** (count - 3)))
            elif i == 4:
                score += (500 * (2 ** (count - 3)))
            else:
                # ***NEW***
                # line changed to account for i being 1 off of the desired dice value
                score += ((i+1) * 100 * (2 ** (count - 3)))
        elif count > 0:
            if i == 0:
                score += (count * 100)
            elif i == 4:
                score += (count * 50)

    return score
~~~

## Prompt 6
- PROMPT: change the calculate_score method so that if each number is rolled once, otherwise known as a straight, the score is 2000

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0
    
    # ***NEW***
    # added an if statement to check for a straight
    if dice_counts == [1, 1, 1, 1, 1, 1]:
        score = 2000
    else:
        for i, count in enumerate(dice_counts):
            if count >= 3:
                if i == 0:
                    score += (1000 * (2 ** (count - 3)))
                elif i == 4:
                    score += (500 * (2 ** (count - 3)))
                else:
                    score += ((i+1) * 100 * (2 ** (count - 3)))
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)

    return score
~~~

## Prompt 7
- PROMPT: change calculate_score so that if there are three pairs rolled, the score is 1500

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0

    # ***NEW***
    # This response from ChatGPT will not work becuase it is accounting for pairs of 1, 2, and 3, not 3 pairs from any 6 numbers
    if dice_counts == [2, 2, 2, 0, 0, 0]:
        score = 1500
    elif dice_counts == [1, 1, 1, 1, 1, 1]:
        score = 2000
    else:
        for i, count in enumerate(dice_counts):
            if count >= 3:
                if i == 0:
                    score += (1000 * (2 ** (count - 3)))
                elif i == 4:
                    score += (500 * (2 ** (count - 3)))
                else:
                    score += ((i+1) * 100 * (2 ** (count - 3)))
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)

    return score
~~~

## Prompt 8
- PROMPT: The last response only accounts for if pairs of 1, 2, and 3 are rolled, I need it to work with any combination of 3 pairs
  - this code is close but obviously it is checking for an extra pair, the sorted `dice_coutns` list should look like this: `[0, 0, 0, 2, 2, 2]`
  - I attempted to get ChatGPT to fix its mistake but it couldn't quite figure out the problem so I ended up just giving it the correct answer

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0

    # ***NEW***
    # changed to check the sorted array but added an extra pair for some reason
    if sorted(dice_counts) == [0, 0, 2, 2, 2, 2]:
        score = 1500
    elif dice_counts == [1, 1, 1, 1, 1, 1]:
        score = 2000
    else:
        for i, count in enumerate(dice_counts):
            if count >= 3:
                if i == 0:
                    score += (1000 * (2 ** (count - 3)))
                elif i == 4:
                    score += (500 * (2 ** (count - 3)))
                else:
                    score += ((i+1) * 100 * (2 ** (count - 3)))
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)

    return score
~~~

## Prompt 9
- ***** Before prompt 9 I gave ChatGPT the solution to the issue with the sorted list in the code above
- PROMPT: change the calculate_score method to double the score if there are two three of a kinds
  - so ChatGpt actually did what I asked for but it also added some funky stuff.
    - The top of the if statement it tries to check for three different 3 of a kinds, this does not make sense as this would mean we rolled the dice 9 times, this code will always be skipped so i removed it.
    - even though I told ChatGPT it needed to change sorted `dice_counts` list when checking pairs to `[0, 0, 0, 2, 2, 2]` and it acknowledged and printed out a new method, it reverted back to the wrong list here.

~~~python
@staticmethod
def calculate_score(dice_roll):
    dice_counts = [dice_roll.count(i) for i in range(1, 7)]
    score = 0
    # ***NEW*** added a counter for instances of 3 of a kind
    three_of_a_kind_count = 0
    
    # ***NEW***
    # added this interesting if statement to check if there are three 3 of a kinds...
    if sorted(dice_counts) == [0, 0, 0, 3, 3, 3]:
        score = 2500
    elif sorted(dice_counts) == [0, 0, 2, 2, 2, 2]:
        score = 1500
    elif dice_counts == [1, 1, 1, 1, 1, 1]:
        score = 2000
    else:
        for i, count in enumerate(dice_counts):
            if count >= 3:
                if i == 0:
                    score += (1000 * (2 ** (count - 3)))
                elif i == 4:
                    score += (500 * (2 ** (count - 3)))
                else:
                    score += ((i+1) * 100 * (2 ** (count - 3)))
                # ***NEW*** adds one to the 3 of a kind counter
                three_of_a_kind_count += 1
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)

        # ***NEW***
        # if statement to check to see how many times the loop ended up in the count >= 3 if statement, multiplies score by 2 if the count equals 2
        if three_of_a_kind_count == 2:
            score *= 2

    return score
~~~
