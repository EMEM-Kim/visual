from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass


class Thumbnail(ABC):
    @abstractmethod
    def create_thumbnail(self, data):
        pass


class Meta(ABC):
    @abstractmethod
    def extract(self, data):
        pass


class Url(ABC):
    @abstractmethod
    def build(self, data):
        pass


#########################################################################################################################


class S3(Storage):
    def save(self, data):
        print("save")


class LambdaImageProcessor(Thumbnail):
    def create_thumbnail(self, data):
        print("create_thumbnail")


class MediaConvert(Meta):
    def extract(self, data):
        print("extract")


class CloudFront(Url):
    def build(self, data):
        print("build CloudFront ")


########################################################################################################################


class LocalStorage(Storage):
    def save(self, data):
        print("save local")


class Pillow(Thumbnail):
    def create_thumbnail(self, data):
        print("create_thumbnail")


class FFmpeg(Meta):
    def extract(self, data):
        print("extract")


class StaticURL(Url):
    def build(self, data):
        print("build static ")


##############################################################


class PrivateStorage(Storage):
    def save(self, data):
        print("save private")


class InternalThumbnail(Thumbnail):
    def create_thumbnail(self, data):
        print("create Internal thumbnail")


class InternalMeta(Meta):
    def extract(self, data):
        print("extract InternalMeta")


class TokenUrl(Url):
    def build(self, data):
        print("build TokenUrl")


###############################################


class StreamingStorage(Storage):
    def save(self, data):
        print("save StreamingStorage")


class StreamingThumbnail(Thumbnail):
    def create_thumbnail(self, data):
        print("create Streaming thumbnail")


class StreamingMeta(Meta):
    def extract(self, data):
        print("extract StreamingMeta")


class StreamingURL(Url):
    def build(self, data):
        print("build StreamingURL")


####################################################


class MediaFactory(ABC):

    @abstractmethod
    def create_storage(self) -> Storage:
        pass

    @abstractmethod
    def create_thumbnail(self) -> Thumbnail:
        pass

    @abstractmethod
    def create_metadata(self) -> Meta:
        pass

    @abstractmethod
    def create_url_builder(self) -> Url:
        pass


#################################################


class EnterpriseFactory(MediaFactory):
    def create_storage(self):
        return S3()

    def create_thumbnail(self):
        return LambdaImageProcessor()

    def create_metadata(self):
        return MediaConvert()

    def create_url_builder(self):
        return CloudFront()


class StartupFactory(MediaFactory):
    def create_storage(self):
        return LocalStorage()

    def create_thumbnail(self):
        return Pillow()

    def create_metadata(self):
        return FFmpeg()

    def create_url_builder(self):
        return StaticURL()


class PrivateFactory(MediaFactory):
    def create_storage(self):
        return PrivateStorage()

    def create_thumbnail(self):
        return InternalThumbnail()

    def create_metadata(self):
        return InternalMeta()

    def create_url_builder(self):
        return TokenUrl()


class StreamingFactory(MediaFactory):
    def create_storage(self):
        return StreamingStorage()

    def create_thumbnail(self):
        return StreamingThumbnail()

    def create_metadata(self):
        return StreamingMeta()

    def create_url_builder(self):
        return StreamingURL()


###############################################


class UploadService:

    def __init__(self, factory: MediaFactory):
        self.storage = factory.create_storage()
        self.thumbnail = factory.create_thumbnail()
        self.metadata = factory.create_metadata()
        self.url_builder = factory.create_url_builder()

    def upload(self, file):
        print("\n=== Upload Start ===")
        self.storage.save(file)
        self.thumbnail.create_thumbnail(file)
        self.metadata.extract(file)
        self.url_builder.build(file)
        print("=== Upload Complete ===\n")