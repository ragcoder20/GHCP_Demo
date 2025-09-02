#!/usr/bin/env python3
"""
Simple Student Management System
Author: Workshop Instructor
Date: 2025-09-02

This is the main file for our student management system.
It demonstrates basic Python concepts and has some issues for learning purposes.
"""

import json
import os
from typing import List, Dict
from student_manager import StudentManager
from utils import calculate_grade_average, format_student_info

def main():
    print("=== Student Management System ===")
    
    # Initialize the student manager
    manager = StudentManager()
    
    # Add some sample students (has inefficient code for learning)
    students_data = [
        {"name": "Alice Johnson", "age": 20, "grades": [85, 92, 78, 90]},
        {"name": "Bob Smith", "age": 19, "grades": [76, 88, 82, 79]},
        {"name": "Charlie Brown", "age": 21, "grades": [94, 87, 91, 89]},
        {"name": "Diana Prince", "age": 20, "grades": [88, 85, 92, 87]}
    ]
    
    # Inefficient way to add students (can be optimized)
    for student in students_data:
        manager.add_student(student["name"], student["age"], student["grades"])
        print(f"Added student: {student['name']}")
    
    print("\n=== All Students ===")
    # Display all students
    all_students = manager.get_all_students()
    for student in all_students:
        print(format_student_info(student))
    
    # Calculate and display statistics
    print("\n=== Statistics ===")
    total_students = len(all_students)
    print(f"Total students: {total_students}")
    
    # Bug: This will cause issues with empty grades
    all_grades = []
    for student in all_students:
        all_grades.extend(student["grades"])
    
    if all_grades:
        average_grade = sum(all_grades) / len(all_grades)
        print(f"Overall average grade: {average_grade:.2f}")
    
    # Save data to file
    save_students_to_file(all_students, "students_data.json")
    print("\nData saved to students_data.json")

def save_students_to_file(students: List[Dict], filename: str):
    """Save students data to a JSON file"""
    try:
        with open(filename, 'w') as file:
            json.dump(students, file, indent=2)
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
