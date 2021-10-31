import py3nvml.nvidia_smi as smi

def search_pid_in_unused_rndr_process():
    smi_info = smi.XmlDeviceQuery().split("\n")
    for i, data in enumerate(smi_info):
        if "<process_name>" in data:
            process_id_for_kill = smi_info[i-1].strip().\
                replace("<pid>", "").\
                replace("</pid>", "")
            print(process_id_for_kill)
            return process_id_for_kill
    return "no process found"
print(search_pid_in_unused_rndr_process())