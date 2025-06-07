# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import MoodViewSet, CategoryViewSet, JournalEntryViewSet

# router = DefaultRouter()
# router.register(r'moods', MoodViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'entries', JournalEntryViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# from rest_framework.routers import DefaultRouter
# from .views import MoodViewSet, CategoryViewSet, JournalEntryViewSet

# router = DefaultRouter()
# router.register(r'moods', MoodViewSet)
# router.register(r'categories', CategoryViewSet)
# router.register(r'entries', JournalEntryViewSet)

# urlpatterns = router.urls

from rest_framework.routers import DefaultRouter
from .views import MoodViewSet, CategoryViewSet, JournalEntryViewSet

router = DefaultRouter()
router.register(r'moods', MoodViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'entries', JournalEntryViewSet, basename='entries')  # هنا أضفنا basename

urlpatterns = router.urls


