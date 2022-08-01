# ansible_factory
How to implement a General Purpose Object Factory in an Ansible module.

# Purpose

In this README file I will show how I implemented a General Purpose Object Factory for use in an Ansible module.
I based the python code on this article: https://realpython.com/factory-method-python/

# Usage Playbook

Here's an example playbook:

```
---
-
  hosts: all
  tasks:
    - name: Do MMR
      realtime_server:
        server_type: 'MMR'
        action: "{{ item }}"
      loop: 
        - 'suspend'
        - 'update_executable'
        - 'unsuspend'

    - name: Do ZC
      realtime_server:
        server_type: 'ZC'
        action: "{{ item }}"
      loop: 
        - 'suspend'
        - 'update_executable'
        - 'unsuspend'

    - name: All done
      local_action: debug msg="All done"
      run_once: True
```


Here's what a run of the playbook look likes:

```
ansible@ubuntu-c:~/ansible_factory/Example$ ansible-playbook -i hosts -l centos test_playbook.yml 

PLAY [all] **********************************************************************************************************************************

TASK [Gathering Facts] **********************************************************************************************************************
ok: [centos3]
ok: [centos2]
ok: [centos1]

TASK [Do MMR] *******************************************************************************************************************************
ok: [centos1] => (item=suspend)
ok: [centos3] => (item=suspend)
ok: [centos2] => (item=suspend)
ok: [centos1] => (item=update_executable)
ok: [centos3] => (item=update_executable)
ok: [centos2] => (item=update_executable)
ok: [centos1] => (item=unsuspend)
ok: [centos3] => (item=unsuspend)
ok: [centos2] => (item=unsuspend)

TASK [Do ZC] ********************************************************************************************************************************
ok: [centos1] => (item=suspend)
ok: [centos2] => (item=suspend)
ok: [centos3] => (item=suspend)
ok: [centos1] => (item=update_executable)
ok: [centos3] => (item=update_executable)
ok: [centos2] => (item=update_executable)
ok: [centos1] => (item=unsuspend)
ok: [centos2] => (item=unsuspend)
ok: [centos3] => (item=unsuspend)

TASK [All done] *****************************************************************************************************************************
ok: [centos1 -> localhost] => {
    "msg": "All done"
}

PLAY RECAP **********************************************************************************************************************************
centos1                    : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
centos2                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
centos3                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

# The Example Directory

In the Example directory there are really just 3 files you should look at:
 
- library/realtime_server.py
- module_utils/object_factory.py
- module_utils/server_types.py

# Also See

# https://realpython.com/factory-method-python/
