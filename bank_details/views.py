from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from models import Branches,Banks
from serializers import BanksSerializer


# Create your views here.


class BranchDetails(APIView):
    """
     Given a bank branch IFSC code, get branch details
    """

    template_name = "branch_details.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request):
        return render(request,self.template_name)

    def post(self, request, format=None):
        ifsc_code = request.POST.get('ifsc')
        message = {}
        message.update({"message":"Please check input fields"})
        try:
            serializer = Branches.objects.get(ifsc=ifsc_code)
            banks = Banks.objects.get(id=serializer.bank_id_id)
            bank_details = [{'ifsc': serializer.ifsc, 'bank': banks.name, 'address': serializer.address,
                             'branch': serializer.branch, 'state': serializer.state}]

            return render(request, "branches.html", {'branches':bank_details})
        except:
            return render(request,self.template_name,{'details': message})


class CityWiseBranchesDetails(APIView):
    """
    Given a bank name and city, gets details of all branches of the bank in the city

    """
    template_name = "branches_details.html"
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request):
        return render(request,self.template_name)

    def post(self, request, format=None):
        name = request.POST.get('bankname')
        city = request.POST.get('city')
        message = {}
        message.update({"message":"Please check input fields"})
        try:
            bank_serializer = BanksSerializer(Banks.objects.get(name__iexact=name))
            ids = bank_serializer.data['id']
            branches_data = Branches.objects.filter(bank_id=int(ids),city__iexact=city)
            bank_details = []
            for branches in branches_data:
                bank_details.append(
                    {'ifsc': branches.ifsc, 'bank':name, 'address': branches.address, 'branch': branches.branch,
                     'city':branches.city,'state': branches.state})

            return render(request, "branches.html", {'branches':bank_details})
        except:
            return render(request, "branches.html", {'details': message})




