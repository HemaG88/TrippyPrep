from services.roadmap_loader import RoadmapLoader


print("=" * 50)
print("TrippyPrep Roadmap Test")
print("=" * 50)

roadmap = RoadmapLoader.load_aptitude()

print()

print("Academy :", roadmap["academy"])

print()

for level in roadmap["levels"]:

    print(level["title"])
    print(level["badge"])

    print("Topics:")

    for topic in level["topics"]:
        print("   •", topic)

    print()