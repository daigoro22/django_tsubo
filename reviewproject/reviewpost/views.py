from django.shortcuts import render

# Create your views here.
def signupview(request):
    if request.method == 'POST':
        print('POST method')
    else:
        print('Get method probably...')
    return render(request, 'signup.html',{})