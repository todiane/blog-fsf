from django.shortcuts import render
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return render(request, 'contact/contact_success.html', {"contact": contact})
    
    else:        
        form = ContactForm()
        
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
