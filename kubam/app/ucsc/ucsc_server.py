from helper import KubamError
from ucscsdk.ucscexception import UcscException


class UCSCServer(object):
    
    @staticmethod
    def list_templates(handle):

        filter_str = "(type, 'initial-template', type='eq') or (type, 'updating-template', type='eq')"
        try:
            query = handle.query_classid("lsServer", filter_str=filter_str)
            templates = list()

            for q in query:
                templates.append({"name": q.name})
            return templates

        except UcsException as e:
            raise KubamError(e)
