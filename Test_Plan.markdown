# Test Plan for Login Functionality Testing

## Objective
To verify that the login functionality of "The Internet" website (https://the-internet.herokuapp.com/login) works as expected using Selenium automation.

## Scope
- Test the login page for valid and invalid credentials.
- Validate UI elements (username field, password field, login button).
- Check error messages for invalid inputs.
- Exclude other pages/features of the website.

## Test Environment
- Browser: Google Chrome 
- Tools: Python 3.8+, Selenium, pytest, ChromeDriver
- Operating System: Windows/Mac/Linux
- Website: https://the-internet.herokuapp.com/login

## Test Scenarios
1. **Valid Login**: Test login with correct username and password.
2. **Invalid Login**: Test login with incorrect username and/or password.
3. **Empty Fields**: Test login with empty username and/or password fields.
4. **UI Validation**: Verify the presence of username field, password field, and login button.

## Test Cases
- **TC1**: Login with valid credentials (username: tomsmith, password: SuperSecretPassword!).
  - Expected: Redirect to secure area with success message.
- **TC2**: Login with invalid username.
  - Expected: Error message "Your username is invalid!".
- **TC3**: Login with invalid password.
  - Expected: Error message "Your password is invalid!".
- **TC4**: Login with empty username and password.
  - Expected: Error message for invalid username.
- **TC5**: Verify UI elements are present and enabled.
  - Expected: Username field, password field, and login button are visible and interactable.

## Test Execution
- Tests will be automated using Selenium with Python and pytest.
- Tests will be run on Chrome browser.
- Results will be logged in the console and saved as a report.

## Deliverables
- Selenium test scripts.
- Test execution report.
- Bug report (if any issues are found).