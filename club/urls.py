from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.club_home, name='club_home'),
    path('clubs-info/', views.all_clubs_info, name='clubs_info'),
    path('club-details/<int:id>/', views.club_info, name='club-info'),
    path('dashboard/', views.club_dashboard, name='club_dashboard'),
    path('president/dashboard/', views.president_dashboard, name='president_dashboard'),
    path('request/', views.recruit, name='recruit'),
    path('add-event/', views.add_event, name='add_event'),
    path('delete_event/<int:id>', views.delete_event, name='delete_event'),
    path('info/advisors', views.clubs_advisor_info, name='clubs_advisor_info'),
    path('info/upcoming-events/<int:id>/',
         views.upcoming_events, name='upcoming_events'),
    path('event_details/<int:id>', views.event_details, name='event_details'),
    path('roombook/', views.room_book, name="room_book"),
    path('assignbudget/', views.assign_budget, name="assignbudget"),
    path('highlights/details/<int:id>', views.highlight_details, name='highlight_details'),
    path('info/update/', views.club_info_update, name='club_info_update')
]
