from services.topic_service import TopicService


class SearchService:

    @classmethod
    def search_topics(cls, keyword):

        keyword = keyword.lower()

        topics = TopicService.get_all_topics()

        results = []

        for topic in topics:

            if keyword in topic["name"].lower():

                results.append(topic)

        return results