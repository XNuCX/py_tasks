import time
import nvidia_smi
import nvsmi
import nvgpu
from nvsmi import GPU
import pynvml
time.sleep(0.5)
# nvidia_smi.nvmlInit()
# handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
# # card id 0 hardcoded here, there is also a call to get all available card ids, so we could iterate
#
# res = nvidia_smi.nvmlDeviceGetUtilizationRates(handle)
# # a = GPU(id=0,
#         uuid=1,
#         gpu_util=2,
#         mem_total=3,
#         mem_used=4,
#         mem_free=5,
#         driver=6,
#         gpu_name=7,
#         serial=8,
#         display_mode=9,
#         display_active=10,
#         temperature=11)
a=[]
a = nvsmi._get_gpu(" , , , , , , , , , , , , ")
print(a)

nvgpu.available_gpus()
