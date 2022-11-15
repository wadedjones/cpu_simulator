# Cache for the CPU

class Cache:
    def __init__(self):
        self._cache = {}
        self._cache_counter = 0
        self.first_in = None

    def write_cache(self, address, value):
        if self._cache_counter < 4:
            self._cache[address] = value
            self._cache_counter += 1
            if self.first_in is None:
                self.first_in = address
        else:
            del self._cache[self.first_in]
            self.first_in = list(self._cache.keys())[0]
            self._cache[address] = value

    def search_cache(self, address):
        if address in self._cache:
            return self._cache[address]
        else:
            return None

    def clear_cache(self):
        self._cache.clear()
        self._cache_counter = 0
        self.first_in = None

    def set_cache(self, target):
        # turn cache on (1) or off (0)
        return int(target)