# CS664-Project1 Phase2 Connect4

This project aims to simulate a game of Connect4 using the minmax algorithm. The game is played between the user and the AI with the user going first. All the rules of the game are followed during the process (A, Ibsen, & Zhang, 2003). The purpose of the agent is to defend the player’s and to avoid losing the game. In order to check for the winning move, the agent must check diagonally, vertically and horizontally to see if the player has a possibility of having 4 disks in row, if so the agent must place a disk and stop the player form winning. 

## Heuristic:
As highlighted in phase 1, the emphasis of the program would be on the MinMax algorithm using the heuristic - where a win would be evaluated higher than a draw, which must be evaluated higher than a loss. 
While testing the program, it seemed easier to test if the program was defensive, i.e. the agent’s purpose is to avoid a defeat. A loss would have a higher weightage compared to a win. For this purpose, the [1,5,10] weightage was assigned to the opponent’s move as opposed to the initial [1,1,5,10] to the agent’s moves. If the opponent had 1 disk, it was given a weightage 1 and if there were 2 disks, then weightage would be 5, and if there were 3 disks, the weightage would be 10. (A, Ibsen, & Zhang, 2003)The resulting move would be assigned the weighted sum of the other squares in the combination. However, the algorithm still checks for the next move only. 
I also ended up assigning weightage to the players as well. Player 1’s moves were given a weightage of 2 while player 2’s moves were given a weightage of 1. I thought this was best approach to keep the agent defensive while still considering the agent’s own moves as well.
## Algorithm Code:
In phase 1, I also proposed using a switch(case) to iterate through the board in different directions while trying to identify the most winnable combinations. This approach was not very efficient as all 3 validations need to be made during each turn and we have to hard code the combinations as well. Instead, I made use of an ndarray which would allow us to easily iterate the board and also pin point each location of a square. I was also able to find some reference code that I was able to reference upon while building my winning combination arrays.
The obvious benefit of this approach was grouping of possible wins from one particular square as implemented in rev_segment[] under tables.py. Ideally, I should have been able to use each entry in the rev_segment[] and identify the exact move by identifying the common square in all the combinations with the highest weighted sum. However, I was unable to implement this and as result the agent currently picks up a combination and the square at random. 
## AI vs AI:
In the initial design, I had also hoped that it would be easier to code an AI vs AI game and while, it does seem easier to have a program working without the user input, it was a lot more difficult to test. There are few random factors also involved in the selecting the winning move, it would have not allowed for a thorough testing to check what part of algorithm was working and what was not. 
Winning Move:
At the time of phase 1 what I didn’t seem to account for the possibility of multiple squares having the same weighted sum. So, to identify the winning move much better, it seems we need another heuristic to pick the winning move (A, Ibsen, & Zhang, 2003). However, for this case, we picked a winning combination at random. An example is discussed in Appendix 1. 

# Tools:
Python 3.6 – Language used to code the program. Since there was a lot of reference material available in python, it was a much easier language to use to implement this program. The language also has multiple frameworks such as Numpy (explained later) that can be leveraged while iterating through a large array multiple times. 
Shortcomings – I mainly have coded in Java in my past and wasn’t very comfortable using python. Also, since I have had no experience with java, it was difficult for me to work with the more complex frameworks which would have built a more effective agent.
Spyder -  I used Spyder IDE. The tool is extremely popular and I have used the same in the past, so it was just a matter of familiarity.
Numpy – It is a Python package used to scientific computation. It was extremely useful for me to code the evaluate.py which evaluates the best move to be made by the agent. The package allowed to effectively iterate through the board and the multiple combinations of the possible winning moves.

# What did not work well:
1.	As mentioned under design and in Appendix 2, since the agents picks all the possible squares with the highest weighted sum, sometimes, it picks a square in the diagonal combination, which may not be a possible move in the next turn. 

2.	Random picking of the move from the select array
Similar to point 1, random picking of the move doesn’t make the agent 100% effective.

3.	AI vs AI 
As discussed earlier, this was a little harder to implement than initially anticipated.

4.	GUI – HTML
There was not enough time to implement.

# What did work:
1.	the rev_segments allowed easy grouping of all winning combinations for a move. 
2.	Using a game helped better understand the logic that’s needs to be used in the program
3.	The AI is able to defend against most moves
4.	The game works as per expectation
5.	I was unable to develop the AI vs Agent or develop GUI for the program.

# Reference:
1. A, R., Ibsen, E., & Zhang, C. (2003, December 15). A connect four playing AI agent: algorithm and creation process.<br>
2. Dignum, F., Westra, J., van Doesburg, W. A., & Harbers, M. (2009). Games and Agents: Designing Intelligent Gameplay. International Journal of Computer Games Technology, 18. <br>
3. Github. (n.d.). Retrieved from https://github.com/duilio/c4 <br>
4. MIT. (2010, March). Retrieved from web.mit.edu: http://web.mit.edu/sp.268/www/2010/connectFourSlides.pdf <br>
5. Pearce, A. (n.d.). Connect 4 AI: How it woks. Retrieved from https://roadtolarissa.com/connect-4-ai-how-it-works/ <br>
6. Russell, S., & Norvig, P. (2010). Artificial Intelligence: A Modern Approach. <br>
7. Sambati, M. (2013). Connect 4. Retrieved from blogs.skicelab.com: http://blogs.skicelab.com/maurizio/connect-four.html <br>
8. Saveski, M. (2009). AI Agent for Connect Four. Retrieved from web.media.mit.edu: http://web.media.mit.edu/~msaveski/projects/2009_connect-four.html<br>
9. Suhartono, D., Wibisono, R., Elvaretta, V., & Willy. (n.d.). A comparison between Greedy and Minimax algorithm in Two Players Game. Retrieved from http://thesis.binus.ac.id/doc/Lain-lain/2013-1-00553-IF%20WorkingPaper001.pdf <br>
10. University of Notre Dame. (n.d.). Project 01: Connect 4. Retrieved from https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html

