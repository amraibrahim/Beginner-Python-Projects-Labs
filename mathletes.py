# mathletes.py
# CSMC 254
# Amra Ibrahim

#function heading
def evaluateTeams(students_data):
    test_counts = {}
    students_counts = {}
    
    #For loop to find student tests 
    for student, tests in students_data.items():
        for test in tests:
            if test in test_counts:
                test_counts[test] += 1
            else:
                test_counts[test] = 1 
        
        # Count the tests taken by students
        student_counts[student] = len(tests)
        
    # Student not meeting the criteria or not taking enough tests
    tests_not_of_criteria = []
    students_not_taking_enough_tests = []

    for test, count in test_counts.items():
        if count != 3:
            if count < 3:
                tests_not_of_criteria.append(f"{test} is under")
        else:
                tests_not_of_criteria.append(f"{test} is over")
                
        for student, test_count in student_counts.items():
            if test_count != 3:
                students_not_taking_enough_tests.append(student)
   
    for student in students:
        if len(student['tests']) < 3:
            issues.append({'student': student['name'], 'tests_taken': len(student['tests'])})
    
    return issues

if __name__ == "__main__": 
    students_data = {
        "Student #1": ["Arithmetic", "Algebra 1", "Trigonometry"],
        "Student #2": ["Algebra 2", "Algebra 1", "Geometry"],
        "Student #3": ["Arithmetic", "Algebra 2", "Algebra 1"],
        "Student #4": ["Geometry", "Trigonomerty", "Algebra 1"],
        "Student #5": ["Trigonometry", "Arithmetic", "Algebra 2"],
                    
     }
     # Evaluate TEAMS OF THE FUNCTION
    tests_not_meeting_criteria, students_not_taking_enough_tests = evaluateTeams(students_data)

    # Print Tests not meeting the criteria
    print("Tests not meeting the criteria:")
    for test in tests_not_meeting_criteria:
        print(test)

    # Print Students not taking enough tests
    print("Students not taking enough tests:")
    for student in students_not_taking_enough_tests:
        print(student)

    test_evaluateTeams_exists()

