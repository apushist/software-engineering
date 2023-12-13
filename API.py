from yandex_tracker_client import TrackerClient
client = TrackerClient(token='y0_AgAAAAANzoqJAAr8WwAAAAD0rFSyIbNbGJ2JRrO1jJOrlGtaXpzFyV8', cloud_org_id='bpfjlb4g80qjr6dl7a4e')
client.issues.create(queue='TEAMCITY', summary='Build is failed', type={'name': 'Bug'}, assignee='uliana.ivashkova')