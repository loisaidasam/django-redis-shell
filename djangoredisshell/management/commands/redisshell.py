
from optparse import make_option
import subprocess
import urlparse

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ""
    help = "Get redis-cli command"

    option_list = BaseCommand.option_list + (
        make_option('-r', '--raw',
            action='store_true',
            dest='raw',
            default=False,
            help='Raw output'
        ),
    )

    def handle(self, *args, **options):
        parsed = urlparse.urlparse(settings.REDIS_URL)
        cmd = "redis-cli "
        if parsed.hostname:
            cmd += "-h %s " % parsed.hostname
        if parsed.port:
            cmd += "-p %s " % parsed.port
        if parsed.password:
            cmd += "-a %s " % parsed.password
        if options['raw']:
            cmd += "--raw "
        if args:
            # Helper for handling stuff like ./manage.py redisshell keys '*'
            if '*' in args:
                args = list(args)
                for i, arg in enumerate(args):
                    if arg == '*':
                        args[i] = "'*'"
            cmd += " ".join(args)
        subprocess.call(cmd, shell=True)
