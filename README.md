# 🔍 Secure Coding Review - Task 3 (CodeAlpha Internship)

## Application Reviewed:
Simple Python Login System using SQLite

## Vulnerabilities Found:

### 1. Hardcoded Credentials
- **Location:** Line 5
- **Problem:** Static username/password in script
- **Fix:** Use environment variables or secure input

### 2. No Input Validation / Sanitization
- **Location:** Line 11
- **Problem:** User input directly used
- **Fix:** Sanitize or validate inputs where necessary

### 3. SQL Injection
- **Location:** Line 13
- **Problem:** Unsafe query with string formatting
- **Fix:** Use parameterized queries

## Secure Version Changes:
- Used `getpass` for hidden password input
- Used `cursor.execute(query, (user, pass))`
- Removed hardcoded sensitive data

## What I Learned:
- Importance of input validation
- Common injection flaws and their fixes
- How to securely handle user authentication

