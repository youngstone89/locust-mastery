from json import JSONDecodeError
import time
import logging
from locust import HttpUser, task, between, User


class MinioEventsUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def minio_events(self):
        with self.client.post("/", json={
            "EventName": "s3:ObjectCreated:Put",
            "Key": "audio-logs/2e545bf3866f490fcbd80eb1ec33658a4ad84950c54c2be889b221dfb8f9cac3/asraas/6476766f-66ea-4255-ab0a-fd4d64aa5d96",
            "Records": [
                {
                    "eventVersion": "2.0",
                    "eventSource": "minio:s3",
                    "awsRegion": "",
                    "eventTime": "2021-08-25T07:37:43.884Z",
                    "eventName": "s3:ObjectCreated:Put",
                    "userIdentity": {
                        "principalId": "minio"
                    },
                    "requestParameters": {
                        "principalId": "minio",
                        "region": "",
                        "sourceIPAddress": "10.244.1.163"
                    },
                    "responseElements": {
                        "content-length": "0",
                        "x-amz-request-id": "169E7C8DD9F129CF",
                        "x-minio-deployment-id": "ad5a2d95-f871-4c6e-ad82-55a6b8546fbe",
                        "x-minio-origin-endpoint": "http://10.244.0.30:9000"
                    },
                    "s3": {
                        "s3SchemaVersion": "1.0",
                        "configurationId": "Config",
                        "bucket": {
                            "name": "audio-logs",
                            "ownerIdentity": {
                                "principalId": "minio"
                            },
                            "arn": "arn:aws:s3:::audio-logs"
                        },
                        "object": {
                            "key": "2e545bf3866f490fcbd80eb1ec33658a4ad84950c54c2be889b221dfb8f9cac3%2Fasraas%2F6476766f-66ea-4255-ab0a-fd4d64aa5d96",
                            "size": 74240,
                            "eTag": "5cd7c2b598f554235035e7180f63deb4",
                            "contentType": "binary/octet-stream",
                            "userMetadata": {
                                "content-type": "binary/octet-stream"
                            },
                            "sequencer": "169E7C8DDC6838BB"
                        }
                    },
                    "source": {
                        "host": "10.244.1.163",
                        "port": "",
                        "userAgent": "MinIO (linux; x64) minio-js/7.0.18"
                    }
                }
            ]
        }, catch_response=True) as response:
            try:
                logging.info(response.json())
            except JSONDecodeError:
                response.failure("Response could not be decoded as JSON")
            except KeyError:
                response.failure(
                    "Response did not contain expected key 'greeting'")
