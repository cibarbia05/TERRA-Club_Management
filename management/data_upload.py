from authentication.models import User
from management.models import Club


def upload_teacher_data(excel_file):
    file_data = excel_file.read().decode("utf-8")

    lines = file_data.split("\n")

    # loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        fields = line.split(",")
        data_dict = {}
        try:
            user = User.objects.create_user_no_password(name=fields[0], school_id=fields[1],
                                                        email=fields[1] + "@students.dadeschools.net")
            data_dict["Teacher Name"] = fields[0]
            data_dict["Employee Number"] = str(fields[1]).split('\r')[0]

        except Exception as e:
            print(e)


def upload_student_data(excel_file):
    file_data = excel_file.read().decode("utf-8")

    lines = file_data.split("\n")

    # loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        fields = line.split(",")
        data_dict = {}
        try:
            user = User.objects.create_user_no_password(name=fields[0], school_id=fields[1],
                                                        email=fields[1] + "@students.dadeschools.net")
            data_dict["Student Name"] = fields[0]
            data_dict["Student Id"] = str(fields[1]).split('\r')[0]

        except Exception as e:
            print(e)


def upload_club_data(excel_file):
    file_data = excel_file.read().decode("utf-8")

    lines = file_data.split("\n")

    # loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        if line != lines[0]:
            try:
                fields = line.split(",")
                corresponding_user = User.objects.get(name=str(fields[1]).split('\r')[0])
                club = Club.objects.create(name=str(fields[0]).split('\r')[0])
                club.save()
                club.sponsors.add(corresponding_user)



            except Exception as e:
                print(e)
