#!/usr/bin/env python
#
# Copyright (c) 2012, Sony Mobile Communications AB
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in
#      the documentation and/or other materials provided with the
#      distribution.
#    * Neither the name of Sony Mobile Communications AB nor the names
#      of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written
#      permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
# OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
# AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#
# DESCRIPTION
#
#   mkbootimg wrapper to create the custom boot.img format used by LT26
#
# SYNOPSIS
#
#   usage: mkbootimg
#          --kernel <filename>
#          --ramdisk <filename>
#          -o|--output <filename>
#          --cmdline <kernel-commandline>
#          --board <boardname>
#
#   For compatibility the following mkbootimg arguments are gracefully ignored
#          [ --second <2ndbootloader-filename> ]
#          [ --base <address> ]
#          [ --pagesize <pagesize> ]
#

import os
import sys
from optparse import OptionParser
from string import Template

mkelf_template = Template('device/sony/huashan/boot/mkelf.py $boardname -o $output $kernel@0x80208000 $ramdisk@0x81900000,ramdisk $rpm@0x00020000,rpm $cmdline@cmdline')

def main(args):
    parser = OptionParser("usage: %prog options")
    parser.add_option("--kernel", dest="kernel", help="path to the kernel image")
    parser.add_option("--ramdisk", dest="ramdisk", help="path to the ramdisk image")
    parser.add_option("-o", "--output", dest="output", help="path to the output file")
    parser.add_option("-n", "--board", dest="boardname", help="optional board name", default="")
    parser.add_option("--second", dest="ignore_second", help="2ndbootloader-filename (mkbootimg compatibility)")
    parser.add_option("--cmdline", dest="cmdline", help="kernel-commandline")
    parser.add_option("--base", dest="ignore_base", help="base (mkbootimg compatibility)")
    parser.add_option("--pagesize", dest="ignore_pagesize", help="pagesize (mkbootimg compatibility)")
    parser.add_option("--rpm", dest="rpm", default="device/sony/huashan/boot/RPM.bin")
    parser.add_option("--os_version", dest="ignore_osver", help="OS version (mkbootimg compatibility)")
    parser.add_option("--os_patch_level", dest="ignore_ospatchlvl", help="OS patch level (mkbootimg compatibility)")
    parser.add_option("--ramdisk_offset", dest="ignore_ramdiskoffset", help="Ramdisk offset (mkbootimg compatibility; hardcoded)")

    (opts, args) = parser.parse_args()

    if(opts.boardname != ""):
        opts.boardname = "-n " + opts.boardname
        
    if(opts.cmdline != None):
        opts.cmdline = "\"" + opts.cmdline + "\""

    os.system(mkelf_template.substitute(vars(opts)))

if __name__ == "__main__":
    main(sys.argv[1:])
