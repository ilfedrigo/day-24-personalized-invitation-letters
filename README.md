# Automated Personalized Invitation Letters

This project is part of my 100 days of code in Python, and it represents my 24th day.

## Overview

- The goal of this project is to automate the process of generating personalized invitation letters. 
- The script reads a list of names from ./Input/Names/invited_names.txt and utilizes a template letter from ./Input/Letters/starting_letter.txt. 
- For each name in the list, the program creates a personalized invitation letter by replacing the placeholder [name] in the template with the individual's name. The resulting letters are then saved in the ./Output/ReadyToSend/ directory.

## How it Works

- The script reads the list of names from ./Input/Names/invited_names.txt.
- It reads the template letter from ./Input/Letters/starting_letter.txt.
- For each name in the list, it replaces the [name] placeholder in the template with the individual's name.
- The personalized letters are saved in the ./Output/ReadyToSend/ directory.
