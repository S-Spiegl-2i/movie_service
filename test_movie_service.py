# . Use mocker.patch() to mock MovieAPI.get_rating
# Simulate each of the following ratings:
# Rating	Expected Result
# 8.5	Highly Recommended
# 7.0	Recommended
# 4.5	Not Recommended
# Assert that the correct recommendation string is returned in each of your mocked tests

from movie_service import RecommendationEngine
from movie_service import MovieAPI

def test_recommend(mocker):

        real_api = MovieAPI()
        fake_api_response = {"rating" == 8}

        mock_recommend = mocker.patch("movie_service.MovieAPI.get_rating", return_value=fake_api_response)
        recommendation = RecommendationEngine(api = real_api)
        result = recommendation.recommend("Die Hard")

        assert result == "Recommended"
        mock_recommend.assert_called_once_with("Die Hard")

