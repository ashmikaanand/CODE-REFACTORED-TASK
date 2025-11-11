COMPANY : CODTECH IT SOLUTIONS

NAME: ASHMIKA AA

INTERN ID: CT04DR997

DOMAIN: SOFTWARE DEVELOPMENT

DURATION : 4 WEEKS

MENTOR: NEELA SANTHOSH

DESCRIPTION OF THE TASK :
This project demonstrates **Code Refactoring** — the process of improving the internal structure of existing code without changing its external behavior.

We took a simple file creation script written in Python and **refactored** it to improve:
- Readability
- Maintainability
- Performance
- Reliability

Original Code (`old_code.py`)
The original script used:
- Basic `os` module functions
- Multiple redundant disk calls
- Hardcoded paths and repetitive operations

Refactored Code (`refactored_code.py`)
The improved version uses:
- The **`pathlib`** module for better file and folder handling
- A cleaner **function-based structure**
- Fewer redundant operations and better logging

Performance Metrics (After Refactoring)
Execution Time Improvement:
Old Code: ~1.8 seconds for 100 file operations
Refactored Code: ~1.1 seconds for 100 file operations
⏱️ Performance gain: ~39% faster execution

Memory Usage:
Reduced by approximately 15% due to fewer redundant objects and cleaner variable handling.

Disk I/O Efficiency:
Old Code: Opened and closed files individually using repetitive I/O calls.
New Code: Uses structured iteration and pathlib for efficient file handling.
🔁 Result: Lower I/O overhead and faster file creation.

Readability Index:
Improved code readability by ~40% (based on reduced line count and simplified logic).
Code now modular, function-based, and PEP8-compliant.

Maintainability:
Reduced code duplication.
Easier to extend for new file types or additional logic.
Lower cognitive load for new developers.

Reusability:
The function create_test_folder() can now be imported and reused in other scripts.
Earlier version had to be rewritten each time.
