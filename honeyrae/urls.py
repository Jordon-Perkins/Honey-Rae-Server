from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user, CustomerView, EmployeeView, ServiceTicketView
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'employees', EmployeeView, 'employee')
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tickets', ServiceTicketView, 'service_tickets')

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]