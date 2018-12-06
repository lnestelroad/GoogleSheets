#!/bin/bash

diskutil list
echo "Which disk would you like to use"
echo -n "Disk: "
read disk

if [ "$disk" = "1" ] || [ "$disk" = 0 ]
then
	echo "Cannot unmount main disks!"
else
	diskutil unmountDisk /dev/disk$disk
fi

file=$(ls | grep -i 'Raspi3v' | cut -d ' ' -f15 | cut -d 'v' -f2 | cut -d '.' -f1)
oldFile=$((file++))

rm Raspi3v$oldFile.vmdk

sudo VBoxManage internalcommands createrawvmdk -filename ./Raspi3v$file.vmdk -rawdisk /dev/disk$disk
sudo chmod 777 Raspi3v$file.vmdk
sudo chmod 777 /dev/disk$disk

diskutil unmountDisk /dev/disk$disk
