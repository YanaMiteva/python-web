from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from django102.models.game import Game
from django102.models.person import Person
from django102.models.player import Player

p = Person(first_name='Yana', last_name='Smith', age=20)

def index(request):
    title = "SoftUni django101"
    users = User.objects.all()
    games = Game.objects.all_with_players_count()

    context = {
        'title': title,
        'users': users,
        'games': games,
    }
    return render(request, 'index.html', context)


def something(request):
    return HttpResponse("<u>Hello, world. You're at the polls page.</u>")
class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From ClassView'
        return context

class GamesListView(ListView):
    model = Game
    template_name = 'games.html'

@require_GET
def methods_demo(request):
    if request.method == 'GET':
        context = {
            'name': 'Yana',
            'age': 20
        }
        if request.content_type == 'application/json':
            return JsonResponse(context)

        return render(request, 'methods_demo.html', context)


def raises_exception(request):
    raise Exception('Something went wrong')


def create_game(request):
    game = Game (
        name='Call of Duty',
        level_of_difficulty=1
    )
    game.save()
    return redirect(request, 'index',)