from subprocess import Popen, PIPE, STDOUT

class Local(object):
    '''
    Local PowerShell commands and queries.
    '''
    def AppCompatCache():
        pass
    def Process_Table():
        cmd = 'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe -windowstyle hidden'
        p = Popen(cmd,stdin=PIPE,stdout=PIPE, stderr=PIPE, universal_newlines=True)#universal_newlines required in order to feed type bytes into redirector in Pineapplegedon
        stdout, stderr = p.communicate(input='get-process')
        return(stdout)
    def Prefetch():
        pass
    def Network_Connections():
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","get-nettcpconnection"])
    def Auto_Runs(self):
        pass
    def Sched_Tasks(self):
        pass
    def Startup_Folders(self):
        pass
    def Services(self):
        subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe","get-services"])
    def Installed_Software(self):
        pass
    def Unsigned_Executables(self):
        pass
    def Installed_Drivers(self):
        pass
    def ADS(self):
        pass
    def Dir_Walk(self):
        pass
    def VSC_Walk_Timestamps(self):
        pass
    def MFT_timestamps(self):
        pass
