import os
import string
import infa.helper
from infa.exceptions import InfaPmrepError

class Pmrep(object):
    """
    Class for interacting with Informatica PowerCenter repository using the pmrep binary.

    It tries to implement a pythonic-API while at the same time introducing as little changes
    as possible to the already known and well documented Informatica pmrep commands.

    All of the implemented methods are named the same, as their pmrep counterparts
    the only difference being changing of naming to lowercase, instead of retaining
    the original CamelCase.

    If a pmrep command requires flags, the counterpart method implements the same flags
    as **kwargs.
    """
    def __init__(self, pmrep, **params):
        self.pmrep = pmrep
        if not (os.path.isfile(self.pmrep) and os.access(self.pmrep, os.X_OK)):
            raise InfaPmrepError("%s is not the correct path to pmrep binary" % self.pmrep)

        opts_args = ['r', 'h', 'o', 'n', 's', 'x', 'u', 't']
        opts_flags = []

        command = [self.pmrep, 'connect']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def addtodeploymentgroup(self):
        """
        Add objects to a deployment group.
        """
        command = [self.pmrep, 'addtodeploymentgroup']
        pass

    def applylabel(self):
        """
        Apply a label to an object or a set of objects in a folder.
        """
        command = [self.pmrep, 'applylabel']
        pass

    def assignpermission(self, **params):
        """
        Add, remove or update permissions on a global object for a user,
        group, or the Others default group.

        Args (all to be supplied as kwargs):
            o (str): object type
            t (str): object subtype
            n (str): object name
            u (str): user name
            g (str): group name
            s (str): security domain
            p (str): permission (r, w, x or a combination of those)
        """
        if ('u' in params.keys()) and ('g' in params.keys()):
            raise InfaPmrepError("both [u] and [g] options supplied. Only one allowed.")

        opts_args = ['o', 't', 'n', 'u', 'g', 's', 'p']
        opts_flags = []

        command = [self.pmrep, 'assignpermission']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def backup(self, **params):
        """
        Backup the repository to the specified file.

        Args:
            o (str): output file name
            d (Optional[str]): dscription
            f (Optional[bool]): overwrite existing output file. Default False.
            b (Optional[bool]): skip workflow and session logs. Default False
            j (Optional[bool]): skip deployment group history. Default False.
            q (Optional[bool]): skip MX data. Default False.
            v (Optional[bool]): skip task statistics. Default False.
        """
        opts_args = ['o', 'd']
        opts_flags = ['f', 'b', 'j', 'q', 'v']

        command = [self.pmrep, 'backup']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def changeowner(self, **params):
        """
        Change the owner name for a global object.
        
        Args:
            o (str): object type. Valid are 'folder', 'label', 'deploymentgroup',
                'query' and 'connection'
            t (Optional[str]): object subtype. Valid only for query and
                connection objects
            n (str): object name
            u (str): new owner name
            s (str): security domain
        """
        opts_args = ['o', 't', 'n', 'u', 's']
        opts_flags = []
        
        command = [self.pmrep, 'changeowner']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def checkin(self, **params):
        """
        Check in an object that has been checked out.
        
        Args:
            o (str): object type
            t (Optional[str]): object subtype
            n (str): object name
            f (str): folder name
            c (Optional[str]): comments
            s (Optional[str]): dbd separator. Relevnt if ODBC source has a period ('.')
                in the name
        """
        opts_args = ['o', 't', 'n', 'f', 'c', 's']
        opts_flags = []
        
        command = [self.pmrep, 'checkin']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def cleanup(self):
        """
        Close the repository connection and clenup (remove the pmrep.cnx file).

        Args:
            None
        """
        command = [self.pmrep, 'cleanup']

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def cleardeploymentgroup(self, **params):
        """
        Clear all objects from a deployment group while retaining the
        group itself.
        
        Args:
            p (str): deployment group name
        """
        opts_args = ['p']
        opts_flags = []
        
        command = [self.pmrep, 'cleardeploymentgroup', '-f']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def create(self, **params):
        """
        Creates the repository tables in the database.
        
        Note:
            Requires the repository to be running in exclusive mode.
            
        Args:
            u (str): domain user name
            s (Optional[str]): domain user security domain. Default is Native.
            p (str): domain password
            g (bool): promote repository to global repository
            v (bool): enable version control
        """
        opts_args = ['u', 's', 'p']
        opts_flags = ['g', 'v']
        
        command = [self.pmrep, 'create']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def createconnection(self):
        """
        Create a source or target connection in the repository.
        """
        command = [self.pmrep, 'createconnection']
        pass

    def createdeploymentgroup(self, **params):
        """
        Create a static or dynamic deployment group.
        
        Args (all to be supplied as kwargs):
            p (str): Required. Deployment group name.
            t (str): Optional. Deployment group type ('static' or 'dynamic').
                Default is static.
            q (str): Required if the deployment groupy is dynamic. Query name.
            u (str): Required if the deployment groupy is dynamic. Valid values 
                are 'shared' or 'personal'.
            c (str): Optional. Comments
        """
        opts_args = ['p', 't', 'q', 'u', 'c']
        opts_flags = []
        
        command = [self.pmrep, 'createdeploymentgroup']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def createfolder(self, **params):
        """
        Create a folder in the repository.

        Args (all to be supplied as kwargs):
            n (str): folder name
            d (Optional[str]): folder description
            o (Optional[str]): owner name. Default is user creating the folder
            a (Optional[str]): owner security domain. Required for LDAP owners.
                Default is Native.
            s (Optional[bool]): shared folder. Default False
            p (Optional[str]): permissions (unix style octal). By default the
                the Repository Service assigns permissions.
            f (Optional[str]): folder status
        """
        opts_args = ['n', 'd', 'o', 'a', 'p', 'f']
        opts_flags = ['s']

        command = [self.pmrep, 'createfolder']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def createlabel(self, **params):
        """
        Create a label that can be used to associate groups of objects during
        development.

        Args (all to be supplied as kwargs):
            a (str): name of label to be created in the repository
            c (Optional[str]): comment about the label
        """
        opts_args = ['a', 'c']
        opts_flags = []

        command = [self.pmrep, 'createlabel']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def delete(self):
        """
        Delete the repository tables from the repository database.
        """
        command = [self.pmrep, 'delete']
        pass

    def deleteconnection(self):
        """
        Delete a relational connection from the repository.
        """
        command = [self.pmrep, 'deleteconnection']
        pass

    def deletedeploymentgroup(self):
        """
        Delete a deployment group.
        """
        command = [self.pmrep, 'deletedeploymentgroup']
        pass

    def deletefolder(self, **params):
        """
        Delete a folder from the repository.

        Args:
            n (str): folder name
        """
        opts_args = ['n']
        opts_flags = []

        command = [self.pmrep, 'deletefolder']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def deletelabel(self, **params):
        """
        Delete a label and remove the label from all objects that use it.

        This method by default uses the '-f' pmrep flag to avoid user
        interaction.

        Args (all to be supplied as kwargs):
            a (str): name of the label to be deleted in the repository
        """
        opts_args = ['a']

        command = [self.pmrep, 'deletelabel', '-f']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def deleteobject(self):
        """
        Delete an object.
        """
        command = [self.pmrep, 'deleteobject']
        pass

    def deploydeploymentgroup(self):
        """
        Deploy a deployment group.
        """
        command = [self.pmrep, 'deploydeploymentgroup']
        pass

    def deployfolder(self):
        """
        Deploy a folder.
        """
        command = [self.pmrep, 'deployfolder']
        pass

    def executequery(self):
        """
        Run a repository query.
        """
        command = [self.pmrep, 'executequery']
        pass

    def findcheckout(self):
        """
        Display a list of checked out objects in the repository.
        """
        command = [self.pmrep, 'findcheckout']
        pass

    def getconnectiondetails(self):
        """
        List the properties and attributes of a connection object as name-value pairs.
        """
        command = [self.pmrep, 'getconnectiondetails']
        pass

    def listconnections(self):
        """
        List all connection objects in the repository and their respective connection types.

        Args:
            None
        """
        column_separator = ','
        command = [self.pmrep, 'listconnections', '-t']

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)
        return infa.helper.format_output(pmrep_output, column_separator)

    def listobjectdependencies(self):
        """
        List dependency objects for reusable and non-reusable objects.
        """
        command = [self.pmrep, 'listobjectdependencies']
        pass

    def listobjects(self, **params):
        """
        Return a list of objects in the repository.

        Args (all to be supplied as kwargs):
            o (str): object type
            t (str): object subtype
            f (str): folder name
            r (str): end-of-record separatr
            l (str): end-of-listing separator
            s (str): dbd separator

            Refer to Informatica Command reference Handbook for details.

        Returns:
            List of Lists
        """
        opts_args = ['o', 't', 'f', 'r', 'l', 's']
        opts_flags = []

        column_separator = '<=#CS#=>'
        command = [self.pmrep, 'listobjects', '-c', column_separator]
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)
        return infa.helper.format_output(pmrep_output, column_separator)

    def listtablesbysess(self, **params):
        """
        Return a list of sources or targets used in a session.

        Args:
            f (str): folder name
            s (str): session name (non-reusable must include workflow name)
            t (str): object type listed ('session' or 'target')

        Note:
            If a mapping contains a mapplet, its name will also be returned
        """
        opts_args = ['f', 's', 't']
        opts_flags = []

        column_separator = '.'
        command = [self.pmrep, 'listtablesbysess']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)
        return infa.helper.format_output(pmrep_output, column_separator)

    def listuserconnections(self):
        """
        List information for each user connected to the repository.
        """
        command = [self.pmrep, 'listuserconnections']
        pass


    def massupdate(self):
        """
        Update session properties for a set of sessions that meet specified conditions.
        """
        command = [self.pmrep, 'massupdate']
        pass


    def modifyfolder(self):
        """
        Modify folder properties in a non-versioned repository.
        """
        command = [self.pmrep, 'modifyfolder']
        pass


    def notify(self):
        """
        Sends notification messages to users connected to a repository or users connected
        to all repositories managed by a Repository Service.
        """
        command = [self.pmrep, 'notify']
        pass


    def objectexport(self):
        """
        Exports objects to an XML file defined by the powrmart.dtd file.
        """
        command = [self.pmrep, 'objectexport']
        pass


    def objectimport(self):
        """
        Imports objects from an XML file.
        """
        command = [self.pmrep, 'objectimport']
        pass


    def purgeversion(self):
        """
        Purge object versions from the repository database.
        """
        command = [self.pmrep, 'purgeversion']
        pass


    def register(self):
        """
        Register a local repository with a connected global repository.
        """
        command = [self.pmrep, 'register']
        pass


    def registerplugin(self):
        """
        Register an external plug-in to a repository.
        """
        command = [self.pmrep, 'registerplugin']
        pass


    def restore(self):
        """
        Restore a repository backup file to a database.
        """
        command = [self.pmrep, 'restore']
        pass


    def rollbackdeployment(self):
        """
        Roll back a deployment to purge deployed versions of objects from the target repository.
        """
        command = [self.pmrep, 'rollbackdeployment']
        pass


    def run(self):
        """
        Open a script file containing multiple pmrep commands, read each command, and run them.
        """
        command = [self.pmrep, 'run']
        pass


    def showconnectioninfo(self):
        """
        Return the repository name and user information for the current connection.
        """
        command = [self.pmrep, 'showconnectioninfo']
        pass


    def switchconnection(self):
        """
        Change the name of an existing connection.
        """
        command = [self.pmrep, 'switchconnection']
        pass

    def truncatelog(self):
        """
        Delete details from the repository. You can delete all logs, or delete logs for a folder or workflow.
        """
        command = [self.pmrep, 'truncatelog']
        pass

    def undocheckout(self):
        """
        Reverses the checkout of an object.
        """
        command = [self.pmrep, 'undocheckout']
        pass


    def unregister(self):
        """
        Unregisters a local repository from a connected global repository.
        """
        command = [self.pmrep, 'unregister']
        pass


    def unregisterplugin(self):
        """
        Removes a plug-in from a repository.
        """
        command = [self.pmrep, 'unregisterplugin']
        pass


    def updateconnection(self):
        """
        Updates the user name, password, connect string, and attributes for a database connection.
        """
        command = [self.pmrep, 'updateconnection']
        pass

    def updateemailaddr(self):
        """
        Updates the session notification email addresses associated with the Email tasks
        assigned to the session.
        """
        command = [self.pmrep, 'updateemailaddr']
        pass

    def updateseqgenvals(self):
        """
        Updates one or more of the following properties for the specified Sequence Generator transformation:
         - Start Value
         - End Value
         - Increment By
         - Current Value
        """
        command = [self.pmrep, 'updateseqgenvals']
        pass

    def updatesrcprefix(self):
        """
        Updates the owner name for session source tables.
        """
        command = [self.pmrep, 'updatesrcprefix']
        pass

    def updatestatistics(self):
        """
        Update statistics for repository tables and indexes.

        Args:
            None
        """
        command = [self.pmrep, 'updatestatistics']
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def updatetargprefix(self):
        """
        Update the table name prefix for session target tables.
        """
        command = [self.pmrep, 'updatetargprefix']
        pass

    def upgrade(self):
        """
        Upgrade a repository to the latest version.
        """
        command = [self.pmrep, 'upgrade']
        pass

    def uninstallabapprogram(self):
        """
        Uninstalls the ABAP program.
        """
        command = [self.pmrep, 'uninstallabapprogram']
        pass

    def validate(self):
        """
        Validates objects.
        """
        command = [self.pmrep, 'validate']
        pass

    def version(self):
        """
        Displays the PowerCenter version and Informatica trademark and copyright information.
        """
        command = [self.pmrep, 'version']
        pass
