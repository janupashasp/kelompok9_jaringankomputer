import threading


class ServiceRegistry:
    def __init__(self, services):
        self._lock = threading.Lock()
        self._active = {
            service: True for service in services
        }

    def is_active(self, service):
        with self._lock:
            return self._active.get(service, False)

    def disable(self, service):
        with self._lock:
            if service not in self._active:
                return False

            was_active = self._active[service]
            self._active[service] = False

            return was_active

    def active_services(self):
        with self._lock:
            return [
                service
                for service, active in self._active.items()
                if active
            ]

    def disabled_services(self):
        with self._lock:
            return [
                service
                for service, active in self._active.items()
                if not active
            ]

    def all_disabled(self):
        with self._lock:
            return not any(self._active.values())

