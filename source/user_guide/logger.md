# Logger

This document is used to introduce how to use a unified `Logger` in `TrafficDL` to output necessary auxiliary information. **The logger that can show a message on standard output and write it into the file simultaneously.**

First call `utils.utils.get_logger()` in the entry file `test_model.py` to instantiate the `Logger` object.

```python
from libtraffic.utils import get_logger
logger = get_logger(config)
```

You can use `Logger` in the file you want like this:

```python
from logging import getLogger
from libtraffic.model.abstract_model import AbstractModel

class NewModel(AbstractModel):
    def __init__(self, config, data_feature):
        self._logger = getLogger()
        
    def forward(self, batch):
        self._logger.info("hahhh")
```

