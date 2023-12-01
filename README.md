# datamanipulation
Task Manager

Project Overview:
The goal is to create a Task Manager that allows users to manage tasks, view statistics, and analyze task-related data. Task information should be stored in either a single or multiple CSV/JSON file(s), depending on the student's design choice. The project will be hosted on GitHub, and students are expected to follow best practices for code organization, documentation, and version control.

Project Features:
Task Management:

The student is expected to implement features to add tasks with title, description, and status (completed or not), view a list of tasks with their details, mark tasks as completed, and remove tasks.
Task Statistics:

The project should display statistics when viewing tasks, including the total number of tasks, completed tasks, and the percentage of completed tasks.
Task Categories:

Students should enable users to assign categories to tasks (e.g., work, personal, study) and implement a feature to display statistics based on task categories.
Data Storage Design:

The student is expected to implement a data storage system (single CSV file or multiple JSON files)
Documentation:

Students should include a README.md file with project details, setup instructions, and usage information. Additionally, they should document each function and class using docstrings.
GitHub Best Practices:

Following best practices, students should use version control effectively with meaningful commit messages.
Coding Best Practices:

Adhering to coding best practices, students are expected to follow PEP 8 style guidelines for Python code, use meaningful variable and function names, implement error handling for user inputs, and organize code into functions or classes for modularity.
Grading Criteria:
Task Management (25 points):

Points will be awarded based on the effectiveness of adding tasks, viewing tasks, marking tasks as completed, removing tasks, and overall functionality and user experience.
Task Statistics (20 points):

Points will be awarded for accurately displaying statistics and implementing category statistics.
Data Storage Design (15 points):

The design choice of the data storage system (single CSV file or multiple JSON files) will be evaluated, with points allocated accordingly.
Documentation (10 points):

Points will be awarded for the clarity and completeness of the README.md file, as well as the inclusion of function and class docstrings.
GitHub Best Practices (10 points):

Students will be evaluated on their effective use of version control, pull requests, code reviews, and maintaining a well-organized repository structure.
Coding Best Practices (20 points):

Points will be awarded for PEP 8 compliance, code readability and organization, and the effective use of the chosen data storage system.
Submission:
Upload your work on github and paste the repository link below.


Task Manager

GUI:
Input
Task Name: 
Activity:
Category: p for personal / w for work
status: a for active / c for complete

Edit: (to edit activity and or to update the status )
list: to list all active task
choose: choose a number to edit
choose: a to add activity / s for status
Output:
- activity update
- status update



View:
Choose: Personal or Work
Personal
list: (list all the task)
active: (list of active task)
completed: (list of completed task)
percentage of completed task: = active / completed

Work
list: (list all the task)
active: (list of active task)
completed: (list of completed task)
percentage of completed task: = active / completed



input data:
(need row number for counting / statistics)
- task name
- activity
- category (personal / work)
- status (can be mark as completed)



category
- work
- personal


display statistics
- viewing
	number of task
	completed task
	percentage of completed task



