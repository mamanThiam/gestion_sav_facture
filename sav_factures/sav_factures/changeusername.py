from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Change the username of a user'

    def add_arguments(self, parser):
        parser.add_argument('old_username', type=str, help='The current username of the user')
        parser.add_argument('new_username', type=str, help='The new username for the user')

    def handle(self, *args, **kwargs):
        old_username = kwargs['old_username']
        new_username = kwargs['new_username']

        try:
            user = User.objects.get(username=old_username)
            user.username = new_username
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Username changed from {old_username} to {new_username}'))
        except User.DoesNotExist:
            self.stderr.write(self.style.ERROR(f'User with username {old_username} does not exist.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {str(e)}'))
