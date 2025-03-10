import calculate_grade # imported calculate_grade file to test the functions there(production code)
score=0
A=90<=score<=100
B=80<=score<=90
C=70<=score<=80

""" Test to check negative values """

def test_negative_value():
    #setup
    score=-95
    expected=("No negative values")
    #invoke
    try:
        actual=calculate_grade.calculate_grade(score)
    except FileNotFoundError:
        print(" wrong file ")
    except ValueError:
        print(" Wrong value in enetered") 
    #analyse
    assert expected==actual 

""" Test to check boundary points"""
def test_boundary_value_test():
    #setup
    score=89
    expected="B"
    #invoke
    try:
        actual=calculate_grade.calculate_grade(score)
    except FileNotFoundError:
        print(" file is doesn't exist")
    except ValueError:
        print(" invalid value input")
    #analyse
    assert expected==actual 

"""Test to check valid in range inputs"""

def test_valid_in_range_value():
    A=90<=score<=100
    #setup
    score=98
    expected="A"
    #invoke
    try:
        actual=calculate_grade.calculate_grade(score)
    except FileNotFoundError:
        print(" file is doesn't exist")
    except ValueError:
        print(" invalid value input")
    #analyse
    assert expected==actual 

"""Test to check zero values"""
def test_Zero_value():
    #setup
    filename="csv_marks.csv"
    expected=("No negative values")
    #invoke
    try:
        actual=calculate_grade.process_students(filename)
    except FileNotFoundError:
        print(" wrong file ")
    except ValueError:
        print(" Wrong value in enetered") 
    #analyse
    assert expected==actual



"""Test to check zero values"""
def test_Zero_value_2():
    #setup
    filename="csv_marks.csv"
    expected=("No negative values")
    #invoke
    try:
        actual=calculate_grade.calculate_average_grade(filename)
    except FileNotFoundError:
        print(" wrong file ")
    except ValueError:
        print(" Wrong value in enetered") 
        # what do you mean by exception handling
    #analyse
    assert expected==actual


"""Test to check zero values"""
def test_Zero_value():
    #setup
    filename="csv_marks.csv"
    expected=("No negative values")
    #invoke
    try:
        actual=calculate_grade.count_failing_students(filename)
    except FileNotFoundError:
        print(" wrong file ")
    except ValueError:
        print(" Wrong value in enetered") 
    #analyse
    assert expected==actual














    