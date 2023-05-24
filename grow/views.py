from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import request
# Create your views here.
def main_page(request):


    return render(request, 'index.html')



def form_submit(request):
    if request.method == 'POST':
        # Access the form data
        employee_name = request.POST.get('employee_name')
        employee_email = request.POST.get('employee_email')
        idea_description = request.POST.get('idea_description')
        shift = request.POST.get('shift')
        division = request.POST.get('division')
        department = request.POST.get('department')
        line = request.POST.get('line')
        station = request.POST.get('station')
        types = request.POST.get('type')
        area = request.POST.get('area')
        current_description = request.POST.get('current_description')
        idea_description = request.POST.get('idea_description')
        # Retrieve other form fields similarly
        print(employee_email)
        # Perform necessary actions with the data

        # Return a JSON response indicating success
        return JsonResponse({'message': 'Form data received successfully'})

    # Return a JSON response indicating an error for other request methods
    return JsonResponse({'error': 'Invalid request method'})
