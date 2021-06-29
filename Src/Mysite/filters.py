from django.db import models
import django_filters


from .models import patients


class patientsfilter(django_filters.FilterSet):

    class Meta:
        models = patients
        fields = [
            'name',
            'gender',
            'age',
        ]
