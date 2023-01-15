from django.shortcuts import render, redirect

from stocky.models import Category, SubCategory


def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')

        category = Category(name=name, description=description)
        category.save()
        return redirect('/')
    else:
        return render(request, 'pages/categories/add_category.html')


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = SubCategory.objects.filter(category_id=category_id)
    return render(request, 'pages/categories/categories.html', {'subcategories': subcategories})


def categories(request):
    parents_categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = {'categories': parents_categories, 'subcategories': subcategories}
    return render(request, 'pages/categories/categories.html', context)
