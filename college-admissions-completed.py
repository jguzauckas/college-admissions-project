import json
import jsonpickle


class College:
    def __init__(self, name: str, apps: int, admits: int, enrolls: int) -> None:
        self._name = name
        self._applications = apps
        self._admissions = admits
        self._enrollments = enrolls

    def __str__(self) -> str:
        return f"{self._name} had {self._applications} applications, {self._admissions} admissions, and {self._enrollments} enrollments."

    @property
    def name(self) -> str:
        return self._name

    @property
    def applications(self) -> int:
        return self._applications

    @property
    def admissions(self) -> int:
        return self._admissions

    @property
    def enrollments(self) -> int:
        return self._enrollments

    def admit_app_ratio(self) -> float:
        return self._admissions / self._applications

    def enroll_admit_ratio(self) -> float:
        return self._enrollments / self._admissions


with open("colleges.json", "r") as my_file:
    colleges: list[College] = jsonpickle.loads(json.load(my_file))  # type: ignore

# Highest and lowest applications

# Use the first college as a default because we can guarentee
# that either the first college will have the max / min applications or be overwritten
# by a college with the max / min applications.
max_apps = colleges[0]
min_apps = colleges[0]

for college in colleges:
    if college.applications > max_apps.applications:
        max_apps = college
    elif college.applications < min_apps.applications:
        min_apps = college

print(
    f"The highest number of applications was {max_apps.name} with {max_apps.applications} student(s) applying."
)
print(
    f"The lowest number of applications was {min_apps.name} with {min_apps.applications} student(s) applying."
)

# Highest and lowest admissions
max_admit = colleges[0]
min_admit = colleges[0]

for college in colleges:
    if college.admissions > max_admit.admissions:
        max_admit = college
    elif college.admissions < min_admit.admissions:
        min_admit = college

print()
print(
    f"The highest number of admissions was {max_admit.name} with {max_admit.admissions} student(s) admitted."
)
print(
    f"The lowest number of admissions was {min_admit.name} with {min_admit.admissions} student(s) admitted."
)

# Highest and lowest enrollments
max_enroll = colleges[0]
min_enroll = colleges[0]

for college in colleges:
    if college.enrollments > max_enroll.enrollments:
        max_enroll = college
    elif college.enrollments < min_enroll.enrollments:
        min_enroll = college

print()
print(
    f"The highest number of enrollments was {max_enroll.name} with {max_enroll.enrollments} student(s) enrolling."
)
print(
    f"The lowest number of enrollments was {min_enroll.name} with {min_enroll.enrollments} student(s) enrolling."
)

# Highest and lowest admissions rates
max_admit_app_ratio = colleges[0]
min_admit_app_ratio = colleges[0]

for college in colleges:
    if college.admit_app_ratio() > max_admit_app_ratio.admit_app_ratio():
        max_admit_app_ratio = college
    elif college.admit_app_ratio() < min_admit_app_ratio.admit_app_ratio():
        min_admit_app_ratio = college

print()
print(
    f"The college with the highest rate of admissions is {max_admit_app_ratio.name} with {max_admit_app_ratio.admit_app_ratio():.2%} of applicants being admitted."
)
print(
    f"The college with the lowest rate of admissions is {min_admit_app_ratio.name} with {min_admit_app_ratio.admit_app_ratio():.2%} of applicants being admitted."
)

# Highest and lowest enrollment rates
max_enroll_admit_ratio = colleges[0]
min_enroll_admit_ratio = colleges[0]

for college in colleges:
    if college.enroll_admit_ratio() > max_enroll_admit_ratio.enroll_admit_ratio():
        max_enroll_admit_ratio = college
    elif college.enroll_admit_ratio() < min_enroll_admit_ratio.enroll_admit_ratio():
        min_enroll_admit_ratio = college

print()
print(
    f"The college with the highest rate of enrollments is {max_enroll_admit_ratio.name} with {max_enroll_admit_ratio.admit_app_ratio():.2%} of admitted students enrolling."
)
print(
    f"The college with the lowest rate of enrollments is {min_enroll_admit_ratio.name} with {min_enroll_admit_ratio.admit_app_ratio():.2%} of admitted students enrolling."
)

print()

my_college_name = input("Which college would you like to look at? ")
my_college = colleges[0]

for college in colleges:
    if college.name == my_college_name:
        my_college = college
        break

if my_college.name != my_college_name:
    print(f"Sorry we couldn't fine {my_college_name} in the list of colleges.")
else:
    print(
        f"{my_college.name} had {my_college.applications:,} applications, {my_college.admissions:,} admissions, and {my_college.enrollments:,} enrollments."
    )
    print(
        f"At {my_college.name}, {my_college.admit_app_ratio():.2%} of students that applied were admitted."
    )
    print(
        f"At {my_college.name}, {my_college.enroll_admit_ratio():.2%} of students that were admitted, enrolled."
    )
