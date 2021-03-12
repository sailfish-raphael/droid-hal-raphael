# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device raphael
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Mi 9T Pro

%define rpm_device raphael
%define installable_zip 1
%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define straggler_files \
    /acct \
    /charger \
    /bt_firmware \
    /bugreports \
    /d \
    /cache \
    /sdcard \
    /dsp \
    /firmware \
    /persist \
    /product \
    /odm \
    /system \
    /oem \
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}
 
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

# On Android 8 the system partition is (intended to be) mounted on /.
%define makefstab_skip_entries /vendor /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl /dev/sdf7 /dev/sdf8

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

