# Lifeboat-Solitaire
Lifeboat is a new solitaire game of my own design in which you load passengers on a sinking cruise ship into lifeboats. I hope you enjoy it!

To play, simply unzip Lifeboat-Solitaire-main, open the file and run Lifeboat.exe. Note that first-time launch may take some time as the .exe must install Python on your computer. Ensure that the /Lifeboat_Assets file is in the same file location as Lifeboat.py. Uses pygame.

Rules:

Lifeboat is a life-and-death solitaire variant in which you, the captain, must sort passengers on a sinking cruise ship into one of four lifeboats. As the captain, you will go down with the ship unless you can save every passenger.

The catch is this: upper-class passengers absolutely refuse to sit next to lower-class passengers! They would rather drown!

This means that a card may only be seated on a lifeboat when the card it would be placed atop differs in rank from it by no more than one. Example: a Jack may only be placed atop another Jack, a Queen, or a Ten. Aces are high and cannot be placed atop Twos, nor Twos atop Aces.

When you pick up a card from the deck, you may seat it on a lifeboat or place it in the waiting pile. The waiting pile can hold no more than five cards at a time. You may pick up any cards in the waiting pile at any time.

There are only 15 seats on each lifeboat. Overloading a lifeboat would cause it to sink, so you may not place more cards in a full boat.

Win the game by seating all 52 passengers into lifeboats!

Good luck, captain!



