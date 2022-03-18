#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type
import requests
import validators

DOCUMENTATION = r'''
---
module: example_py
author: Pupkin V.
short_description: Get status code from remote server
description:
  - Get status code from remote server
version_added: 1.0.0
options:
  url:
    description:
      - Url address where we to get the status code
      - This is a required parameter
    type: str
'''

EXAMPLES = r'''
- name: Get status code
  get_status_code_py:
    url: http://ya.ru
  connection: local
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: ""
result_str:
  description: final string
  returned: always
  type: str
  sample: Just do it
rc:
  description: Return code
  returned: always
  type: int
  sample: 0
'''

from ansible.module_utils.basic import (
    AnsibleModule
)

def uri_validator(x):
    try:
        result = validators.url(x)
        if result is True:
            return True
        else:
            return False
    except:
        return False

def get_status_code(url):
    failed = True
    msg = ""
    result = ""
    rc = 1
    status = 0
    try:
        if not isinstance(url, str):
            raise TypeError("String type is expected, "
                            "got type %s instead" % type(url))
        if not uri_validator(url): 
            raise RuntimeError("Not valid url")
        response= requests.get(url)
        status = response.status_code
        if status != 200:
            raise RuntimeError("Not alowed status code. "
                                "Status code is %d" % status) 
        result = status
        msg = "Status code is valid"
        failed = False
        rc = 0
    except TypeError as e:
        msg = "TypeError. Input url is not strings %s" % e
    except RuntimeError as e:
        msg = "Error. %s" % e
        result = status
    except:
        msg = "General connection error"
    return(failed, result, rc, msg)    

def main():
    # Задаем аргументы модуля
    module_args = dict(
        url = dict(required = True, type = 'str')
    )
    # Создаем объект - модуль
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = False
    )
    # Получаем из модуля аргументы
    url = module.params["url"]
    # Вызываем нашу функцию
    lc_return = get_status_code(url)
    # Если задача зафейлилась
    if lc_return[0]:
        module.fail_json(changed=False,
                         failed=lc_return[0],
                         result_str=lc_return[1],
                         rc=lc_return[2],
                         msg=lc_return[3])
    # Если задача успешно завершилась
    else:
        module.exit_json(changed=False,
                         failed=lc_return[0],
                         result_str=lc_return[1],
                         rc=lc_return[2],
                         msg=lc_return[3])


if __name__ == "__main__":
    main()
