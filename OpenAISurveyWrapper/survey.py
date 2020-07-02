# AUTOGENERATED! DO NOT EDIT! File to edit: 01_survey.ipynb (unless otherwise specified).

__all__ = ['survey']

# Cell
import openai, pandas as pd, numpy as np, datetime, json
from OpenAISurveyWrapper import wrapper

# Cell
class survey(wrapper.wrapper):
    """
    wrapper on the API to load in survey definitions
    a format for displaying

    self.myFormat: a function to format a prompt
    """
    labeled = pd.DataFrame()
    raw = pd.DataFrame()
    examples = pd.DataFrame()
    definitions = {}
    myFormat = """A post is about {} if it {} Consider the following post:\npost: "{}"\nq: Was the post about {} (yes or no)?\na:""".format
    kwargs = {
        "engine":"davinci",
        "temperature":0,
        "max_tokens":10,
        "stop":"\n",
    }

    def setFormat(self, func):
        """
        set prompt format to newFormat
        """
        self.myFormat = func

    def formatQuery(self, *args):
        return (self.myFormat(*args))

    def addDefinition(self, label:str, definition:str):
        """
        set definition of label to definition)
        """
        self.definitions[label] = definition

    def removeDefinition(self, label:str):
        """
        set definition of label to definition)
        """
        del self.definitions[label]

    def loadExamplesFromDataFrame(self, examples:dict):
        """
        takes a 2 column dataframe; first column should be "text", second "label"
        """
        if len(examples.columns)!=2:
            raise Exception("need 2 columns, first should be data second label")
        self.examples = examples
        self.examples.columns=["data", "label"]

    def generateResponses(self, queries, prompt, verbose=False):
        """
        run a prompt against queries.
        prompt should be formated as "str {} str" to be able to use format
        to stick each query in
        """
        print("before")

        results = []
        for query in queries:
            r = self.query(prompt=prompt.format(query[:1500]), **self.kwargs)["choices"][0]["text"]
            if verbose:
                print(r)
            results.append(r)

        print("after")
        print(results)
        return results

    def tryLabels(self, n=20, overwrite=True, inplace=True, fewShot = 0, labels=[], verbose=False):
        """
        for each label in labels, add to the
        """
        if len(labels) == 0:
            labels = [x for x in self.definitions]

        if n > 0:
            targets = self.examples.sample(n)
        else:
            targets = self.examples.copy()


        all_responses = {}
        for label in labels:
                prompt = self.formatQuery(label, self.definitions[label],"{}", label)
                print(prompt)
                responses = self.generateResponses(targets["data"].to_list(), prompt, verbose=verbose)

                with open("{}/{}".format(self.outdir, datetime.datetime.now().strftime("%Y%m%d%H%m%S") + ".json"), "w") as fh:
                    json.dump({"prompt":prompt, "data":{"queries":targets["data"].to_list(), "preds":responses}}, fh, indent=4)

                all_responses[label]=responses

                targets[label] = responses
                self.labeled = targets
        self.labeled = targets

