#  i have created this file - GTA
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from django.http import HttpResponse
from .models import Ehr_data
import random

from django.utils import timezone



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from django.conf import settings
from django.core.files.storage import FileSystemStorage

# media_full_path = settings.MEDIA_ROOT + "\playapp_data"
media_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\ehr_app\\uploads"



# Create your views here.
def index(request):
    # return HttpResponse('Securix V2    |      index Page')
    return render(request,'ehr_app/welcome.html')

def dashboard(request):
    # return HttpResponse('Securix V2    |      index Page')
    return render(request,'ehr_app/index.html')

def privacypolicy(request):
    return render(request,'ehr_app/Privacy_Policy.html')

def upload_ehr(request):
    return render(request,'ehr_app/upload_EHR.html')

def support(request):
    return render(request,'ehr_app/EHR_Support.html')



def upload_files(request):
    if request.method == 'POST':
        # Extract form data
        ehr_dataset_name = request.POST['ehr_dataset_name']
        dataset_description = request.POST['dataset_description']
        category = request.POST['category']
        license = request.POST['license']

        ehr_dataset_size = request.POST['ehr_dataset_size']
        ehr_dataset_type = request.POST['ehr_dataset_type']

        # Handle file uploads
        upload_file = request.FILES['upload_file']
        upload_image = request.FILES['upload_image']

        # Save the uploaded files
        fs = FileSystemStorage(location=media_full_path)
        file_path = fs.save(upload_file.name, upload_file)
        image_path = fs.save(upload_image.name, upload_image)

        # print(f"file path : {media_full_path} / {file_path}")
        # print(f"image path : {media_full_path} / {image_path}")

        dataandtime = timezone.now()

        current_date = dataandtime.date()
        current_time = dataandtime.strftime('%H:%M:%S')

        _slug = slugify(f"/dataset_view/ehr-dataset-{ehr_dataset_name}-{current_date}-{current_time}")


        # Create a new Ehr_data instance and save it to the database
        ehr_data = Ehr_data(
            name=ehr_dataset_name,
            category=category,
        
            # slug=f"/dataset_view/ehr-dataset-{ehr_dataset_name}-{current_date}-{current_time}/",
            slug=_slug,
            # /dataset_view/ehr-dataset-1/

            file_type=ehr_dataset_type,
            file_size=ehr_dataset_size,
            
            file_path=f'ehr_app/uploads/{file_path}',
            image_path=f'ehr_app/uploads/{image_path}',

            desc=dataset_description,
            license=license,
            pub_date=current_date,  # Use the current timestamp as the publication date
        )
        ehr_data.save()

        # Redirect to the index page or any other desired page after successful submission
        return redirect('dashboard')

    return render(request, 'ehr_app/upload_EHR.html')  # Create an HTML file for your upload form


def dataset_view(request, myslug):
    # Fetch the Ehr_data object based on the provided slug
    print("myslug : ", myslug)
    cleaned_slug = f'/dataset_view/{myslug}'
    print("cleaned_slug : ", cleaned_slug)

    ehr_dataset = get_object_or_404(Ehr_data, slug=cleaned_slug)

    # You can pass the 'ehr_dataset' object to the template
    context = {'ehr_dataset': ehr_dataset}

    return render(request, 'ehr_app/dataset_view.html', context)
    # return HttpResponse(f'Securix V2    |      {context}')


def all_ehr_datasets(request):
    # Fetch all Ehr_data objects
    ehr_datasets = Ehr_data.objects.all()

    # Pass the Ehr_data objects to the template
    context = {'ehr_datasets': ehr_datasets}

    return render(request, 'ehr_app/all_ehr.html', context)




# def upload_files__(request):
#     if request.method == 'POST':

#         print("form post working : ")

#         # Handle video file upload
#         video_file = request.FILES['video_file']
#         # print("settings.MEDIA_ROOT : ",media_full_path)
#         fs = FileSystemStorage(location=media_full_path)
#         print("fs : ", fs)
#         video_path = fs.save(video_file.name, video_file)
#         print("video_path : ", media_full_path + "\\" + video_path)

#         # Handle subtitle file upload
#         subtitle_file = request.FILES['subtitle_file']
#         subtitle_path = fs.save(subtitle_file.name, subtitle_file)
#         print("subtitle_path : ", media_full_path + "\\" + subtitle_path)

#         # Save information to the database
#         # video = Videos(title=request.POST['title'], v_path=video_path, sub_path=subtitle_path)
#         # video.save()

#         # return redirect('upload_success')  # You can redirect to a success page or any other page
#         return redirect('index')  # You can redirect to a success page or any other page

#     return render(request, 'ehr_app/upload_video.html')  # Create an HTML file for your upload form













# Register | Login | Logout Functions

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'ehr_app/register.html', {'error_message': error_message})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'ehr_app/login.html', {'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view


# Example usage
# api_key = generate_api_key()
# print(api_key)

# def generate_api_key():
#     key_length = 36  # Length of the API key
#     dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

#     characters = "abcdefghijklmnopqrstwxyz0123456789"

#     api_key = ''.join(random.choice(characters) if i not in dash_positions else '-' for i in range(key_length))
#     return api_key

# def generate_unique_api_key():
#     while True:
#         # api_key = str(uuid.uuid4())
#         api_key = str(generate_api_key())
#         if not Nodedata.objects.filter(api_key=api_key).exists():
#             return api_key


# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n]) 

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)


# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)


#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })


# # def index(request):
# #     return HttpResponse('Teamzeffort    |      index Page')