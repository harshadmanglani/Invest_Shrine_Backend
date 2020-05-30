from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'insurance1' # Must be replaced by your <storage_account_name>
    account_key = 'cGsUA4iQRecniVfwgVBhTMyVDRBo5xvr5If0YquUuZ9HkK3pUeXv+ELasPVWS7eTkqVFB87Eeiyk4VbtPlveiQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'insurancealpha'
    expiration_secs = None 

class AzureStaticStorage(AzureStorage):
    account_name = 'insurance1' # Must be replaced by your storage_account_name
    account_key = 'cGsUA4iQRecniVfwgVBhTMyVDRBo5xvr5If0YquUuZ9HkK3pUeXv+ELasPVWS7eTkqVFB87Eeiyk4VbtPlveiQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None