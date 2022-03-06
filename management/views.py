import csv

# import pandas as pd
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from authentication.models import User
from authentication.user_utility import is_club_sponsor
from management.data_upload import upload_teacher_data, upload_club_data
from management.forms import UploadTeacherFileForm, UploadStudentFileForm, UploadClubFileForm
from management.models import Club


# from pyexcel_xls import get_data as xls_get
# from pyexcel_xlsx import get_data as xlsx_get


def dashboard(request):
    # print(is_club_sponsor)
    clubs = Club.objects.filter(name=is_club_sponsor(request.user))
    return render(request, 'management/dashboard.html', {
        "is_club_sponsor": is_club_sponsor(request.user),
        "clubs": clubs,
        "navbar": "dashboard",
    })


def all_clubs(request):
    clubs = Club.objects.all()
    return render(request, 'management/all_clubs.html', {
        'clubs': clubs,
        "navbar": "all_clubs",
    })


def my_clubs(request):
    clubs = Club.objects.filter(name=is_club_sponsor(request.user))
    return render(request, 'management/my_clubs.html', {
        'clubs': clubs,
        "navbar": "my_clubs",
    })


def favorites(request):
    return render(request, 'management/favorites.html', {
        "navbar": "favorites",
    })


def analytics(request):
    return render(request, 'management/analytics.html', {
        "navbar": "analytics",
    })


def documents(request):
    print('Manijkfdfd')
    global data
    if request.method == "GET":
        upload_teacher_excel_file_form = UploadTeacherFileForm()
        upload_student_excel_file_form = UploadStudentFileForm()
        upload_club_excel_file_form = UploadClubFileForm()
        return render(request, 'management/documents.html', {
            'upload_teacher_excel_file_form': upload_teacher_excel_file_form,
            'upload_student_excel_file_form': upload_student_excel_file_form,
            'upload_club_excel_file_form': upload_club_excel_file_form,
            "navbar": "documents",

        })
    else:
        upload_teacher_excel_file_form = UploadTeacherFileForm(request.POST, request.FILES)
        upload_student_excel_file_form = UploadStudentFileForm(request.POST, request.FILES)
        upload_club_excel_file_form = UploadClubFileForm(request.POST, request.FILES)

        # excel_file_teacher_data = request.FILES['teacher_data']
        # print(excel_file_teacher_data)
        # upload_teacher_data(excel_file_teacher_data)
        #
        # excel_file_student_data = request.FILES['student_data']
        # print(excel_file_student_data)
        # upload_teacher_data(excel_file_student_data)

        excel_file_club_data = request.FILES['club_data']
        print(excel_file_club_data)
        print("AYO")
        if excel_file_club_data is not None:
            upload_club_data(excel_file_club_data)
            return render(request, 'management/documents.html', {
                'upload_teacher_excel_file_form': upload_teacher_excel_file_form,
                'upload_student_excel_file_form': upload_student_excel_file_form,
                'upload_club_excel_file_form': upload_club_excel_file_form,
                "navbar": "documents",
            })


def settings(request):
    pass


def club_info(request, club_id):
    selected_club = Club.objects.get(pk=club_id)
    return render(request, 'management/club_info.html', {
        'club': selected_club,
    })
