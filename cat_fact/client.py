import posixpath


class CatClient(object):

    def __init__(self, session, host_url):
        self._session = session
        self._host_url = host_url

    def rooted_uri(self, *args):
        return posixpath.join(self._host_url, *args)

    def get_random_fact(self):
        api_end_point = self.rooted_uri("facts/random")
        response = self._session.get(api_end_point)
        if response.ok:
            return response.json()
        return []

