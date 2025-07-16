# Test Plan for Automation Test Selenium Suite

## 1. Introduction
This test plan outlines the strategy, scope, and execution details for the automated functional testing of 16 features on the web application `https://the-internet.herokuapp.com`. The test suite is built using Selenium WebDriver, pytest, and the Page Object Model (POM) to ensure maintainability, scalability, and adherence to industry-standard Software Quality Assurance (SQA) practices. The "Forgot Password" feature was excluded due to inconsistent behavior observed during manual testing, which returned errors such as "Internal Server Error."

## 2. Objectives
- Verify the functional behavior of 16 key features on `https://the-internet.herokuapp.com`.
- Ensure robust automation by handling dynamic elements, waits, and edge cases.
- Generate a detailed HTML test report for traceability and documentation.
- Validate the test suite’s reliability for deployment to a GitHub repository.

## 3. Scope
### 3.1 In-Scope
The test suite covers the following 16 features:
1. **Login**: Test valid and invalid login scenarios, including UI element verification.
2. **Checkboxes**: Verify selecting/deselecting checkboxes updates their state.
3. **Context Menu**: Validate right-click triggers an alert with the correct message.
4. **Digest Authentication**: Confirm successful login with credentials (admin/admin).
5. **Disappearing Elements**: Handle elements that may disappear/reappear on page refresh.
6. **Drag and Drop**: Verify dragging an element to a target updates the UI.
7. **Dropdown**: Test selecting options by text, value, and index.
8. **File Download**: Confirm downloading a file and verify its presence.
9. **File Upload**: Validate uploading a file and confirm the success message.
10. **Horizontal Slider**: Verify moving the slider updates the displayed value.
11. **Hovers**: Check hovering over elements displays additional information.
12. **Key Presses**: Validate keypress events (e.g., ENTER) are captured correctly.
13. **Multiple Windows**: Test switching between windows and verifying content.
14. **Nested Frames**: Verify navigation and content access in nested frames.
15. **Notification Messages**: Confirm notification messages display as expected.
16. **Redirect Link**: Test redirect links navigate to the correct page.

### 3.2 Out-of-Scope
- **Forgot Password**: Excluded due to unreliable behavior (e.g., "Internal Server Error") observed during manual testing.
- Performance, security, or accessibility testing.
- Testing on browsers other than Chrome 138.0.7204.50.
- Mobile or cross-device compatibility testing.

## 4. Test Environment
- **Operating System**: Windows 10
- **Browser**: Google Chrome (version 138.0.7204.50)
- **Automation Tools**:
  - Python: 3.11.9
  - Selenium WebDriver: 4.34.0
  - webdriver-manager: 4.0.2
  - pytest: 8.4.1
  - pytest-html: For HTML report generation
  - pytest-xdist: For parallel test execution
- **Test Site**: `https://the-internet.herokuapp.com`

## 5. Test Strategy
### 5.1 Approach
- **Automation Framework**: Use Selenium WebDriver with pytest and POM for modular, maintainable tests.
- **Test Types**: Functional tests to verify UI interactions, navigation, and expected outcomes.
- **Test Data**:
  - Login: Valid credentials (`tomsmith`, `SuperSecretPassword!`), invalid credentials, and empty fields.
  - Digest Authentication: `admin`/`admin`.
  - File Upload: A dynamically created `test_file.txt`.
  - Other features use predefined inputs (e.g., `Keys.ENTER` for Key Presses, `test@example.com` for email inputs where applicable).
- **Error Handling**: Use explicit waits (`WebDriverWait`) to handle dynamic elements and timeouts.
- **Reporting**: Generate an HTML report (`report.html`) for test results.

### 5.2 Test Levels
- **Unit Testing**: Individual page object methods are tested within test cases.
- **Integration Testing**: Verify interactions between page elements and navigation (e.g., redirect links, multiple windows).

### 5.3 Test Execution
- Tests are executed in parallel using `pytest-xdist` to reduce runtime.
- Command: `pytest tests/ --html=report.html --self-contained-html -v -n auto`
- Expected test count: 25 tests (5 for Login, 5 for Login with Selenium Manager, 1 for each of the 15 other features).

## 6. Test Cases
Below is a summary of the test cases for each feature, including objectives and expected outcomes.

| **Feature**                | **Test Case**                     | **Description**                                                                 | **Expected Outcome**                                                                 |
|----------------------------|-----------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| **Login**                  | `test_valid_login`               | Enter valid credentials (`tomsmith`, `SuperSecretPassword!`) and submit.        | Success message: "You logged into a secure area!"                                    |
|                            | `test_invalid_username`          | Enter invalid username and valid password, submit.                              | Error message: "Your username is invalid!"                                           |
|                            | `test_invalid_password`          | Enter valid username and invalid password, submit.                              | Error message: "Your password is invalid!"                                           |
|                            | `test_empty_fields`              | Submit with empty username and password fields.                                 | Error message: "Your username is invalid!"                                           |
|                            | `test_ui_elements`               | Verify username, password, and login button are displayed and enabled.          | All elements are visible and enabled.                                                |
| **Login (Selenium Manager)** | Same as above                    | Same as above, using Selenium Manager for ChromeDriver.                         | Same as above.                                                                       |
| **Checkboxes**             | `test_checkboxes_toggle`         | Toggle the first and second checkboxes and verify state changes.                | Checkbox states change (selected/deselected) as expected.                            |
| **Context Menu**           | `test_context_menu_alert`        | Right-click the hot-spot and verify the alert message.                          | Alert displays: "You selected a context menu".                                       |
| **Digest Authentication**  | `test_digest_auth_success`       | Navigate with credentials `admin`/`admin`.                                      | Success message contains "Digest Auth".                                              |
| **Disappearing Elements**  | `test_disappearing_elements`     | Refresh until the "Gallery" link appears (up to 5 attempts).                    | "Gallery" link is found within 5 refreshes.                                          |
| **Drag and Drop**          | `test_drag_and_drop`             | Drag column A to column B and verify the UI update.                            | Column B text updates to "A".                                                        |
| **Dropdown**               | `test_dropdown_selection`        | Select options by text ("Option 1"), value ("2"), and index (1).                | Selected option text matches the input ("Option 1" or "Option 2").                   |
| **File Download**          | `test_file_download`             | Click to download `some-file.txt` and verify its presence in `downloads/`.      | File exists in the `downloads/` directory.                                           |
| **File Upload**            | `test_file_upload`               | Upload `test_file.txt` and verify the uploaded file name.                       | Uploaded file name is "test_file.txt".                                               |
| **Horizontal Slider**      | `test_horizontal_slider`         | Move the slider and verify the value updates.                                   | Slider value is greater than 0.                                                      |
| **Hovers**                 | `test_hovers`                    | Hover over the first figure and verify the user name displayed.                | User name contains "user1".                                                          |
| **Key Presses**            | `test_key_presses`               | Press the `ENTER` key and verify the result text.                              | Result text contains "You entered: ENTER".                                           |
| **Multiple Windows**       | `test_multiple_windows`          | Open a new window, switch to it, and verify the content.                        | New window text contains "New Window".                                               |
| **Nested Frames**          | `test_nested_frames`             | Switch to the top and left frames, verify the content.                          | Frame text contains "LEFT".                                                          |
| **Notification Messages**  | `test_notification_messages`     | Click the link and verify the flash message.                                    | Message contains "Action successful" or "Action unsuccessful".                       |
| **Redirect Link**          | `test_redirect_link`             | Click the redirect link and verify the resulting URL.                           | URL contains "status_codes".                                                         |

## 7. Entry Criteria
- Dependencies are installed via `requirements.txt`:
  ```
  selenium==4.34.0
  webdriver-manager==4.0.2
  pytest==8.4.1
  pytest-html
  pytest-xdist
  ```
- Chrome browser is version 138.0.7204.50.
- `https://the-internet.herokuapp.com` is accessible.

## 8. Exit Criteria
- All 25 test cases pass, as verified by pytest output and `report.html`.
- HTML report (`report.html`) is generated and documents test results.
- Project is uploaded to GitHub with a complete `README.md` and this test plan.
- Any known issues (e.g., "Key Presses" timing issues) are resolved or documented.

## 9. Test Deliverables
- **Test Scripts**: Located in `pages/` and `tests/` directories, implementing POM.
- **HTML Report**: `report.html` generated by `pytest --html=report.html`.
- **Test Plan**: This document (`Test_Plan.md`).
- **README**: `README.md` with setup and usage instructions for GitHub.

## 10. Risks and Mitigation
| **Risk**                                      | **Impact**                             | **Mitigation**                                                                 |
|-----------------------------------------------|----------------------------------------|-------------------------------------------------------------------------------|
| Site changes break locators                    | Test failures due to outdated locators | Manually inspect page source and update locators in page objects.              |
| ChromeDriver version mismatch                 | Tests fail to run                     | Use `webdriver-manager` 4.0.2 or manually download ChromeDriver 138.0.7204.49. |
| Site downtime or errors (e.g., "Internal Server Error") | Unreliable test results               | Skip affected features (e.g., Forgot Password) and document in test plan.      |
| Timing issues with dynamic elements           | `TimeoutException` failures           | Use explicit waits and fallback locators in page objects.                      |
| File system permissions                       | File download/upload tests fail       | Ensure write permissions for `downloads/` and project root.                    |

## 11. Roles and Responsibilities
- **Test Developer**: Implement and maintain test scripts, debug failures, and update locators.
- **Test Executor**: Run tests, generate reports, and verify results.
- **Reviewer**: Validate test plan, scripts, and GitHub repository for completeness.

## 12. Test Schedule
- **Setup**: Complete project structure, install dependencies (1 hour).
- **Test Development**: Implement page objects and test cases (already completed).
- **Test Execution**: Run all tests and generate report (5-10 minutes per run, depending on parallel execution).
- **Debugging**: Address failures (e.g., `test_key_presses`) based on manual inspection (1-2 hours).
- **GitHub Upload**: Push to GitHub and verify repository (30 minutes).
- **Completion Date**: July 1, 2025, pending resolution of `test_key_presses`.

## 13. Assumptions
- `https://the-internet.herokuapp.com` remains accessible and stable.
- Chrome 138.0.7204.50 is compatible with Selenium 4.34.0.
- All features except "Forgot Password" function as expected per manual testing.

## 14. Known Issues
- **Key Presses**: The `test_key_presses` test fails due to a `TimeoutException` when locating the `result` element (`id="result"`). A fix has been applied with a fallback locator and implicit wait, but manual inspection is recommended to confirm the element’s presence.
- **Forgot Password**: Excluded due to unreliable behavior (e.g., "Internal Server Error") observed during manual testing.

## 15. Approval
- **Author**: [Your Name]
- **Date**: July 1, 2025
- **Status**: Draft, pending successful execution of all 25 tests.
