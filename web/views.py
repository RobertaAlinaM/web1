from django.shortcuts import render

from .models import Passenger, Ticket, Transport, Pollution

def passenger_tickets_view(request, passenger_id):
    passenger_id = Passenger.objects.get(id=passenger_id)

def passenger_from_origin_view(request, origin):
    tickets = Ticket.objects.filter(origin=origin)
    passengers = set(ticket.passenger for ticket in tickets)

def highest_pollution_transport_view(request):
    highest_pollution = Pollution.objects.order_by('-pollution').first()

def ticket_details_view(request):
    tickets = Ticket.objects.all()

def calculate_contamination(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        transport_id = request.POST.get('transport_id')

        transport = Transport.objects.get(id=transport_id)

        try:
            contamination = calculate_index_contamination(origin, destination, transport)
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})

        Pollution.objects.create(pollution=contamination, transport=transport_id)

        return render(request, 'result_pollution.html', {'contamination': contamination})
    else:
        return render(request, 'form_contamination.html')

def calculate_index_contamination(origin, destination, transport):
    # Usarem la API que hem proposat al inici de curs per calcular-ho
    print("Contamination: " + origin, destination, transport)
