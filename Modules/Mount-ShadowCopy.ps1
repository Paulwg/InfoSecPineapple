function Mount-ShadowCopy{

    [CmdletBinding()]
    Param(
        [Parameter()]
        [Alias("Remove Shadow Mount")]
        [switch]$Remove
    )
    Begin {}
    Process{
        if ($Remove){    
        
            try{
                #$s2.Delete() #<--To unmount the shadow copy/BROKEN
                [System.IO.Directory]::Delete('C:\shadowcopy') #<---To delete symlink    
            }
            catch{
                Write-Warning -Message "Failed because $($_.Exception.Message)"
            }
        }               
        else{
            try{
                $s1 = (Get-WmiObject -List Win32_ShadowCopy).Create("C:\", "ClientAccessible")
                $s2 = Get-WmiObject Win32_ShadowCopy | Where-Object { $_.ID -eq $s1.ShadowID }

                $d  = $s2.DeviceObject + "\"   # <-- this here

                cmd /c mklink /d C:\shadowcopy "$d"
           
            }catch{
                Write-Warning -Message "Failed to grab mount shadow copy because $($_.Exception.Message)"
            }                
        }
    }
    End {}
}
