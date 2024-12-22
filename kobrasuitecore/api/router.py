from django.conf import settings
from rest_framework_nested import routers

router = routers.DefaultRouter()

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
notifications_router = routers.NestedDefaultRouter(router, r"notifications", lookup="notifications")