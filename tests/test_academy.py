from services.academy_service import AcademyService

print("Academies:")
print(AcademyService.get_academies())

print("\nTopics:")
print(AcademyService.get_aptitude_topics())