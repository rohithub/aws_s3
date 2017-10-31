# owner: Rohit Kumar

#Install Boto package. sudo apt-get install python-boto
import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

bucket_name ='ember-s3'   #Name of the bucket
testfile = "Memory_Discussion.pdf"
key_file = 'prediction.json' # name of the file to be accessed on the S3
download_path = '/home/user/Downloads/ember/prediction.json' ## change this to your local machine path

# Connect to the S3 using the access keys set in /etc/boto.cfg. If not set, follow the these steps:
# 1) Go to Amazon AWS account-> Click the top right account name -> My security Credentials -> Continue (if pop up arrives) -> Access Keys -> Create New Access Keys -> Download the CSV file
# Note that you cannot retreive this file from your account again, so keep it saved someplace
# 2) Go to the directory where the file is downloaded. Open terminal froom here and type in
# cp <your key name> /etc/boto.cfg
# 3) Open /etc/boto.cfg in editor and ensure that it is in following format:
# 
# [Credentials]
# aws_access_key_id = {ACCESS KEY ID}
# aws_secret_access_key = {SECRET ACCESS KEY}
#
# If not, make changes to reflect in the above format

#conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
conn = boto.connect_s3()

#Count all the buckets
all_b = conn.get_all_buckets()
if all_b is None:
	print "No bucket exists "

## Following contains the method to create a new bucket in given location
#bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

##Create a key of given name and  transfer contents to that from local file
#k = Key(bucket)
#k.key = key_file
#k.set_contents_from_filename(testfile, cb=percent_cb, num_cb=10)
#k.set_acl('public-read')
#def percent_cb(complete, total):
#    sys.stdout.write('.')
#    sys.stdout.flush()

##Download the file from S3
conn_bucket = conn.get_bucket(bucket_name)
if conn_bucket is None:
	print "Bucket does not exist!"
else:
	for key_list in conn_bucket.list():
		print key_list.name

all_files = conn_bucket.list()   #list all keys inside the bucket

#key_file = [i.name for i in conn_bucket.list()]
#all_files.name.encode('utf-8')[1];

#down_key = conn_bucket.get_key(key_file)
#down_key.get_contents_to_filename(download_path) 

