import cloudinary
import cloudinary.api
import cloudinary.uploader
from decouple import config

cloudinary.config(
    cloud_name=config('CLOUDINARY_CLOUD_NAME'),
    api_key=config('CLOUDINARY_API_KEY'),
    api_secret=config('CLOUDINARY_API_SECRET'),
)


class CloudinaryApi:
    UPLOAD_PATH = ''

    def upload_image(self, file, nome):
        filename = nome
        tags = []
        alt = nome
        request = cloudinary.uploader.upload(file=file,
                                             public_id=filename,
                                             height=300,
                                             width=300,
                                             quality="auto:eco",
                                             crop="limit",
                                             tags=tags,
                                             alt=alt)
        if not request:
            response = {}
            return response

        response = {'url': request['url']}
        return response

cloudyapi = CloudinaryApi()
