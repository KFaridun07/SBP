from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register('courses', CoursesView, basename='courses')
router.register('modules', ModulesView, basename='modules')
router.register('task', TaskView, basename='task')
router.register('test-case', TestCasesView, basename='test-case')

urlpatterns = [
    path('', include(router.urls)),
    path('submit',SubmissionsView.as_view())

]