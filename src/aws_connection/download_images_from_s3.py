import os
import boto3
from botocore.exceptions import NoCredentialsError

# Update these variables based on your preferences
aws_access_key_id = 'your_aws_access_key_id'
aws_secret_access_key = 'your_aws_secret_access_key'
bucket_name = 'your_bucket_name'
output_directory = 'data/raw'

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Initialize a boto3 S3 client with your AWS credentials
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def download_images(bucket, output_dir):
    try:
        # List objects in the specified S3 bucket
        objects = s3_client.list_objects(Bucket=bucket)

        # Check if there are any objects in the bucket
        if 'Contents' not in objects:
            print(f"No objects found in bucket {bucket}.")
            return

        # Iterate through the objects in the bucket and download the images
        for obj in objects['Contents']:
            # Download the object (image) from the bucket and save it to the output directory
            file_name = os.path.basename(obj['Key'])
            local_file_path = os.path.join(output_dir, file_name)
            s3_client.download_file(bucket, obj['Key'], local_file_path)
            print(f"Downloaded {file_name} from {bucket} to {local_file_path}")

    except NoCredentialsError:
        print("Unable to access S3. Please check your AWS credentials.")
        return

# Download the images from the specified S3 bucket
download_images(bucket_name, output_directory)

