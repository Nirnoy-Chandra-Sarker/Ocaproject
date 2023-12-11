from django.shortcuts import render, HttpResponse, redirect
from .helper import get_designation
from .models import *
from user.models import Advisor, Student, StudentProfile
from django.shortcuts import get_object_or_404
from .forms import *
from django.contrib import messages
from django.db.models import Q


def club_home(request):
    highlights = Highlights.objects.all()
    return render(request, 'homepage.html', {'highlights': highlights})


def all_clubs_info(request):
    clubs_info = ClubInfo.objects.all()
    return render(request, 'clubs_info.html', {'clubs_info': clubs_info})


def club_info(request, id):
    club = None
    club_info = None
    club_achievments = None
    if (Club.objects.filter(id=id)):
        club = (Club.objects.filter(id=id))[0]
    if (ClubInfo.objects.filter(club=club)):
        club_info = (ClubInfo.objects.filter(club=club))[0]
    if (Achievement.objects.filter(club=club)):
        club_achievments = Achievement.objects.filter(club=club)
    return render(request, 'club_info.html', {'club_info': club_info, 'achievements': club_achievments})


def clubs_advisor_info(request):
    clubs = Club.objects.all()
    return render(request, 'clubsadvisorinfo.html', {'clubs': clubs})


def club_dashboard(request):
    advisor = get_object_or_404(Advisor, id=request.user.id)
    clubs = Club.objects.filter(advisor=advisor)
    members = Membership.objects.filter(club__in=clubs).order_by('-id')
    panel_list = []
    for member in members:
        if member.designation.upper() not in ["President".upper(),'Member'.upper(), 'Executive'.upper()]:
            panel_list.append(member)
    
    pres_profile = StudentProfile.objects.get(student = clubs[0].president)
    context = {'advisor': advisor, 'club': clubs[0], 'panel': panel_list,
                'president': clubs[0].president, 'pres_profile': pres_profile}
    return render(request, 'clubdashboard.html', context)

def president_dashboard(request):
    club = Club.objects.get(president = request.user)
    members = Membership.objects.filter(club=club).order_by('-id')
    panel_list = []
    for member in members:
        if member.designation.upper() not in ["President".upper(),'Member'.upper(), 'Executive'.upper()]:
            panel_list.append(member)
    pres_profile = StudentProfile.objects.get(student = request.user)

    context = {'advisor': club.advisor, 'club': club, 'panel': panel_list,
                'president': club.president, 'pres_profile': pres_profile}
    return render(request, "president_dashboard.html", context)

def club_info_update(request):
    club = Club.objects.get(president = request.user)
    club_info = ClubInfo.objects.get(club=club)
    form = ClubInfoForm(instance=club_info)
    if request.method == 'POST':
        form = ClubInfoForm(request.POST, instance=club_info)
        if form.is_valid():
            form.save()
            return redirect('president_dashboard')
    return render(request, 'club_info_update.html', {'form':form})



def recruit(request):
    clubs = Club.objects.filter(recruit=True)
    return render(request, 'request.html', {'clubs': clubs})


def add_event(request):
    club = Club.objects.filter(Q(advisor=request.user) | Q(president=request.user))
    events = Event.objects.all()
    if request.method == "POST":
        form = EventCreationForm(request.POST)
        if form.is_valid:
            data = form.save(commit=False)
            data.club = club[0]
            data.save()
    form = EventCreationForm()
    return render(request, 'add_event.html', {'events': events, 'form': form})


def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('add_event')


def room_book(request):
    club = Club.objects.filter(advisor=request.user)
    form = RoomBookingForm()
    if request.method == "POST":
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            is_booked = Room.objects.filter(
                name=data.name, start_date=data.start_date, end_date=data.end_date)
            if is_booked:
                messages.warning(request, "Room is Already Booked")
            else:
                data.club = club[0]
                data.save()
    return render(request, 'room_book.html', {'form': form})


def upcoming_events(request, id):
    club = Club.objects.get(id=id)
    events = Event.objects.filter(club=club)
    return render(request, 'upcoming_events.html', {'events': events})


def event_details(request, id):
    event = Event.objects.get(id=id)
    sponsors = Sponsor.objects.filter(event=event)
    room = Room.objects.filter(event=event)
    context = {"event": event, 'sponsors': sponsors}
    if room:
        context = {"event": event, 'sponsors': sponsors, 'room': room[0]}
    return render(request, 'event_details.html', context)


def assign_budget(request):
    club = Club.objects.get(advisor=request.user)
    budget = None
    transactions = Transaction.objects.filter(club=club)
    if Budget.objects.filter(club=club):
        budget = Budget.objects.filter(club=club)[0]

    if request.method == "POST":
        form = BudgetAssignForm(request.POST, instance=budget)
        if form.is_valid():
            new_assigned_budget = form.cleaned_data['assigned_budget']
            if new_assigned_budget > budget.remaining_budget:
                messages.warning(request, "You don't have Sufficient amount")
                return redirect('assignbudget')
            else:
                assigned_budget_change = new_assigned_budget - budget.assigned_budget

                budget.assigned_budget = new_assigned_budget
                budget.remaining_budget -= assigned_budget_change
                budget.save()
                transaction = Transaction(club=club, transaction=budget.assigned_budget)
                transaction.save()

            return redirect('club_dashboard')
    else:
        form = BudgetAssignForm(instance=club)

    return render(request, 'budget.html', {'form': form, 'budget': budget, 'transactions': transactions})


def highlight_details(request, id):
    highlight = Highlights.objects.get(id=id)
    return render(request, 'highlights.html', {'highlight': highlight})
