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

        if ('x' in params.keys()) and ('X' in params.keys()):
            raise InfaPmrepError("both [x] and [X] options supplied. Only one allowed.")

        options_allowed = ['r', 'h', 'o', 'n', 's', 'x', 'X', 'u', 't']
        command = [self.pmrep, 'connect']

        for key, value in params.iteritems():
            if key in options_allowed:
                command.extend(['-' + key, value])
            else:
                raise InfaPmrepError("unsupported init option: %s" % key)

        pmrep_output = infa.helper.execute_cmd(command)
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

    def assignpermission(self):
        """
        Add, remove or update permissions on a global object for a user,
        group, or the Others default group.
        """
        command = [self.pmrep, 'assignpermission']
        pass

    def backup(self):
        """
        Backup the repository to the specified file.
        """
        command = [self.pmrep, 'backup']
        pass

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
        pmrep_output = infa.helper.execute_cmd(command)

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
            elif key in options_allowed_bool:
                command.extend(['-' + key])
            else:
                raise Exception("unsupported createfolder option: %s" % key)

        pmrep_output = infa.helper.execute_cmd(command)
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

        pmrep_output = infa.helper.execute_cmd(command)
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

        pmrep_output = infa.helper.execute_cmd(command)
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

        pmrep_output = infa.helper.execute_cmd(command)
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
        pmrep_output = infa.helper.execute_cmd(command)
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

        pmrep_output = infa.helper.execute_cmd(command)
        return infa.helper.format_output(pmrep_output, ' ')
