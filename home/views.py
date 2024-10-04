from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages

# Homepage View
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
