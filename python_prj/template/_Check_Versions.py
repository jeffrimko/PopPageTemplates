##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import verace

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

VERCHK = verace.VerChecker("{{long_name}}", __file__)
VERCHK.include(r"{{prj_type}}\setup.py", match="version = ", splits=[('"',1)])
VERCHK.include(r"CHANGELOG.adoc", match="{{short_name}}-", splits=[("-",1),(" ",0)], updatable=False)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    VERCHK.prompt()
