# Lab 09 - 
## Author: Ethan Albers and Dominick Martin

### Links and Resources
- Obtained starter code from clas repo
- [ten-thousand repository](https://github.com/ekalbers/ten-thousand.git)

### How to initialize/run your application
~~~
python3 -m env .venv
source .venv/bin/activate
pip install pytest
~~~
#### run:`python3 bots.py`

### Of Note:
- Looking at our code you'll see that there is a lot commented out and our actual bot is extremely basic. We tried to implement a bot that played by a larger list of rules but nothing seemed to be able to beat the original single dual rul bot we made when playing around with the code in the first 15 minutes. I would be interested to go back and take a closer look at the probabilities going on behind the scenes. I think for a game like this, it is a case of less is more... unless you have time to implement an extremely robust bot that uses probabilities to back up its decision making. All in all I think we made the correct decision to keep it simple because we came in 2nd in the class during testing.