
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name=""),

    path('register', views.register, name="register"),

    path('my-login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create-record"),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),

    path('reportsuspect/', views.reportsuspectView, name="reportsuspect"),

    path('suspect/<int:pk>', views.singular_suspect, name="suspect"),


#	 path('crime_reports_list/<int:pk>', views.crime_reports_list, name="crime_reports_list"),
#    path('create-report/', views.create_report, name="create-report")
#    path('wanted/', views.wantedView, name="wanted-list"),
#    path('tips/', views.tipsView, name="tips"),
#    path('announcements/', views.news, name="news")
]
