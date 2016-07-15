import boto3
session = boto3.session.Session(region_name='us-east-1', profile_name = 'dataservicesdev')
ec2 = session.resource('ec2', use_ssl=False)

def ls():
    for i in ec2.instances.all():
        if i.tags is None:
            continue
        for t in i.tags:
            if t['Key'] == 'Name':
                print (i.id, t['Value'], i.instance_type, i.state['Name']
                )

filters = [{
	'tag:Owner': 'ekibalko'
}]

ls()