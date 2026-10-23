from django.shortcuts import render

# Create your views here.
import subprocess

from rest_framework import generics, status

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class CoursesView(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class ModulesView(ModelViewSet):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer


class TaskView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TestCasesView(ModelViewSet):
    queryset = TestCases.objects.all()
    serializer_class = TestCasesSerializer


class SubmissionsView(APIView):

    @swagger_auto_schema(
        request_body=SubmissionSerializer,
        responses={201: "Submission result",400: "Validation error",},
    )
    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = serializer.validated_data["task_id"]
        code = serializer.validated_data["code"]
        user = request.user


        submission = Subissions.objects.create(
            user=user,
            code=code,
            task=task,
        )

        test_cases = TestCases.objects.filter(task=task)

        for test in test_cases:
            result = subprocess.run(('python','-c',code),text = True,capture_output = True, input = test.input)
            if result.stdout.strip()!=test.output:
                submission.status = 'WRONG_ANSWER'
                submission.save()
                return Response({
                    'id': submission.id,
                    'code': code,
                    'expacted_output':test.output,
                    'your code':result.stdout,
                    'status': submission.status
                })
        submission.status = 'ACCEPTED'
        submission.save()
        return Response({
                            'id': submission.id,
                            'code': code,
                            'status': submission.status
                        })
                



       