set year=%date:~0,4%
set month=%date:~5,2%
set day=%date:~8,2%
set hour=%time:~0,2%
set min=%time:~3,2%

if %hour% lss 10 (
    set /a hour=0%time:~0,2%
)