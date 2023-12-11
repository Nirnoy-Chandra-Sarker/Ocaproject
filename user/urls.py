from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("profile/", views.profile_view, name = 'profile'),
    path('register/', views.register, name = 'register'),
    path('student/register/', views.student_register, name = 'student_register'),
    path('student/complete_profile/', views.complete_profile, name = 'complete_profile'),
    path('student/profile/<int:id>/', views.student_profile, name = 'student_profile'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('update/<str:user_id>', views.user_info_update, name = 'user_update'),
    path('password-reset/', views.password_reset, name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/', views.password_confirm, name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] 