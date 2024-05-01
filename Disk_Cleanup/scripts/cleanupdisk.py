import os
import shutil
import click
from datetime import datetime, timedelta

def searchAndDeleteMatchedFolder(targetdir, daysAgo, dryrun):
    for root, dirs, files in os.walk(targetdir):
        if not len(dirs):
            filetime = datetime.fromtimestamp(os.path.getctime(root))
            if filetime < daysAgo:
                if dryrun:
                    print ("Dry Run -- Delete:", root)
                else:
                    print ("Delete:", root)
                    shutil.rmtree(root)

@click.command()
@click.option('--targetlist', '-t', required=True, multiple=True, help='Target folder where disk cleanup will start. Can specify multiple targets i.e. -t A -t B')
@click.option('--keepxdays', '-k', default=7, help='Default is 7.  Folders that are older than this X day will be deleted')
@click.option('--dryrun', '-d', is_flag=True, show_default=True, help='If -d is passed to the script, it would show folders that would get deleted without actual deletion')

def cleanupDisk(targetlist, keepxdays, dryrun):
    daysAgo = datetime.now() - timedelta(days=keepxdays)
    for targetdir in targetlist:
        searchAndDeleteMatchedFolder(targetdir, daysAgo, dryrun)

if __name__ == '__main__':
    cleanupDisk()