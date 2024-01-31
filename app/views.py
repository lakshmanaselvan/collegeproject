from django.shortcuts import render
from .models import Event
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Venue

# Generate Event  PDF
def generate_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    events = Event.objects.all()
    lines = []
    for event in events:
        lines.append(event.title)
        lines.append(event.venue)
        lines.append(event.organizer)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Events.pdf')

def home(request):
    return render(request, "home.html", {})

def event_list(request):
    events = Event.objects.all()
    return render(request, "events.html", {'events':events})

def add_events(request):
    return render(request, "add_events.html", {})