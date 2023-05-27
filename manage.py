#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import discord


from dotenv import load_dotenv
project_folder = os.path.expanduser('~/web_project')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('GUILD')


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)

