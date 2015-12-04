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
* Implemeted and tested on Linux

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

# Close connections and cleanup
p.cleanup()
```
The most significant difference is how both tools handle the output. Native pmrep produces a human readable, machine unfriendly output with a lot of additional "noise" that blurs the desired information. The data is often delivered in an incosistent manner (example: blanks or commas as field delimiters).
_infa_ takes a different approach. The focus is to deliver the results in an API friendly way. The irrelevant data is removed from the output and the requested information is provided in an easy-to-parse and consistent format.

For detailed documentation please refer to the wiki pages.

## Installation

_To do._

## Road Map / State of play

_infa_ is a work-in-progres. Below is an overview of features currently implemented and reasoning behind not implementing others.

### Pmrep

| pmrep Command                       | Pmrep Class method                 | Implemented? | Comment  |
| ------------------------------------|------------------------------------|:------------:|----------|
| AddToDeploymentGroup                |                                    | ✘            |          |
| ApplyLabel                          |                                    | ✘            |          |
| AssignPermission                    |                                    | ✘            |          |
| BackUp                              |                                    | ✘            |          |
| ChangeOwner                         |                                    | ✘            |          |
| CheckIn                             |                                    | ✘            |          |
| CleanUp                             | cleanup                            | ✅            |          |
| ClearDeploymentGroup                |                                    | ✘            |          |
| Connect                             | \_\_init\_\_                       | ✅            |Used implicitly when class instance is created|
| Create                              |                                    | ✘            |          |
| CreateConnection                    |                                    | ✘            |          |
| CreateDeploymentGroup               |                                    | ✘            |          |
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
| ListTablesBySess                    |                                    | ✘            |          |
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
| UpdateStatistics                    |                                    | ✘            |          |
| UpdateTargPrefix                    |                                    | ✘            |          |
| Upgrade                             |                                    | ✘            |          |
| UninstallAbapProgram                |                                    | ✘            |          |
| Validate                            |                                    | ✘            |          |
| Version                             |                                    | ✘            |          |

### Pmcmd

_Comming up._

### Authors

infa was created and is being developed (krzysztof.radecki/gmail/com) by Krzysztof Radecki. Contributions from other developers are most welcome and will be credited.

### License

[GPL License](/LICENSE)
