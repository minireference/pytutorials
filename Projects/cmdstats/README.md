Command stats
=============

Write a program that reads the command usage statistics data from `commands_data.csv`
and convert the counts into probabilities.

Preliminary data checks:

  - Git pull from the
  - How big is the file `commands_data.csv`?
  - How many lines does it have?
  - How many rows of data does it contain?


Project steps:

  - Read about the the Python standard library module `csv`
  - Run `source venv/bin/activate` then `jupyter notebook` to start Jupyter
  - Start script with `import csv`
  - Load csv file and `csv.DictReader`
  - Process the data as needed to compute probabilities for each command
  - create a standalone script that can be run from the command line


Numeric questions:

  - What is the probability of the command `git`?


Bonus points

  - Download data.csv using python:
    https://gist.githubusercontent.com/jvns/def5fbea05f58c0645cd/raw/d19d12570b0ecf6640a487e97443ce4b68d7b4b7/top_200_ish_commands.csv


