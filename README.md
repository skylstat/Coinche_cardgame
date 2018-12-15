# Coinche_cardgame

Old python project where I coded a famous card game highly popular amoung french southerners, called La Coinche. 
I started by implementing basic artificial intelligences based on simple decisions.I intend to develop new AI 
based on genetic algorithms and Reinforcement Learning.

Rules of the Coinche :

La Coinche is a strategic game similar to the Bridge. In Coinche, players must evaluate their hands and estimate 
the number of points they think they can reach in the game. Players make contracts and the ads have a major role in the game.


How to play coinche:
- You need 4 players
- Number of cards = 32 
- End of the game, when one of the teams reaches 701 points. 

The goal of the Coinche :
The goal of the game is to score more points than the opposing team. The winning team must realize the contract 
announced to win a round, and also realize at least 82 points of fold without announcement and belote-rebelote. 
The first team to reach a minimum of 701 points wins the game. In the case, both teams exceed 701 points, the one 
with the highest score wins the game. 

The distribution of cards :
On iBelote.com maps are distributed automatically. They are thrown in a counterclockwise direction. At La Coinche, 
all cards are dealt at the beginning of the round. Each player received 8 cards, 3 first cards then 2 then 3.

Auctions :
The player to the left of the dealer starts. He can either pass his turn or announce a contract according to his cards.
Once the player has announced a contract or has passed the nex player may announce a higher contract or pass.
No advertised contract can be canceled. The team having announced the highest contract determines the color of the trump. 
The auction ends after 3 consecutive "Passes" if you have announced one of the players or if all players have announced
passes in the first round. The last announced contract wins and the game phase can begin.

For the trump color player can choose between: 
One of the four colors; 
All trump (AT) - all colors are trump, no color stronger than others; 
No trump (NT) - for all colors is applied rules for a color other than the asset, no color is greater than the others
After a first bid by one of the players, one of the opposing players may announce Coinche. This assumes that the player thinks that the opponent will not realize his contract. A surcoinche can be made by the team that announced the auction, if the opposite player announces Coinche and the team feels certain to realize the contract that it announces.
