import os

year=2017

url = 'https://adventofcode.com/' # I wanted to also download the input with a script, but it did not cooperate
for day in range(1,26):
    os.mkdir(f'day{day}')
    fp = open(f'day{day}/day{day}.py', 'x')
    fp.close()
