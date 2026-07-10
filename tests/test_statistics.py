from services.statistics_service import StatisticsService

stats_service = StatisticsService()

json_file = "aptitude/01_foundation/number_system.json"

stats = stats_service.get_topic_statistics(json_file)

print("=" * 60)
print("        TrippyPrep Statistics Engine Test")
print("=" * 60)

print(f"Total Questions : {stats['total']}")
print(f"Easy Questions  : {stats['easy']}")
print(f"Medium Questions: {stats['medium']}")
print(f"Hard Questions  : {stats['hard']}")