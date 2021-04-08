from burp import IBurpExtender
from java.io import PrintWriter, File
from datetime import datetime

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks( self, callbacks):
        extName = "AutoGenerate Report"
        pathString = "/PLEASE/REPLACE/ME/" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".xml"

        # keep a reference to our callbacks object and add helpers
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        # set our extension name
        callbacks.setExtensionName(extName)

        # obtain our output streams
        self._stdout = PrintWriter(callbacks.getStdout(), True)
        self._stderr = PrintWriter(callbacks.getStderr(), True)

        # print extension name
        self._stdout.println(extName + " initialized!")

        # Generate report
        issueList = self._callbacks.getScanIssues(None)
        self._callbacks.generateScanReport('XML', issueList, File(pathString))
        self._stdout.println("Report located at " + pathString)

        return
