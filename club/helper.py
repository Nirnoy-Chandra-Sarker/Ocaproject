def get_designation(Student, Club, Model):
    membership = Model.objects.get(student = Student, club = Club)
    return membership.designation

def calculate_remaining(a, b):
    return a - b