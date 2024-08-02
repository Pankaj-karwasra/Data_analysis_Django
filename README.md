**CSV File Analysis with Django**
**Overview**
This Django application allows users to upload CSV files for analysis. 
The application performs the following tasks:

Displays the first few rows of the dataset.
Provides summary statistics.
Shows missing values in the dataset.
Generates histograms for numeric columns in the dataset.
**

**Features****
Upload CSV files using a web form.
Visualize data distributions with histograms.
View data preview, summary statistics, and missing values.

**Code Structure**
forms.py: Contains the UploadFileForm class for handling file uploads.
urls.py: Configures the URL routing for the application.
views.py: Contains the upload_file view function, which handles file uploads and data analysis.
templates/analysis/upload.html: Template for uploading CSV files.
templates/analysis/results.html: Template for displaying the analysis results



Run these two command:-
                      python manage.py makemigrtaions
                      python manage.py migrate
Run Project:-
            python manage.py runserver
