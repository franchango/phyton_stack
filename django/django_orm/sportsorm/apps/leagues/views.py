from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		# # All teams in the Atlantic Soccer Conference
		# "teams": Team.objects.filter(league = 5),
		# # All (current) players on the Boston Penguins
		# "players": Player.objects.filter(curr_team = 28),
		# # All (current) players in the International Collegiate Baseball Conference
		# "players": Player.objects.filter(curr_team__league_id = 2),
		# # All (current) players in the American Conference of Amateur Football with last name "Lopez"
		# "players": Player.objects.filter(curr_team__league_id = 7).filter(last_name = 'Lopez'),
		# # All football players
		# "players": Player.objects.filter(curr_team__league__sport = 'Football'),
		# # All teams with a (current) player named "Sophia"
		# "teams": Team.objects.filter(curr_players__first_name = 'Sophia'),
		# # All leagues with a (current) player named "Sophia"
		# "leagues": League.objects.filter(teams__curr_players__first_name = 'Sophia'),
		# # Everyone with the last name "Flores" who DOESN'T (currently) play for the Washington Roughriders
		# "players": Player.objects.filter(last_name = 'Flores').exclude(curr_team_id = 10),
		# # All teams, past and present, that Samuel Evans has played with
		# "teams": Team.objects.filter(all_players__id = 115),
		# # All players, past and present, with the Manitoba Tiger-Cats
		# "players": Player.objects.filter(all_teams__id = 37),
		# # All players who were formerly (but aren't currently) with the Wichita Vikings
		# "players": Player.objects.filter(all_teams__id = 40).exclude(curr_team_id = 40),
		# # Every team that Jacob Gray played for before he joined the Oregon Colts
		# "teams": Team.objects.filter(all_players__id = 151).exclude(curr_players__id = 151),
		# # Everyone named "Joshua" who has ever played in the Atlantic Federation of Amateur Baseball Players
		# "players": Player.objects.filter(all_teams__league_id = 3).filter(first_name = 'Joshua'),
		# # All teams that have had 12 or more players, past and present. (HINT: Look up the Django annotate function.)
		# "teams": Team.objects.annotate(nplayer=Count('all_players')).filter(nplayer__gt=12),
		# # All players and count of teams played for, sorted by the number of teams they've played for
		# "teams": Team.objects.annotate(nplayer=Count('all_players')).order_by('nplayer')
		
		# "leagues": League.objects.all(),
		# "teams": Team.objects.all(),
		# "players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")