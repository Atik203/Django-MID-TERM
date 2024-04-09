from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView

from .forms import CommentForm
from .models import CarModel, Order


@method_decorator(login_required, name='dispatch')
class CarDetailView(DetailView):
    model = CarModel
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'car'
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car_model = self.get_object()
            comment.save()
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        context['comments'] = car.comments.all()
        context['form'] = CommentForm()
        return context

@login_required
def buy_car(request,id):
    car = CarModel.objects.get(pk=id)
    if car.quantity == 0:
        messages.warning(request, 'This car is out of stock')
    else:
        car.quantity -= 1
        order = Order(car=car, user=request.user)
        messages.success(request, 'You have successfully bought this car')
        order.save()
        car.save()
    return render(request,'buy.html',{'car':car})