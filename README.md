# Student Management System

A simple Python project designed for learning Git, debugging, refactoring, and optimization concepts.

## Project Structure

```
student-management/
├── main.py                 # Main application entry point
├── student_manager.py      # StudentManager class
├── utils.py               # Utility functions
├── test_student_manager.py # Test file with intentional bugs
├── requirements.txt       # Project dependencies
└── README.md             # This file
```

## Features

- Add and manage student records
- Calculate grade averages
- Find students by name or ID
- Generate student reports
- Export data to JSON format

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Basic understanding of Python programming

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd student-management
```

2. (Optional) Install development dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the main application:
```bash
python main.py
```

Run tests:
```bash
python test_student_manager.py
```

## Learning Objectives

This project is designed to teach:

### 1. Git and Version Control
- Initialize a Git repository
- Add and commit files
- Push to GitHub
- Create branches for different features
- Handle merge conflicts

### 2. Code Reading and Understanding
- Follow code flow between modules
- Understand class relationships
- Identify function dependencies

### 3. Debugging Skills
- Find and fix runtime errors
- Handle edge cases
- Use print statements and debugger
- Read error messages effectively

### 4. Refactoring Techniques
- Improve code readability
- Eliminate code duplication
- Better error handling
- Improve function design

### 5. Code Optimization
- Identify performance bottlenecks
- Reduce time complexity
- Optimize memory usage
- Use appropriate data structures

## Known Issues (For Learning)

This codebase intentionally contains several issues:

1. **Runtime Errors**: Division by zero in empty grade lists
2. **Logic Bugs**: Case-sensitive searches, missing validation
3. **Performance Issues**: Inefficient algorithms, redundant calculations
4. **Code Quality**: Poor string formatting, nested conditionals
5. **Missing Features**: Input validation, error handling

## Git Workshop Commands

Here are the essential Git commands you'll practice:

```bash
# Initialize repository
git init

# Check status
git status

# Add files
git add .
git add main.py

# Commit changes
git commit -m "Initial commit"

# Add remote origin
git remote add origin <your-github-url>

# Push to GitHub
git push -u origin main

# Create and switch to new branch
git checkout -b fix-bugs

# Switch between branches
git checkout main
git checkout fix-bugs

# Merge branches
git merge fix-bugs

# View commit history
git log --oneline
```

## Workshop Exercises

### Exercise 1: Git Basics
1. Initialize Git repository
2. Make initial commit
3. Create GitHub repository
4. Push code to GitHub

### Exercise 2: Bug Hunting
1. Run the tests and identify failing tests
2. Find the root cause of each bug
3. Fix one bug at a time
4. Commit each fix separately

### Exercise 3: Refactoring
1. Improve the `format_student_info` function
2. Simplify the `calculate_letter_grade` function
3. Add proper input validation
4. Improve error handling

### Exercise 4: Optimization
1. Optimize the student search functionality
2. Improve the `get_top_students` method
3. Cache calculated averages
4. Use more efficient data structures

## Common Debugging Techniques

1. **Read Error Messages Carefully**
   - Look at the line number
   - Understand the error type
   - Trace the call stack

2. **Use Print Debugging**
   - Add print statements to track values
   - Print function entry/exit points
   - Display variable states

3. **Test Edge Cases**
   - Empty inputs
   - Boundary values
   - Invalid data types

4. **Code Review Checklist**
   - Are all variables initialized?
   - Are edge cases handled?
   - Is error handling present?
   - Are data types consistent?

## Next Steps

After completing the workshop:
1. Create your own branch for additional features
2. Add input validation to all functions
3. Implement proper logging
4. Add more comprehensive tests
5. Consider using a database instead of lists

## Contributing

This is a learning project. Feel free to:
- Fix bugs you find
- Add new features
- Improve documentation
- Optimize existing code

Remember to create a new branch for each feature or fix!
