from turtle import width
from django.test import TestCase

from movies.services import MovieService

class MovieServiceTestCase(TestCase):
    """
    Test function generate_iframe_ytb (Unit Test)
    """
    def test_generate_iframe_ytb_success(self):
        """
        Input:
            url: http://youtu.be/SA2iWivDJiE

            width: 500
            height: 300
        Output:
            '<iframe width="500" height="300" src="https://www.youtube.com/embed/SA2iWivDJiE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        """
        url = "http://youtu.be/SA2iWivDJiE"
        expected_iframe = '<iframe width="500" height="300" src="https://www.youtube.com/embed/SA2iWivDJiE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        self.assertEqual(MovieService.generate_iframe_ytb(url, width=500, height=300), expected_iframe)
        
        url = "http://www.youtube.com/watch?v=SA2iWivDJiE&feature=feedu"
        self.assertEqual(MovieService.generate_iframe_ytb(url, width=500, height=300), expected_iframe)

        url = "http://www.youtube.com/embed/SA2iWivDJiE"
        self.assertEqual(MovieService.generate_iframe_ytb(url, width=500, height=300), expected_iframe)

        url = "http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US"
        self.assertEqual(MovieService.generate_iframe_ytb(url, width=500, height=300), expected_iframe)

    def test_generate_iframe_ytb_with_wrong_url(self):
        url = "http://youtube.com"
        expected_iframe = ""
        self.assertEqual(MovieService.generate_iframe_ytb(url), expected_iframe)