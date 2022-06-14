import tango
from tango.futures import DeviceProxy

device = DeviceProxy('NanoControl/NanoControl/1')
# device.init_device()
# device.set_timeout_millis(10000000)
device.apply_calibration()
device.set_fh_time_profile([0,500,1000,2000,2500,3000])
device.set_fh_temp_profile([0.,0.,1.,1.,0.,0.]) 
device.arm_fast_heat()      
device.run_fast_heat(wait=False)