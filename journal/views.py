# from rest_framework import viewsets
# from .models import Mood, Category, JournalEntry
# from .serializers import MoodSerializer, CategorySerializer, JournalEntrySerializer

# class MoodViewSet(viewsets.ModelViewSet):
#     queryset = Mood.objects.all()
#     serializer_class = MoodSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class JournalEntryViewSet(viewsets.ModelViewSet):
#     queryset = JournalEntry.objects.all()
#     serializer_class = JournalEntrySerializer




# from rest_framework import viewsets
# from .models import Mood, Category, JournalEntry
# from .serializers import MoodSerializer, CategorySerializer, JournalEntrySerializer

# class MoodViewSet(viewsets.ModelViewSet):
#     queryset = Mood.objects.all()
#     serializer_class = MoodSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class JournalEntryViewSet(viewsets.ModelViewSet):
#     queryset = JournalEntry.objects.all()
#     serializer_class = JournalEntrySerializer

#     def perform_create(self, serializer):
#         # هذا السطر يربط الملاحظة بالمستخدم الحالي تلقائيًا من التوكن
#         serializer.save(user=self.request.user)








# from rest_framework import viewsets
# from .models import Mood, Category, JournalEntry
# from .serializers import MoodSerializer, CategorySerializer, JournalEntrySerializer

# class MoodViewSet(viewsets.ModelViewSet):
#     queryset = Mood.objects.all()
#     serializer_class = MoodSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class JournalEntryViewSet(viewsets.ModelViewSet):
#     queryset = JournalEntry.objects.all()
#     serializer_class = JournalEntrySerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


from rest_framework import viewsets, permissions
from .models import Mood, Category, JournalEntry
from .serializers import MoodSerializer, CategorySerializer, JournalEntrySerializer

class MoodViewSet(viewsets.ModelViewSet):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

