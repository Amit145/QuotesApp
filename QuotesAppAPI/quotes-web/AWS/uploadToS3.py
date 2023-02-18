import boto3
from botocore.client import Config


class AWSOperations:
    session = None
    bucket = None
    source_file = None
    s3_file_key = None
    expiry = None

    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id='AKIATCVLRI3BQIXNK26B',
            aws_secret_access_key='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'
        )

        self.bucket = 'quotesapp-user-gen-images'
        self.expiry = 300

    def upload_file(self, file_url, file_key):
        s3 = self.session.resource('s3', config=Config(signature_version='v4'), region_name='ap-south-1')
        s3.Bucket(self.bucket).upload_file(file_url, file_key)
        return file_key

    def get_presigned_url_for_file(self, file_key):
        s3 = self.session.client('s3', config=Config(signature_version='v4'), region_name='ap-south-1')
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': self.bucket,
                                                     'Key': file_key},
                                             ExpiresIn=self.expiry)
        return {"url": response,
                "msg": f'Link accessible only for {self.expiry} seconds'
                }
