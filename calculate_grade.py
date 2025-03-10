import csv
import re
""" Task 1 , we created a function that calculates the grade by returning A,B,C,D,F depending on the corresponding score"""
def calculate_grade(score):
    with open ("csv_score.csv","r") as f:
        reader=csv.reader(f)
        next(reader)
        score=int(score)
        A= 90<=score and score<=100     
        B=score>=80 and score<=89
        C=score>=70 and score<=79 
        D= score>=60 and score<=69
        F=score<60
        if A:
            return 'A' 
        elif B:
                return 'B'  
        elif C:
            return 'C'  
        elif D:
            return 'D' 
        elif F:
            return'F'
        else:  
            print(" Score is outside the range") 
    """
    Task 2, reads a csv file of student names and scores also determines their grades and prints them
    it laso handles errors 
     """
def process_students(filename):
    try:
        with open ("csv_marks.csv") as filename:
            reader=csv.reader(filename)
            next(reader)
            grade=0
            for line in reader:
                grade=calculate_grade(int(line[1]))#implementing the calculate_grade function which converts the score into an intenger and saves it in the variable grade
                print(line[0],grade)#prints the students name which is in index 0 and their grade
    except FileNotFoundError: # handle
        print(" file does not exist")
    except ValueError:
        print(" This is a non numeric score")
        print(" missing a value")

"""Task 3, reads students scores from csv file and calculates the average score, and prints the class average using the calculate_grade function as well as handling errors"""
def calculate_average_grade(filename):
    try:
        with open("csv_marks.csv") as filename:
            reader=csv.reader(filename)
            tempgrade=0 # a variable that receives the output of the calculate_grade function
            sum=0 #acts like a counter for counting the numbers of students in a csv file
            final_score=0 # a variable that stores 
            next(reader)
            for line in reader:
                sum+=1 # iterate number of student names
                final_score+=sum# for adding each number of students to the final_score
                tempgrade=calculate_grade(int(line[1])/final_score)
                print(tempgrade)
    except FileNotFoundError:
        print("file doesn't exist")
    except ValueError:
        print(" Value is invalid")

"""Task 4, counts the number of failing students using regular expressions """
def count_failing_students(filename):
    with open("csv_marks.csv") as filename: # opens the file
        reader=csv.reader(filename) # opens and reads the file
        next (reader) #skips header row
        failing_students=0
        for line in re.findall("[0-5]+",int(line[1])):
            print(line[1])
            failing_students+=1
        print("Number of Falining students:",failing_students)

"""Task 5,asking user for the file name,calling the functions and handling errors"""
def main():
    try:
        file=input(" Enter the files name:")
    except FileNotFoundError:
        print("File not found",file) 
    calculate_grade(95)
    process_students("csv_marks.csv")
    calculate_average_grade("csv_marks.csv")
    count_failing_students("csv_marks.csv") 
      

main()