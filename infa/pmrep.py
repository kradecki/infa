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

    def __default_io_command(self, pmrep_command, opts_args, opts_flags, params, column_separator='.'):
        command = [self.pmrep]
        if isinstance(pmrep_command, list):
         command.extend(pmrep_command)
        else:
         command.append(pmrep_command)

        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)
        return infa.helper.format_output(pmrep_output, column_separator)

    def addtodeploymentgroup(self, **params):
        """
        Add objects to a deployment group.
        
        Args (all to be supplied as kwargs):
            p (str): Required. Deployment group name.
            n (str): Required if adding a specific object. Object name.
            o (str): Required if adding a specific object. Object type.
            t (str): Required when using valid subtypes. Object subtype.
            v (str): Optional. Version number. Default is latest version.
            f (str): Required if adding a specific object. Folder name.
            i (str): Required if not using [n], [o] and [f]. Persistant
                input file.
            d (str): Optional. DBD Separator.
            
            Refer to Informatica Command reference Handbook for details.
        """
        opts_args = ['p', 'n', 'o', 't', 'v', 'f', 'i', 'd']
        opts_flags = []
        
        command = [self.pmrep, 'addtodeploymentgroup']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def applylabel(self, **params):
        """
        Apply a label to an object or a set of objects in a folder.
        
        Args (all to be supplied as kwargs):
            a (str): Required. Label name.
            n (str): Required if adding a specific object. Object name.
            o (str): Required if adding a specific object. Object type.
            t (str): Required when using valid subtypes. Object subtype.
            v (str): Optional. Version number. Default is latest version.
            f (str): Optional. Folder name.
            i (str): Required if not using [n], [o] and [f]. Persistant
                input file.
            d (str): Optional. Dependency object types.
            p (str): Optional. Dependency direction.
            s (bool): Optional. Include PK-FK depenency objects.
            g (bool): Optional. Find dependencies across repositories.
            m (bool): Optional. Move label to the latest version.
            c (str): Optional. Comments.
            e (str): Optional. DBD Separator.
        
            Refer to Informatica Command reference Handbook for details.
        """
        opts_args = ['a', 'n', 'o', 't', 'v', 'f', 'i', 'd', 'p', 'c', 'e']
        opts_flags = ['s', 'g', 'm']
        
        command = [self.pmrep, 'applylabel']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))
        
        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def assignpermission(self, **params):
        """
        Add, remove or update permissions on a global object for a user,
        group, or the Others default group.

        Args (all to be supplied as kwargs):
            o (str): Required. Object type.
            t (str): Optional. Object subtype, relevant only for connection
                object or query.
            n (str): Required. Object name.
            u (str): Required if [g] is not used. User name.
            g (str): Required if [u] is not used. Group name.
            s (str): Required only is LDAP authentication is in use. Security domain.
                Default is Native.
            p (str): Required. Permissions to be added, removed or updated.
                Valid values are 'r', 'w', 'x' or a combination of those.
            
            Refer to Informatica Command reference Handbook for details.
        """
        opts_args = ['o', 't', 'n', 'u', 'g', 's', 'p']
        opts_flags = []

        command = [self.pmrep, 'assignpermission']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def backup(self, **params):
        """
        Backup the repository to the specified file.

        Args (all to be supplied as kwargs):
            o (str): Required. Output file name.
            d (str): Optional. Description.
            f (bool): Optional. Overwrite existing output file. Default is False.
            b (bool): Optional. Skip workflow and session logs. Default is False
            j (bool): Optional. Skip deployment group history. Default is False.
            q (bool): Optional. Skip MX data. Default is False.
            v (bool): Optional. Skip task statistics. Default is False.
            
            Refer to Informatica Command reference Handbook for details.
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

        Args (all to be supplied as kwargs):
            o (str): Required. Object type. Valid values are 'folder', 'label',
                'deploymentgroup', 'query' and 'connection'.
            t (str): Optional. Object subtype, relevant only for connection
                object or query.
            n (str): Required. Object name.
            u (str): Required. New owner name.
            s (str): Required only is LDAP authentication is in use. Security domain.
                Default is Native.
            
            Refer to Informatica Command reference Handbook for details.
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

        Args (all to be supplied as kwargs):
            o (str): Required. Object type.
            t (str): Required for task or transformation type. Object subtype.
            n (str): Required. Object name.
            f (str): Required. Folder name.
            c (str): Optional. Comments.
            s (str): Optional. DBD separator. Relevant if ODBC source has a
                period ('.') in its name.
            
            Refer to Informatica Command reference Handbook for details.
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
            
            Refer to Informatica Command reference Handbook for details.
        """
        command = [self.pmrep, 'cleanup']

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def cleardeploymentgroup(self, **params):
        """
        Clear all objects from a deployment group while retaining the
        group itself.

        Args (all to be supplied as kwargs):
            p (str): Required. Deployment group name.
            
            Refer to Informatica Command reference Handbook for details.

        Note:
            The [-f] flag (force) is automatically submitted to avoid user
            interaction.
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

        Args (all to be supplied as kwargs):
            u (str): Required. Domain user name.
            s (str): Required only is LDAP authentication is in use. Security domain.
                Default is Native.
            p (str): Required. Domain password.
            g (bool): Optional. Promote repository to global repository.
                Default is False.
            v (bool): Optional. Enable version control. Default is False.
            
            Refer to Informatica Command reference Handbook for details.
        """
        opts_args = ['u', 's', 'p']
        opts_flags = ['g', 'v']

        command = [self.pmrep, 'create']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

    def createconnection(self, **params):
        """
        Create a source or target connection in the repository.
        
        Args (all to be supplied as kwargs):
            s (str): Required. Connection type.
            n (str): Required. Connection name.
            u (str): Required for some connection types. User name.
            p (str): Required for some connection types. Password.
            P (str): Optional. Password environment variable.
            K (str): Optional. Connection to the Kerberos server.
            c (str): Required. Connect string.
            l (str): Required for some connection types. Code page.
            r (str): Optional for Oracle connections. Rollback segment.
            e (str): Optional. Connection environment SQL.
            f (str): Optional. Transaction environment SQL.
            z (str): Optional for Sybase ASE and MSSQL. Packet size.
            b (str): Optional for Sybase ASE and MSSQL. Database name.
            v (str): Optional for Sybase ASE and MSSQL. Database name.
            d (str): Optional for MSSQL. Domain name.
            t (bool): Optional for MSSQL. Integration Service uses Windows
                authentication to access MSSQL database.
            a (str): Optional for Teradata. ODBC data source name.
            x (bool): Optional. Enable enhanced security.
            k (str): Optional. Enable user defined connection attributes.
        
            Refer to Informatica Command reference Handbook for details.
        """
        opts_args = ['s', 'n', 'u', 'p', 'P', 'K', 'c', 'l', 'r', 'e', 'f', 'z', 'b', 'v', 'd', 'a', 'k']
        opts_flags = ['t', 'x']
        
        command = [self.pmrep, 'createconnection']
        command.extend(infa.helper.cmd_prepare(params, opts_args, opts_flags))

        pmrep_output = infa.helper.cmd_execute(command)
        infa.helper.cmd_status(command, pmrep_output)

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

        Args (all to be supplied as kwargs):
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

    def listobjectdependencies(self, **params):
        """
        List dependency objects for reusable and non-reusable objects.
        """
        col_sep = '<=#CS#=>'
        return self.__default_io_command(['listobjectdependencies', '-c', col_sep], ['n', 'o', 't', 'v', 'f', 'i', 'd', 'p', 'u', 'r', 'l', 'b', 'e'], ['s', 'g', 'a'], params, col_sep)

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

        Args (all to be supplied as kwargs):
            f (str): folder name
            s (str): session name (non-reusable must include workflow name)
            t (str): object type listed ('session' or 'target')

        Note:
            If a mapping contains a mapplet, its name will also be returned as
            the first element of a list holding the session's name.
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


    def objectexport(self, **params):
        """
        Exports objects to an XML file defined by the powrmart.dtd file.
        """
        return self.__default_io_command('objectexport', ['n', 'o', 't', 'v', 'f', 'i', 'u', 'l', 'e'], ['m', 's', 'b', 'r'], params)

    def objectimport(self, src_folder, src_repo, tgt_folder, tgt_repo, **params):
        """
        Imports objects from an XML file.
        """
        if 'c' not in params:
            infa.helper.create_import_control_xml('impcntl.xml', src_folder, src_repo, tgt_folder, tgt_repo, 
                 dtd=os.path.join(os.path.dirname(self.pmrep), 'impcntl.dtd'))
            params['c'] = 'impcntl.xml'

        return self.__default_io_command('objectimport', ['i', 'c', 'l'], ['p'], params)

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

    def validate(self, **params):
        """
        Validates objects.
        """
        return self.__default_io_command('validate', ['n', 'o', 'v', 'f', 'i', 'm', 'p', 'u'], ['s', 'k', 'a', 'b'], params)

    def version(self):
        """
        Displays the PowerCenter version and Informatica trademark and copyright information.
        """
        command = [self.pmrep, 'version']
        pass
