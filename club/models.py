from django.db import models
from user.models import Student, Advisor


class Highlights(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='highlights/')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Club(models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=15, null=True, blank=True)
    advisor = models.OneToOneField(
        Advisor, on_delete=models.CASCADE, null=True, blank=True, related_name='club_advisor')
    president = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name='president_of')
    students = models.ManyToManyField(
        Student, through='Membership', related_name='member')
    recruit = models.BooleanField(default=False)


    def __str__(self):
        return self.name



class ClubInfo(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    contact_mail = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='club_photo/')

    def __str__(self):
        return self.club.short_name


class Achievement(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='achivements/')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    achieved_date = models.DateField()

    def __str__(self):
        return f"{self.title} Achieved By {self.club.short_name}"


class Membership(models.Model):
    DESIGNATION_CHOICES = (
        ('Vice President', 'Vice President'),
        ('Secretary', 'Secretary'),
        ('Senior Executive', 'Senior Executive'),
        ('Executive', 'Executive'),
        ('Member', 'Member'),
    )
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.club.name} ({self.designation})"


class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    eventname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
    enrollurl = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.eventname


ROOMNAME = (
    ('UB20202', 'UB20202'),
    ('UB60101', 'UB60101'),
    ('UB60909', 'UB60909'),
)


class Room(models.Model):
    name = models.CharField(max_length=50, choices=ROOMNAME)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True, blank=True)

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.event.eventname} by {self.club.short_name}"


class Sponsor(models.Model):
    class Title(models.TextChoices):
        GOLD = "Golden", "Golden"
        SILVER = "Silver", "Silver"
        BRONZE = "Bronze", "Bronze"
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, choices=Title.choices, null=True)
    url= models.URLField(null=True,blank=True)

    def __str__(self):
        return self.name


class Budget(models.Model):
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True, blank=True)
    total_budget = models.IntegerField(default=0)
    remaining_budget = models.IntegerField(default=0)
    assigned_budget = models.IntegerField(default=0)

    def __str__(self):
        return self.club.name

    def rp(self):
        return (self.remaining_budget/self.total_budget) * 100

    def save(self, *args, **kwargs):
        self.remaining_budget -= self.assigned_budget
        super().save(*args, **kwargs)


class Transaction(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    transaction = models.IntegerField(null=True, blank=True)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.club.name
