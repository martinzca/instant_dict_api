import justpy as jp
import definition
import json


class Api:
    """
    Example use: http://localhost:8000/api?w=rain
    """
    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')

        defined = definition.Definition(word).get()
        res = {
            "word": word,
            "definition": defined
        }
        wp.html = json.dumps(res)
        return wp

