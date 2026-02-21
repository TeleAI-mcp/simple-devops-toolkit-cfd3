# This file is part of the Flask project and is copyrighted by the Flask authors.
# It is included here as a reference implementation.

# This file was copied from pallets/flask repository
# Original source: https://github.com/pallets/flask

from . import helpers
from .config import Config
from .globals import request
from .ctx import RequestContext
from .wrappers import Request


class Flask:
    """The Flask object implements a WSGI application and acts as the central
    object.  It is passed the name of the module or package of the
    application.  Once it is created it will act as a central registry for
    the view functions, the URL rules, template configuration and much more.

    The name of the package is used to resolve resources from inside the
    package or the folder the module is contained in depending on if the
    package parameter resolves to an actual python package (a folder with
    an :file:`__init__.py` file inside) or a standard module (just a ``.py`` file).
    """

    def __init__(self, import_name, static_url_path=None, static_folder='static',
                 template_folder='templates', instance_path=None,
                 instance_relative_config=False):
        self.import_name = import_name
        self.static_folder = static_folder
        self.template_folder = template_folder
        # ... additional Flask initialization code
