# (c) 2017, Ron Arts <ron.arts@gmail.com>
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
    lookup: gitlab_env
    author: Ron Arts <ron.arts@gmail.com>
    version_added: "0.1"
    short_description: Read all GitLba CI variables, and the ones prefixed with a given value
    description:
        - Allows you to query the environment variables available during GitLan CI builds, including secret variables
    options:
      _terms:
        description: Environment variable or list of them to lookup the values for
        required: True
"""

EXAMPLES = """
- environment: "{{ lookup('gitlab_env','ENV') }}"
"""

RETURN = """
  _list:
    description:
      - all environment variables, with prefixes removed
    type: list
"""
import os

from ansible.plugins.lookup import LookupBase
from ansible.module_utils._text import to_text

class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        env = {}
        for var in os.environ:
            if (var.startswith('CI_')):
                env[var] = to_text(os.getenv(var))
        for prefix_var in terms:
            prefix = to_text(os.getenv(prefix_var))
            env[prefix_var] = prefix
            for var in os.environ:
                if (var.startswith(prefix + '_')):
                    env[var[len(prefix)+1:]] = to_text(os.getenv(var))
        return [env]

