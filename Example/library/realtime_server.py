#!/usr/bin/python3
# see https://stackoverflow.com/questions/35328177/how-to-import-a-py-file-into-an-ansible-module
from ansible.module_utils.basic import AnsibleModule
try:
    from ansible.module_utils.server_types import factory
except:
    from server_types import factory

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r''' '''

EXAMPLES = r''' '''


def run_server_action(server_type, action):
    rt_server = factory.create(key=server_type)
    rt_server.execute(action=action)


def run_module():
    # define the available arguments/parameters that a user can pass to the module
    module_args = dict( server_type=dict(type='str', required=True), action=dict(type='str', required=True) )
    result = dict( changed=False )
    module = AnsibleModule( argument_spec=module_args, supports_check_mode=True )

    if module.check_mode:
        return result

    rc = {}
    if module.params.get('server_type'):
        if module.params.get('action'):
            rc = run_server_action(module.params.get('server_type'),
                              module.params.get('action'))
    module.exit_json(changed=False, meta=rc)

def main():
    run_module()


if __name__ == '__main__':
    main()
