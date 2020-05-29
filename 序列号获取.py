import wmi
import win32api


print(win32api.GetVolumeInformation(r'E:/'))

c = wmi.WMI()

# # 硬盘序列号
for physical_disk in c.Win32_DiskDrive():
    print(physical_disk.SerialNumber)

import wmi
c = wmi.WMI()
for item in c.Win32_PhysicalMedia():
    print (item)