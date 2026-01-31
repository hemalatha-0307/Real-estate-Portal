# Test Plans and Test Cases for Real Estate Portal

## Test Plan Overview
**Objective**: Ensure the real estate portal functions correctly, covering user stories, NFRs, and edge cases.
**Scope**: Unit tests (models), integration tests (routes), UI tests (forms), security tests.
**Tools**: unittest (Python), pytest for extensions.
**Environment**: Local Flask app, SQLite DB.
**Roles**: Tester simulates users; Developer reviews.

### Test Strategy
- **Unit Testing**: Test individual functions/models.
- **Integration Testing**: Test route interactions.
- **System Testing**: End-to-end user flows.
- **Acceptance Testing**: Validate against user stories.
- **Non-Functional**: Performance, security checks.

## Test Cases for Key User Stories

### User Story: User Registration
**Test Case 1: Happy Path**
- **Preconditions**: None
- **Steps**:
  1. Navigate to /register
  2. Enter valid name, email, password
  3. Submit form
- **Expected**: User created, redirected to /login
- **Postconditions**: User in DB

**Test Case 2: Error - Duplicate Email**
- **Preconditions**: User with email exists
- **Steps**: Register with same email
- **Expected**: Error message, no redirect

### User Story: Write Review for Seller
**Test Case 1: Happy Path**
- **Preconditions**: Logged-in buyer, seller exists
- **Steps**:
  1. View seller profile
  2. Submit review form (rating 4, comment)
- **Expected**: Review saved, visible on profile

**Test Case 2: Error - Invalid Rating**
- **Steps**: Submit rating >5
- **Expected**: Validation error

### NFR Test Cases
**Performance Test**: Load /properties with 100 properties in <2s
**Security Test**: Attempt SQL injection in forms

## Test Execution
- Run via `python -m unittest tests/test_*.py`
- Report bugs in Azure Boards.

This covers at least 5 user stories with happy/error paths.