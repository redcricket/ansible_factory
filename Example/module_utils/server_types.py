# from decorators import debug_printer
try:
    from ansible.module_utils.object_factory import ObjectFactory
except:
    from object_factory import ObjectFactory

class RealtimeService:

    def __init__(self, config):
        self.config = config
        self.config_filename = f"/tmp/ssb-{config.get('instance_seq')}.cfg"

    def get_server_info(self):
        raise NotImplementedError

    def suspend(self):
        raise NotImplementedError

    def unsuspend(self):
        raise NotImplementedError

    def update_config(self, config):
        raise NotImplementedError

    def write_config(self, make_backup=False):
        raise NotImplementedError

    def update_executable(self):
        raise NotImplementedError

    def restart_service(self):
        raise NotImplementedError

    def execute(self, action):
        if action == 'suspend':
            return self.suspend()
        if action == 'unsuspend':
            return self.unsuspend()
        if action == 'update_config':
            return self.update_config()
        if action == 'write_config':
            return self.write_config()
        if action == 'update_executable':
            return self.update_executable()
        if action == 'restart_service':
            return self.restart_service()


class ServerTypeServiceProvider(ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


class MMRService(RealtimeService):

    def suspend(self):
        with open(self.config_filename, "a") as fh:
            print(f"Suspending MMR-{self.config.get('instance_seq')}", file=fh)

    def unsuspend(self):
        with open(self.config_filename, "a") as fh:
            print(f"Unsuspending MMR-{self.config.get('instance_seq')}", file=fh)

    def update_executable(self):
        with open(self.config_filename, "a") as fh:
            print(f"Update_executable MMR-{self.config.get('instance_seq')}", file=fh)

    def update_config(self, config):
        with open(self.config_filename, "a") as fh:
            self.config = config

    def write_config(self, make_backup=False):
        with open(self.config_filename, "a") as fh:
            print(f'Writing {self.config_filename} config.')

    def restart_service(self):
        with open(self.config_filename, "a") as fh:
            print(f'restarting MMR-{self.config.instance_seq} config.')


class MMRServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = MMRService(config={"instance_seq" : "1"})
        return self._instance


class ZCService(RealtimeService):

    def suspend(self):
        with open(self.config_filename, "a") as fh:
            print(f"Suspending ZC-{self.config.get('instance_seq')} .", file=fh)

    def unsuspend(self):
        with open(self.config_filename, "a") as fh:
            print(f"Unsuspend ZC-{self.config.get('instance_seq')} .", file=fh)

    def update_config(self, config):
        with open(self.config_filename, "a") as fh:
            self.config = config

    def write_config(self, make_backup=False):
        with open(self.config_filename, "a") as fh:
            print(f'ZC Writing {self.config_filename} .')

    def restart_service(self):
        with open(self.config_filename, "a") as fh:
            print(f"restarting ZC-{self.config.get('instance_seq')} .")

    def update_executable(self):
        with open(self.config_filename, "a") as fh:
            print(f"Update Exe ZC-{self.config.get('instance_seq')}", file=fh)



class ZCServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, **_ignored):
        if not self._instance:
            self._instance = ZCService(config={"instance_seq": "0"})
        return self._instance

factory = ObjectFactory()
factory.register_builder('MMR', MMRServiceBuilder())
factory.register_builder('ZC', ZCServiceBuilder())

#services = ServerTypeServiceProvider()
#services.register_builder('MMR', MMRServiceBuilder())
#services.register_builder('ZC', ZCServiceBuilder())
