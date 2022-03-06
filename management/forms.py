from django import forms


class UploadTeacherFileForm(forms.Form):
    teacher_data = forms.FileField(label='',
                                   widget=forms.FileInput(attrs={'class': 'dropzone box', 'name': 'teacher_data'}))


class UploadStudentFileForm(forms.Form):
    student_data = forms.FileField(label='',
                                   widget=forms.FileInput(attrs={'class': 'dropzone box', 'name': 'student_data'}))


class UploadClubFileForm(forms.Form):
    club_data = forms.FileField(label='', widget=forms.FileInput(attrs={'class': 'dropzone box', 'name': 'club_data'}))
