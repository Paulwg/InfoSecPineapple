
#(creationTimeutc = BornTime,FNBORNTIME)
#(lastAccessTimeutc = AccessedTime,FNACCESSEDTIME)

function Parse-MFT_VSC{

    [CmdletBinding()]
    Param(
        [Parameter(Mandatory,ValueFromPipeline,ValueFromPipelineByPropertyName)]
        [Alias("FullName")]
        [string[]]$Path,

        #All for recursive directory, or specify extension
        [Parameter(ParameterSetName='Parameter Set 1')]
        [AllowNull()]
        [AllowEmptyCollection()]
        [AllowEmptyString()]
        [ValidateScript({$true})]
        [String]$Type,

        #Choose MFT or VSC if you don't want both
        [Parameter(ParameterSetName='Parameter Set 1')]
        [AllowNull()]
        [AllowEmptyCollection()]
        [AllowEmptyString()]
        [string]$Select
    )

    Begin {
    }
    Process {
     if ($Path,$Select -eq 'VSC')
        {
            $Path | ForEach-Object -Process {
            $sPath =  $_
            try{
                Get-ItemProperty -Path $sPath | select -Property Name,LastAccessTimeUtc,LastWriteTimeUtc | Out-File -FilePath $env:HOMEPATH\ShadowTimes.txt
            } catch {
                Write-Warning -Message "Failed to grab times from VSC because $($_.Exception.Message)"
            }
        }
    }
     if($Path,$Select -eq 'MFT')
        {
            $Path | ForEach-Object -Process {
                try{
                    Get-ForensicFileRecord -Path $_ | Select -Property Name,ModifiedTime,AccessedTime,ChangedTime,BornTime,FNModifiedTime,FNAccessedTime,FNChangedTime,FNBornTime | Out-File -FilePath $env:HOMEPATH\MFTtimes.txt
                } catch {
                    Write-Warning -Message "Failed to grab times from VSC because $($_.Exception.Message)"
                }
        }
    }
     if ($Path)
        {            
            $Path | ForEach-Object -Process {
            $sPath =  $_            
            try {
                    Get-ItemProperty -Path $sPath | select -Property Name,LastAccessTimeUtc,LastWriteTimeUtc | Out-File -FilePath $env:HOMEPATH\ShadowTimes.txt                  
                    Get-ForensicFileRecord -Path $_ | Select -Property Name,ModifiedTime,AccessedTime,ChangedTime,BornTime,FNModifiedTime,FNAccessedTime,FNChangedTime,FNBornTime | Out-File -FilePath $env:HOMEPATH\MFTtimes.txt
                } catch {
                    Write-Warning -Message "Failed to grab times from $sPath because $($_.Exception.Message)"
                }
            }          
         }     
     if ($Path, $Type)
        {
            $Path | ForEach-Object -Process {
                    $sPath =  $_            
                    if ($Type -match "All")
                        {
                            try {
                                Get-ItemProperty -Path $sPath\* | select -Property Name,LastAccessTimeUtc,LastWriteTimeUtc | Out-File -filepath $env:HOMEPATH\ShadowTimes.txt
                                gci $sPath | foreach{Get-ForensicFileRecord -Path ($_).FullName | Select -Property Name,ModifiedTime,AccessedTime,ChangedTime,BornTime,FNModifiedTime,FNAccessedTime,FNChangedTime,FNBornTime} | Out-File -FilePath $env:HOMEPATH\MFTtimes.txt
                            } catch {
                                Write-Warning -Message "Failed to grab times from $sPath because $($_.Exception.Message)"
                            }
                        } 
                           
                }
        }
    }

    End {}

}
