class SharedVariables:
    def __init__(self):
        self.rulename = None
        self.reason = None
        self.status = None
        self.alertname  = None
        self.description = None
        self.appName = None
        self.message = None
        self.language = None
    # def __init__(self,rulename,reason,status,alertname,description,appName,message,language):
    #     self.rulename = rulename
    #     self.reason = reason
    #     self.status = status
    #     self.alertname  = alertname
    #     self.description = description
    #     self.appName = appName
    #     self.message = message
    #     self.language = language
    def define_value_kibana():
        SharedVariables.alertname = "None"
        SharedVariables.status = "None"
        SharedVariables.description = "None"
        SharedVariables.appName = "None"
        SharedVariables.language = "None"
        SharedVariables.message = "None"
    def define_value_prometheus():
        SharedVariables.rulename = "None"
        SharedVariables.reason = "None"
        SharedVariables.appName = "None"
        SharedVariables.language = "None"
        SharedVariables.message = "None"
    def define_value_log():
        SharedVariables.alertname = "None"
        SharedVariables.status = "None"
        SharedVariables.description = "None"
        SharedVariables.rulename = "None"
        SharedVariables.reason = "None"