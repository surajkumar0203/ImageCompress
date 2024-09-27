from django.shortcuts import render,redirect
# from django.http import 
# import pprint
def home(request):
    if request.method=="POST":
        print(request.FILES)
        if 'images' in request.FILES:
            image_file = request.FILES['images'] 
            print(image_file)
        else:
            print("Nahi hua")

        redirect('/')
    return render(request,'myapp/home.html')
