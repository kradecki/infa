# infa

**_infa_** is the missing link between Informatica PowerCenter and Python. It creates a wrapper around PowerCenter's Command Line Tools (pmrep, pmcmd) and handles the communication to and output from those tools.

Why use infa?
* no native Python API provided by Informatica Corp. itself
* native PowerCenter command line tools are user focused and provide an output which is difficult to parse programmatically
* _infa_ focuses on API: output is provided in a machine friendly way (for example: lists)
* easy to grasp for seasoned Informatica developers and administrators

## Requirements

* Python 2.x (implemented and tested on 2.7.5)
* Informatica command line tools (pmrep, pmcmd) installed on the same machine
* Implemented and tested on Linux

## Usage

Each Informatica command line tool is implemented as a Python class and the tool specific commands are designed as class methods.
The following example compares the usage of the native pmrep command line tool and infa's Pmrep class.

Shell:
```sh
# Connect to Informatica Repository
$ /opt/informatica/9.6.1/server/bin/pmrep Connect -r Repository_Name -h localhost -o 6005 -n admin -x secret_password

# Get a list of all aggregator transformations in the "Demo" folder
$ /opt/informatica/9.6.1/server/bin/pmrep ListObjects -o transformation -t aggregator -f Demo

# Close connections and cleanup
$ /opt/informatica/9.6.1/server/bin/pmrep Cleanup
```
The native command calls result with the following output:
```
(...)

Informatica(r) PMREP, version [9.6.1 HotFix3], build [990.0611], LINUX 64-bit
Copyright (c) Informatica Corporation 1994 - 2015
All Rights Reserved.
This Software is protected by U.S. Patent Numbers 5,794,246; 6,014,670; 6,016,501; 6,029,178; 6,032,158; 6,035,307; 6,044,374; 6,092,086; 6,208,990; 6,339,775; 6,640,226; 6,789,096; 6,823,373; 6,850,947; 6,895,471; 7,117,215; 7,162,643; 7,243,110; 7,254,590; 7,281,001; 7,421,458; 7,496,588; 7,523,121; 7,584,422; 7,676,516; 7,720,842; 7,721,270; 7,774,791; 8,065,266; 8,150,803; 8,166,048; 8,166,071; 8,200,622; 8,224,873; 8,271,477; 8,327,419; 8,386,435; 8,392,460; 8,453,159; 8,458,230; 8,707,336; 8,886,617; and RE44,478, International Patents and other Patents Pending.

Invoked at Thu Dec 10 19:50:02 2015

SANDBOX_1
SANDBOX_2
SANDBOX_3
SANDBOX_4
SANDBOX_5
.listobjects completed successfully.

Completed at Thu Dec 10 19:50:07 2015
```

Python:
```Python
import infa

# Create Pmrep class instance and open a connection to the repository
p = infa.Pmrep(
    '/opt/informatica/9.6.1/server/bin/pmrep',
    r='Repository_Name',
    h='localhost',
    o='6005',
    n='admin',
    x='secret_password'
)

# Get a list of all aggregator transformations in the "Demo" folder
a = p.listobjects(o='transformation', t='aggregator', f='Demo')
print(a)

# Close connections and cleanup
p.cleanup()
```
The above code yields the following results:
```
[['SANDBOX_1'], ['SANDBOX_2'], ['SANDBOX_3'], ['SANDBOX_4'], ['SANDBOX_5']]
```

The most significant difference is how both tools handle the output. Native pmrep produces a human readable, machine unfriendly output with a lot of additional "noise" that blurs the desired information. The data is often delivered in an inconsistent manner (example: blanks or commas as field delimiters).
_infa_ takes a different approach. The focus is to deliver the results in an API friendly way. The irrelevant data is removed from the output and the requested information is provided in an easy-to-parse and consistent format.

For detailed documentation please refer to the wiki pages.

## Installation

_To do._

## Road Map / State of play

_infa_ is a work-in-progres. Below is an overview of features currently implemented and reasoning behind not implementing others.

### Pmrep

| pmrep Command                       | Pmrep Class method                 | Implemented? | Comment  |
| ------------------------------------|------------------------------------|:------------:|----------|
| AddToDeploymentGroup                | addtodeploymentgroup               | ✅            |          |
| ApplyLabel                          | applylabel                         | ✅            |          |
| AssignPermission                    | assignpermission                   | ✅            |          |
| BackUp                              | backup                             | ✅            |          |
| ChangeOwner                         | changeowner                        | ✅            |          |
| CheckIn                             | checkin                            | ✅            |          |
| CleanUp                             | cleanup                            | ✅            |          |
| ClearDeploymentGroup                | cleardeploymentgroup               | ✅            |          |
| Connect                             | \_\_init\_\_                       | ✅            |Used implicitly when class instance is created|
| Create                              | create                             | ✅            |          |
| CreateConnection                    | createconnection                   | ✅            |          |
| CreateDeploymentGroup               | createdeploymentgroup              | ✅            |          |
| CreateFolder                        | createfolder                       | ✅            |          |
| CreateLabel                         | createlabel                        | ✅            |          |
| Delete                              |                                    | ✘            |          |
| DeleteConnection                    |                                    | ✘            |          |
| DeleteDeploymentGroup               |                                    | ✘            |          |
| DeleteFolder                        | deletefolder                       | ✅            |          |
| DeleteLabel                         | deletelabel                        | ✅            |          |
| DeleteObject                        |                                    | ✘            |          |
| ExecuteQuery                        |                                    | ✘            |          |
| Exit                                |                                    | ✘            |No interactive mode planned|
| FindCheckout                        |                                    | ✘            |          |
| GetConnectionDetails                |                                    | ✘            |          |
| GenerateAbapProgramToFile           |                                    | ✘            |          |
| Help                                |                                    | ✘            |Not supported|
| InstallAbapProgram                  |                                    | ✘            |          |
| KillUserConnection                  |                                    | ✘            |          |
| ListConnections                     | listconnections                    | ✅            |          |
| ListObjectDependencies              |                                    | ✘            |          |
| ListObjects                         | listobjects                        | ✅            |          |
| ListTablesBySess                    | listtablesbysess                   | ✅            |          |
| ListUserConnections                 |                                    | ✘            |          |
| MassUpdate                          |                                    | ✘            |          |
| ModifyFolder                        |                                    | ✘            |          |
| Notify                              |                                    | ✘            |          |
| ObjectExport                        |                                    | ✘            |          |
| ObjectImport                        |                                    | ✘            |          |
| PurgeVersion                        |                                    | ✘            |          |
| Register                            |                                    | ✘            |          |
| RegisterPlugin                      |                                    | ✘            |          |
| Restore                             |                                    | ✘            |          |
| RollbackDeployment                  |                                    | ✘            |          |
| Run                                 |                                    | ✘            |          |
| ShowConnectionInfo                  |                                    | ✘            |          |
| SwitchConnection                    |                                    | ✘            |          |
| TruncateLog                         |                                    | ✘            |          |
| UndoCheckout                        |                                    | ✘            |          |
| Unregister                          |                                    | ✘            |          |
| UnregisterPlugin                    |                                    | ✘            |          |
| UpdateConnection                    |                                    | ✘            |          |
| UpdateEmailAddr                     |                                    | ✘            |          |
| UpdateSeqGenVals                    |                                    | ✘            |          |
| UpdateSrcPrefix                     |                                    | ✘            |          |
| UpdateStatistics                    | updatestatistics                   | ✅            |          |
| UpdateTargPrefix                    |                                    | ✘            |          |
| Upgrade                             |                                    | ✘            |          |
| UninstallAbapProgram                |                                    | ✘            |          |
| Validate                            |                                    | ✘            |          |
| Version                             |                                    | ✘            |          |

### Pmcmd

_Comming up._

### Authors

_infa_ was created and is being developed by Krzysztof Radecki (krzysztof.radecki/gmail/com). Contributions from other developers are most welcome and will be credited to them.

### License

[GPL License](/LICENSE)
