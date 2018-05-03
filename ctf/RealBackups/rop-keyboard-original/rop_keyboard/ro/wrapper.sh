#!/bin/bash

cd /opt/ctf/rop_keyboard/rw

if [[ "i386" == "i386" ]] || [[ "x86_64" == "i386" ]] ; then
  ../ro/rop_keyboard 2>/dev/null
else
  qemu-i386 ../ro/rop_keyboard 2>/dev/null
fi