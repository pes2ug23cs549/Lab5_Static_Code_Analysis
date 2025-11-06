# Reflection – Lab 5: Static Code Analysis

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
- The easiest issues to fix were removing the unsafe `eval()` call and replacing bare `except:` with a specific `KeyError` handler.  
- The hardest fix was the mutable default argument (`[]`) issue since it required understanding Python’s memory handling for default parameters.

### 2. Did the static analysis tools report any false positives? If so, describe one example.
- No false positives were observed.  
- All reported issues were valid and led to genuine improvements in security, code clarity, and maintainability.

### 3. How would you integrate static analysis tools into your actual software development workflow?
- I would integrate **Pylint**, **Flake8**, and **Bandit** into a **Continuous Integration (CI)** pipeline using GitHub Actions.  
- This ensures every code commit is automatically checked for logical, stylistic, and security issues before being merged into the main branch.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- The Pylint score improved from **4.8/10 to around 8.8/10**.  
- The code became more secure (removed `eval()` and bare `except:`).  
- Readability and maintainability improved with proper structure and safe file handling using context managers.
