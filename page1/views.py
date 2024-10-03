from django.shortcuts import render

# View for Page 1
def page1_view(request):
    return render(request, 'page1/page1.html')
