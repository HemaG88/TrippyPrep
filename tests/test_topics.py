from services.topic_loader import TopicLoader

print("=" * 50)
print("TrippyPrep Topic Loader")
print("=" * 50)

topics = TopicLoader.load_topics()

for topic in topics:
    print()
    print(topic["topic"])
    print(topic["dataset"])
    print(topic["estimated_questions"])
    print(topic["estimated_learning_time"])