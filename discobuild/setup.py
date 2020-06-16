#!/usr/bin/env python3

import sys, yaml, re

with open('/tmp/disco.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    project = sys.argv[1]
    repo = data['repo']['url']
    packages = data['packages']
    build = data['build']

    with open('/tmp/Dockerfile', 'w') as d:
        def writeln(s):
            d.write(s + '\n')

        def writebuild(s):
            writeln('  echo ' + re.escape(s) + '>> /tmp/build && \\')
            
        writeln('FROM disco')
        writeln('RUN \\')
        writeln(f'  DEBIAN_FRONTEND=noninteractive apt install -y {packages}')

        writeln('RUN \\')
        writeln('  [ ! -f /tmp/build ] || rm /tmp/build && \\')
        writeln('  touch /tmp/build && \\')

        writebuild('#!/usr/bin/env bash')
        writebuild('cd /projects')
        writebuild(f'[ -d {project} ] || git clone --recursive {repo}')
        writebuild(f'cd {project}')

        for s in build.split('\n'):
            writebuild(s)
        writeln(f'  chmod a+x /tmp/build');



