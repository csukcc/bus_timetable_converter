# Bus Timetable Converter (CSV to JSON)

## Introduction

This project is a Python 3 script that converts a given bus timetable in CSV format into a JSON file. The goal is to output a JSON file which can be imported into a MongoDB database.

## File structure

Here's a basic overview of the directory:

+ parse.py
    + The main Python script which handles all the conversion from CSV to JSON
+ timetable.pdf
    + The original data found on the Bus website
+ timetable.csv
    + The CSV version of timetable.pdf file (See Useful tools section for more info on how this was created).
+ test.csv and test.json
    + The CSV file is the input file and JSON is the output, this is a simpler problem to work with as it has less data. But it is a subset of timetable.csv.

## Prerequisites

+ Python 3 installed
+ CSV file in the format which is similar to "timetable.csv" and "test.csv" provided in this project

## Useful tools

I did a lot of research on how to convert the timetable.pdf file into a well formatted CSV file. to be honest there isn't a lot of good tools out there, I personally came across 2 that was quick and easy.

1. https://pdftables.com
    + Easy to use
    + Converts PDF to CSV very well
    + However needs to pay for its service after Trial ends

2. http://tabula.technology
    + Requires slightly more work to convert PDF to CSV
    + But it is FREE
