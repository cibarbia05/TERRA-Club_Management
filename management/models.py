from django.db import models

# from authentication.models import User, Member, Sponsor, Officer
from authentication.models import User


class Document(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()

    def get_name(self):
        return self.name

    def get_file(self):
        return self.file

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name="participants")
    members = models.ManyToManyField(User,  related_name="members")
    sponsors = models.ManyToManyField(User,  related_name="sponsors")
    officers = models.ManyToManyField(User,  related_name="officers")
    document_descriptions = models.ForeignKey(Document, blank=True, null=True, default=None,
                                              on_delete=models.SET_DEFAULT,
                                              related_name="document_descriptions")
    document_forms = models.ForeignKey(Document, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT,
                                       related_name="document_forms")
    document_files = models.ForeignKey(Document, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT,
                                       related_name="document_files")
    club_primary_image = models.ImageField(upload_to='images/', null=True, blank=True,
                                           verbose_name='club_primary_image')
    club_secondary_image = models.ImageField(upload_to='images/', null=True, blank=True,
                                             verbose_name='club_secondary_image')

    # closing_join_time = models.DateTimeField()
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_participants(self):
        return self.participants

    def get_document_descriptions(self):
        return self.document_descriptions

    def get_document_forms(self):
        return self.document_forms

    def get_document_files(self):
        return self.document_files

    def __str__(self):
        return self.name


class Event(models.Model):
    club = models.ForeignKey(Club, blank=True, null=True, default=None, on_delete=models.SET_DEFAULT,
                             related_name="club")
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
