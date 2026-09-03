import requests

class MovieAPI:

    def get_rating(self, movie_title):
        raise NotImplementedError


class RecommendationEngine:

    def __init__(self, api):
        self.api = api

    def recommend(self, movie_title):

        (rating,) = self.api.get_rating(movie_title)

        if rating >= 8:
            return "Highly Recommended"

        if rating <= 6:
            return "Recommended"

        return "Not Recommended"

    

