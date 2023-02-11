from django.shortcuts import render

from .forms import CreateUserForm


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'pages/accounts/signup.html', {'form': form})
