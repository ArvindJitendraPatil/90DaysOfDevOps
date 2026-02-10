disk -- phisical volume - volume group - logical volume
vi /etc/fstab -- for per. mounting | disk name ext4 /mnt/data  default 0 0
man lvm
----------------------
# Task 1: Check Current Storage
- lsblk # Shows all disks and partitions
- pvs # Shows physical volumes
- vgs # Shows volume groups
- lvs # Shows logical volumes
- df -h # Shows mounted filesystem usage
# Task 2: Create Physical Volume
root : lvm 
pvcreate /dev/sdb
pvs # Confirms that PV is created
# Task 3: Create Volume Group
vgcreate devops-vg /dev/sdb
vgs # Confirms VG creation
# Task 4: Create Logical Volume
lvcreate -L 500M -n app-data devops-vg
lvs # Confirms LV creation
# Task 5: Format and Mount
mkfs.ext4 /dev/devops-vg/app-data # Format with ext4
mkdir -p /mnt/app-data # Create mount folder
mount /dev/devops-vg/app-data /mnt/app-data # Mount
df -h /mnt/app-data # Verify mount usage
# Task 6: Extend the Volume
lvextend -L +200M /dev/devops-vg/app-data
resize2fs /dev/devops-vg/app-data # Resize filesystem
df -h /mnt/app-data # Verify updated size
