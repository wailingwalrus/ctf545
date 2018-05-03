#!/bin/bash

cd /opt/ctf/backup-child/rw

if [[ "i386" == "i386" ]] || [[ "x86_64" == "i386" ]] ; then
  ../ro/backup-child 2>/dev/null
else
  qemu-i386 ../ro/backup-child 2>/dev/null
fi