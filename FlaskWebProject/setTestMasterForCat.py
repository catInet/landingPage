#update test cat's owner
#whom we will send messages
from azure.storage import TableService
import config
table_service = TableService(account_name=config.ACC_NAME, 
                             account_key=config.ACC_KEY)
#newMaster = {'masterID' : '188622142'}
#table_service.update_entity('bandcredentials', 'band','test', newMaster)
#table_service.insert_entity('bandcredentials', newMaster)

task = table_service.get_entity('bandcredentials', 'band', 'test')
print task.masterID