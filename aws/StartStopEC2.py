import boto3
ids = ['i-51dc9ac9','i-b3b5a336']
session = boto3.session.Session(region_name='us-east-1', profile_name = 'dataservicesdev')
ec2 = session.resource('ec2', use_ssl=False)
instances = ec2.instances.filter(InstanceIds=ids)

def stop_instances():
	instances.stop()
	

def start_instances():
	instances.start()
	
	
start_instances()
