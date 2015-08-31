# Stubs for hashlib

# NOTE: These are incomplete!

from abc import abstractmethod, ABCMeta
import typing

class Hash(metaclass=ABCMeta):
    @abstractmethod
    def update(self, arg: bytes) -> None: ...
    @abstractmethod
    def digest(self) -> bytes: ...
    @abstractmethod
    def hexdigest(self) -> str: ...
    @abstractmethod
    def copy(self) -> 'Hash': ...

def md5(arg: bytes = None) -> Hash: ...
def sha1(arg: bytes = None) -> Hash: ...
def sha224(arg: bytes = None) -> Hash: ...
def sha256(arg: bytes = None) -> Hash: ...
def sha384(arg: bytes = None) -> Hash: ...
def sha512(arg: bytes = None) -> Hash: ...

def new(name: str, data: bytes = None) -> Hash: ...