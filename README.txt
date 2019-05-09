OvnisChallenge
Version v0.1.4


------
OvnisChallenge is a coding game of capture the flag. Two teams are competing 
for the victory. The two teams are composed of a base, a flag to defend and two
ovnis. 

Ovnis are controlled with the code user.py. You need to code the best IA 
program to beat your opponent's code.  

To launch the game and try your IA, you need to run OvniChallenge.pyc. Capture 
more flag than your opponent to win a game. A game last less than 1 minute.

You need to have Python 3.7 installed on your computer. You can check it by 
running the Command Prompt and using the command: python --version.
Delete any other version of Python in conflict with the 3.7.
https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe


------
Positions of ovnis are integrated from velocities. Velocities of ovnis are 
integrated from accelerations. Integrations use Euler's formulas. The time step
is 0.01 seconds. Accelerations of ovnis are their motor powers, given by the 
user in the code user.py for each frame. 

Collision between ovnis are non-elastic, with a restitution coefficient of 0.2.
There are repulsions between ovnis when they collide.
Collision with walls are elastic, with a restitution coefficient of 1.1.
There is a natural friction with the ground, with a coefficient of 0.9992.


------
For any further information, please contact gregoire.henry@ipsa.fr.
Please report any bug or suggest any modification to the contact.


------
Game created by Grégoire HENRY.
Inspired from the Thales Hackathon on CodeInGame.
Free to use, free to modify.