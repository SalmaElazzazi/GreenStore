from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Contact_Us

def contact(request):
    contact_form = Contact_Us()
    if request.method == 'POST':
        contact_form = Contact_Us(request.POST)
        if contact_form.is_valid():
            new_comment = contact_form.save(commit=False)
            new_comment.save()
            messages.success(
                request, 'Votre message a été envoyé avec succès.'
            )
            return redirect('home')
    
    context = {
        'title': 'Contact Us',
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context)

def about(request):
    return render(request, 'about.html')
