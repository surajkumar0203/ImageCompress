from django.shortcuts import render,redirect
from myapp.models import ImageModel
from django.contrib import messages
import os
import shutil
from django.conf import settings
from django.http import HttpResponse


def home(request):
    context={
            'isDownload':False
        }
    if request.method=="POST":
        if 'images' in request.FILES:
            image_file = request.FILES['images'] 
            ImageModel.objects.create(original_image=image_file)
            # Specify the folder to be zipped
            folder_to_zip = 'thumnails'
            # The name for the output zip file (without extension)
            output_filename = 'thumnails_output_zip'
            # Create the zip file (it adds the .zip extension automatically)
            shutil.make_archive(output_filename, 'zip', folder_to_zip)
            
            context['isDownload']=True

        else:
            messages.error(request,"Something error")
        redirect('/')

    
    return render(request,'myapp/home.html',context)

def download(request):
    # delete thumnails file
    dir_path = "thumnails"
    shutil.rmtree(dir_path, ignore_errors=True)
    
    # Download zip file
    # Define the path to the existing .zip file
    file_path = os.path.join(settings.MEDIA_ROOT, 'thumnails_output_zip.zip')
    # Open the file in binary mode
    with open(file_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="thumnails_output_zip.zip"'
        return response
    
    messages.error(request,"Something error")
    return redirect("/")