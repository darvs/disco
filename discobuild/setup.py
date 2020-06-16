#!/usr/bin/env python3

import sys, yaml, re, os

project = os.environ['PROJECT']
puid = os.environ['PUID']
pgid = os.environ['PGID']

with open('/tmp/disco.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)

    repo = data['repo']['url']
    packages = data['packages']
    build = data['build']

    with open('/tmp/Dockerfile', 'w') as d:
        def writeln(s):
            d.write(s + '\n')

        def writebuild(s):
            if not writebuild.emptyBuild:
                writeln(' && \\')

            d.write('  echo ' + re.escape(s) + '>> /tmp/build')
            writebuild.emptyBuild = False
        
        writebuild.emptyBuild = True
            
        writeln('FROM disco')

        writeln(f'ENV PROJECT="{project}"')
        writeln(f'ENV REPO="{repo}"')
        writeln(f'ENV PUID={puid}')
        writeln(f'ENV PGID={pgid}')

        writeln('RUN \\')
        writeln(f'  DEBIAN_FRONTEND=noninteractive apt install -y {packages}')

        writeln('RUN \\')
        for s in build.split('\n'):
            writebuild(s)
        writeln('')

        writeln(f'ENTRYPOINT ["/usr/bin/sudo", "-E", "-u", "#{puid}", "-g", "#{pgid}", "/discobuild/bootstrap"]');
