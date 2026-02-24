from factory_ex1 import (
    UploadService,
    EnterpriseFactory,
    StartupFactory,
    PrivateFactory,
    StreamingFactory
)


if __name__ == "__main__":

    # Enterprise
    print("\n=== Enterprise Tenant ===")
    enterprise_service = UploadService(EnterpriseFactory())
    enterprise_service.upload("enterprise_video.mp4")

    # Startup
    print("\n=== Startup Tenant ===")
    startup_service = UploadService(StartupFactory())
    startup_service.upload("startup_image.png")

    # Privacy
    print("\n=== Privacy Tenant ===")
    privacy_service = UploadService(PrivateFactory())
    privacy_service.upload("secure_document.mp4")

    # Streaming Pro
    print("\n=== Streaming Pro Tenant ===")
    streaming_service = UploadService(StreamingFactory())
    streaming_service.upload("streaming_movie.mkv")