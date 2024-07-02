from subprocess import run as srun
import logging
from os import path as ospath

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

UPSTREAM_REPO = 'https://github.com/Strelizia-007/index'
UPSTREAM_BRANCH = 'SH24BOTS'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update = srun([f"git init -q \
                     && git config --global user.email iamstrelizia07@gmail.com \
                     && git config --global user.name strelizia-007 \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

    if update.returncode == 0:
        logging.info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        logging.error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')