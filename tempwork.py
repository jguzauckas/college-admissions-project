import json
import jsonpickle
import csv

colleges_raw = []
with open("colleges.csv") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        colleges_raw.append(row)


class College:
    def __init__(self, name: str, apps: int, admits: int, enrolls: int) -> None:
        self._name = name
        self._applications = apps
        self._admissions = admits
        self._enrollees = enrolls

    def __str__(self) -> str:
        return f"{self._name} had {self._applications} applications, {self._admissions} admissions, and {self._enrollees} enrollees."

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
    def enrollees(self) -> int:
        return self._enrollees

    def admit_app_ratio(self) -> float:
        return self._admissions / self._applications

    def enroll_admit_ratio(self) -> float:
        return self._enrollees / self._admissions


colleges = []

for college_raw in colleges_raw:
    college = College(
        college_raw[0], int(college_raw[1]), int(college_raw[2]), int(college_raw[3])
    )
    colleges.append(college)

colleges_pickle = jsonpickle.dumps(colleges)

with open("colleges.json", "w") as my_file:
    json.dump(colleges_pickle, my_file)


max_apps = College("Max", 0, 0, 0)
min_apps = College("Min", 1_000_000, 1_000_000, 1_000_000)
max_admit = College("Max", 0, 0, 0)
min_admit = College("Min", 1_000_000, 1_000_000, 1_000_000)
max_enroll = College("Max", 0, 0, 0)
min_enroll = College("Min", 1_000_000, 1_000_000, 1_000_000)
for college in colleges:
    if college.applications > max_apps.applications:
        max_apps = college
    elif college.applications < min_apps.applications:
        min_apps = college
    if college.admissions > max_admit.admissions:
        max_admit = college
    elif college.admissions < min_admit.admissions:
        min_admit = college
    if college.enrollees > max_enroll.enrollees:
        max_enroll = college
    elif college.enrollees < min_enroll.enrollees:
        min_enroll = college

print(
    f"The highest number of applications was {max_apps.name} with {max_apps.applications} student(s) applying."
)
print(
    f"The lowest number of applications was {min_apps.name} with {min_apps.applications} student(s) applying."
)

print()
print(
    f"The highest number of admissions was {max_admit.name} with {max_admit.admissions} student(s) admitted."
)
print(
    f"The lowest number of admissions was {min_admit.name} with {min_admit.admissions} student(s) admitted."
)

print()
print(
    f"The highest number of enrollees was {max_enroll.name} with {max_enroll.enrollees} student(s) enrolling."
)
print(
    f"The lowest number of enrollees was {min_enroll.name} with {min_enroll.enrollees} student(s) enrolling."
)

max_admit_app_ratio = College("Max", 1, 0, 0)
min_admit_app_ratio = College("Min", 1, 1_000_000, 0)
max_enroll_admit_ratio = College("Max", 0, 1, 0)
min_enroll_admit_ratio = College("Min", 0, 1, 1_000_000)

for college in colleges:
    if college.admit_app_ratio() > max_admit_app_ratio.admit_app_ratio():
        max_admit_app_ratio = college
    elif college.admit_app_ratio() < min_admit_app_ratio.admit_app_ratio():
        min_admit_app_ratio = college
    if college.enroll_admit_ratio() > max_enroll_admit_ratio.enroll_admit_ratio():
        max_enroll_admit_ratio = college
    elif college.enroll_admit_ratio() < min_enroll_admit_ratio.enroll_admit_ratio():
        min_enroll_admit_ratio = college

print()
print(
    f"The college with the highest rate of admissions is {max_admit_app_ratio.name} with {max_admit_app_ratio.admit_app_ratio():.2%} of applicants being admitted."
)
print(
    f"The college with the lowest rate of admissions is {min_admit_app_ratio.name} with {min_admit_app_ratio.admit_app_ratio():.2%} of applicants being admitted."
)
