from django.shortcuts import render, redirect
from.models import Appointment

# Create your views here.
def index_page(request):
    context = {}
    return render(request, 'index.html', context)
def portfolio(request):
    context = {}
    return render(request, 'portfolio-details.html', context)
def service(request):
    context = {}
    return render(request, 'service-details.html', context)
def starter_page(request):
    context = {}
    return render(request, 'starter-page.html', context)
def appointment(request):
    context = {}
    return render(request, 'appointment.html', context)
    ''' function  '''
def appointment(request):

    """ Appointment booking """

        # Check if its a post method

    if request.method == 'POST':

        # Create variable to pick the input fields

        appointments = Appointment(

            # list the input fields here

            name = request.POST['name'],

            email = request.POST['email'],

            phone = request.POST['phone'],

            date = request.POST['date'],

            service = request.POST['service'],

            specialist = request.POST['specialist'],

            message = request.POST['message'],
                    

        )

        # save the variable

        appointments.save()

        # redirect to a page

        return redirect('gym_app:index')

    else:

        return render(request, 'appointment.html')

#retrivial of all appointments
def retrieve_appointments(request):
    ''' function to fetch all appointments '''
    #create variables
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'show_appointment.html', context)

#Delete
# def delete_appointment(request, id):
#     ''' delete '''
#     appointments = Appointment.objects.get(id=id)
#     appointments.delete()
#     return redirect(request,"gym_app:show_appointment.html")

def delete_appointment(request, id):
    ''' Delete appointment by ID '''
    try:
        appointment = Appointment.objects.get(id=id)
        appointment.delete()
        # Redirect to a success page or list view after deletion
        return redirect('gym_app:show')  # Replace with correct view name
    except Appointment.DoesNotExist:
        return redirect('gym_app:appointments_list')  # Redirect to an appointments list or another view