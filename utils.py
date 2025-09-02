"""
Utility functions for the Student Management System.

This file contains helper functions with various issues for educational purposes.
"""

import math
from typing import List, Dict

def calculate_grade_average(grades: List[float]) -> float:
    """
    Calculate the average of a list of grades.
    
    Bug: Doesn't handle empty lists properly.
    """
    # This will cause ZeroDivisionError if grades is empty
    return sum(grades) / len(grades)

def format_student_info(student: Dict) -> str:
    """
    Format student information for display.
    
    This function has some inefficiencies and could be improved.
    """
    name = student["name"]
    age = student["age"]
    grades = student["grades"]
    
    # Inefficient string concatenation
    result = "Student: " + name + "\n"
    result = result + "Age: " + str(age) + "\n"
    
    if grades:
        avg = calculate_grade_average(grades)
        result = result + "Grades: " + str(grades) + "\n"
        result = result + "Average: " + str(round(avg, 2)) + "\n"
    else:
        result = result + "No grades recorded\n"
    
    result = result + "-" * 30 + "\n"
    return result

def validate_grade(grade: float) -> bool:
    """
    Validate if a grade is within acceptable range.
    
    Bug: Missing edge case handling.
    """
    # Should validate range 0-100, but has issues
    if grade >= 0 and grade <= 100:
        return True
    return False

def calculate_letter_grade(average: float) -> str:
    """
    Convert numerical average to letter grade.
    
    Inefficient implementation with room for improvement.
    """
    # Inefficient nested if statements
    if average >= 90:
        if average >= 97:
            return "A+"
        elif average >= 93:
            return "A"
        else:
            return "A-"
    elif average >= 80:
        if average >= 87:
            return "B+"
        elif average >= 83:
            return "B"
        else:
            return "B-"
    elif average >= 70:
        if average >= 77:
            return "C+"
        elif average >= 73:
            return "C"
        else:
            return "C-"
    elif average >= 60:
        if average >= 67:
            return "D+"
        elif average >= 63:
            return "D"
        else:
            return "D-"
    else:
        return "F"

def find_outlier_grades(grades: List[float]) -> List[float]:
    """
    Find grades that are outliers (more than 2 standard deviations from mean).
    
    This function has bugs and inefficiencies.
    """
    if len(grades) < 3:
        return []
    
    # Inefficient calculation - calculates mean multiple times
    mean = sum(grades) / len(grades)
    
    # Calculate standard deviation manually (inefficient)
    variance = 0
    for grade in grades:
        variance += (grade - mean) ** 2
    variance = variance / len(grades)
    std_dev = math.sqrt(variance)
    
    outliers = []
    for grade in grades:
        # Bug: Should use absolute value for distance
        if grade - mean > 2 * std_dev or grade - mean < -2 * std_dev:
            outliers.append(grade)
    
    return outliers

def sort_students_by_average(students: List[Dict]) -> List[Dict]:
    """
    Sort students by their grade average.
    
    Inefficient implementation that recalculates averages unnecessarily.
    """
    # Inefficient: calculates average for each comparison during sorting
    def get_average(student):
        if not student["grades"]:
            return 0
        return sum(student["grades"]) / len(student["grades"])
    
    # This will call get_average many times during sorting
    return sorted(students, key=get_average, reverse=True)

def generate_student_report(student: Dict) -> str:
    """
    Generate a detailed report for a single student.
    
    Has some bugs and could be more efficient.
    """
    report = f"STUDENT REPORT\n"
    report += f"==============\n"
    report += f"Name: {student['name']}\n"
    report += f"Age: {student['age']}\n"
    report += f"Student ID: {student['id']}\n\n"
    
    grades = student["grades"]
    if not grades:
        report += "No grades available.\n"
        return report
    
    # Bug: Will crash if grades is empty (already checked above, but redundant)
    avg = calculate_grade_average(grades)
    letter_grade = calculate_letter_grade(avg)
    
    report += f"Grades: {', '.join(map(str, grades))}\n"
    report += f"Average: {avg:.2f}\n"
    report += f"Letter Grade: {letter_grade}\n"
    
    # Find best and worst grades (inefficient)
    best_grade = grades[0]
    worst_grade = grades[0]
    for grade in grades:
        if grade > best_grade:
            best_grade = grade
        if grade < worst_grade:
            worst_grade = grade
    
    report += f"Best Grade: {best_grade}\n"
    report += f"Worst Grade: {worst_grade}\n"
    
    return report
