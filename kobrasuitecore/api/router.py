from django.conf import settings
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r"users", user.views.UserViewSet)
router.register(r"login", user.views.LoginViewSet, basename="login")
router.register(r"logout", user.views.LogoutViewSet, basename="logout")
router.register(r"customers", customer.views.CustomerViewSet, basename="customers")

# Customer
customer_router = routers.NestedDefaultRouter(router, r"customers", lookup="customer")

# Homelife
homelife_router = routers.NestedDefaultRouter(router, r"homelife", lookup="homelife")

# Finances
finances_router = routers.NestedDefaultRouter(router, r"finances", lookup="finances")

# Work
work_router = routers.NestedDefaultRouter(router, r"work", lookup="work")

# School
school_router = routers.NestedDefaultRouter(router, r"school", lookup="school")

# Investing
investing_router = routers.NestedDefaultRouter(router, r"investing", lookup="investing")

# Notifications
notifications_router = routers.NestedDefaultRouter(router, r"notifications", lookup="investing")