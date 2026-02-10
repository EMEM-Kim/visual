from abc import ABC, abstractmethod


class storage(ABC):
    @abstractmethod
    def store(self, data):
        pass


class thumbnail(ABC):
    @abstractmethod
    def load(self, data):
        pass


class meta(ABC):
    @abstractmethod
    def meta(self, data):
        pass


class url(ABC):
    def generate(self, data):
        pass


class servicefactory(ABC):
    @abstractmethod
    def create_storage(self, data):
        pass

    def create_thumbnail(self, data):
        pass

    def create_meta(self, data):
        pass

    def create_url(self, data):
        pass
