"""
Student Manager Module
Contains the StudentManager class for managing student data.

This file has several issues that can be used for debugging and refactoring exercises.
"""

import json
from typing import List, Dict, Optional

class StudentManager:
    """
    A class to manage student information.
    
    This class has some inefficiencies and bugs for educational purposes.
    """
    
    def __init__(self):
        self.students = []  # List to store student dictionaries
        self.next_id = 1
    
    def add_student(self, name: str, age: int, grades: List[float] = None):
        """
        Add a new student to the system.
        
        Args:
            name: Student's full name
            age: Student's age
            grades: List of grades (optional)
        """
        if grades is None:
            grades = []
        
        # Bug: No validation for negative age or empty name
        student = {
            "id": self.next_id,
            "name": name,
            "age": age,
            "grades": grades
        }
        
        self.students.append(student)
        self.next_id += 1
        return student["id"]
    
    def find_student_by_name(self, name: str) -> Optional[Dict]:
        """
        Find a student by name (case-sensitive search).
        
        Bug: This is inefficient for large datasets and case-sensitive.
        """
        for student in self.students:
            if student["name"] == name:
                return student
        return None
    
    def find_student_by_id(self, student_id: int) -> Optional[Dict]:
        """Find a student by ID"""
        # Inefficient linear search (can be optimized)
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None
    
    def update_student_grades(self, student_id: int, new_grades: List[float]):
        """Update grades for a specific student"""
        student = self.find_student_by_id(student_id)
        if student:
            student["grades"] = new_grades
            return True
        return False
    
    def add_grade(self, student_id: int, grade: float):
        """Add a single grade to a student's record"""
        student = self.find_student_by_id(student_id)
        if student:
            # Bug: No validation for grade range (should be 0-100)
            student["grades"].append(grade)
            return True
        return False
    
    def get_all_students(self) -> List[Dict]:
        """Return all students"""
        return self.students.copy()  # Return a copy to prevent external modification
    
    def remove_student(self, student_id: int) -> bool:
        """Remove a student from the system"""
        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                del self.students[i]
                return True
        return False
    
    def get_top_students(self, count: int = 3) -> List[Dict]:
        """
        Get top performing students based on average grades.
        
        This method has optimization opportunities.
        """
        students_with_averages = []
        
        # Inefficient calculation - recalculates every time
        for student in self.students:
            if student["grades"]:
                avg = sum(student["grades"]) / len(student["grades"])
                student_copy = student.copy()
                student_copy["average"] = avg
                students_with_averages.append(student_copy)
        
        # Inefficient sorting (could use heapq for large datasets)
        students_with_averages.sort(key=lambda x: x["average"], reverse=True)
        
        return students_with_averages[:count]
    
    def get_student_count(self) -> int:
        """Get total number of students"""
        return len(self.students)
    
    def export_to_json(self, filename: str) -> bool:
        """Export all student data to JSON file"""
        try:
            with open(filename, 'w') as file:
                json.dump(self.students, file, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting data: {e}")
            return False
