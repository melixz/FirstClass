from django.shortcuts import render
from django.http import HttpRequest

from .forms import FeedbackForm
from .models import Feedback


def feedback(request: HttpRequest, template_name='index.html'):
    # form = FeedbackForm(request.POST or None, template_name)
    # if form.is_valid():
    #     form.save()
    #     return render(request, template_name='index.html')
    # return render(request, template_name=template_name, context={'form': form})

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            full_name = form_data['full_name']
            number = form_data['number']
            email = form_data['email']
            contact_method = form_data['contact_method']
            Feedback.objects.create(full_name=full_name, number=number, email=email,
                                    contact_method=contact_method)
    elif request.method == 'GET':
        form = FeedbackForm()
        return render(request, template_name=template_name, context={'form': form})
    return render(request, template_name=template_name, context={'form': FeedbackForm()})


# class FeedbackView(CreateView):
#     template_name = 'feedback.html'
#     model = Feedback
#     form_class = FeedbackForm
#     success_url = ''
#     success_message = 'Your feedback has been successfully submitted'
#     error_message = 'Your feedback could not be submitted'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)
