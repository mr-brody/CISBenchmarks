#!/usr/bin/python

import os, sys, time, re
import argparse
import subprocess

#Scored - Success/Failure to comply will incerease/decrease the final benchmark score
#Not Scored - Failure to comply will not decrease the final benchmark score. Compliance will not increase the score.
#Level 1 Server - general requirement
#Level 1 Workstation - general requirement
#Level 2 Server - required where security is paramount. Extends Level 1 profile
#Level 2 Workstation - required where security is paramount. Extends Level 1 profile

total_compliances = 0
compliant_count = 0

def update_compliance_status(compliance_check, compliance_status):
    global total_compliances
    total_compliances +=1
    CRED    = '\33[31m'
    CGREEN  = '\33[32m'
    CEND    = '\33[0m'

    if args.nocolor:
        print compliance_check + ": " + compliance_status
    else:
        if "NON-" in compliance_status:
            print compliance_check + ": " + CRED + compliance_status + CEND
        else:
            print compliance_check + ": " + CGREEN + compliance_status + CEND
    return

def exec_command(cmd):
    global total_compliances
    global compliant_count
    try:
        out = subprocess.check_output(cmd,stderr=subprocess.STDOUT,shell=True)
    except:
        out = "EXCEPTION. Command execution failed or no output"
    return out

def verbose_logs(info_str, op):
    if args.verbose:
        print info_str +": "+ op
    return

def filesystem_config():
    global compliant_count

    compliance_check = "Ensure mounting of cramfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v cramfs"
    is_cramfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep cramfs"
    is_cramfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_cramfs_mp_present)
    verbose_logs("Command Output", is_cramfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install cramfs /bin/true\"")
    if "cramfs.ko" in is_cramfs_mp_present:
        if "EXCEPTION" in is_cramfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of freevxfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v freevxfs"
    is_freevxfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep freevxfs"
    is_freevxfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_freevxfs_mp_present)
    verbose_logs("Command Output", is_freevxfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install freevxfs /bin/true\"")
    if "freevxfs.ko" in is_freevxfs_mp_present:
        if "EXCEPTION" in is_freevxfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of jffs2 filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v jffs2"
    is_jffs2_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep jffs2"
    is_jffs2_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_jffs2_mp_present)
    verbose_logs("Command Output", is_jffs2_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install jffs2 /bin/true\"")
    if "jffs2.ko" in is_jffs2_mp_present:
        if "EXCEPTION" in is_jffs2_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of hfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v hfs"
    is_hfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep hfs"
    is_hfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_hfs_mp_present)
    verbose_logs("Command Output", is_hfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install hfs /bin/true\"")
    if "hfs.ko" in is_hfs_mp_present:
        if "EXCEPTION" in is_hfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of hfsplus filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v hfsplus"
    is_hfsplus_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep freevxfs"
    is_hfsplus_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_hfsplus_mp_present)
    verbose_logs("Command Output", is_hfsplus_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install hfsplus /bin/true\"")
    if "hfsplus.ko" in is_hfsplus_mp_present:
        if "EXCEPTION" in is_hfsplus_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of squashfs filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v squashfs"
    is_squashfs_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep squashfs"
    is_squashfs_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_squashfs_mp_present)
    verbose_logs("Command Output", is_squashfs_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install squashfs /bin/true\"")
    if "squashfs.ko" in is_squashfs_mp_present:
        if "EXCEPTION" in is_squashfs_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of udf filesystems is disabled (Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v udf"
    is_udf_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep udf"
    is_udf_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_udf_mp_present)
    verbose_logs("Command Output", is_udf_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install udf /bin/true\"")
    if "udf.ko" in is_udf_mp_present:
        if "EXCEPTION" in is_udf_lm_present:
            update_compliance_status(compliance_check, "COMPLIANT")
            compliant_count += 1
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
            compliant_count -= 1
    else:
        update_compliance_status(compliance_check, "COMPLIANT")
        compliant_count += 1

    compliance_check = "Ensure mounting of FAT filesystems is disabled (Scored, Level 1 Server Level 2 Workstation)"
    cmd1 = "modprobe -n -v vfat"
    is_vfat_mp_present = exec_command(cmd1)
    cmd2 = "lsmod | grep vfat"
    is_vfat_lm_present = exec_command(cmd2)
    verbose_logs("Command used", cmd1 + cmd2)
    verbose_logs("Command Output", is_vfat_mp_present)
    verbose_logs("Command Output", is_vfat_lm_present)
    verbose_logs("Expected output to be compliant","No output from above commands")
    verbose_logs("To be compliant, run","Edit/Create /etc/modprobe.d/CIS.conf and add line \"install vfat /bin/true\"")
    if "vfat.ko" in is_vfat_mp_present:
        if "EXCEPTION" in is_vfat_lm_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Ensure separate partition exists for /tmp (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /tmp"
    is_tmpfs_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    tmpfs_present = 0
    verbose_logs("Expected output to be compliant","similar to \"tmpfs on /tmp type tmpfs (rw,nosuid,nodev,noexec,relatime)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /tmp. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/tmp " in is_tmpfs_partition_present:
        tmpfs_present = 1
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /tmp partition (Scored)(Not Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nodev mount option specifies that the filesystem cannot contain special devices")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","verify that the nodev option is set on /tmp")
    verbose_logs("To be compliant, run","mount -o remount,nodev /tmp")
    if tmpfs_present:
        if "nodev" in is_tmpfs_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nosuid option set on /tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nosuid mount option specifies that the filesystem cannot contain setuid files")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the nosuid option is set on /tmp")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /tmp")
    if tmpfs_present:
        if "nosuid" in is_tmpfs_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure noexec option set on /tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "noexec mount option specifies that the filesystem cannot contain executable binaries")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the noexec option is set on /tmp")
    verbose_logs("To be compliant, run","mount -o remount,noexec /tmp")
    if tmpfs_present:
        if "noexec" in is_tmpfs_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var"
    is_var_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_var_partition_present)
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdg1 on /var type ext4 (rw,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var " in is_var_partition_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var/tmp (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var/tmp"
    is_vartmp_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_vartmp_partition_present)
    vartmp_present = 0
    verbose_logs("Expected output to be compliant","similar to \"tmpfs on /var/tmp type ext4 (rw,nosuid,nodev,noexec,relatime)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var/tmp. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var/tmp " in is_vartmp_partition_present:
        vartmp_present = 1
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /var/tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nodev mount option specifies that the filesystem cannot contain special devices")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","verify that the nodev option is set on /var/tmp")
    verbose_logs("To be compliant, run","mount -o remount,nodev /var/tmp")
    if vartmp_present:
        if "nodev" in is_vartmp_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nosuid option set on /var/tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nosuid mount option specifies that the filesystem cannot contain setuid files")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_vartmp_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the nosuid option is set on /var/tmp")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /var/tmp")
    if vartmp_present:
        if "nosuid" in is_vartmp_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure noexec option set on /var/tmp partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("INFO", "nosuid mount option specifies that the filesystem cannot contain setuid files")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tmpfs_partition_present)
    verbose_logs("Expected output to be compliant","Verify that the nosuid option is set on /var/tmp")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /var/tmp")
    if vartmp_present:
        if "nosuid" in is_vartmp_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var/log (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var/log"
    is_varlog_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_varlog_partition_present)
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdh1 on /var/log type ext4 (rw,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var/log. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var/log " in is_varlog_partition_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /var/log/audit (Scored)(Not Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /var/log/audit"
    is_varlogaudit_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_varlogaudit_partition_present)
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdi1 on /var/log/audit type ext4 (rw,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /var/log/audit. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/var/log/audit " in is_varlogaudit_partition_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure separate partition exists for /home (Scored, Level 2 Server and Workstation)"
    cmd = "mount | grep /home"
    is_home_partition_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_home_partition_present)
    home_present = 0
    verbose_logs("Expected output to be compliant","similar to \"/dev/xvdf1 on /home type ext4 (rw,nodev,relatime,data=ordered)\"")
    verbose_logs("To be compliant","For new systems create separate partition for /home. For previously installed systems, create a new partition and configure /etc/fstab as appropriate.")
    if "/home " in is_home_partition_present:
        home_present = 1
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /home partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_home_partition_present)
    verbose_logs("Expected output to be compliant","nodev option set on /home. Set this option to ensure users cannot attempt to create block or character special devices")
    verbose_logs("To be compliant, run","mount -o remount,nodev /home")
    if home_present:
        if "nodev" in is_home_partition_present:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on /dev/shm partition (Scored, Level 1 Server and Workstation)"
    cmd = "mount | grep /dev/shm"
    is_devshm_partition_present = exec_command(cmd)
    verbose_logs("INFO","/dev/shm filesystem is not intended to support devices, prevent users creating special devices")
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_devshm_partition_present)
    devshm_present = 0
    verbose_logs("Expected output to be compliant","nodev option set on /home. Set this option to ensure users cannot attempt to create block or character special devices")
    verbose_logs("To be compliant, run","mount -o remount,nodev /dev/shm")
    if "/dev/shm " in is_devshm_partition_present:
        devshm_present = 1

    if devshm_present:
        if ("nodev" in is_devshm_partition_present):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nosuid option set on /dev/shm partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_devshm_partition_present)
    verbose_logs("Expected output to be compliant","nosuid option set on /home. Set this option to ensure filesystem cannot contain setuid files, not-setting this option allows non-root users to execute privileged programs")
    verbose_logs("To be compliant, run","mount -o remount,nosuid /dev/shm")
    if devshm_present:
        if ("nosuid" in is_devshm_partition_present):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure noexec option set on /dev/shm partition (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_devshm_partition_present)
    verbose_logs("Expected output to be compliant","noexec option is set on /dev/shm")
    verbose_logs("To be compliant, run","mount -o remount,noexec /dev/shm")
    if devshm_present:
        if ("noexec" in is_devshm_partition_present):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure nodev option set on removable media partitions (Scored, Level 1 Server and Workstation)"
    cmd = "mount |grep -i /dev"
    is_removablemedia_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_removablemedia_present)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure nosuid option set on removable media partitions (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_removablemedia_present)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure noexec option set on removable media partitions (Scored, Level 1 Server and Workstation)"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_removablemedia_present)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    #TODO Removable media ^^. blkid cmd might be useful

    compliance_check = "Ensure sticky bit is set on all world-writable directories (Scored, Level 1 Server and Workstation)"
    cmd = "df -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \\( -perm -0002 -a ! -perm -1000 \\)"
    is_sb_wwf = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sb_wwf)
    verbose_logs("Expected output to be compliant","No output should be returned")
    verbose_logs("To be compliant, run","df -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d -perm -0002 2>/dev/null | chmod a+t")
    if "EXCEPTION" in is_sb_wwf or len(is_sb_wwf) <1:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Disable Automounting (Scored)(Not Scored, Level 1 Server and Workstation)"
    #command similar to "chkconfig --list autofs" on alpine
    cmd = "rc-status -a | grep -i autofs"
    proc_status_rlevels = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", proc_status_rlevels)
    verbose_logs("Expected output to be compliant","autofs is not available")
    verbose_logs("To be compliant, run","rc-service autofs stop")
    if "EXCEPTION" in proc_status_rlevels or len(proc_status_rlevels) <1:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def config_swUpdates():
    global compliant_count

    compliance_check = "Ensure package manager repositories are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "apk policy"
    is_apk_policy_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_apk_policy_present)
    verbose_logs("Expected output to be compliant","Verify package repositories are configured correctly")
    verbose_logs("To be compliant","Configure your package manager repositories according to site policy.")
    if "EXCEPTION" in is_apk_policy_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
        

    compliance_check = "Ensure GPG keys are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "TODO: DID NOT FIND SPECIFIC COMMAND"
    #repo_gpgkeys_config = exec_command(cmd)
    verbose_logs("Command used", cmd)
    #verbose_logs("Command Output", repo_gpgkeys_config)
    verbose_logs("Expected output to be compliant","Verify GPG keys are configured correctly for your package manager")
    verbose_logs("To be compliant, run","")
    """
    if "EXCEPTION" in is_apk_policy_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    """

def fs_integrity_checking():
    global compliant_count

    compliance_check = "Ensure AIDE is installed (Scored, Level 1 Server and Workstation)"
    #AIDE not present on Alpine release 3.6.2. inotifyd is inbuild FIM
    cmd = "ps | grep -i inotifyd"
    is_inotifyd_running = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_inotifyd_running)
    verbose_logs("Expected output to be compliant","inotifyd or similar FIM tools must be running")
    verbose_logs("To be compliant, run","inotifyd on sensitive files")
    inotifyd_proc = is_inotifyd_running.split('\n')
    if len(inotifyd_proc) >=2:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure filesystem integrity is regularly checked (Scored, Level 1 Server and Workstation)"
    cmd = "crontab -u root -l | grep inotifyd"
    is_fim_cron_present = exec_command(cmd)
    #also run, "grep -r aide /etc/cron.* /etc/crontab"
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_fim_cron_present)
    verbose_logs("Expected output to be compliant","inotifyd or similar FIM tools configured as cron job")
    verbose_logs("To be compliant, run","\"crontab -u root -e\" and add \"0 5 * * * /usr/sbin/aide --check\" to crontab")
    if "inotifyd" in is_fim_cron_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def sec_boot_settings():
    global compliant_count
    compliance_check = "Ensure permissions on bootloader config are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /boot/grub/menu.lst"
    bootloader_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bootloader_perm)
    # Access: (0600/-rw-------) Uid: ( 0/ root) Gid: ( 0/ root)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","\"chown root:root /boot/grub/menu.lst\",\"chmod og-rwx /boot/grub/menu.lst\"")
    check_stat_match = re.match(r'.*?Access:\s*\(\d{4}....------\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)',bootloader_perm, re.I|re.M|re.S)
    if check_stat_match:
        print "check_stat_match.groups():", check_stat_match.groups()
        print "check_stat_match.group(1):", check_stat_match.group(1)
        print "check_stat_match.groups(2):", check_stat_match.group(2)
    #TODO

    compliance_check = "Ensure bootloader password is set (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^password\" /boot/grub/menu.lst"
    bootloader_password = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", bootloader_password)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","generate <encrypted-password> for grub/grub2 using command grub-md5-crypt/grub-mkpasswd-pbkdf2, paste it into the global section of /boot/grub/menu.lst as \"password --md5 <encrypted-password>\" and \"set superusers=\"<username>\"\" and \"password_pbkdf2 <username> <encrypted-password>\" for grub2 then run update-grub command")
    if "password" in bootloader_password:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure authentication required for single user mode (Not Scored, Level 1 Server and Workstation)"
    cmd = "grep \"/sbin/sulogin\" /etc/inittab"
    auth_sum = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", auth_sum)
    verbose_logs("Expected output to be compliant","similar to \"~~:S:respawn:/sbin/sulogin\"")
    verbose_logs("To be compliant, run","configure single user mode to require a password for login as appropriate")
    if ":S:respawn:/sbin/sulogin" in auth_sum:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure interactive boot is not enabled (Not Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^PROMPT_FOR_CONFIRM=\" /etc/sysconfig/boot"
    is_iboot_enabled = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_iboot_enabled)
    verbose_logs("Expected output to be compliant","PROMPT_FOR_CONFIRM=\"no\"")
    verbose_logs("To be compliant, check","if interactive boot is available disable it.")
    iboot_no = re.match(r'^PROMPT_FOR_CONFIRM="(.*?)".*?',is_iboot_enabled, re.I|re.M)
    if iboot_no:
        if "no" in iboot_no.group(1):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def process_hardening():
    global compliant_count

    compliance_check = "Ensure core dumps are restricted (Scored, Level 1 Server and Workstation)"
    cmd1 = "grep -r \"hard core\" /etc/security/limits.conf /etc/security/limits.d/"
    #cmd1 = "grep \"hard core\" /etc/security/limits.conf"
    is_limits_set = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    verbose_logs("Command Output", is_limits_set)
    verbose_logs("Expected output to be compliant","* hard core 0")
    verbose_logs("To be compliant, run","Edit /etc/security/limits.conf file or a /etc/security/limits.d/* file by adding \"* hard core 0\"")
    hard_core_0 = re.match(r'.*?\*\s+hard\s+core\s+0.*?',is_limits_set,re.I|re.M)

    cmd2 = "sysctl fs.suid_dumpable"
    sysctl_suiddump = exec_command(cmd2)
    verbose_logs("Command used", cmd2)
    verbose_logs("Command Output", sysctl_suiddump)
    verbose_logs("Expected output to be compliant","fs.suid_dumpable = 0")
    verbose_logs("To be compliant, run","Set \"fs.suid_dumpable = 0\" in /etc/sysctl.conf. Run \"sysctl -w fs.suid-dumpable=1\"to set the active kernel parameter")
    is_suid_dumpable = re.match(r'fs\.suid_dumpable\s*=\s*0',sysctl_suiddump,re.I|re.M)
    if hard_core_0 and is_suid_dumpable:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure XD/NX support is enabled (Not Scored, Level 1 Server and Workstation)"
    cmd = "dmesg | grep NX"
    is_NX_active = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_NX_active)
    verbose_logs("Expected output to be compliant","NX (Execute Disable) protection: active")
    verbose_logs("To be compliant, run","enable NX or XD support in your bios")
    if ("NX " in is_NX_active) and (" active" in is_NX_active):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure address space layout randomization (ASLR) is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl kernel.randomize_va_space"
    is_aslr_set = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_aslr_set)
    verbose_logs("Expected output to be compliant","kernel.randomize_va_space = 2")
    verbose_logs("To be compliant, run","\"sysctl -w kernel.randomize_va_space=2\" or edit /etc/sysctl.conf and add kernel.randomize_va_space = 2")
    if ("kernel.randomize_va_space" in is_aslr_set) and (" 2" in is_aslr_set):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure prelink is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "apk info prelink"
    is_prelink_disabled = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_prelink_disabled)
    verbose_logs("Expected output to be compliant","Verify prelink is not installed")
    verbose_logs("To be compliant, run","apk del prelink")
    if "prelink-" in is_prelink_disabled:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

def mandatory_access_control():
    global compliant_count

    compliance_check = "Ensure SELinux is not disabled in bootloader configuration (Scored, Level 2 Server and Workstation)"
    #check /boot/grub/menu.lst, /boot/grub/grub.cfg
    #bootloader information, file -s /dev/sda
    #SELinux may be disabled by changing 'selinux=1' to 'selinux=0'
    #'enforcing=0' (which means permissive where denied actions are logged but still executed i.e. selinux policy is not enforced, but denials are logged)
    #enforcing=1, selinux policy is enforced and denials are logged
    cmd = "grep -iE \"^\s*(kernel|linux)\" /boot/grub/menu.lst |grep -iE \"selinux|enforcing\""
    is_selinux_grub = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_grub)
    cmd = "grep -iE \"selinux|enforcing\" /boot/extlinux.conf"
    is_selinux_syslinux = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_syslinux)
    verbose_logs("Expected output to be compliant","verify that no kernel line has the selinux=0 or enforcing=0 parameters set")
    verbose_logs("To be compliant, run","Edit /boot/grub/menu.lst (grub), /etc/default/grub (grub2) and remove all instances of selinux=0 and enforcing=0 from all CMDLINE_LINUX parameters")
    if "selinux=1" in is_selinux_grub or "selinux=1" in is_selinux_syslinux:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure the SELinux state is enforcing (Scored, Level 2 Server and Workstation)"
    cmd = "grep SELINUX=enforcing /etc/selinux/config"
    #can also be verified using sestatus command
    is_selinux_enforced = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_enforced)
    verbose_logs("Expected output to be compliant","SELINUX=enforcing")
    verbose_logs("To be compliant, run","Edit /etc/selinux/config by adding SELINUX=enforcing")
    if "SELINUX=enforcing" in is_selinux_enforced:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SELinux policy is configured (Scored, Level 2 Server and Workstation)"
    cmd = "grep SELINUXTYPE=targeted /etc/selinux/config"
    is_selinux_policy = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_policy)
    verbose_logs("Expected output to be compliant","SELINUXTYPE=targeted or SELINUXTYPE=mls")
    verbose_logs("To be compliant, run","Edit /etc/selinux/config by adding SELINUXTYPE=targeted")
    if "SELINUXTYPE=targeted" in is_selinux_policy or "SELINUXTYPE=mls" in is_selinux_policy:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SETroubleshoot is not installed (Scored, Level 2 Server)"
    cmd = "apk info setroubleshoot"
    is_setroubleshoot = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_setroubleshoot)
    verbose_logs("Expected output to be compliant","Verify s etroubleshoot is not installed")
    verbose_logs("To be compliant, run","Uninstall setroubleshoot using, apk del setroubleshoot")
    if "setroubleshoot" in is_setroubleshoot:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Ensure the MCS Translation Service (mcstrans) is not installed (Scored, Level 2 Server and Workstation)"
    cmd = "apk info mcstrans"
    is_mcstrans = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_mcstrans)
    verbose_logs("Expected output to be compliant","Verify mcstrans is not installed")
    verbose_logs("To be compliant, run","apk del mcstrans")
    if "mcstrans" in is_mcstrans:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Ensure no unconfined daemons exist (Scored, Level 2 Server and Workstation)"
    cmd = "ps -eZ | egrep \"initrc\" | egrep -vw \"tr|ps|egrep|bash|awk\" | tr ':' ' ' |awk '{ print $NF }'"
    no_uncofined_daemons = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", no_uncofined_daemons)
    verbose_logs("Expected output to be compliant","verify not output is produced for executed command")
    verbose_logs("To be compliant, run","Investigate any unconfined daemons found during the audit action")
    if "EXCEPTION" in no_uncofined_daemons:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    #bootloader: check /boot/grub/menu.lst (grub), /boot/grub/grub.cfg, /boot/extlinux.conf, /etc/default/grub (grub2)
    compliance_check = "Ensure AppArmor is not disabled in bootloader configuration (Scored, Level 2 Server and Workstation)"
    grub_file = ""
    if os.path.isfile("/boot/grub/menu.lst"):
        grub_file = "/boot/grub/menu.lst"
    elif os.path.isfile("/boot/grub/grub.cfg"):
        grub_file = "/boot/grub/grub.cfg"
    if len(grub_file) > 4:
        cmd = "grep -iE \"^\s*(kernel|linux)\"" + grub_file 
        is_apparmor = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_apparmor)
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","Edit /boot/grub/menu.lst and remove apparmor=0 on all kernel/linux lines. Or change apparmor=0 to apparmor=1")
        if "apparmor=0" in is_apparmor:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure all AppArmor Profiles are enforcing (Scored, Level 2 Server and Workstation)"
    cmd = "apparmor_status"
    apparmor_status = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", apparmor_status)
    verbose_logs("Expected output to be compliant","Verify that profiles are loaded, no profiles are in complain mode, and no processes are unconfined")
    verbose_logs("To be compliant, run","enforce /etc/apparmor.d/*")

    compliance_check = "Ensure SELinux or AppArmor are installed (Not Scored, Level 2 Server and Workstation)"
    cmd = "apk info selinux && apk info apparmor"
    is_selinux_apparmor_installed = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_selinux_apparmor_installed)
    verbose_logs("Expected output to be compliant","Verify either SELinux or AppArmor is installed")
    verbose_logs("To be compliant, run","apk add selinux && apk add apparmor")
    if "selinux" in is_selinux_apparmor_installed or "apparmor" in is_selinux_apparmor_installed:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def warning_banners():
    global compliant_count

    compliance_check = "Ensure message of the day is configured properly (Scored, Level 1 Server and Workstation)"
    cmd = "cat /etc/motd"
    #\m - machine architecture (uname -a); \r - operating system release (uname -r); \s - operating system name; \v - operating system version (uname -v)
    #above options will work when there is mingetty(8) support
    #cmd = "egrep '(\\v|\\r|\\m|\\s)' /etc/motd"
    is_motd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_motd)
    verbose_logs("Expected output to be compliant","verify that the contents match Corporate policy")
    verbose_logs("To be compliant, run","Edit /etc/motd file with the appropriate contents as per Corporate policy, remove instances of \m, \r, \s, or \v")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")

    compliance_check = "Ensure local login warning banner is configured properly (Not Scored, Level 1 Server and Workstation)"
    cmd = "cat /etc/issue"
    is_loginbanner_present = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_loginbanner_present)
    verbose_logs("Expected output to be compliant","Verify that the contents match Corporate policy. Remove OS, Kernel, Release, Architecture related information.")
    verbose_logs("To be compliant, add","Authorized uses only. All activity may be monitored and reported instead of OS, Kernel, Release, Architecture related information.")
    if "Welcome to Alpine Linux" in is_loginbanner_present:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    
    compliance_check = "Ensure remote login warning banner is configured properly (Not Scored, Level 1 Server and Workstation)"
    cmd = "cat /etc/issue.net"
    is_rlogin_banner = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rlogin_banner)
    verbose_logs("Expected output to be compliant","Verify that the contents match Corporate policy. Remove OS, Kernel, Release, Architecture related information.")
    verbose_logs("To be compliant, add","Authorized uses only. All activity may be monitored and reported instead of OS, Kernel, Release, Architecture related information.")
    if "Welcome to Alpine Linux" in is_rlogin_banner:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    

    compliance_check = "Ensure permissions on /etc/motd are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/motd"
    motd_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", motd_permissions)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
    verbose_logs("To be compliant, run","chown root:root /etc/motd; chmod 644 /etc/motd")
    #Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
    stat_motd = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',motd_permissions, re.I|re.M|re.S)
    if stat_motd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/issue are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/issue"
    issue_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", issue_permissions)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
    verbose_logs("To be compliant, run","chown root:root /etc/issue; chmod 644 /etc/issue")
    stat_issue = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',issue_permissions, re.I|re.M|re.S)
    if stat_issue:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/issue.net are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/issue.net"
    issuenet_permissions = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", issuenet_permissions)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
    verbose_logs("To be compliant, run","chown root:root /etc/issue.net; chmod 644 /etc/issue.net")
    stat_issuenet = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',issue_permissions, re.I|re.M|re.S)
    if stat_issuenet:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure GDM login banner is configured (Scored, Level 1 Server and Workstation)"
    #/root/xorg.conf.new; /etc/X11/xorg.conf; /etc/dconf/profile/gdm
    cmd = "grep -riE \"banner-message-enable=true|banner-message-text=\" /root/xorg.conf.new /etc/X11/xorg.conf /etc/dconf/profile/gdm"
    is_gdm_login = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_gdm_login)
    verbose_logs("Expected output to be compliant","Verify the banner-message-enable and banner-message-text options are configured")
    verbose_logs("To be compliant, run","Configure login banners as needed")
    if "banner-message-enable=true" in is_gdm_login or "banner-message-text" in is_gdm_login:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure updates, patches, and additional security software are installed (Not Scored, Level 1 Server and Workstation)"
    cmd1 = "apk update"
    n = exec_command(cmd1)
    cmd = "apk version"
    apk_version = exec_command(cmd)
    verbose_logs("Command used", cmd1 + cmd)
    verbose_logs("Command Output", apk_version)
    verbose_logs("Expected output to be compliant","Verify there are no updates or patches to install")
    verbose_logs("To be compliant, run","apk add --upgrade <package_name>")
    available_updates = apk_version.split('\n')
    #print "len(available_updates):", len(available_updates), "available_updates:", available_updates
    if len(available_updates) > 2:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def inetd_services():
    global compliant_count

    compliance_check = "Ensure chargen services are not enabled (Scored, Level 1 Server and Workstation)"
    #rc-status -a |grep -i chargen
    #/c-service chargen status
    #rc-service -l |grep chargen
    cmd = "rc-status -a |grep -i chargen; rc-service -l |grep -i chargen"
    is_chargen = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_chargen)
    verbose_logs("Expected output to be compliant","Verify the chargen service is not enabled. Verify chargen-dgram and chargen-stream are off or missing")
    verbose_logs("To be compliant, run","rc-service chargen stop; apk del chargen")
    if "chargen" not in is_chargen:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure daytime services are not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i daytime; rc-service -l |grep -i daytime"
    is_daytime = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_daytime)
    verbose_logs("Expected output to be compliant","Verify the daytime service is not enabled. Verify daytime-dgram and daytime-stream are off or missing")
    verbose_logs("To be compliant, run","rc-service chargen stop; apk del daytime")
    if "daytime" not in is_daytime:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure discard services are not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i discard; rc-service -l |grep -i discard"
    is_discard = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_discard)
    verbose_logs("Expected output to be compliant","Verify the discard service is not enabled. Verify discard-dgram and discard-stream are off or missing")
    verbose_logs("To be compliant, run","rc-service discard stop and apk del discard")
    if "discard" not in is_discard:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure echo services are not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i echo; rc-service -l |grep -i echo"
    is_echo = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_echo)
    verbose_logs("Expected output to be compliant","Verify the echo service is not enabled. Verify echo-dgram and echo-stream are off or missing")
    verbose_logs("To be compliant, run","rc-service echo stop; apk del echo")
    if "echo" not in is_echo:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure time services are not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i time; rc-service -l |grep -i time"
    is_time = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_time)
    verbose_logs("Expected output to be compliant","Verify the time service is not enabled. Verify time-dgram and time-stream are off or missing")
    verbose_logs("To be compliant, run","rc-service time stop; apk del time")
    if "time" not in is_time:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure tftp server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i tftp; rc-service -l |grep -i tftp"
    is_tftpd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tftpd)
    verbose_logs("Expected output to be compliant","Verify tftp is off or missing")
    verbose_logs("To be compliant, run","rc-service tftp stop; apk del tftp")
    if "tftp" not in is_tftpd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure xinetd is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i xinetd; rc-service -l |grep xinetd"
    #find / -name xinetd
    is_xinetd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_xinetd)
    verbose_logs("Expected output to be compliant","Verify the xinetd service is not enabled. Verify xinetd are off or missing")
    verbose_logs("To be compliant, run","rc-service xinetd stop; apk del xinetd")
    if "xinetd" not in is_xinetd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def special_purpose_services():
    global compliant_count

    compliance_check = "Ensure time synchronization is in use (Not Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i ntp; rc-service -l |grep -i ntp; rc-status -a |grep -i chrony; rc-service -l |grep -i chrony"
    is_ntpd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ntpd)
    verbose_logs("Expected output to be compliant","Verify either ntp or chrony is installed")
    verbose_logs("To be compliant, run","apk add openntpd or apk add chrony")
    if "ntpd" in is_ntpd or "chrony" in is_ntpd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure ntp is configured (Scored, Level 1 Server and Workstation)"
    verbose_logs("Expected output to be compliant","similar to \"restrict -4 default kod nomodify notrap nopeer noquery\" and \"server <remote-server>\"")
    verbose_logs("To be compliant (for openntpd)","Edit /etc/ntp.conf by adding restrict and server options and \"-u ntpd:ntpd\" option in command_args of /etc/init.d/ntpd")
    verbose_logs("To be compliant (for chronyd)","Edit /etc/chrony/chrony.conf by adding restrict and server options and \"-u ntpd:ntpd\" option in command_args of /etc/init.d/chronyd")
    if os.path.isfile("/etc/ntp.conf"):
        cmdo1 = "grep \"^restrict\" /etc/ntp.conf"
        is_ontpd_restrict = exec_command(cmdo1)
        cmdo2 = "grep \"^server\" /etc/ntp.conf"
        is_ontpd_server = exec_command(cmdo2)
        verbose_logs("Command's used", cmdo1+cmdo2)
        verbose_logs("Command Output", is_ontpd_restrict + is_ontpd_server)
        is_ontpd_ntpd = exec_command("grep -i \"u ntpd:ntpd\" /etc/init.d/ntpd")
        if "restrict" in is_ontpd_restrict and "server" in is_ontpd_server and "ntpd:ntpd" in is_ontpd_ntpd:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else: 
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure chrony is configured (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/chrony/chrony.conf"):
        cmdc1 = "grep \"^restrict\" /etc/chrony/chrony.conf"
        is_cntpd_restrict = exec_command(cmdc1)
        cmdc2 = "grep \"^server\" /etc/chrony/chrony.conf"
        is_cntpd_server = exec_command(cmdc2)
        verbose_logs("Command's used", cmdc1+cmdc2)
        verbose_logs("Command Output", is_cntpd_restrict + is_cntpd_server)
        is_cntpd_ntpd = exec_command("grep -i \"u ntpd:ntpd\" /etc/init.d/chronyd")
        if "restrict" in is_cntpd_restrict and "server" in is_cntpd_server and "ntpd:ntpd" in is_cntpd_ntpd:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else: 
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure X Window System is not installed (Scored, Level 1 Server)"
    cmd = "apk info |grep -i xorg"
    is_xorg = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_xorg)
    verbose_logs("Expected output to be compliant","verify no output is returned")
    verbose_logs("To be compliant, run","apk del xorg")
    if "xorg" not in is_xorg:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure Avahi Server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i avahi |grep -iv grep"
    is_avahi = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_avahi)
    verbose_logs("Expected output to be compliant","Verify avahi is not running")
    verbose_logs("To be compliant, run","apk del avahi")
    if "avahi" not in is_avahi:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure CUPS is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i cups |grep -iv grep"
    is_cups = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_cups)
    verbose_logs("Expected output to be compliant","Verify CUPS is not running")
    verbose_logs("To be compliant, run","apk del cups")
    if "cups" not in is_cups.lower():
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure DHCP Server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i dhcpd |grep -iv grep"
    is_dhcpd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_dhcpd)
    verbose_logs("Expected output to be compliant","Verify DHCP Server is not running (udhcpd)")
    verbose_logs("To be compliant, run","apk del dhcp")
    if "dhcpd" not in is_dhcpd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure LDAP server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -iE \"ldap|slapd\" |grep -iv grep"
    is_ldap = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ldap)
    verbose_logs("Expected output to be compliant","Verify LDAP Server is not running")
    verbose_logs("To be compliant, run","apk del openldap")
    if "ldap" not in is_ldap and "slapd" not in is_ldap:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure NFS and RPC are not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -iE \"nfs|rpc\" |grep -iv grep"
    is_nfs_rpc = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_nfs_rpc)
    verbose_logs("Expected output to be compliant","Verify NFS and RPC Servers is not running")
    verbose_logs("To be compliant, run","apk del unfs3; apk del rpcbind")
    if "unfs" not in is_nfs_rpc and "rpcbind" not in is_nfs_rpc:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure DNS Server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i dns |grep -iv grep"
    is_dns = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_dns)
    verbose_logs("Expected output to be compliant","Verify DNS Server is not running")
    verbose_logs("To be compliant, run","apk del bind/udns/djbdns")
    if "dns" not in is_dns:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    

    compliance_check = "Ensure FTP Server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i ftp |grep -iv grep"
    is_ftpd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ftpd)
    verbose_logs("Expected output to be compliant","Verify FTP Server is not running")
    verbose_logs("To be compliant, run","")
    if "ftp" not in is_ftpd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure HTTP server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -iE \"http|nginx\" |grep -iv grep"
    is_http = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_http)
    verbose_logs("Expected output to be compliant","Verify HTTP Server is not running")
    verbose_logs("To be compliant, run","")
    if "http" not in is_http and "nginx" not in is_http:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure IMAP and POP3 server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i dovecot |grep -iv grep"
    is_dovecot = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_dovecot)
    verbose_logs("Expected output to be compliant","Verify IMAP and POP3 Server is not running")
    verbose_logs("To be compliant, run","apk del devecot")
    if "dovecot" not in is_dovecot:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    

    compliance_check = "Ensure Samba is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i samba |grep -iv grep"
    is_samba = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_samba)
    verbose_logs("Expected output to be compliant","Verify sanba Server is not running")
    verbose_logs("To be compliant, run","")
    if "samba" not in is_samba:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure HTTP Proxy Server is not enabled (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i squid |grep -iv grep"
    is_squid = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_squid)
    verbose_logs("Expected output to be compliant","Verify squid is not running")
    verbose_logs("To be compliant, run","apk del squid")
    if "xorg" not in is_xorg:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure SNMP Server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i snmp |grep -iv grep"
    is_snmp = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_snmp)
    verbose_logs("Expected output to be compliant","Verify SNMP is not running")
    verbose_logs("To be compliant, run","apk del net-snmp")
    if "snmp" not in is_snmp:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure mail transfer agent is configured for local-only mode (Scored, Level 1 Server and Workstation)"
    cmd = "netstat -an | grep LIST | grep \":25 \""
    is_mta = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_mta)
    verbose_logs("Expected output to be compliant","Verify MTA(say, postfix) is not running")
    verbose_logs("To be compliant, run","apk del postfix. Edit /etc/postfix/main.cf and add \"inet_interfaces = localhost\" to RECEIVING MAIL section")
    if "127.0.0." not in is_mta:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure NIS Server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i ypserv |grep -iv grep"
    is_nis = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_nis)
    verbose_logs("Expected output to be compliant","Verify NIS Server (say, ypserv) in not running")
    verbose_logs("To be compliant, run","apk del ypserv")
    if "ypserv" not in is_nis:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure rsh services are not enabled (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -iE \"rsh|rlogin|rexec\" |grep -iv grep"
    is_rsh = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rsh)
    verbose_logs("Expected output to be compliant","Verify rsh, rlogin and rexec are not running")
    verbose_logs("To be compliant, run","apk del rsh/rlogin/rexec")
    if "rsh" not in is_rsh and "rlogin" not in is_rsh and "rexec" not in is_rsh:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure telnet server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i telnet |grep -iv grep; netstat -ant | grep \":23\""
    is_telnet = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_telnet)
    verbose_logs("Expected output to be compliant","Verify telnet is not running")
    verbose_logs("To be compliant, run","apk del telnet")
    if "telnet" not in is_telnet and ":23" not in is_telnet:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure tftp server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i tftp |grep -iv grep; netstat -anu | grep \":69\""
    is_tftpd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tftpd)
    verbose_logs("Expected output to be compliant","Verify tftp Server is not running")
    verbose_logs("To be compliant, run","apk del tftpd")
    if "tftp" not in is_tftpd and ":69" not in is_tftpd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure rsync service is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i rsync |grep -iv grep"
    is_rsync = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rsync)
    verbose_logs("Expected output to be compliant","Verify rsync is not running")
    verbose_logs("To be compliant, run","apk del rsync")
    if "rsync" not in is_rsync:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure talk server is not enabled (Scored, Level 1 Server and Workstation)"
    cmd = "ps |grep -i talk |grep -iv grep"
    is_talk = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_talk)
    verbose_logs("Expected output to be compliant","Verify talk is not running")
    verbose_logs("To be compliant, run","apk del talk")
    if "talk" not in is_talk:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def service_clients():
    global compliant_count

    compliance_check = "Ensure NIS Client is not installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep ypbind"
    is_ypbind = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ypbind)
    verbose_logs("Expected output to be compliant","Verify ypbind (NIS Client) is not installed")
    verbose_logs("To be compliant, run","apk del ypbind")
    if "ypbind" not in is_ypbind:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    
    compliance_check = "Ensure rsh client is not installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep rsh"
    is_rshc = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rshc)
    verbose_logs("Expected output to be compliant","Verify rsh is not installed")
    verbose_logs("To be compliant, run","apk del rsh")
    if "rsh" not in is_rshc:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure talk client is not installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep talk"
    is_talkc = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_talkc)
    verbose_logs("Expected output to be compliant","Verify talk is not installed")
    verbose_logs("To be compliant, run","apk del talk")
    if "talk" not in is_talkc:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure telnet client is not installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep telnet"
    is_telnetc = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_telnetc)
    verbose_logs("Expected output to be compliant","Verify telnet is not installed")
    verbose_logs("To be compliant, run","apk del telnet")
    if "telnet" not in is_telnetc:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure LDAP client is not installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep openldap-clients"
    is_ldapcli = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ldapcli)
    verbose_logs("Expected output to be compliant","Verify openldap-clients not installed")
    verbose_logs("To be compliant, run","apk del openldap-clients")
    if "openldap" not in is_ldapcli:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def networkParam_hostRouter():
    global compliant_count

    #/etc/sysctl.d/00-alpine.conf
    compliance_check = "Ensure IP forwarding is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.ip_forward"
    is_ipforward = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_ipforward)
    verbose_logs("Expected output to be compliant","net.ipv4.ip_forward = 0")
    verbose_logs("To be compliant, run","Edit /etc/sysctl.conf or /etc/sysctl.d/00-alpine.conf and add net.ipv4.ip_forward = 0")
    if "= 0" in is_ipforward:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure packet redirect sending is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.conf.all.send_redirects"
    is_send_redirects = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_send_redirects)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.all.send_redirects = 0")
    cmd = "sysctl net.ipv4.conf.default.send_redirects"
    is_def_send_redirects = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_send_redirects)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.default.send_redirects = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.all.send_redirects=0; sysctl -w net.ipv4.conf.default.send_redirects=0")
    if "= 0" in is_send_redirects and "= 0" in is_def_send_redirects:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure source routed packets are not accepted (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.conf.all.accept_source_route"
    is_all_accept_source_route = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_accept_source_route)
    cmd = "sysctl net.ipv4.conf.default.accept_source_route"
    is_def_accept_source_route = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_accept_source_route)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.all.accept_source_route = 0 and net.ipv4.conf.default.accept_source_route = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.all.accept_source_route=0; sysctl -w net.ipv4.conf.default.accept_source_route=0")
    if "= 0" in is_all_accept_source_route and "= 0" in is_def_accept_source_route:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure ICMP redirects are not accepted (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.conf.all.accept_redirects"
    is_all_accept_redirects = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_accept_redirects)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.all.accept_redirects = 0")
    cmd = "sysctl net.ipv4.conf.default.accept_redirects"
    is_def_accept_redirects = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_accept_redirects)
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.all.accept_redirects=0; sysctl -w net.ipv4.conf.default.accept_redirects=0")
    if "= 0" in is_all_accept_redirects and "= 0" in is_def_accept_redirects:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure secure ICMP redirects are not accepted (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.conf.all.secure_redirects"
    is_all_secure_redirects = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_secure_redirects)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.all.secure_redirects = 0")
    cmd = "sysctl net.ipv4.conf.default.secure_redirects"
    is_def_secure_redirects = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_secure_redirects)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.default.secure_redirects = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.all.secure_redirects=0; sysctl -w net.ipv4.conf.default.secure_redirects=0")
    if "= 0" in is_all_secure_redirects and "= 0" in is_def_secure_redirects:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure suspicious packets are logged (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.conf.all.log_martians"
    is_all_log_martians = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_log_martians)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.all.log_martians = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.all.log_martians=1")
    cmd = "sysctl net.ipv4.conf.default.log_martians"
    is_def_log_martians = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_log_martians)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.default.log_martians = 1")
    if "= 1" in is_all_log_martians and "= 1" in is_def_log_martians:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure broadcast ICMP requests are ignored (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.icmp_echo_ignore_broadcasts"
    is_icmp_echo_ignore_broadcasts = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_icmp_echo_ignore_broadcasts)
    verbose_logs("Expected output to be compliant","net.ipv4.icmp_echo_ignore_broadcasts = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1")
    if "= 1" in is_icmp_echo_ignore_broadcasts:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure bogus ICMP responses are ignored (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.icmp_ignore_bogus_error_responses"
    is_icmp_ignore_bogus_error_responses = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_icmp_ignore_bogus_error_responses)
    verbose_logs("Expected output to be compliant","net.ipv4.icmp_ignore_bogus_error_responses = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=1")
    if "= 1" in is_icmp_ignore_bogus_error_responses:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure Reverse Path Filtering is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.conf.all.rp_filter"
    is_all_rp_filter = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_rp_filter)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.all.rp_filter = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.all.rp_filter=1")
    cmd = "sysctl net.ipv4.conf.default.rp_filter"
    is_def_rp_filter = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_rp_filter)
    verbose_logs("Expected output to be compliant","net.ipv4.conf.default.rp_filter = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.conf.default.rp_filter=1")
    if "= 1" in is_all_rp_filter and "= 1" in is_def_rp_filter:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure TCP SYN Cookies is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv4.tcp_syncookies"
    is_tcp_syncookies = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tcp_syncookies)
    verbose_logs("Expected output to be compliant","net.ipv4.tcp_syncookies = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv4.tcp_syncookies=1")
    if "= 1" in is_tcp_syncookies:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def ipv6():
    global compliant_count

    compliance_check = "Ensure IPv6 router advertisements are not accepted (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv6.conf.all.accept_ra"
    is_all_accept_ra = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_accept_ra)
    verbose_logs("Expected output to be compliant","net.ipv6.conf.all.accept_ra = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv6.conf.all.accept_ra=0")
    cmd = "sysctl net.ipv6.conf.default.accept_ra"
    is_def_accept_ra = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_accept_ra)
    verbose_logs("Expected output to be compliant","net.ipv6.conf.default.accept_ra = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv6.conf.default.accept_ra=0")
    if "= 0" in is_all_accept_ra and "= 0" in is_def_accept_ra:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure IPv6 redirects are not accepted (Scored, Level 1 Server and Workstation)"
    cmd = "sysctl net.ipv6.conf.all.accept_redirects"
    is_all_accept_redirects6 = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_all_accept_redirects6)
    verbose_logs("Expected output to be compliant","net.ipv6.conf.all.accept_redirect = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv6.conf.all.accept_redirects=0")
    cmd = "sysctl net.ipv6.conf.default.accept_redirects"
    is_def_accept_redirects6 = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_def_accept_redirects6)
    verbose_logs("Expected output to be compliant","net.ipv6.conf.default.accept_redirect = 0")
    verbose_logs("To be compliant, run","sysctl -w net.ipv6.conf.default.accept_redirects=0")
    if "= 0" in is_all_accept_redirects6 and "= 0" in is_def_accept_redirects6:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure IPv6 is disabled (Scored, Level 1 Server and Workstation)"
    #cmd = "modprobe -c | grep ipv6"
    cmd = "sysctl net.ipv6.conf.all.disable_ipv6"
    is_disable_ipv6 = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_disable_ipv6)
    verbose_logs("Expected output to be compliant","net.ipv6.conf.all.disable_ipv6 = 1")
    verbose_logs("To be compliant, run","sysctl -w net.ipv6.conf.all.disable_ipv6 = 1")
    if "= 1" in is_disable_ipv6:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def tcp_wrappers():
    global compliant_count

    compliance_check = "Ensure TCP Wrappers is installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep -iE \"tcp(_|-)wrappers\""
    is_tcp_wrappers = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_tcp_wrappers)
    verbose_logs("Expected output to be compliant","Verify tcp_wrappers is installed")
    verbose_logs("To be compliant, run","")
    if "tcp_wrappers" in is_tcp_wrappers or "tcp-wrappers" in is_tcp_wrappers:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure /etc/hosts.allow is configured (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/hosts.allow"):
        cmd = "cat /etc/hosts.allow"
        hostsallow = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", hostsallow)
        verbose_logs("Expected output to be compliant","Authorised IP Addresses are configured in the file")
        verbose_logs("To be compliant, run","Edit /etc/hosts.allow by adding IP's and network blocks which need access to this system")
        if len(hostsallow) >=12:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure /etc/hosts.deny is configured (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/hosts.deny"):
        cmd = "cat /etc/hosts.deny"
        hostsdeny = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", hostsdeny)
        verbose_logs("Expected output to be compliant","Unauthorised IP Addresses are configured in the file")
        verbose_logs("To be compliant, run","Edit /etc/hosts.deny by adding IP's and network blocks which are blocked from accessing the system")
        if "ALL:" in hostsdeny:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/hosts.allow are configured (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/hosts.allow"):
        cmd = "stat /etc/hosts.allow"
        is_hostsallow = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
        verbose_logs("To be compliant, run","chmod 644 /etc/hosts.allow")
        stat_hostsallow = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',is_hostsallow, re.I|re.M|re.S)
        if stat_hostsallow:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/hosts.deny are 644 (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/hosts.deny"):
        cmd = "stat /etc/hosts.deny"
        is_hostsdeny = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access is 644")
        verbose_logs("To be compliant, run","chmod 644 /etc/hosts.deny")
        stat_hostsdeny = re.match(r'((.*?Access:\s*\(.644/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\)))',is_hostsdeny, re.I|re.M|re.S)
        if stat_hostsdeny:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def uncommon_nwProtocols():
    global compliant_count
    compliance_check = "Ensure DCCP is disabled (Not Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v dccp"
    is_dccp_modprobe = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    cmd2 = "lsmod | grep dccp"
    is_dccp_lsmod = exec_command(cmd2)
    verbose_logs("Command used", cmd2)
    verbose_logs("Command Output", is_dccp_modprobe + is_dccp_lsmod)
    verbose_logs("Expected output to be compliant","No output from lsmod command")
    verbose_logs("To be compliant, run","Edit or create the file /etc/modprobe.d/CIS.conf and add \"install dccp /bin/true\"")
    if "dccp" not in is_dccp_lsmod:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SCTP is disabled (Not Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v sctp"
    is_sctp_modprobe = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    cmd2 = "lsmod | grep sctp"
    is_sctp_lsmod = exec_command(cmd2)
    verbose_logs("Command used", cmd2)
    verbose_logs("Command Output", is_sctp_modprobe + is_sctp_lsmod)
    verbose_logs("Expected output to be compliant","No output from lsmod command")
    verbose_logs("To be compliant, run","Edit or create the file /etc/modprobe.d/CIS.conf and add \"install sctp /bin/true\"")
    if "sctp" not in is_sctp_lsmod:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure RDS is disabled (Not Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v rds"
    is_rds_modprobe = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    cmd2 = "lsmod | grep rds"
    is_rds_lsmod = exec_command(cmd2)
    verbose_logs("Command used", cmd2)
    verbose_logs("Command Output", is_rds_modprobe + is_rds_lsmod)
    verbose_logs("Expected output to be compliant","No output from lsmod command")
    verbose_logs("To be compliant, run","Edit or create the file /etc/modprobe.d/CIS.conf and add \"install rds /bin/true\"")
    if "rds" not in is_rds_lsmod:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure TIPC is disabled (Not Scored, Level 1 Server and Workstation)"
    cmd1 = "modprobe -n -v tipc"
    is_tipc_modprobe = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    cmd2 = "lsmod | grep tipc"
    is_tipc_lsmod = exec_command(cmd2)
    verbose_logs("Command used", cmd2)
    verbose_logs("Command Output", is_tipc_modprobe + is_tipc_lsmod)
    verbose_logs("Expected output to be compliant","No output from lsmod command")
    verbose_logs("To be compliant, run","Edit or create the file /etc/modprobe.d/CIS.conf and add \"install tipc /bin/true\"")
    if "tipc" not in is_tipc_lsmod:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def firewall_configuration():
    global compliant_count

    compliance_check = "Ensure iptables is installed (Scored, Level 1 Server and Workstation)"
    cmd = "apk info |grep -i iptables"
    is_iptables = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_iptables)
    verbose_logs("Expected output to be compliant","Verify iptables is installed")
    verbose_logs("To be compliant, run","apk add iptables")
    if "iptables" in is_iptables:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure default deny firewall policy (Scored, Level 1 Server and Workstation)"
    cmd = "iptables -L"
    all_iptables_acls = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", all_iptables_acls)
    verbose_logs("Expected output to be compliant","Verify that the policy for the INPUT, OUTPUT, and FORWARD chains is DROP or REJECT")
    verbose_logs("To be compliant, run","iptables -P INPUT DROP; iptables -P OUTPUT DROP; iptables -P FORWARD DROP")
    is_in_defdrop = re.match(r'.*?Chain INPUT (policy DROP).*?',all_iptables_acls,re.I|re.M|re.S)
    is_out_defdrop = re.match(r'.*?Chain\s+OUTPUT\s+\(policy\s+DROP\).*?',all_iptables_acls,re.I|re.M|re.S)
    is_for_defdrop = re.match(r'.*?Chain\s+FORWARD\s+\(policy\s+DROP\).*?',all_iptables_acls,re.I|re.M|re.S)
    if is_in_defdrop and is_out_defdrop and is_for_defdrop:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure loopback traffic is configured (Scored, Level 1 Server and Workstation)"
    cmd = "iptables -L INPUT -v -n"
    is_iptables_lo = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_iptables_lo)
    verbose_logs("Expected output to be compliant","loopback interface is the only place that loopback network (127.0.0.0/8) traffic should be seen, all other interfaces should ignore traffic on this network as an anti-spoofing measure")
    verbose_logs("To be compliant, run","iptables -A INPUT -i lo -j ACCEPT; iptables -A OUTPUT -o lo -j ACCEPT; iptables -A INPUT -s 127.0.0.0/8 -j DROP")
    if "127.0.0.0/8" in is_iptables_lo:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure outbound and established connections are configured (Not Scored, Level 1 Server and Workstation)"
    cmd = "iptables -L -v -n"
    is_iptables_out_in = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_iptables_out_in)
    verbose_logs("Expected output to be compliant","verify all rules for new outbound, and established connections match Corporate policy")
    verbose_logs("To be compliant, run","")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")
    verbose_logs("Example ACL Config", "iptables -A OUTPUT -p tcp -m state --state NEW,ESTABLISHED -j ACCEPT")
    verbose_logs("Example ACL Config", "iptables -A OUTPUT -p udp -m state --state NEW,ESTABLISHED -j ACCEPT")
    verbose_logs("Example ACL Config", "iptables -A OUTPUT -p icmp -m state --state NEW,ESTABLISHED -j ACCEPT")
    verbose_logs("Example ACL Config", "iptables -A INPUT -p tcp -m state --state ESTABLISHED -j ACCEPT")
    verbose_logs("Example ACL Config", "iptables -A INPUT -p udp -m state --state ESTABLISHED -j ACCEPT")
    verbose_logs("Example ACL Config", "iptables -A INPUT -p icmp -m state --state ESTABLISHED -j ACCEPT")

    compliance_check = "Ensure firewall rules exist for all open ports (Scored, Level 1 Server and Workstation)"
    cmd1 = "netstat -ln | grep -v 127\.0\.0\."
    netstat_op = exec_command(cmd1)
    verbose_logs("Command used", cmd1)
    verbose_logs("Command Output", netstat_op)
    cmd = "iptables -L INPUT -v -n"
    iptables_openports = exec_command(cmd)
    verbose_logs("Expected output to be compliant","Verify all open ports listening on non-localhost addresses have at least one firewall rule")
    verbose_logs("To be compliant, run","iptables -A INPUT -p <protocol> --dport <port> -m state --state NEW -j ACCEPT")
    open_ports = netstat_op.split('\n')
    acls_present = 0
    for each_port_line in open_ports:
        extract_port = re.match(r'(^\w+)\s+\d+\s+\d+.*?:(\d+).*?LISTEN', each_port_line, re.I|re.M|re.S)
        if extract_port:
            protocol =  extract_port.group(1)
            port_num = extract_port.group(2)
            expected_out = protocol + " dpt:" + port_num + " state NEW"
            if expected_out in iptables_openports:
                acls_present = 1
            else:
                acls_present = 0
                break
    if acls_present:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:    
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure wireless interfaces are disabled (Not Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = "which iwconfig"
    is_iwconfig = exec_command(cmd)
    verbose_logs("Command used", cmd)
    if "iwconfig" in is_iwconfig:
        cmd = "ip link show up"
        iwconfig_interfaces = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", iwconfig_interfaces)
        verbose_logs("Expected output to be compliant","Verify no wireless interfaces are active")
        verbose_logs("To be compliant, run","ip link set <interface> down")
        if "wlan" in iwconfig_interfaces:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

def config_sysAccounting():
    global compliant_count

    compliance_check = "Ensure audit log storage size is configured (Not Scored, Level 2 Server and Workstation)"
    if os.path.isfile("/etc/audit/auditd.conf"):
        cmd = "grep max_log_file /etc/audit/auditd.conf"
        max_log_file = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant","Set \"max_log_file = <MB>\" parameter in /etc/audit/auditd.conf")
        if "max_log_file" in max_log_file:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure system is disabled when audit logs are full (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/auditd.conf"):
        cmd = "grep -iE \"space_left_action|action_mail_acct|dmin_space_left_action\" /etc/audit/auditd.conf"
        is_auditd_actionspace = exec_command(cmd)
        is_space_left_action = re.match(r'.*?space_left_action\s*=\s*email.*?',space_left_action,re.I|re.M|re.S)
        is_action_mail_acct = re.match(r'.*?action_mail_acct\s*=\s*root.*?',action_mail_acct,re.I|re.M|re.S)
        is_dmin_space_left_action = re.match(r'.*?admin_space_left_action\s*=\s*halt.*?',is_dmin_space_left_action,re.I|re.M|re.S)
        verbose_logs("Command Output", cmd)
        verbose_logs("Expected output to be compliant","Parameters space_left_action = email, action_mail_acct = root, admin_space_left_action = halt must be configured")
        verbose_logs("To be compliant, run","Edit /etc/audit/auditd.conf by adding space_left_action = email, action_mail_acct = root, admin_space_left_action = halt")
        if is_space_left_action and is_action_mail_acct and is_dmin_space_left_action:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure audit logs are not automatically deleted (Scored, Level 2 Server and Workstation)"
    if os.path.isfile("/etc/audit/auditd.conf"):
        cmd = "grep max_log_file_action /etc/audit/auditd.conf"
        max_log_file_action = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", max_log_file_action)
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","Edit /etc/audit/auditd.conf by adding max_log_file_action = keep_logs")
        is_max_log_file_action = re.match(r'.*?max_log_file_action\s*=\s*keep_logs.*?',action_mail_acct,re.I|re.M|re.S)
        if is_max_log_file_action:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure auditd service is enabled (Scored, Level 2 Server and Workstation)"
    cmd = "rc-service -l |grep -i auditd"
    is_auditd = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_auditd)
    verbose_logs("Expected output to be compliant","Verify auditd is enabled")
    verbose_logs("To be compliant, run","rc-service auditd start or service auditd start or /etc/init.d/auditd start")
    if "auditd" in is_auditd:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure auditing for processes that start prior to auditd is enabled (Scored, Level 2 Server and Workstation)"
    #Bootconfig is present in either extlinux.conf, syslinux.cfg, grub.cfg, /etc/default/grub, /proc/cmdline
    #https://wiki.alpinelinux.org/wiki/Bootloaders
    if os.path.isfile("/boot/extlinux.conf"):
        cmd = "cat /boot/extlinux.conf"
        is_audit = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_audit)
        verbose_logs("Expected output to be compliant","Verify that each linux line has the audit=1 parameter set")
        if "audit=1" in is_audit:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif os.path.isfile("/boot/syslinux/syslinux.cfg"):
        cmd = "cat /boot/syslinux/syslinux.cfg"
        is_audit = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_audit)
        verbose_logs("Expected output to be compliant","Verify that each linux line has the audit=1 parameter set")
        if "audit=1" in is_audit:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif os.path.isfile("/boot/grub/grub.cfg"):
        cmd = "cat /boot/grub/grub.cfg"
        is_audit = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_audit)
        verbose_logs("Expected output to be compliant","Verify that each linux line has the audit=1 parameter set")
        if "audit=1" in is_audit:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif os.path.isfile("/etc/default/grub"):
        cmd = "cat /etc/default/grub"
        is_audit = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_audit)
        verbose_logs("Expected output to be compliant","Verify that each linux line has the audit=1 parameter set")
        verbose_logs("To be compliant","Edit /etc/default/grub and add GRUB_CMDLINE_LINUX=\"audit=1\"")
        if "audit=1" in is_audit:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif os.path.isfile("/proc/cmdline"):
        cmd = "cat /proc/cmdline"
        is_audit = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_audit)
        verbose_logs("Expected output to be compliant","Verify that each linux line has the audit=1 parameter set")
        verbose_logs("To be compliant","Add GRUB_CMDLINE_LINUX=\"audit=1\" as kernel parameter")
        if "audit=1" in is_audit:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure events that modify date and time information are collected (Scored, Level 2 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = "grep time-change /etc/audit/audit.rules"
        is_auditrules = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_auditrules)
        verbose_logs("Expected output to be compliant","Set adjtimex, settimeofday, stime, clock_settime etc in /etc/audit/audit.rules")
        verbose_logs("To be compliant, run","Edit /etc/audit/audit.rules by adding adjtimex, settimeofday, stime, clock_settime etc")
        cmd = "uname -m"
        os_bit = exec_command(cmd)
        is_stod = 0
        is_stime = 0
        is_cst64 = 0
        is_cst32 = 0
        is_ltime = 0
        if "time-change" in is_auditrules:
            audit_rules = is_auditrules.split('\n')
            for each_au_tc_rule in audit_rules:
                print "each_au_tc_rule:", each_au_tc_rule
                stod = re.match(r'.*?(-a\s+always,exit\s+-F\s+arch=b64\s+-S\s+adjtimex\s+-S\s+settimeofday\s+-k\s+time-change).*?', each_au_tc_rule, re.I|re.M|re.S)
                stime = re.match(r'.*?(-a\s+always,exit\s+-F\s+arch=b32\s+-S\s+adjtimex\s+-S\s+settimeofday\s+-S\s+stime\s+-k\s+time-change).*?',each_au_tc_rule, re.I|re.M|re.S)
                cst64 = re.match(r'.*?(-a\s+always,exit\s+-F\s+arch=b64\s+-S\s+clock_settime\s+-k\s+time-change).*?',each_au_tc_rule, re.I|re.M|re.S)
                cst32 = re.match(r'.*?(-a\s+always,exit\s+-F\s+arch=b32\s+-S\s+clock_settime\s+-k\s+time-change).*?',each_au_tc_rule, re.I|re.M|re.S)
                ltime = re.match(r'.*?(-w\s+/etc/localtime\s+-p\s+wa\s+-k\s+time-change).*?',each_au_tc_rule, re.I|re.M|re.S)
                if stod:
                    is_stod = 1
                if stime:
                    is_stime = 1
                if cst64:
                    is_cst64 = 1
                if cst32:
                    is_cst32 = 1
                if ltime:
                    is_ltime = 1
            if is_stod and stime and cst64 and cst32 and ltime and "64" in os_bit:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            elif stime and cst32 and ltime:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:   
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure events that modify user/group information are collected (Scored, Level 2 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = "grep identity /etc/audit/audit.rules"
        is_identity = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_identity)
        verbose_logs("Expected output to be compliant","identity set on sensitive files like /etc/passwd, /etc/shadow")
        verbose_logs("To be compliant, run","Edit /etc/audit/audit.rules by adding \"-w /etc/(group,passwd,shadow,gshadow) -p wa -k identity\" or \"-w /etc/security/opasswd -p wa -k identity\"")
        is_group = 0
        is_passwd= 0
        is_gshadow = 0
        is_shadow = 0
        is_securityopasswd = 0
        if "identity" in is_identity:
            file_identity = is_identity.split('\n')
            for each_file_identity in file_identity:
                print "each_file_identity:", each_file_identity
                group = re.match(r'.*?(-w\s+/etc/group\s+-p\s+wa\s+-k\s+identity).*?',each_file_identity, re.I|re.M|re.S)
                passwd = re.match(r'.*?(-w\s+/etc/passwd\s+-p\s+wa\s+-k\s+identity).*?',each_file_identity, re.I|re.M|re.S)
                gshadow = re.match(r'.*?(-w\s+/etc/gshadow\s+-p\s+wa\s+-k\s+identity).*?',each_file_identity, re.I|re.M|re.S)
                shadow = re.match(r'.*?(-w\s+/etc/shadow\s+-p\s+wa\s+-k\s+identity).*?',each_file_identity, re.I|re.M|re.S)
                securityopasswd = re.match(r'.*?(-w\s+/etc/security/opasswd\s+-p\s+wa\s+-k\s+identity).*?',each_file_identity, re.I|re.M|re.S)
                if group:
                    is_group = 1
                if passwd:
                    is_passwd = 1
                if gshadow:
                    is_gshadow = 1
                if shadow:
                    is_shadow = 1
                if securityopasswd:
                    is_securityopasswd = 1
            if is_group and is_passwd and gshadow and shadow and securityopasswd:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure events that modify the system's network environment are collected (Scored, Level 2 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure events that modify the system's Mandatory Access Controls are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure login and logout events are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure session initiation information is collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure discretionary access control permission modification events are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure unsuccessful unauthorized file access attempts are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure use of privileged commands is collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure successful file system mounts are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure file deletion events by users are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure changes to system administration scope (sudoers) is collected(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure system administrator actions (sudolog) are collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure kernel module loading and unloading is collected (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:   
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure the audit configuration is immutable (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/audit/audit.rules"):
        cmd = "grep \"^\s*[^#]\" /etc/audit/audit.rules | tail -1"
        is_auconf_immu = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_auconf_immu)
        verbose_logs("Expected output to be compliant","-e 2")
        verbose_logs("To be compliant, run","Edit /etc/audit/audit.rules and add \"-e 2\" at the end of file")
        if "-e 2" in is_auconf_immu:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def config_logging():
    global compliant_count

    compliance_check = "Ensure rsyslog Service is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i rsyslog; rc-service -l |grep -i rsyslog"
    is_rsyslog = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_rsyslog)
    verbose_logs("Expected output to be compliant","Verify rsyslog Service is enabled")
    verbose_logs("To be compliant, run","apk add rsyslog && rc-service rsyslog start")
    if "rsyslog" in is_rsyslog:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure logging is configured (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/rsyslog.conf"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure rsyslog default file permissions configured (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/rsyslog.conf"):
        cmd = "grep ^\$FileCreateMode /etc/rsyslog.conf"
        rsyslog_file_perm = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", rsyslog_file_perm)
        verbose_logs("Expected output to be compliant","$FileCreateMode 0640")
        verbose_logs("To be compliant","Edit the /etc/rsyslog.conf and set $FileCreateMode to 0640 or more restrictive")
        #TODO: extract permission, convert into int which should be less than or equal to 640
        if "640" in rsyslog_file_perm:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    
    compliance_check = "Ensure rsyslog is configured to send logs to a remote log host (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/rsyslog.conf"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure remote rsyslog messages are only accepted on designated log hosts. (Not Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/rsyslog.conf"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure syslog-ng service is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i syslog-ng; rc-service -l |grep -i syslog-ng"
    is_syslogng = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_syslogng)
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","apk add syslog-ng && rc-service syslog-ng start")
    if "syslog-ng" in is_syslogng:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure logging is configured (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/syslog-ng/syslog-ng.conf"):
        cmd = "cat /etc/syslog-ng/syslog-ng.conf"
        content_syslogng = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", content_syslogng)
        verbose_logs("Expected output to be compliant","Review the contents of the /etc/syslog-ng/syslog-ng.conf file to ensure appropriate logging is set.")
        verbose_logs("To be compliant, check","execute ls -l /var/log/")
        update_compliance_status(compliance_check, "COMPLIANT (verify manually)")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT (verify manually)")

    compliance_check = "Ensure syslog-ng default file permissions configured (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/syslog-ng/syslog-ng.conf"):
        cmd = "grep ^options /etc/syslog-ng/syslog-ng.conf"
        is_syslogng_options = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_syslogng_options)
        verbose_logs("Expected output to be compliant","verify the perm option is 0640 or more restrictive")
        verbose_logs("To be compliant, run","Edit the /etc/syslog-ng/syslog-ng.conf and set perm option to 0640 or more restrictive")
        if "options" in is_syslogng_options:
            syslogng_perm = re.match(r'^options\s+{.*?perm\(.(\d{3})\)\s*;.*?',is_syslogng_options,re.I|re.M|re.S)
            if syslogng_perm:
                if int(syslogng_perm.group(1)) <= 640:
                    update_compliance_status(compliance_check, "COMPLIANT")
                else:
                    compliant_count -= 1
                    update_compliance_status(compliance_check, "NON-COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure syslog-ng is configured to send logs to a remote log host (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/syslog-ng/syslog-ng.conf"):
        cmd = "grep \"destination logserver\" /etc/syslog-ng/syslog-ng.conf | grep -vE \"127\.0\.0\|localhost\""
        syslogng_remote_log = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", syslogng_remote_log)
        verbose_logs("Expected output to be compliant","Verify that logs are sent to a central host")
        verbose_logs("To be compliant, run","Edit /etc/syslog-ng/syslog-ng.conf by adding Server IP/Domain")
        if "destination logserver" in syslogng_remote_log:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure remote syslog-ng messages are only accepted on designated log hosts (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/syslog-ng/syslog-ng.conf"):
        cmd = "grep \"destination remote\" /etc/syslog-ng/syslog-ng.conf | grep -vE \"127\.0\.0\|localhost\""
        syslogng_remote_desig = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", syslogng_remote_desig)
        verbose_logs("Expected output to be compliant","Verify that logs are sent to a central host")
        verbose_logs("To be compliant, run","Edit /etc/syslog-ng/syslog-ng.conf by adding Server IP/Domain")
        if "destination logserver" in syslogng_remote_log:
            compliant_count += 1
            update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure rsyslog or syslog-ng is installed (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -iE \"rsyslog|syslog-ng\"; rc-service -l |grep -iE \"rsyslog|syslog-ng\""
    is_syslogRsyslogng = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_syslogRsyslogng)
    verbose_logs("Expected output to be compliant","verify at least syslog or syslog-ng is running")
    verbose_logs("To be compliant, run","apk add syslog-ng/rsyslog && rc-service syslog-ng/rsyslog start")
    if "rsyslog" in is_syslogRsyslogng or "syslog-ng" in is_syslogRsyslogng:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure permissions on all logfiles are configured (Scored, Level 1 Server and Workstation)"
    cmd = "find /var/log -type f |xargs stat | grep -i uid: | grep -v 640"
    logfiles_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", logfiles_perm)
    verbose_logs("Expected output to be compliant","verify that other has no permissions on any files and group does not have write or execute permissions on any files i.e. 0640")
    verbose_logs("To be compliant, run","find /var/log -type f -exec chmod g-wx,o-rwx {} +")
    if "access:" in logfiles_perm.lower() and "uid:" in logfiles_perm.lower():
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    

    compliance_check = "Ensure logrotate is configured (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/logrotate.conf"):
        cmd = "grep /var/log /etc/logrotate.conf"
        is_logrotate_configured = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_logrotate_configured)
        verbose_logs("Expected output to be compliant","Verify logs are rotated according to Corporate policy")
        verbose_logs("To be compliant","Edit /etc/logrotate.conf and /etc/logrotate.d/* to ensure logs are rotated according to Corporate policy")
        if "/var/log" in is_logrotate_configured:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
def config_cron():
    global compliant_count

    compliance_check = "Ensure cron daemon is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "rc-status -a |grep -i cron; rc-service -l |grep -i cron"
    is_cron = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_cron)
    verbose_logs("Expected output to be compliant","Verify cron daemon is enabled")
    verbose_logs("To be compliant, run","apk add cron && rc-service cron start")
    if "cron" in is_cron:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/crontab are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/crontab"
    crontab_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", crontab_perm)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/crontab && chmod og-rwx /etc/crontab")
    required_crontab_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',crontab_perm, re.I|re.M|re.S)
    if required_crontab_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/cron.hourly are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/cron.hourly"
    cronhourly_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", cronhourly_perm)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/cron.hourly && chmod og-rwx /etc/cron.hourly")
    required_cronhourly_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',cronhourly_perm, re.I|re.M|re.S)
    if required_cronhourly_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/cron.daily are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/cron.daily"
    crondaily_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", crondaily_perm)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/cron.daily && chmod og-rwx /etc/cron.daily")
    required_crondaily_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',crondaily_perm, re.I|re.M|re.S)
    if required_crondaily_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/cron.weekly are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/cron.weekly"
    cronweekly_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", cronweekly_perm)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/cron.weekly && chmod og-rwx /etc/cron.weekly")
    required_cronweekly_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',cronweekly_perm, re.I|re.M|re.S)
    if required_cronweekly_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure permissions on /etc/cron.monthly are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/cron.monthly"
    cronmonthly_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", cronmonthly_perm)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/cron.monthly && chmod og-rwx /etc/cron.monthly")
    required_cronmonthly_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',cronmonthly_perm, re.I|re.M|re.S)
    if required_cronmonthly_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure permissions on /etc/cron.d are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/cron.d"
    crond_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", crond_perm)
    verbose_logs("Expected output to be compliant","Verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/crond && chmod og-rwx /etc/crond")
    required_crond_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',crond_perm, re.I|re.M|re.S)
    if required_crond_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure at/cron is restricted to authorized users (Scored, Level 1 Server and Workstation)"
    is_cron_deny = 0
    is_cron_allow = 0
    if os.path.isfile("/etc/cron.deny") or os.path.isfile("/etc/at.deny"):
        is_cron_deny = 1
    if os.path.isfile("/etc/cron.allow") and os.path.isfile("/etc/at.allow"):
        is_cron_allow = 1
    if is_cron_deny == 0 and is_cron_allow == 1:
        cmd1 = "stat /etc/cron.allow"
        cronallow = exec_command(cmd1)
        required_crond_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',crond_perm, re.I|re.M|re.S)
        if required_crond_perm:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
        cmd2 = "stat /etc/at.allow"
        atallow = exec_command(cmd2)
        required_crond_perm  = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))',crond_perm, re.I|re.M|re.S)
        if required_crond_perm:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
        verbose_logs("Command used", cmd1 + cmd2)
        verbose_logs("Command Output", cronallow + atallow)
        verbose_logs("Expected output to be compliant","ensure /etc/cron.deny and /etc/at.deny do not exist. verify Uid and Gid are both 0/root and Access does not grant permissions to group or other for both /etc/cron.allow and /etc/at.allow")
        verbose_logs("To be compliant, run","remove /etc/cron.deny and /etc/at.deny and create and set permissions and ownership for /etc/cron.allow and /etc/at.allow")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def config_SSH():
    global compliant_count

    compliance_check = "Ensure permissions on /etc/ssh/sshd_config are configured (Scored, Level 1 Server and Workstation)"
    cmd = "stat /etc/ssh/sshd_config"
    sshd_config_perm = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_config_perm)
    verbose_logs("Expected output to be compliant","verify Uid and Gid are both 0/root and Access does not grant permissions to group or other")
    verbose_logs("To be compliant, run","chown root:root /etc/ssh/sshd_config && chmod og-rwx /etc/ssh/sshd_config")
    is_sshd_config_perm = re.match(r'(.*?Access:\s*\(0600/..........\)\s*Uid:\s*\(\s*0/\s*root\)\s*Gid:\s*\(\s*0/\s*root\))', sshd_config_perm, re.I|re.M|re.S)
    if is_sshd_config_perm:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH Protocol is set to 2 (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^Protocol\" /etc/ssh/sshd_config"
    ssh_protocol = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", ssh_protocol)
    verbose_logs("Expected output to be compliant","Protocol 2")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as Protocol 2")
    if "protocol" in ssh_protocol.lower():
        is_sshprotocol2 = re.match(r'^Protocol\s+2.*?', ssh_protocol, re.I|re.M)
        if is_sshprotocol2:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH LogLevel is set to INFO (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^LogLevel\" /etc/ssh/sshd_config"
    is_sshloglevel_info = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", is_sshloglevel_info)
    verbose_logs("Expected output to be compliant","LogLevel INFO")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as LogLevel INFO")
    if " INFO" in is_sshloglevel_info:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH X11 forwarding is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^X11Forwarding\" /etc/ssh/sshd_config"
    sshd_x11forwarding = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_x11forwarding)
    verbose_logs("Expected output to be compliant","X11Forwarding no")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as X11Forwarding no")
    if " no" in sshd_x11forwarding:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH MaxAuthTries is set to 4 or less (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^MaxAuthTries\" /etc/ssh/sshd_config"
    sshd_maxauthtries = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_maxauthtries)
    verbose_logs("Expected output to be compliant","verify that output MaxAuthTries is 4 or less")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as MaxAuthTries 4")
    if "MaxAuthTries" in sshd_maxauthtries:
        is_maxauthtries = re.match(r'^MaxAuthTries\s+(\d+).*?', sshd_maxauthtries, re.I|re.M)
        if is_maxauthtries:
            if int(is_maxauthtries.group(1)) <=1:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure SSH IgnoreRhosts is enabled (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^IgnoreRhosts\" /etc/ssh/sshd_config"
    sshd_ignorerhosts = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_ignorerhosts)
    verbose_logs("Expected output to be compliant","IgnoreRhosts yes")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as IgnoreRhosts yes")
    if " yes" in sshd_ignorerhosts:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH HostbasedAuthentication is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^HostbasedAuthentication\" /etc/ssh/sshd_config"
    sshd_hostbasedauthentication = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_hostbasedauthentication)
    verbose_logs("Expected output to be compliant","HostbasedAuthentication no")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as HostbasedAuthentication no")
    if " no" in sshd_hostbasedauthentication:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH root login is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^PermitRootLogin\" /etc/ssh/sshd_config"
    sshd_permitrootlogin = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_permitrootlogin)
    verbose_logs("Expected output to be compliant","PermitRootLogin no")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as PermitRootLogin no")
    if " no" in sshd_permitrootlogin:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH PermitEmptyPasswords is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^PermitEmptyPasswords\" /etc/ssh/sshd_config"
    sshd_permitemptypasswords = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_permitemptypasswords)
    verbose_logs("Expected output to be compliant","PermitEmptyPasswords no")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as PermitEmptyPasswords no")
    if " no" in sshd_permitemptypasswords:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH PermitUserEnvironment is disabled (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^PermitUserEnvironment\" /etc/ssh/sshd_config"
    sshd_permituserenvironment = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_permituserenvironment)
    verbose_logs("Expected output to be compliant","PermitUserEnvironment no")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as PermitUserEnvironment no")
    if " no" in sshd_permituserenvironment:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure only approved ciphers are used (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"Ciphers\" /etc/ssh/sshd_config"
    sshd_ciphers = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_ciphers)
    verbose_logs("Expected output to be compliant","Verify that output does not contain any cipher block chaining (-cbc) algorithms")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as Ciphers aes256-ctr,aes192-ctr,aes128-ctr")
    if "-cbc" in sshd_ciphers:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")

    compliance_check = "Ensure only approved MAC algorithms are used (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"MACs\" /etc/ssh/sshd_config"
    sshd_macs = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_macs)
    verbose_logs("Expected output to be compliant","Verify output does not contain any unlisted MAC algorithms")
    verbose_logs("To be compliant, run","")
    update_compliance_status(compliance_check, "MANUAL VERIFICATION NEEDED")

    compliance_check = "Ensure SSH Idle Timeout Interval is configured (Scored, Level 1 Server and Workstation)"
    cmd = "grep -iE \"^(ClientAliveInterval|ClientAliveCountMax)\" /etc/ssh/sshd_config"
    sshd_clientalive_interval_countmax = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_clientalive_interval_countmax)
    verbose_logs("Expected output to be compliant","Verify ClientAliveInterval is 300 or less and ClientAliveCountMax is 3 or less")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as ClientAliveInterval 300, ClientAliveCountMax 0")
    is_clientaliveinterval = re.match(r'^ClientAliveInterval\s+(\d+).*?', sshd_clientalive_interval_countmax, re.I|re.M|re.S)
    is_clientalivecountmax = re.match(r'^ClientAliveCountMax\s+(\d+).*?', sshd_clientalive_interval_countmax, re.I|re.M|re.S)
    if is_clientaliveinterval and is_clientalivecountmax:
        if (int(is_clientaliveinterval.group(1) <=300)) and (int(is_clientalivecountmax.group(1)) <=3):
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH LoginGraceTime is set to one minute or less (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^LoginGraceTime\" /etc/ssh/sshd_config"
    sshd_logingracetime = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_logingracetime)
    verbose_logs("Expected output to be compliant","Verify that output LoginGraceTime is 60 or less")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as LoginGraceTime 60")
    is_sshd_logingracetime = re.match(r'^LoginGraceTime\s+(\d+).*?', sshd_logingracetime, re.I|re.M|re.S)
    if is_sshd_logingracetime:
        if int(is_sshd_logingracetime.group(1)) <= 60:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure SSH access is limited (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^(AllowUsers|AllowGroups|DenyUsers|DenyGroups)\" /etc/ssh/sshd_config"
    sshd_users_groups = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_users_groups)
    verbose_logs("Expected output to be compliant","Verify that output matches for at least one of AllowUsers, AllowGroups, DenyUsers and DenyGroups")
    verbose_logs("To be compliant, run","Edit the /etc/ssh/sshd_config by adding one or more of the parameters AllowUsers <userlist>, AllowGroups <grouplist>, DenyUsers <userlist>, DenyGroups <grouplist>")
    if ("AllowUsers" in sshd_users_groups) or ("AllowGroups" in sshd_users_groups) or ("DenyUsers" in sshd_users_groups) or ("DenyGroups" in sshd_users_groups):
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")


    compliance_check = "Ensure SSH warning banner is configured (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^Banner\" /etc/ssh/sshd_config"
    sshd_banner = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", sshd_banner)
    verbose_logs("Expected output to be compliant","Banner /etc/issue.net")
    verbose_logs("To be compliant, run","Edit /etc/ssh/sshd_config set the parameter as Banner /etc/issue.net")
    if " /etc/issue.net" in sshd_banner:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def config_PAM():
    global compliant_count

    compliance_check = "Ensure password creation requirements are configured (Scored, Level 1 Server and Workstation)"
    #password required pam_cracklib.so try_first_pass retry=3 minlen=14 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1 
    #password requisite pam_pwquality.so try_first_pass retry=3
    if os.path.isfile("/etc/pam.d/common-password"):
        cmd1 = "grep pam_cracklib.so in /etc/pam.d/common-password"
        is_pam_cracklib = exec_command(cmd1)
        cmd2 = "grep pam_pwquality.so in /etc/pam.d/common-password"
        is_pam_pwquality = exec_command(cmd2)
        verbose_logs("Command used", cmd1 + cmd2)
        verbose_logs("Command Output", is_pam_cracklib + is_pam_pwquality)
        verbose_logs("Expected output to be compliant","Verify password creation requirements are as listed or stricter(commonly configured with the pam_cracklib.so or pam_pwquality.so options in /etc/pam.d)")
        verbose_logs("To be compliant, run","If pam_pwquality.so is in use also configure settings in /etc/security/pwquality.conf.")
    elif os.path.isfile("/etc/pam.d/system-auth"):
        cmd = ""
        n = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", )
        verbose_logs("Expected output to be compliant","")
        verbose_logs("To be compliant, run","")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure lockout for failed password attempts is configured (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/pam.d/common-password"):
        cmd = ""
        n = exec_command(cmd)
    elif os.path.isfile("/etc/pam.d/system-auth"):
        cmd = ""
        n = exec_command(cmd)
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure password reuse is limited (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/pam.d/common-password"):
        cmd = "grep -iE \"pam_pwhistory|pam_unix\" /etc/pam.d/common-password"
        is_pwhistory_unix = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_pwhistory_unix)
        verbose_logs("Expected output to be compliant","password required pam_pwhistory.so remember=5; password sufficient pam_unix.so remember=5")
        verbose_logs("To be compliant, run","edit the appropriate /etc/pam.d/ configuration file")
        passwd_remember = re.match(r'password\s+(required\s+pam_pwhistory|sufficient\s+pam_unix)\.so\s+remember=(\d+)',is_pwhistory_unix, re.I|re.M|re.S)
    elif os.path.isfile("/etc/pam.d/system-auth"):
        cmd = "grep -iE \"pam_pwhistory|pam_unix\" /etc/pam.d/system-auth"
        is_pwhistory_unix = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", is_pwhistory_unix)
        verbose_logs("Expected output to be compliant","password required pam_pwhistory.so remember=5; password sufficient pam_unix.so remember=5")
        verbose_logs("To be compliant, run","edit the appropriate /etc/pam.d/ configuration file")
        passwd_remember = re.match(r'password\s+(required\s+pam_pwhistory|sufficient\s+pam_unix)\.so\s+remember=(\d+)',is_pwhistory_unix, re.I|re.M|re.S)
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

    compliance_check = "Ensure password hashing algorithm is SHA-512 (Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/pam.d/common-password"):
        cmd = "grep pam_unix.so /etc/pam.d/common-password"
        passwd_hashing = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", passwd_hashing)
        verbose_logs("Expected output to be compliant","Verify password hashing algorithm is sha512")
        verbose_logs("To be compliant, run","")
        if "sha512" in passwd_hashing:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif os.path.isfile("/etc/pam.d/system-auth"):
        cmd = "grep pam_unix.so /etc/pam.d/system-auth"
        passwd_hashing = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", passwd_hashing)
        verbose_logs("Expected output to be compliant","Verify password hashing algorithm is sha512")
        verbose_logs("To be compliant, run","edit the appropriate /etc/pam.d/ configuration file and add/modify password sufficient pam_unix.so sha512")
        if "sha512" in passwd_hashing:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")

def userAccounts_andEnvironment():
    global compliant_count

    compliance_check = "Ensure password expiration is 90 days or less (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/login.defs"):
        cmd = "grep PASS_MAX_DAYS /etc/login.defs"
        pass_max_days = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", pass_max_days)
        verbose_logs("Expected output to be compliant","Verify PASS_MAX_DAYS is 90 or less")
        verbose_logs("To be compliant","Set the PASS_MAX_DAYS parameter to 90 in /etc/login.defs")
        if "PASS_MAX_DAYS" in pass_max_days:
            no_pass_max_days = re.match(r'PASS_MAX_DAYS\s+(\d+)', pass_max_days, re.I|re.M)
            if int(no_pass_max_days.group(1)) <=90:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure minimum days between password changes is 7 or more (Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/login.defs"):
        cmd = "grep PASS_MIN_DAYS /etc/login.defs"
        pass_min_days = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", pass_min_days)
        verbose_logs("Expected output to be compliant","Verify PASS_MIN_DAYS is 7 or more")
        verbose_logs("To be compliant","Set the PASS_MIN_DAYS parameter to 7 in /etc/login.defs")
        if "PASS_MIN_DAYS" in pass_min_days:
            no_pass_min_days = re.match(r'PASS_MIN_DAYS\s+(\d+)', pass_min_days, re.I|re.M)
            if int(no_pass_min_days.group(1)) >= 7:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure password expiration warning days is 7 or more (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/login.defs"):
        cmd = "grep PASS_WARN_AGE /etc/login.defs"
        pass_warn_age = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", pass_warn_age)
        verbose_logs("Expected output to be compliant","Verify PASS_WARN_AGE is 7 or more")
        verbose_logs("To be compliant","Set the PASS_WARN_AGE parameter to 7 in /etc/login.defs")
        if "PASS_MAX_DAYS" in pass_warn_age:
            no_pass_warn_age = re.match(r'PASS_WARN_AGE\s+(\d+)', pass_warn_age, re.I|re.M)
            if int(no_pass_warn_age.group(1)) >= 7:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure inactive password lock is 30 days or less (Scored)(Not Scored, Level 1 Server and Workstation)"
    if os.path.isfile("/etc/login.defs"):
        cmd = "useradd -D | grep INACTIVE"
        inactive_pass = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", inactive_pass)
        verbose_logs("Expected output to be compliant","Verify INACTIVE is 30 or less")
        verbose_logs("To be compliant","Set the PASS_MAX_DAYS parameter to 30 in /etc/login.defs")
        if "PASS_MAX_DAYS" in pass_max_days:
            no_pass_max_days = re.match(r'PASS_MAX_DAYS\s+(\d+)', pass_max_days, re.I|re.M)
            if int(no_pass_max_days.group(1)) <=90:
                compliant_count += 1
                update_compliance_status(compliance_check, "COMPLIANT")
            else:
                compliant_count -= 1
                update_compliance_status(compliance_check, "NON-COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure system accounts are non-login (Scored, Level 1 Server and Workstation)"
    cmd = "egrep -v \"^\+\" /etc/passwd | awk -F: '($1!=\"root\" && $1!=\"sync\" && $1!=\"shutdown\" && $1!=\"halt\" && $3<500 && $7!=\"/sbin/nologin\" && $7!=\"/bin/false\") {print}'"
    users_nonlogin = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", users_nonlogin)
    verbose_logs("Expected output to be compliant","verify no results are returned")
    verbose_logs("To be compliant, run","usermod -s /sbin/nologin <user>")
    if "EXCEPTION:" in users_nonlogin:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure default group for the root account is GID 0 (Scored, Level 1 Server and Workstation)"
    cmd = "grep \"^root:\" /etc/passwd | cut -f4 -d:"
    def_grp_gid0 = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", def_grp_gid0)
    verbose_logs("Expected output to be compliant","Verify default group for the root account is GID 0")
    verbose_logs("To be compliant, run","usermod -g 0 root")
    if "0" in users_nonlogin:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count -= 1
        update_compliance_status(compliance_check, "NON-COMPLIANT")
    
    compliance_check = "Ensure default user umask is 027 or more restrictive (Scored, Level 1 Server and Workstation)"
    #077-causes files and directories created by users to not be readable by any other user on the system
    #027-would make files and directories readable by users in the same Unix group
    #022-would make files readable by every user on the system
    is_bashrc = 0
    is_pofile= 0
    bashrc_umaskval = 0
    profile_umaskval = 0
    if os.path.isfile("/etc/bashrc"):
        is_bashrc = 1
        cmd = "grep \"^umask\" /etc/bashrc"
        umask_bashrc = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", umask_bashrc)
        verbose_logs("Expected output to be compliant","Verify umask returned are 027 or more restrictive")
        verbose_logs("To be compliant, run","Edit /etc/bashrc, /etc/profile or files for any other shell supported on your system by adding umask 027")
        if "umask" in umask_basjrc:
            umask_val_bashrc = re.match(r'umask\s+(\d+)', umask_bashrc, re.M|re.I|re.S)
            bashrc_umaskval = int(umask_val_bashrc.group(1))
    
    if os.path.isfile("/etc/profile"):
        is_profile= 1
        cmd = "grep \"^umask\" /etc/profile"
        umask_profile = exec_command(cmd)
        verbose_logs("Command used", cmd)
        verbose_logs("Command Output", umask_profile)
        verbose_logs("Expected output to be compliant","Verify umask returned are 027 or more restrictive")
        verbose_logs("To be compliant, run","Edit /etc/bashrc, /etc/profile or files for any other shell supported on your system by adding umask 027")
        if "umask" in umask_profile:
            umask_val_profile = re.match(r'umask\s+(\d+)', umask_profile, re.M|re.I|re.S)
            profile_umaskval = int(umask_val_profile.group(1))

    if is_bashrc and is_profile:
        verbose_logs("INFO","/etc/bashrc file not found, /etc/profile found!")
        if bashrc_umaskval >= 27 and profile_umaskval >= 27:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif is_bashrc == 0 and is_profile == 1:
        verbose_logs("INFO","/etc/bashrc file not found, /etc/profile found!")
        if profile_umaskval >= 27:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif is_bashrc == 1 and is_profile == 0:
        verbose_logs("INFO","/etc/bashrc file found, /etc/profile not found!")
        if bashrc_umaskval >= 27:
            compliant_count += 1
            update_compliance_status(compliance_check, "COMPLIANT")
        else:
            compliant_count -= 1
            update_compliance_status(compliance_check, "NON-COMPLIANT")
    elif is_bashrc == 0 and is_profile == 0:
        verbose_logs("INFO","/etc/bashrc file not found, /etc/profile not found!")
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")
    else:
        compliant_count += 1
        update_compliance_status(compliance_check, "COMPLIANT")


    compliance_check = "Ensure root login is restricted to system console (Not Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure access to the su command is restricted (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def sysFilePermissions():
    global compliant_count

    compliance_check = "Audit system file permissions (Not Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure permissions on /etc/passwd are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/shadow are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/group are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/gshadow are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/passwd- are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/shadow- are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/group- are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure permissions on /etc/gshadow- are configured (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no world writable files exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no unowned files or directories exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no ungrouped files or directories exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Audit SUID executables (Not Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Audit SGID executables (Not Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
def userGroupSettings():
    global compliant_count

    compliance_check = "Ensure password fields are not empty (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no legacy \"+\" entries exist in /etc/passwd (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no legacy \"+\" entries exist in /etc/shadow (Scored)(Scored, Level 1 Server and Workstation))"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")

    compliance_check = "Ensure no legacy \"+\" entries exist in /etc/group (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "(Ensure root is the only UID 0 account (Scored)Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure root PATH Integrity (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure all users' home directories exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users' home directories permissions are 750 or more restrictive (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users own their home directories (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users' dot files are not group or world writable (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no users have .forward files (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no users have .netrc files (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure users' .netrc Files are not group or world accessible (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no users have .rhosts files (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure all groups in /etc/passwd exist in /etc/group (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate UIDs exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate GIDs exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate user names exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure no duplicate group names exist (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
    compliance_check = "Ensure shadow group is empty (Scored)(Not Scored, Level 1 Server and Workstation)"
    cmd = ""
    n = exec_command(cmd)
    verbose_logs("Command used", cmd)
    verbose_logs("Command Output", )
    verbose_logs("Expected output to be compliant","")
    verbose_logs("To be compliant, run","")
    
if __name__ == "__main__":
    global total_compliances
    global compliant_count

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
    parser.add_argument("-n", "--nocolor", help="plain console output(default logging uses color)",action="store_true")
    args = parser.parse_args()

    print "Hardening Checks for Alpine Linux based on Centre for Internet Security Benchmarks"
    print "Benchmark Reference","CIS Distribution Independent Linux v1.0.1 - 01-31-2017"
    print "Author: Praveen Darshanam"

    verbose_logs("RECOMMENDATION SECTION","Initial Setup")
    filesystem_config()
    config_swUpdates()
    fs_integrity_checking()
    sec_boot_settings()
    process_hardening()
    mandatory_access_control()
    warning_banners()

    verbose_logs("RECOMMENDATION SECTION","Services")
    inetd_services()
    special_purpose_services()
    service_clients()
    
    verbose_logs("RECOMMENDATION SECTION","Network Configuration")
    networkParam_hostRouter()
    ipv6()
    tcp_wrappers()
    uncommon_nwProtocols()
    firewall_configuration()

    verbose_logs("RECOMMENDATION SECTION","Logging and Auditing")
    config_sysAccounting()
    config_logging()

    verbose_logs("RECOMMENDATION SECTION","Access, Authentication and Authorization")
    config_cron()
    config_SSH()
    config_PAM()
    userAccounts_andEnvironment()

    verbose_logs("RECOMMENDATION SECTION","System Maintenance")
    sysFilePermissions()
    userGroupSettings()


    """
    print "Checking File System Permissions and Access Controls"
    print "Checking Password Management"
    """
    verbose_logs("RECOMMENDATION SECTION","User Accounts and Environment")
    user_AccountsEnvironment()

    verbose_logs("RECOMMENDATION SECTION","Additional Considerations")
    additional_considerations()

    print "Total Compliances Checklist:", total_compliances
    print "Total Compliances Passed:", compliant_count
