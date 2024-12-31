# api/router.py

from rest_framework_nested import routers
from customer.views import AuthViewSet  # Our auth logic
from customer.views import UserViewSet, RoleViewSet
from homelife.views import HouseholdViewSet, ChoreViewSet, SharedCalendarEventViewSet
from finances.views import BankAccountViewSet, BudgetViewSet, TransactionViewSet
from work.views import TeamViewSet, ProjectViewSet, WorkTaskViewSet
from school.views import CourseViewSet, AssignmentViewSet, SubmissionViewSet
from investing.views import PortfolioViewSet, AssetViewSet, TradeTransactionViewSet
from notifications.views import NotificationViewSet

# 1) Create the base router
router = routers.DefaultRouter()

# 2) Register top-level endpoints
## Auth
router.register(r'auth', AuthViewSet, basename='auth')

## Customer
router.register(r'users', UserViewSet, basename='users')
router.register(r'roles', RoleViewSet, basename='roles')

## Homelife
router.register(r'households', HouseholdViewSet, basename='households')
router.register(r'chores', ChoreViewSet, basename='chores')
router.register(r'shared-events', SharedCalendarEventViewSet, basename='sharedcalendar')

## Finances
router.register(r'bank-accounts', BankAccountViewSet, basename='bankaccounts')
router.register(r'budgets', BudgetViewSet, basename='budgets')
router.register(r'transactions', TransactionViewSet, basename='transactions')

## Work
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'worktasks', WorkTaskViewSet, basename='worktasks')

## School
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'submissions', SubmissionViewSet, basename='submissions')

## Investing
router.register(r'portfolios', PortfolioViewSet, basename='portfolios')
router.register(r'assets', AssetViewSet, basename='assets')
router.register(r'trade-transactions', TradeTransactionViewSet, basename='tradetransactions')

## Notifications
router.register(r'notifications', NotificationViewSet, basename='notifications')