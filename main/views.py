from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

# Global votes dictionary: IP -> vote
votes = {}

# Create your views here.
def home(request):
    tomato_count = sum(1 for v in votes.values() if v == 'tomato')
    not_tomato_count = sum(1 for v in votes.values() if v == 'not tomato')
    return render(request, 'main/home.html', {
        'tomato_count': tomato_count,
        'not_tomato_count': not_tomato_count
    })

def vote(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        vote_option = data.get('vote')
        print(vote_option)
        voter_ip = request.META.get('REMOTE_ADDR', 'unknown')
        print(voter_ip)
        votes[voter_ip] = vote_option
        tomato_count = sum(1 for v in votes.values() if v == 'tomato')
        not_tomato_count = sum(1 for v in votes.values() if v == 'not tomato')

        print(votes)
        return JsonResponse({
            'tomato_count': tomato_count,
            'not_tomato_count': not_tomato_count
        })
