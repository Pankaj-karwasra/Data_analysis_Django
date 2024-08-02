import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

def get_plot(df, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram for {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)
    return uri

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_path = fs.url(filename)
            df = pd.read_csv(fs.path(filename))
            data_head = df.head()
            summary_stats = df.describe()
            missing_values = df.isnull().sum().to_frame('Missing Values')  
            plots = {}
            for column in df.select_dtypes(include='number').columns:
                plots[column] = get_plot(df, column)
            context = {
                'form': form,
                'file_path': file_path,
                'data_head': data_head.to_html(classes='table table-striped'),
                'summary_stats': summary_stats.to_html(classes='table table-striped'),
                'missing_values': missing_values.to_html(classes='table table-striped'),  
                'plots': plots,
            }
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
