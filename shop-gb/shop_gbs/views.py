from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game, GameDescription, Cart
from django.urls import reverse_lazy

class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'
    context_object_name = 'games'
    queryset = Game.objects.all()

class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'

class GameDescriptionDetailView(DetailView):
    model = GameDescription
    template_name = 'game_description_detail.html'
    context_object_name = 'description'

class GameCreateView(CreateView):
    model = Game
    template_name = 'game_form.html'
    fields = '__all__'

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'game_form.html'
    fields = '__all__'
    context_object_name = 'game'

class CartListView(ListView):
    model = Cart

class CartDetailView(DetailView):
    model = Cart

class CartCreateView(CreateView):
    model = Cart
    fields = ['games', 'total_price']
    success_url = reverse_lazy('cart_list')

class CartUpdateView(UpdateView):
    model = Cart
    fields = ['games', 'total_price']
    success_url = reverse_lazy('cart_list')

class CartDeleteView(DeleteView):
    model = Cart
    success_url = reverse_lazy('cart_list')