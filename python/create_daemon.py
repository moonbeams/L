# -*- coding: utf-8 -*-


import os
import sys


def daemonize (stdin='/dev/null', stdout='/var/log/vmd_dbg', stderr='/var/log/vmd_dbg'):
    # Perform first fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %sn" % (e.errno, e.strerror))
        sys.exit(1)
    # Decouple from parent environment.
    os.chdir("/usr/vmd")
    os.umask(0)
    os.setsid( )
    # Perform second fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit second parent.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %sn" % (e.errno, e.strerror))
        sys.exit(1)

    # e.g for /sbin/cryptsetup
    # The process is now daemonized, redirect standard file descriptors.
    for f in sys.stdout, sys.stderr: f.flush( )
    si = file(stdin, 'r')
    #so = file(stdout, 'a+')
    #se = file(stderr, 'a+', 0)
    os.dup2(si.fileno( ), sys.stdin.fileno( ))
    #os.dup2(so.fileno( ), sys.stdout.fileno( ))
    #os.dup2(se.fileno( ), sys.stderr.fileno( ))
    sys.stdout=open(stdout, 'a', False)
    sys.stderr=open(stderr, 'a', False)

