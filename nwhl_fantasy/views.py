from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Teams
from .models import Players

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'index.html', context=None)

def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    team1 = Teams.objects.get(team_id=1)
    context = {'fwd1': (team1.fwd1.first_name + " " + team1.fwd1.last_name),
                'fwd2': (team1.fwd2.first_name + " " + team1.fwd2.last_name),
                'fwd3': (team1.fwd3.first_name + " " + team1.fwd3.last_name),
                'def1': (team1.def1.first_name + " " + team1.def1.last_name),
                'def2': (team1.def2.first_name + " " + team1.def2.last_name),
                'goalie': (team1.goalie.first_name + " " + team1.goalie.last_name),
                'util': (team1.util.first_name + " " + team1.util.last_name),
                'bench1': (team1.bench1.first_name + " " + team1.bench1.last_name),
                'bench2': (team1.bench2.first_name + " " + team1.bench2.last_name),
                'bench3': (team1.bench3.first_name + " " + team1.bench3.last_name),
                'bench4': (team1.bench4.first_name + " " + team1.bench4.last_name)

}
    return render(request, 'index.html', context)
#    return HttpResponse("Hello, world. You're at the nwhl fantasy hockey index. The first player on Hailey's team is " + (team1.fwd1.first_name + " " + team1.fwd1.last_name))

# eventually when there are differnet teams and leagues, the "query" will be more complicated and will include the league id and team id, so it'll be like Teams.objects.get(team_id = X, league_id = Y)

# Create your views here.


