
# google.py

# This file should contain function to interact with the Google Custom Search API.
#  - The free quota:
#        - 100 queries per day
#        - 100 results per query with pagination
# Sample steps :
#  - The function should fetch page urls and names from Google search API using relevant keywords(queries).
#  - The sample working function to fetch results can be found in tests/test_google.py file.
#  - You can follow the test script and make necessary updates.
#  - Queries can be general like student club, student association
#     or more specific like university, colleges, school name(shown in test script) so that the results are filtered and more specific.
#  - The function should build request parameters: API key, CSE ID, query, start index, country, language
#  - Loop through each page of results
#  - Calculate the correct start index for this page so that it can loop all pages for each query
#  - Send Get request using python
#  - Return collected results to be saved in google sheet and database(Functions in separate files)
#  - Should be clean and maintainable and should have mechanism to avoid hitting API rate limits(.eg. sleep)
#  - Handle errors and exceptions.
#  - Export the function so that it can be called from main.py
