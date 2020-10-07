import importlib
import os
import re
import typing

class Loader:
    def __init__(self, dir: str) -> None:
        self.__loaded_objects: list = []
        self.__load_dir: str = os.path.normpath(dir)
        self.__append_to_path(self.__load_dir)
    
    def load(self, ) -> list:
        modules_names = []

        for module in self.__get_modules(self.__load_dir):
            modules_names.append(module)
        
        for module in modules_names:
            try:
                loaded_module = importlib.import_module(module)
                self.__get_module_objects(loaded_module)
            except ModuleNotFoundError:
                pass
        return self.__loaded_objects
    
    def __get_module_objects(self, module) -> None:
        for module_object in dir(module):
            object_ = getattr(module, module_object)
            if hasattr(object_, 'loader_flag'):
                if object_.loader_flag:
                    self.__loaded_objects.append(object_)

    def __append_to_path(self, path):
        if not path in os.sys.path:
            os.sys.path.append(path)
    
    def __get_modules(self, path) -> typing.Generator:
        self.__append_to_path(path)
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                yield f[:-3]
            elif os.path.isdir(os.path.join(path, f)):
                f = os.path.join(self.__load_dir, f)
                yield from self.__get_modules(f)