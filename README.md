# OpenAI Survey Wrapper
> wrapper to label survey respones and test accuracy


## Install

`pip install OpenAISurveyWrapper`

## How to use

Fill me in please! Don't forget code examples:

```python
print("in progress")
```

    in progress


## Create and Add Key

```python
from OpenAISurveyWrapper.survey import survey
import json, pandas as pd
```

```python
tmp = survey()
tmp.add_key(json.load(open("../gpt3/key.json", "r"))["key"])
```
