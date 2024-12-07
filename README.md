To set up a Google Cloud Project with a Service Account for accessing the Google Sheets API,
start by creating a project in the Google Cloud Console. Once the project is created, enable the necessary APIs—specifically, 
the Google Sheets API and Google Drive API—through the "APIs & Services > Library" section. 
Next, create a Service Account by navigating to "IAM & Admin > Service Accounts," giving it a descriptive name, and assigning it an appropriate role, such as Editor or a more restrictive role like Sheets Admin or Drive API User. 
After creating the Service Account, generate a JSON key by selecting "Add Key > Create New Key" from the Service Account's details page and choosing the JSON format. 
Download and securely store this key, as it contains credentials for accessing your project.

IMPORTANT!!
To allow the Service Account to access specific Google Sheets, share the desired spreadsheet with the Service Account email, found in the JSON file (usually in the format @<project-id>.iam.gserviceaccount.com), granting appropriate permissions such as Viewer or Editor
Line 22 of Main make sure to replace with file path of your own api keys :)
