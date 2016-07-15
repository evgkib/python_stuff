import boto3
ids = ['i-51dc9ac9']
session = boto3.session.Session(region_name='us-east-1',
								profile_name = 'dataservicesdev')
ec2 = session.resource('ec2', use_ssl=False)
instances = ec2.instances.filter(InstanceIds=ids)

def scale_down():
	for instance in instances:
		print(instance.id,'is', instance.state['Name'])
		if  instance.state['Name'] == 'running':
			print('Modifying type to t2.medium')
			instance.stop()
			instance.wait_until_stopped()
			instance.modify_attribute(InstanceType={'Value':'t2.medium'})
			print('Stopped')
			instance.start()
			instance.wait_until_running()
			print('Running')
			

def scale_up():
	for instance in instances:
		print(instance.id,'is', instance.state['Name'])
		if  instance.state['Name'] == 'running':
			print('Modifying type to t2.large')
			instance.stop()
			instance.wait_until_stopped()
			instance.modify_attribute(InstanceType={'Value':'t2.large'})
			print('Stopped')
			instance.start()
			instance.wait_until_running()
			print('Running')

scale_up()
