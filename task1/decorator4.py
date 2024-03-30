from typing import Callable, Any
import logging

def html(tag: str) -> Callable[...,Any]:
    def decorator(func: Callable[...,Any]):
        def wrapper(*args: Any, **kwargs: Any) ->str:
            return f'<{tag}> {func(*args, **kwargs)}</{tag}>'
        return wrapper
    return decorator

@html('h1')
def get_string() ->str:
    return 'this is string'

@html('h2')
def get_another_string() ->str:
    return 'this is another string'

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-\ %(levelname)s - %(message)s')


logging.info(get_string())
logging.info(get_another_string())
