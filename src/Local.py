from subprocess import Popen, PIPE, STDOUT

class Local(object):
    '''
    Local PowerShell commands and queries.
    '''
    #universal_newlines required in order to feed type bytes into redirector in Pineapplegedon
    cmd = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden'

    def AppCompatCache():
        pass
    
    def Process_Table():
        proc = Popen(Local.cmd,stdin=PIPE,stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = proc.communicate(input='get-process')
        print(stdout)
        while proc.returncode is None:
            proc.poll()
    
    def Prefetch():        
        pass
    
    def Network_Connections():
        proc = Popen(Local.cmd,stdin=PIPE,stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = proc.communicate(input='get-nettcpconnection')
        print(stdout)
        while proc.returncode is None:
            proc.poll()
            
    def Auto_Runs():
        pass
    
    def Sched_Tasks():
        pass
    
    def Startup_Folders():
        pass
    
    def Services():
        proc = Popen(Local.cmd,stdin=PIPE,stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = proc.communicate(input='get-service')
        print(stdout)
        while proc.returncode is None:
            proc.poll()
        
    def Installed_Software():
        pass
    
    def Unsigned_Executables():
        pass
    
    def Installed_Drivers():
        pass
    
    def ADS():
        pass
    
    def Dir_Walk():
        pass
    
    def VSC_Walk_Timestamps():
        pass
    
    def MFT_timestamps():
        pass
    
