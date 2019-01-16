import posixpath


class CatClient(object):

    def __init__(self, session, host_url):
        self._session = session
        self._host_url = host_url
        self.animals = ["cat", "horse", "dog"]

    def animal_exists(self, animal):
        return animal in self.animals

    def rooted_uri(self, *args):
        return posixpath.join(self._host_url, *args)

    def get_random_fact(self, animal):
        if not self.animal_exists(animal):
            return None
        api_end_point = self.rooted_uri(
            "facts/random",
            "?animal_type={}".format(animal)
        )
        response = self._session.get(api_end_point)
        if response.ok:
            return response.json()
        return []

