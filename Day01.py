'''
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

def part1():
    total = 0

    with open('Day01_Input.txt') as f:
        for i in range(1000): # check each line
            numArr = []
            str = next(f)

            for j in range(len(str) - 1): # check each character
                curr = str[j:j+1]

                if curr.isdigit(): # if character is digit
                    numArr.append(int(curr))
            
            total += (numArr[0] * 10) + numArr[-1]

    print(total)

#part1()
# solution: 54331



'''--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''

def check1(entry: str, index: int):
    return entry[index:index+3] == "one", 1

def check2(entry: str, index: int):
    return entry[index:index+3] == "two", 2

def check3(entry: str, index: int):
    return entry[index:index+5] == "three", 3

def check4(entry: str, index: int):
    return entry[index:index+4] == "four", 4

def check5(entry: str, index: int):
    return entry[index:index+4] == "five", 5

def check6(entry: str, index: int):
    return entry[index:index+3] == "six", 6

def check7(entry: str, index: int):
    return entry[index:index+5] == "seven", 7

def check8(entry: str, index: int):
    return entry[index:index+5] == "eight", 8

def check9(entry: str, index: int):
    return entry[index:index+4] == "nine", 9

    

# first two letters as key, length of word for definition
numbers = {"on": [3, check1], "tw": [3, check2], "th": [5, check3], "fo": [4, check4], "fi": [4, check5], 
           "si": [3, check6], "se": [5, check7], "ei": [5, check8], "ni":[4, check9]}

def part2():
    total = 0

    with open('Day01_Input.txt') as f:
    #with open('day01test.txt') as f:
        for i in range(1000): # check each line
        #for i in range(7): # check each line
            numArr = []
            line = next(f)

            for j in range(len(line)): # check each character
                curr = line[j:j+1]
                rem = len(line) - j

                if curr.isdigit(): # if character is digit
                    numArr.append(int(curr))
                elif rem > 2 and (line[j:j+2] in numbers) and rem > numbers[line[j:j+2]][0]:
                    # if there are enough letters to do comparision
                    # and the next 2 letters are in the dictionary
                    # and if there are enough letters remaining to contain the word
                    hasIt, value = numbers[line[j:j+2]][1](line, j) #checker(line, j)
                    if hasIt:
                        numArr.append(value)
            
            #print(numArr)       
            #print((numArr[0] * 10) + numArr[-1])
            total += (numArr[0] * 10) + numArr[-1]
    print(total)

part2()
# solution 54518

