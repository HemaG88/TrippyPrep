from services.topic_loader import TopicLoader


class TopicService:

    @staticmethod
    def get_all_topics():

        return TopicLoader.load_topics()

    @staticmethod
    def get_topic(name):

        topics = TopicLoader.load_topics()

        for topic in topics:

            if topic["name"] == name:

                return topic

        return None

    @staticmethod
    def get_topics_by_folder(folder):

        topics = TopicLoader.load_topics()

        return [
            topic
            for topic in topics
            if topic["folder"] == folder
        ]