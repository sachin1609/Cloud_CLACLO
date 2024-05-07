from django.shortcuts import render
from .models import University
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required
from .models import University

@login_required
@permission_required('university_service.change_university', raise_exception=True)
def activate_university(request, uni_id):
    university = get_object_or_404(University, id=uni_id)
    university.is_active = True
    university.activation_date = timezone.now()
    university.save()
    return HttpResponse("University Activated")

@login_required
@permission_required('university_service.change_university', raise_exception=True)
def deactivate_university(request, uni_id):
    university = get_object_or_404(University, id=uni_id)
    university.is_active = False
    university.deactivation_date = timezone.now()
    university.save()
    return HttpResponse("University Deactivated")
