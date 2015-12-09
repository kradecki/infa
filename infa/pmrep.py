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

        opts_r = ['r', 'h', 'o', 'n', 's', 'x', 'u', 't']
        opts_q = []
        opts_b = []

        command = [self.pmrep, 'connect']
        command.extend(infa.helper.cmd_prepare(params, opts_r, opts_q, opts_b))

        pmrep_output = infa.helper.cmd_execute(command)
        if not "connect completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise InfaPmrepError("connection to repository failed using %s" % " ".join(command))

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

        options_allowed = ['o', 't', 'n', 'u', 'g', 's', 'p']
        command = [self.pmrep, 'assignpermission']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, value])
            else:
                raise InfaPmrepError("unsupported assignpermission option: %s" % key)

        pmrep_output = infa.helper.cmd_execute(command)
        if not "assignpermission completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise InfaPmrepError("execution of assignpermission failed using %s" % " ".join(command))

    def backup(self, **params):
        """
        Backup the repository to the specified file.
        """
        options_allowed = ['o']
        options_allowed_quote = ['d']
        options_allowed_bool = ['f', 'b', 'j', 'q', 'v']

        command = [self.pmrep, 'backup']
        command.extend(infa.helper.cmd_prepare(params, options_allowed, options_allowed_quote, options_allowed_bool))
        print command

    def changeowner(self):
        """
        Change the owner name for a global object.
        """
        command = [self.pmrep, 'changeowner']
        pass

    def checkin(self):
        """
        Check in an object that has been checked out.
        """
        command = [self.pmrep, 'checkin']
        pass

    def cleanup(self):
        """
        Close the repository connection and clenup (remove the pmrep.cnx file).

        Args:
            None

        Returns:
            None
        """
        command = [self.pmrep, 'cleanup']
        pmrep_output = infa.helper.cmd_execute(command)

    def cleardeploymentgroup(self):
        """
        Clear all objects from a deployment group.
        """
        command = [self.pmrep, 'cleardeploymentgroup']
        pass

    def create(self):
        """
        Creates the repository tables in the database.
        """
        command = [self.pmrep, 'create']
        pass

    def createconnection(self):
        """
        Create a source or target connection in the repository.
        """
        command = [self.pmrep, 'createconnection']
        pass

    def createdeploymentgroup(self):
        """
        Create a static or dynamic deployment group.
        """
        command = [self.pmrep, 'createdeploymentgroup']
        pass

    def createfolder(self, **params):
        """
        Create a folder in the repository.

        Args (all to be supplied as kwargs):
            n (str): folder name
            d (str): folder description
            o (str): owner name
            a (str): owner security domain
            s (bool): shared folder (default false)
            p (str): permissions
            f (str): folder status
        """
        options_allowed = ['n', 'o', 'a', 'p', 'f']
        options_allowed_quote = ['d']
        options_allowed_bool = ['s']
        command = [self.pmrep, 'createfolder']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, value])
            elif key in options_allowed_quote:
                command.extend(['-' + key, '"' + value + '"'])
            elif key in options_allowed_bool and value == True:
                command.extend(['-' + key])
            elif key not in options_allowed + options_allowed_quote + options_allowed_bool:
                raise Exception("unsupported createfolder option: %s" % key)

        pmrep_output = infa.helper.cmd_execute(command)
        if not "createfolder completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise Exception("failed to create label using %s" % " ".join(command))

    def createlabel(self, **params):
        """
        Create a label that can be used to associate groups of objects during
        development.

        Args (all to be supplied as kwargs):
            a (str): name of label to be created in the repository
            c (str): optional comment about the label
        """
        options_allowed = ['a', 'c']
        command = [self.pmrep, 'createlabel']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, '"' + value + '"'])
            else:
                raise Exception("unsupported createlabel option: %s" % key)

        pmrep_output = infa.helper.cmd_execute(command)
        if not "createlabel completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise Exception("failed to create label using %s" % " ".join(command))

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
        """
        options_allowed = ['n']
        command = [self.pmrep, 'deletefolder']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, value])
            else:
                raise Exception("unsupported deletefolder option: %s" % key)

        pmrep_output = infa.helper.cmd_execute(command)
        if not "deletefolder completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise Exception("failed to delete folder using %s" % " ".join(command))

    def deletelabel(self, **params):
        """
        Delete a label and remove the label from all objects that use it.

        This method by default uses the '-f' pmrep flag to avoid user
        interaction.

        Args (all to be supplied as kwargs):
            a (str): name of the label to be deleted in the repository
        """
        options_allowed = ['a']
        command = [self.pmrep, 'deletelabel', '-f']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, '"' + value + '"'])
            else:
                raise Exception("unsupported delete option: %s" % key)

        pmrep_output = infa.helper.cmd_execute(command)
        if not "deletelabel completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise Exception("failed to delete label using %s" % " ".join(command))

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
        """
        command = [self.pmrep, 'listconnections', '-t']
        pmrep_output = infa.helper.cmd_execute(command)
        return infa.helper.format_output(pmrep_output, ',')

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
            c (str): column separator
            r (str): end-of-record separatr
            l (str): end-of-listing separator
            s (str): dbd separator

            Refer to Informatica Command reference Handbook for details.
        """
        options_allowed = ['o', 't', 'f', 'c', 'r', 'l', 's']
        command = [self.pmrep, 'listobjects']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, value.lower()])
            else:
                raise Exception("unsupported listobjects option: %s" % key)

        pmrep_output = infa.helper.cmd_execute(command)
        return infa.helper.format_output(pmrep_output, ' ')

    def listtablesbysess(self):
        """
        Return a list of sources or targets used in a session.
        """
        command = [self.pmrep, 'listtablesbysess']
        pass

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
        if not "updatestatistics completed successfully." in pmrep_output:
            print "\n".join(pmrep_output)
            raise InfaPmrepError("failed to update statistics using %s" % " ".join(command))

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
