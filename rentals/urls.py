from django.urls import path
from . import views

app_name = 'rentals'  # Ensure namespace is set correctly

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('our-cars/', views.our_cars_view, name='our_cars'),  # Ensure this exists
    path('contact-us/', views.contact_us, name='contact_us'),
    path('register/', views.register, name='register'),
    path('cars/', views.car_list, name='car_list'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('book/', views.book_car, name='book_car'),
    # Add this to urlpatterns
    

  

path('book-now/', views.book_now_view, name='book_now'),  # No preselected car
    path('book-now/<int:car_id>/', views.book_now_view, name='book_now_with_car'),  # With preselected car

]
