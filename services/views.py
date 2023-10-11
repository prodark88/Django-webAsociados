from django.shortcuts import render
from .models import Service , Category , SubCategory
# Create your views here.
def services(request):
    services =Category.objects.all()
    context = {
        'services':services,
    }
    return render(request,'services/services.html', context)

def services_by_especialidad(request, id):
    category = Category.objects.get(pk=id)
    sub_categories = category.subcategory_set.all()
    services = category.service_set.all()
    print(category)
    print(sub_categories)
    print(services)
    context = {
        'categories':[category] if category else [],
        'sub_categories':sub_categories,
        'services':services,
    }
    return render(request,'services/services_detail.html', context)

""" categories =Category.objects.get(pk =id)
    sub_categories = SubCategory.objects.filter(category=categories)
    services = Service.objects.filter(category=categories)
    print(categories)
    print(sub_categories)
    print(services) """