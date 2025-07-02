from django.shortcuts import render

# Create your views here.
def render_sign_up_page(request):
	return render(request, 'public/signUp.html')


def render_sign_in_page(request):
	return render(request, 'public/sign_in.html')