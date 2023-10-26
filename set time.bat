set year=%date:~0,4%
set month=%date:~5,2%
set day=%date:~8,2%
if %time:~0,2% lss 10 (
    set hour=0%time:~1,1%
) else (
    set hour=%time:~0,2%
)
set min=%time:~3,2%