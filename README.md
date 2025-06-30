# E-commerce Selenium Test Suite

## Overview
This project is an automated test suite for the web application at `https://the-internet.herokuapp.com`, built using **Selenium WebDriver**, **pytest**, and the **Page Object Model (POM)**. It tests 17 key features of the site, including login, checkboxes, context menus, and more, to ensure functionality and reliability. The project follows industry-standard practices for maintainability, scalability, and reporting.

## Features Tested
- Login
- Checkboxes
- Context Menu
- Digest Authentication
- Disappearing Elements
- Drag and Drop
- Dropdown
- File Download
- File Upload
- Forgot Password
- Horizontal Slider
- Hovers
- Key Presses
- Multiple Windows
- Nested Frames
- Notification Messages
- Redirect Link

## Project Structure
```
E-commerce_Selenium/
├── pages/
│   ├── __init__.py             # Marks directory as a Python package
│   ├── base_page.py            # Base page with common methods
│   ├── login_page.py           # Page object for Login
│   ├── checkboxes_page.py      # Page object for Checkboxes
│   ├── context_menu_page.py    # Page object for Context Menu
│   ├── digest_auth_page.py     # Page object for Digest Authentication
│   ├── disappearing_elements_page.py # Page object for Disappearing Elements
│   ├── drag_drop_page.py       # Page object for Drag and Drop
│   ├── dropdown_page.py        # Page object for Dropdown
│   ├── file_download_page.py   # Page object for File Download
│   ├── file_upload_page.py     # Page object for File Upload
│   ├── forgot_password_page.py # Page object for Forgot Password
│   ├── horizontal_slider_page.py # Page object for Horizontal Slider
│   ├── hovers_page.py          # Page object for Hovers
│   ├── key_presses_page.py     # Page object for Key Presses
│   ├── multiple_windows_page.py # Page object for Multiple Windows
│   ├── nested_frames_page.py   # Page object for Nested Frames
│   ├── notification_messages_page.py # Page object for Notification Messages
│   ├── redirect_link_page.py   # Page object for Redirect Link
├── tests/
│   ├── __init__.py             # Marks directory as a Python package
│   ├── test_login.py           # Tests for Login
│   ├── test_checkboxes.py      # Tests for Checkboxes
│   ├── test_context_menu.py    # Tests for Context Menu
│   ├── test_digest_auth.py    # Tests for Digest Authentication
│   ├── test_disappearing_elements.py # Tests for Disappearing Elements
│   ├── test_drag_drop.py       # Tests for Drag and Drop
│   ├── test_dropdown.py        # Tests for Dropdown
│   ├── test_file_download.py   # Tests for File Download
│   ├── test_file_upload.py     # Tests for File Upload
│   ├── test_forgot_password.py # Tests for Forgot Password
│   ├── test_horizontal_slider.py # Tests for Horizontal Slider
│   ├── test_hovers.py          # Tests for Hovers
│   ├── test_key_presses.py     # Tests for Key Presses
│   ├── test_multiple_windows.py # Tests for Multiple Windows
│   ├── test_nested_frames.py   # Tests for Nested Frames
│   ├── test_notification_messages.py # Tests for Notification Messages
│   ├── test_redirect_link.py   # Tests for Redirect Link
├── downloads/                   # Directory for downloaded files
├── Test_Plan.md                # Test plan documentation
├── requirements.txt            # Python dependencies
├── report.html                 # Generated HTML test report
├── README.md                   # This file
```

## Prerequisites
- **Python**: 3.11.9
- **Google Chrome**: Version 138.0.7204.50
- **Dependencies**:
  - selenium==4.34.0
  - webdriver-manager==4.0.2
  - pytest==8.4.1
  - pytest-html

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/E-commerce_Selenium.git
   cd E-commerce_Selenium
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Chrome Version**:
   Ensure Google Chrome is version 138.0.7204.50 (check via Help > About Google Chrome).

## Running Tests
1. **Run All Tests**:
   ```bash
   pytest tests/ -v -n auto
   ```
   This executes all 21 test cases across 17 features, with verbose output showing each test's status.

2. **Generate HTML Report**:
   ```bash
   pytest tests/ --html=report.html --self-contained-html
   ```
   Open `report.html` in a browser to view detailed test results.

3. **Run Specific Tests** (optional):
   - For a single feature (e.g., Login):
     ```bash
     pytest tests/test_login.py -v
     ```
   - For a specific test case:
     ```bash
     pytest tests/test_login.py::test_valid_login -v
     ```

## Test Plan
The test plan (`Test_Plan.md`) outlines the objectives, scope, and test cases for each feature. It ensures comprehensive coverage of functional testing for `https://the-internet.herokuapp.com`.

## Troubleshooting
- **Element Not Found**: If `NoSuchElementException` occurs, inspect the page source to verify locators and update page objects if needed.
- **ChromeDriver Mismatch**: Ensure ChromeDriver matches Chrome version 138.0.7204.50. Use `webdriver-manager` or download manually from https://chromedriver.storage.googleapis.com/index.html?path=138.0.7204.49/.
- **Network Issues**: Verify `https://the-internet.herokuapp.com` is accessible.
- **File Download/Upload**: Ensure write permissions in the `downloads/` directory and project root.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Add new tests or improvements in the `tests/` or `pages/` directories.
4. Commit changes (`git commit -m "Add new feature tests"`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License
This project is licensed under the MIT License.