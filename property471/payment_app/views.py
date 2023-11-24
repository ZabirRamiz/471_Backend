from django.shortcuts import render

# Create your views here.
from django.http import FileResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from io import BytesIO
from django.http import HttpResponse


class GeneratePDF(View):
    template_name = 'your_template.html'  # Replace with your HTML template

    def get(self, request, *args, **kwargs):
        template = get_template(self.template_name)
        context = {
            'data': 'Property Management Contract:n/ This property contract is issued on [ Date ] between:n/ [Property owners name] and [Property buyers name]n/Property Manager agrees to provide the following property management services for the property located at:n/Property Address: [Property Address]n/',  # PDF template
        }
        html = template.render(context)

        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="your_pdf.pdf"'
            return response

        return HttpResponse("Error generating the PDF", status=500)
