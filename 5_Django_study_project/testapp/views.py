from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'testapp/home.html'

    def render_to_response(self, context, **response_kwargs):

        if self.request.COOKIES.get('my_cookie') == 'my_cookie_value':
            response = HttpResponse('WITH COOKIE!')
            return response
        return super().render_to_response(context, **response_kwargs)


class AboutPageView(TemplateView):
    template_name = 'testapp/about.html'


def home_view(request):
    print(request)
    print(request.method == "GET")
    print(request.method)
    print(request.COOKIES)
    response = render(request, 'testapp/home2.html', {"message": "Welcome to the homepage!"})
    print('Response:', response)
    return response
    # response_2 = HttpResponse("Welcome to the homepage!")
    # response_2.write("<h1> Hello World! </h1>")
    # return response_2


def about_view(request):
    return render(request, 'testapp/about2.html', {"message": "About us page!"})


def server_time_view(request):
    return render(request, 'testapp/server_time.html')


class LoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.COOKIES.get('my_cookie') != 'my_cookie_value':
            return HttpResponse("You are not logged in!")
        return super().dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'testapp/dashboard.html'

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        response.set_cookie('my_cookie', 'my_cookie_value')
        return response

    # what this render_to_response method does is that it first calls the render_to_response method of the parent class,
    # which is the TemplateView class, and then it sets the cookie on the response object that is returned by the parent class.
    # So, the parent class is responsible for rendering the template and returning the response object, and then we are
    # setting the cookie on that response object.

    # The reason we are doing this is that we want to set the cookie only if the user is logged in. If the user is not logged in,
    # then we don't want to set the cookie. So, we are checking if the user is logged in or not, and if the user is logged in,
    # then we are setting the cookie. If the user is not logged in, then we are not setting the cookie.

    # So, this is how we can use the render_to_response method to set the cookie on the response object.

