from dataclasses import dataclass
from typing import TypeVar


@dataclass
class BaseSensor:
    _uuid: int
    _device_name: str

    @property
    def uuid(self) -> int:
        return self._uuid

    @uuid.setter
    def set_uuid(self, _: int) -> bool:
        return False

    @property
    def device_name(self) -> str:
        return self._device_name

    @device_name.setter
    def set_device_name(self, _: str) -> bool:
        return False
