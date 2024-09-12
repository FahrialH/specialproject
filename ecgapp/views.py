from django.shortcuts import render, redirect
from .forms import ECGFileForm
from PyPDF2 import PdfReader
from .models import ECGFile
# Create your views here.

'''pdf parsing'''
def extract_pdf_data(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text



def upload_file(request):
    if request.method == 'POST':
        form = ECGFileForm(request.POST, request.FILES)
        #data authentication
        if form.is_valid():
            ecg_file = form.save()
            pdf_path = ecg_file.file.path
            ecg_data = extract_pdf_data(pdf_path)
            return render(request, 'upload/display.html', {'ecg_data': ecg_data})

        
    else:
        form = ECGFileForm()

    uploaded_files = ECGFile.objects.all()
    
    return render(request, 'upload/upload.html', {
        'form': form,
        'uploaded_files': uploaded_files,
        
        })