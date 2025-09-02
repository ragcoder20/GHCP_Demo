"""
Test file for Student Management System
This file contains tests with intentional bugs for debugging practice.
"""

import unittest
from student_manager import StudentManager
from utils import calculate_grade_average, validate_grade, calculate_letter_grade

class TestStudentManager(unittest.TestCase):
    """Test cases for StudentManager class"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.manager = StudentManager()
    
    def test_add_student(self):
        """Test adding a student"""
        student_id = self.manager.add_student("John Doe", 20, [85, 90, 78])
        self.assertEqual(student_id, 1)
        self.assertEqual(self.manager.get_student_count(), 1)
    
    def test_find_student_by_name(self):
        """Test finding student by name"""
        self.manager.add_student("Jane Smith", 19, [88, 92, 85])
        student = self.manager.find_student_by_name("Jane Smith")
        self.assertIsNotNone(student)
        self.assertEqual(student["name"], "Jane Smith")
        
        # Bug: This test will fail due to case sensitivity
        student = self.manager.find_student_by_name("jane smith")
        self.assertIsNotNone(student)  # This assertion will fail
    
    def test_calculate_average(self):
        """Test grade average calculation"""
        grades = [80, 85, 90, 75]
        avg = calculate_grade_average(grades)
        self.assertEqual(avg, 82.5)
        
        # Bug: This will cause ZeroDivisionError
        empty_grades = []
        avg = calculate_grade_average(empty_grades)
        self.assertEqual(avg, 0)  # This will never be reached
    
    def test_grade_validation(self):
        """Test grade validation function"""
        self.assertTrue(validate_grade(85))
        self.assertTrue(validate_grade(100))
        self.assertTrue(validate_grade(0))
        
        # Bug: These should fail but might pass due to validation issues
        self.assertFalse(validate_grade(-5))
        self.assertFalse(validate_grade(105))
    
    def test_letter_grade_conversion(self):
        """Test letter grade conversion"""
        self.assertEqual(calculate_letter_grade(95), "A")
        self.assertEqual(calculate_letter_grade(85), "B")
        self.assertEqual(calculate_letter_grade(75), "C")
        
        # Bug: Edge case not handled properly
        self.assertEqual(calculate_letter_grade(100), "A+")
    
    def test_remove_student(self):
        """Test removing a student"""
        student_id = self.manager.add_student("Test Student", 20, [80])
        self.assertTrue(self.manager.remove_student(student_id))
        self.assertEqual(self.manager.get_student_count(), 0)
        
        # Bug: Removing non-existent student
        self.assertFalse(self.manager.remove_student(999))

def run_manual_tests():
    """
    Manual tests that demonstrate various issues.
    These are not proper unit tests but help show debugging concepts.
    """
    print("Running manual tests...")
    
    manager = StudentManager()
    
    # Test 1: Add student with invalid data
    print("\nTest 1: Adding student with invalid age")
    try:
        manager.add_student("Invalid Student", -5, [85, 90])
        print("✓ Student added (should this be allowed?)")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 2: Calculate average of empty grades
    print("\nTest 2: Calculate average of empty grades")
    try:
        avg = calculate_grade_average([])
        print(f"✓ Average: {avg}")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 3: Add invalid grade
    print("\nTest 3: Adding invalid grade")
    student_id = manager.add_student("Test Student", 20, [])
    try:
        manager.add_grade(student_id, 150)  # Invalid grade > 100
        print("✓ Grade added (should this be allowed?)")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Test 4: Search case sensitivity
    print("\nTest 4: Case-sensitive search issue")
    manager.add_student("Alice Cooper", 21, [88, 92])
    student1 = manager.find_student_by_name("Alice Cooper")
    student2 = manager.find_student_by_name("alice cooper")
    
    print(f"Found with correct case: {student1 is not None}")
    print(f"Found with wrong case: {student2 is not None}")

if __name__ == "__main__":
    # Run the manual tests first to show issues
    run_manual_tests()
    
    print("\n" + "="*50)
    print("Running unit tests...")
    print("="*50)
    
    # Run unit tests
    unittest.main(verbosity=2)
