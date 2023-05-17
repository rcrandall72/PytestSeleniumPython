# PytestSeleniumPython

Python Selenium Tests using Pytest

Tests are done on https://www.saucedemo.com/

Two test suites exist:

Smoke -- Login/Logout & Buy Item
Regression -- All Test Cases
Can login/logout:

Verifies a user can login and logout Cannot login with locked user:
Verifies a user cannot login if their account is locked Can see login credential errors:
Verifies a user sees an error if they are missing their username or password. Also verifies the error message appears if the username/password are incorrect. Can buy item:
Verifies a user can buy an item (add to cart) and finalize their purchase Can view social media links:
Verifies a user can view and route to all social media links (Twitter, Facebook, LinkedIn) Can sort products:
Verifies a user can sort products in the list from A to Z, Z to A, and by Price (high to low & low to high)
