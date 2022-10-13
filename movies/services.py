from urllib.parse import urlparse, parse_qs

class MovieService:
    @classmethod
    def get_video_id(cls, url):
        """
        Get video id from Youtube Link
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=SA2iWivDJiE&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        return: SA2iWivDJiE
        """
        if url:
            query = urlparse(url)
            if query.hostname == 'youtu.be':
                return query.path[1:]
            if query.hostname in ('www.youtube.com', 'youtube.com'):
                if query.path == '/watch':
                    p = parse_qs(query.query)
                    return p['v'][0]
                if query.path[:7] == '/embed/':
                    return query.path.split('/')[2]
                if query.path[:3] == '/v/':
                    return query.path.split('/')[2]
        return None

    @classmethod
    def generate_iframe_ytb(cls, url, **kwargs):
        """
        Genenrate iframe video to show in HTML from Youtube URL
        return:
        <iframe width="560" height="315" src="https://www.youtube.com/embed/GrnpwSa2QN4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """
        width = kwargs.get("width", 560)
        height = kwargs.get("height", 315)
        video_id = cls.get_video_id(url)
        if video_id:
            return f'<iframe width="{width}" height="{height}" src="https://www.youtube.com/embed/{video_id}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        return ""