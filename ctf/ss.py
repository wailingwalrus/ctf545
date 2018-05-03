from swpag_client import Team

team = Team('http://52.52.219.26/', 'sEek7pgZDmYYwEbTzi4K1CwxrjCZ5H7p')

print team.get_targets(10003)
