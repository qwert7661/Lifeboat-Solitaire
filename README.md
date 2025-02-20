# Lifeboat-Solitaire
Lifeboat is a solitaire variant in which you sort passengers on a sinking cruise ship into four lifeboats.

Lifeboat is a new game of my own design. I hope you enjoy it!

Ensure that /graphics and /audio files are in the same file location as Lifeboat.py

Requires pygame.

Rules:

Lifeboat is a life-and-death solitaire game where you sort passengers on a sinking cruise ship into four lifeboats. 
As the captain, you will go down with the ship unless you can save every single passenger. 
Here's the catch: the upper-class passengers absolutely refuse to sit next to the lower-class passengers! 
They would rather drown! 

This means that cards can only be placed on a card whose rank differs from theirs by no more than ONE. 
So a Jack may only be placed on another Jack, a Queen, or a Ten. 
Aces are high, and cannot be placed next to 2s or vice-versa. 

There are only 15 spots on each lifeboat, so allocate passengers wisely! 
Overloading a lifeboat will cause it to sink, losing the game. 

When you cannot place a card from the deck on one of the four lifeboats, you must place it in the waiting pile. 
The waiting pile can hold no more than five cards. 

Win the game by emptying the deck and the waiting pile. 

Tip: Try to spread out the card ranks across your four lifeboats. 
With 13 ranks to distribute across 4 boats, if the top cards in each boat was, e.g., 3, 6, 9, and Q, you would be able to seat every card but Aces. 
Likewise, with top cards of 4, 7, 10, and K, you could seat every card but Twos.
That makes these eight ranks more strategically valuable than the other five (2s, 5s, 8s, Js, As). 
Note also that Twos and Aces can only be placed on 2 different ranks, unlike the rest which can be placed on 3 different ranks. 
Try to seat these cards earlier rather than later! 

Good luck, captain!



