import asyncio
import typing

from cepy.loader import Loader

class Cepy:
    def __init__(self, *, loader=Loader) -> None:
        self.__loader = loader       
    
    def get(self, cep: typing.Union[str, int]):
        cep = self.__apply_transforms(cep)
        tasks: typing.Set[typing.Awaitable] = set()
        loop = asyncio.get_event_loop()
        for service in self.__loader('cepy/services').load():
            future = loop.run_in_executor(None, service().get, cep)
            tasks.add(future)
        
        async def exec_tasks(tasks=tasks):
            ended, working = await asyncio.wait(
                tasks, 
                return_when=asyncio.FIRST_COMPLETED
            )
            if list(ended)[0].exception():
                if working:
                    return await exec_tasks(working)
                else:
                    def make_result():
                        def result(self,):
                            return {'response':'Cep não encontrado'}
                        obj = type('Result', (object,), {})
                        obj.result = result
                        return obj()
                    return {make_result()}
            return ended

        response = list(loop.run_until_complete(exec_tasks()))[0]
        return response.result()
    
    def __apply_transforms(self, cep: typing.Union[str, int]) -> str:
        for transform in self.__loader('cepy/transforms').load():
            cep = transform.transform(cep)
        return str(cep)

    def __call__(self, cep):
        return self.get(cep)