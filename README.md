# infa

infa is the missing link between Informatica Platform and Python. It creates a wrapper around Informatica's Command Line Tools and handles the communication to and output from the tools.

Why use infa?
* no native Python support provided by Informatica itself
* native command line tools are user focused and provide an output which is difficult to parse
* infa focuses on API: output is provided in a machine friendly way (i.e. lists)
* easy to grasp for seasoned Informatica developers and administrators

## Requirements

* Python 2.x (at least 2.6.6)
* Informatica command line tools installed on the same machine
* Linux

## Usage

Each Informatica command line tool is implemented as a Python class and the tool specific commands are designed as class methods.
The following example compares the usage of the pmrep command line tool and the Pmrep class.

```sh
# Connect to Informatica Repository
$ /opt/informatica/9.6.1/server/bin/pmrep Connect -r Repository_Name -h localhost -o 6005 -n admin -x secret_password

# Get a list of all aggregator transformations in the "Demo" folder
$ /opt/informatica/9.6.1/server/bin/pmrep ListObjects -o transformation -t aggregator -f Demo

# Close connections and cleanup
$ /opt/informatica/9.6.1/server/bin/pmrep Cleanup
```

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
The most significant difference is how the two tools handle the output. Native pmrep produces a human readable, machine unfreiendly output with a lot of additional information that blurs the output.
infa handl

For detailed documentation please refer to the wiki pages.

## Installation

To-Do

## Road Map / State of play

infa ist currently a work in progres. Below is an overview of features currently implemented and reasoning behind not implementing others.

### Pmrep

| pmrep Command                       | Pmrep Class method                 | Implemented? | Comment  |
| ------------------------------------|------------------------------------|:------------:|----------|
| AddToDeploymentGroup                |                                    | NO           |          |
| ApplyLabel                          |                                    | NO           |          |
| AssignPermission                    |                                    | NO           |          |
| BackUp                              |                                    | NO           |          |
| ChangeOwner                         |                                    | NO           |          |
| CheckIn                             |                                    | NO           |          |
| CleanUp                             | cleanup                            | YES          |          |
| ClearDeploymentGroup                |                                    | NO           |          |
| Connect                             | __init__                           | YES          |Used implicitly when class instance is created|
| Create                              |                                    | NO           |          |
| CreateConnection                    |                                    | NO           |          |
| CreateDeploymentGroup               |                                    | NO           |          |
| CreateFolder                        | createfolder                       | YES          |          |
| CreateLabel                         | createlabel                        | YES          |          |
| Delete                              |                                    | NO           |          |
| DeleteConnection                    |                                    | NO           |          |
| DeleteDeploymentGroup               |                                    | NO           |          |
| DeleteFolder                        | deletefolder                       | YES          |          |
| DeleteLabel                         | deletelabel                        | YES          |          |
| DeleteObject                        |                                    | NO           |          |
| ExecuteQuery                        |                                    | NO           |          |
| Exit                                |                                    | NO           |No interactive mode planned|
| FindCheckout                        |                                    | NO           |          |
| GetConnectionDetails                |                                    | NO           |          |
| RelationalGenerateAbapProgramToFile |                                    | NO           |          |
| Help                                |                                    | NO           |Not supported|
| InstallAbapProgram                  |                                    | NO           |          |
| KillUserConnection                  |                                    | NO           |          |
| ListConnections                     | listconnections                    | YES          |          |
| ListObjectDependencies              |                                    | NO           |          |
| ListObjects                         | listobjects                        | YES          |          |
| ListTablesBySess                    |                                    | NO           |          |
| ListUserConnections                 |                                    | NO           |          |
| MassUpdate                          |                                    | NO           |          |
| ModifyFolder                        |                                    | NO           |          |
| Notify                              |                                    | NO           |          |
| ObjectExport                        |                                    | NO           |          |
| ObjectImport                        |                                    | NO           |          |
| PurgeVersion                        |                                    | NO           |          |
| Register                            |                                    | NO           |          |
| RegisterPlugin                      |                                    | NO           |          |
| Restore                             |                                    | NO           |          |
| RollbackDeployment                  |                                    | NO           |          |
| Run                                 |                                    | NO           |          |
| ShowConnectionInfo                  |                                    | NO           |          |
| SwitchConnection                    |                                    | NO           |          |
| TruncateLog                         |                                    | NO           |          |
| UndoCheckout                        |                                    | NO           |          |
| Unregister                          |                                    | NO           |          |
| UnregisterPlugin                    |                                    | NO           |          |
| UpdateConnection                    |                                    | NO           |          |
| UpdateEmailAddr                     |                                    | NO           |          |
| UpdateSeqGenVals                    |                                    | NO           |          |
| UpdateSrcPrefix                     |                                    | NO           |          |
| UpdateStatistics                    |                                    | NO           |          |
| UpdateTargPrefix                    |                                    | NO           |          |
| Upgrade                             |                                    | NO           |          |
| UninstallAbapProgram                |                                    | NO           |          |
| Validate                            |                                    | NO           |          |
| Version                             |                                    | NO           |          |

### Pmcmd

Comming up.
