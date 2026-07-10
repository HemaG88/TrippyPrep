class NavigationService:

    current_page = "🏠 Home"

    @classmethod
    def set_page(cls, page):
        cls.current_page = page

    @classmethod
    def get_page(cls):
        return cls.current_page