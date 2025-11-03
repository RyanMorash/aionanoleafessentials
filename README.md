# aioNanoleafEssentials package 
[![PyPI](https://img.shields.io/pypi/v/aionanoleaf)](https://pypi.org/project/aionanoleaf/) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aionanoleaf) [![PyPI - License](https://img.shields.io/pypi/l/aionanoleaf?color=blue)](https://github.com/RyanMorash/aionanoleafessentials/blob/main/COPYING)

An async Python wrapper for the Nanoleaf API.

## Installation
```bash
pip install aionanoleafessentials
```

## Usage
### Import
```python
from aionanoleafessentials import Nanoleaf
```

### Create a `aiohttp.ClientSession` to make requests
```python
from aiohttp import ClientSession
session = ClientSession()
```

### Create a `Nanoleaf` instance
```python
from aionanoleafessentials import Nanoleaf
light = Nanoleaf(session, "192.168.0.100")
```

## Example
```python
from aiohttp import ClientSession
from asyncio import run

import aionanoleafessentials

async def main():
    async with ClientSession() as session:
        nanoleaf = aionanoleafessentials.Nanoleaf(session, "192.168.0.73")
        try:
            await nanoleaf.authorize()
        except aionanoleafessentials.Unauthorized as ex:
            print("Not authorizing new tokens:", ex)
            return
        await nanoleaf.turn_on()
        await nanoleaf.get_info()
        print("Brightness:", nanoleaf.brightness)
        await nanoleaf.deauthorize()
run(main())
```
