#  i have created this file - GTA
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import SensorData, UserData
import random
import os
import requests

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
# upload_file_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\bandapp\\uploaded_files"
# results_full_path = settings.STATIC_MEDIA_ROOT + "\\static\\bandapp\\ResultsFiles"

# bandapp\static\bandapp\uploaded_files
# C:\\Users\\Atharva Pawar\\Documents\\GitHub\\SECUIRX-v2\\securix_v2_project\\bandapp\\static\\playapp\\ResultsFiles\\codeGoat.py


# Create your views here.
def index(request):
    # return HttpResponse('Securix V2    |      index Page')
    return render(request,'bandapp/welcome.html')

def showresult(request):
    # return HttpResponse('Securix V2    |      index Page')
    return render(request,'bandapp/showresult.html')

def dashboard(request):
    # return HttpResponse('Securix V2    |      index Page')

    # Get the logged-in user's username
    logedIn_user = request.user.username
    
    # Query the database to get all records for the logged-in user
    userData = SensorData.objects.filter(user_name=logedIn_user)

    # Pass the data to the template
    context = {'userSensorData': userData}
    
    # Render the template with the data
    return render(request, 'bandapp/dashboard.html', context)

# API : sensor_latest_data 
# @csrf_exempt
def sensor_latest_data(request):
    if request.method == 'GET':
        # Get parameters from the GET request
        _user_name = request.GET.get('user_name', '')
        _api_key = request.GET.get('api_key', '')

        # Validate the username, API key, and nodename
        user_node_data = UserData.objects.filter(user_name=_user_name, api_key=_api_key).first()

        if user_node_data:
            latest_sensor_data = SensorData.objects.filter(user_name=_user_name).order_by('-pub_date', '-pub_time').first()

            if latest_sensor_data:
                # Serialize the data into a dictionary
                serialized_data = {
                    'user_name': latest_sensor_data.user_name,
                    'pub_date': latest_sensor_data.pub_date,
                    'pub_time': latest_sensor_data.pub_time,
                    'heartPulse': latest_sensor_data.heartPulse,
                    'dhtTemp': latest_sensor_data.dhtTemp,
                    'dhtHum': latest_sensor_data.dhtHum,
                    'gyrometer': [latest_sensor_data.gyroX, latest_sensor_data.gyroY, latest_sensor_data.gyroZ],
                    
                    'accelerometer': [latest_sensor_data.acceleroX, latest_sensor_data.acceleroY, latest_sensor_data.acceleroZ]
                }
                return JsonResponse(serialized_data)
            
            else:
                return JsonResponse({'error': 'No data found for the specified user_name'}, status=404)        


            # return JsonResponse({'status': 'success'})
        
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or API key'})



# @csrf_exempt
def sensor_data(request):
    if request.method == 'GET':
        # Get parameters from the GET request
        _user_name = request.GET.get('user_name', '')

        _api_key = request.GET.get('api_key', '')

        _heartPulse = float(request.GET.get('heartPulse', None))
        _dhtTemp = float(request.GET.get('dhtTemp', None))
        _dhtHum = float(request.GET.get('dhtHum', None))

        _gyroX = float(request.GET.get('gyroX', None))
        _gyroY = float(request.GET.get('gyroY', None))
        _gyroZ = float(request.GET.get('gyroZ', None))

        _acceleroX = float(request.GET.get('acceleroX', None))
        _acceleroY = float(request.GET.get('acceleroY', None))
        _acceleroZ = float(request.GET.get('acceleroZ', None))

        dataandtime = timezone.now()

        # current_date = dataandtime.date()
        current_time = dataandtime.strftime('%H:%M:%S')



        # Validate the username, API key, and nodename
        user_node_data = UserData.objects.filter(user_name=_user_name, api_key=_api_key).first()

        if user_node_data:
            # Save data to the database
            sensor_data = SensorData(
                user_name=_user_name,

                heartPulse = _heartPulse,
                dhtTemp    = _dhtTemp,
                dhtHum = _dhtHum,
            
                gyroX=_gyroX,
                gyroY=_gyroY,
                gyroZ=_gyroZ,

                acceleroX = _acceleroX,
                acceleroY = _acceleroY,
                acceleroZ = _acceleroZ,

                pub_date=dataandtime,
                pub_time=current_time
            )
            sensor_data.save()

            return JsonResponse({'status': 'success'})
        
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or API key'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})



# def upload_file(request):
#     if request.method == 'POST':

#         title = request.POST.get('title')
#         mode = request.POST.get('mode')
#         code_file = request.FILES['code_file']

#         # Print the logged-in user's name to the console
#         # if request.user.is_authenticated:
#             # print("Logged-in User:", request.user.username)
        
#         logedIn_user = request.user.username

#         # Save the file to the specified location
#         file_path = f"{upload_file_full_path}\\{logedIn_user}_{code_file.name}"

#         if not os.path.exists(file_path):
#             # If the file doesn't exist, create it
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)

#         # Assuming code_file is the uploaded file
#         with open(file_path, 'wb') as destination:
#             for chunk in code_file.chunks():
#                 destination.write(chunk)

#         result_file_path = f"{results_full_path}\\{logedIn_user}_{title}.json"

#         scan_file_final(file_path, result_file_path, mode = mode)


#         # Create a database entry if needed
#         SecurityFinding.objects.create(user_name=logedIn_user, file_name=title, file_path=file_path,result_file_path=result_file_path)

#         # Print the file name and path on the terminal
#         print(f"File title: {title}")
#         print(f"File Name: {code_file.name}")
#         print(f"File Path: {file_path}")

#         # Redirect to the dashboard or any desired page
#         return redirect('dashboard')  # Replace 'dashboard' with the actual URL or view name

#     return redirect('dashboard')  


# domain_link = "https://045d-35-229-130-116.ngrok-free.app/"

# def scan_file(mode='regex'):
# def scan_file_final(file_path, result_file_path, mode):
#     print("upload_GitLink() function running ...")
#     # url = "http://localhost:5000/download_repo"
#     # url = f"{domain_link}scanrepo"
#     url = f"{domain_link}file_scan"

#     # mode = 'regex'
#     # mode = 'semgrep'

#     # file_path = "api_sample_uploads\codeGoat - Copy (2).c++"
#     # file_path = "api_sample_uploads\codeGoat - Copy.java"
#     # file_path = "api_sample_uploads\codeGoat.py"

#     # Extract the file name
#     file_name = os.path.basename(file_path)

#     # Prepare the file content and other data
#     files = {'file_content': (file_name, open(file_path, 'r'))}
#     data = {'file_name': file_name, 'mode': mode}

#     response = requests.post(url, files=files, data=data)

#     # Print the first 500 characters of the response
#     # print(response.text[:500])    

#     if not os.path.exists(result_file_path):
#         # If the file doesn't exist, create it
#         os.makedirs(os.path.dirname(result_file_path), exist_ok=True)


#     # You can also save the response to a file for further analysis
#     with open(result_file_path, 'w') as file:
#         file.write(response.text)




# def showresult(request, myid):

#     # Retrieve the SecurityFinding object based on myid
#     finding = get_object_or_404(SecurityFinding, id=myid)

#     # Pass the finding object to the template
#     # context = {'finding': finding}

#     result_file_path =  finding.result_file_path
#     with open(result_file_path) as f:
#         data = json.load(f)

#     projectName = finding.file_name


#     # vulPer = len(data["results"])
#     results_list = data.get("results", [])
#     length_of_results_list = len(results_list)
#     print("Length of the 'results' list:", length_of_results_list)

#     scanned_list = data.get("paths", {}).get("scanned", [])
#     length_of_scanned_list = len(scanned_list)
#     print("Length of the 'scanned' list:", length_of_scanned_list)

#     # Assuming you have already calculated the lengths as mentioned earlier
#     vulPercentage = ((length_of_scanned_list  - length_of_results_list) / length_of_scanned_list) * 100

#     vulPercentage = round(vulPercentage, 2)

#     impact_categories = {'MEDIUM': [], 'LOW': [], 'HIGH': []}


#     for result in results_list:
#         impact = result['extra']['metadata']['impact']
#         if impact in impact_categories:
#             impact_categories[impact].append(result)

#     # # Printing items in each impact category
#     # for impact, items in impact_categories.items():
#     #     print(f'Category: {impact}')
#     #     for item in items:
#     #         print(f'Check ID: {item["check_id"]}')
#     #         print(f'Message: {item["extra"]["message"]}')
#     #         print()  # Empty line for separation

#     highVar = len(impact_categories['HIGH'])
#     lowVar = len(impact_categories['LOW'])
#     mediumVar = len(impact_categories['MEDIUM'])

#     total_items = highVar + lowVar + mediumVar

#     risk_percentage = (mediumVar / total_items) * 100

    

#     impact = {
#         'highVar' : highVar,
#         'lowVar' : lowVar,
#         'mediumVar' : mediumVar,
#         'risk_percentage' : round(risk_percentage,2),
#     }
    


#     return render("bandapp/showresult.html", results=data, projectName=projectName, vulPercentage=vulPercentage, impact=impact)

#     # return render(request, 'bandapp/dashboard.html', context)





# Register | Login | Logout Functions

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email    = request.POST['email']

        _api_key = generate_unique_api_key()

        
        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            dataandtime = timezone.now()

            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)

            sensor_data = UserData(
                user_name=username,
                pub_date=dataandtime,
                api_key=_api_key
            )
            sensor_data.save()
            
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'bandapp/register.html', {'error_message': error_message})

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

    return render(request, 'bandapp/login.html', {'error_message': error_message})

def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view


def generate_api_key():
    key_length = 36  # Length of the API key
    dash_positions = [8, 13, 18, 23]  # Positions of dashes in the API key

    characters = "abcdefghijklmnopqrstwxyz0123456789"

    api_key = ''.join(random.choice(characters) if i not in dash_positions else '-' for i in range(key_length))
    return api_key

def generate_unique_api_key():
    while True:
        # api_key = str(uuid.uuid4())
        api_key = str(generate_api_key())
        if not UserData.objects.filter(api_key=api_key).exists():
            return api_key






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