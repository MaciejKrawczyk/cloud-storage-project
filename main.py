import psutil

obj_Disk = psutil.disk_usage('/')

print (obj_Disk.total / (1024.0 ** 3))
print (obj_Disk.used / (1024.0 ** 3))
print (obj_Disk.free / (1024.0 ** 3))
print (obj_Disk.percent)

