from accounts.models import CustomUser
from rest_framework import serializers

from .models import *


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    is_solved_by_me = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id','title','context','module','is_solved_by_me',]

    def get_is_solved_by_me(self, obj):
        request = self.context.get('request')

        if not request or not request.user.is_authenticated:
            return False

        return Subissions.objects.filter(user=request.user,task_id=obj,status='ACCEPTED').exists()


class TestCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subissions
        fields = '__all__'
        read_only_fields = ['user', 'status']