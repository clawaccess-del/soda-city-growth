#!/usr/bin/env python3
import base64
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path('/data/.openclaw/workspace/projects/soda-city-growth')
SECRETS = Path('/data/.openclaw/credentials/user-secrets.json')

obj = json.loads(SECRETS.read_text())
gh_token = obj.get('tokens', {}).get('github', {}).get('personalAccessToken')
vercel_token = obj.get('tokens', {}).get('vercel', {}).get('token')

if not gh_token:
    print('ERROR: missing GitHub token')
    sys.exit(2)
if not vercel_token:
    print('ERROR: missing Vercel token')
    sys.exit(3)

basic = base64.b64encode(f'x-access-token:{gh_token}'.encode()).decode()

def run(cmd, *, env=None, label=None):
    print(f'==> {label or cmd[0]}')
    proc = subprocess.run(cmd, cwd=ROOT, env=env, text=True, capture_output=True)
    if proc.stdout:
        print(proc.stdout.strip())
    if proc.returncode != 0:
        if proc.stderr:
            print(proc.stderr.strip())
        sys.exit(proc.returncode)
    if proc.stderr:
        print(proc.stderr.strip())

push_env = os.environ.copy()
push_env['GIT_TERMINAL_PROMPT'] = '0'
run([
    'git',
    '-c', f'http.https://github.com/.extraheader=AUTHORIZATION: basic {basic}',
    'push', 'origin', 'main'
], env=push_env, label='git push')

vercel_env = os.environ.copy()
vercel_env['VERCEL_TOKEN'] = vercel_token
run(['vercel', '--token', vercel_token, '--prod', '--yes'], env=vercel_env, label='vercel deploy')
