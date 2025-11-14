# DnDCombatHelper
I wanted to automate some of my dice rolls during combat. 
Since I have been wanting to expand my Python skills, I thought using Python for the project would be perfect as I have been learning how to use Python to automate tasks.

# Overview
This project will allow me to streamline the dice process and easily attack and look up spells. Allowing for faster gameplay and more things that can be done in one session!

To reduce complexity, this application will be using the ruleset of Dungeon Crawl Classic

## The basic form:

In the basic form, this program will:
 - Roll a dice as accurately to random as possible
 - Based on a dice roll determine if a spell cast (of any spell) is a fail or succeed based on the dice roll and a bonus
 - Based on a dice roll determine what the outcome of a d20 attack roll is

## More complex:

More complex tasks I wish to achieve are:
   - Entering in all of the spells In the rulebook I am using and then call that method to determine success and its effects.
   - The ability to create [[Characters]] and add, edit, and remove a character bonuses or stats
   - The ability to temporarily reduce or improve stats or remove the ability to use a spell based on real time rolling in the app. This includes resetting those values

## Streach Goals:
   - Make program applicable to all rulesets?
   - Create a GUI to make things pretty and handle the character editing.

 # Current project phase:
Programming is on pause as I do research on how to do UI. Currently, I am exploring PyQT for the UI, as I wish for this project to be built fully in python. However, this may change and I might find a more sutible programming language to do the UI in.

Updates: 
As my college classes get harder, I have not been able to update this project as much. However, I did learn that Python was not the best choice for this application and have been looking into making a Win32 application or porting all of this into a WebApp for my WebApp class. 
11/14/2025:
I have decided not to use a web app because I don't like working with JavaScript. I now have two options: Utilize the fact that Python is built on C and manipulate the linking step to create a multi-programmed EXE file, or rewrite my logic in C++ or C#
