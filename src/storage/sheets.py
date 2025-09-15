# sheets.py
# This file is to define functions for reading/writing collected data from Google and facebook to Google Sheets.
# Sample steps:
#  - Load Google Sheet ID and credentials from .env
#  - Authorize using Google service account credentials
#  - Open the target Google Sheet by ID
#  - Define a function to read data from the worksheet
#  - Define a function to write/append rows of data to the worksheet
#  - Check for duplicates before writing
#  - Handle errors and exceptions (e.g., network issues, authorization failure)
#  - Export the function so that it can be called from main.py


