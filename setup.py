#!/usr/bin/env python
"""
Licensed under the Apache License, Version 2.0 (the "License"); 
you may not use this file except in compliance with the License. 
You may obtain a copy of the License at 

   http://www.apache.org/licenses/LICENSE-2.0 

Unless required by applicable law or agreed to in writing, software 
distributed under the License is distributed on an "AS IS" BASIS, 
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
See the License for the specific language governing permissions and 
limitations under the License. 
"""

from distutils.core import setup

setup(
    name='redhot',
    version='0.0.1',
    description='Stupid redis model thing.',
    author='Josh Marshall',
    author_email='catchjosh@gmail.com',
    url="http://github.com/joshmarshall/redhot/",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    requires=["interfaces", "redis"],
    py_modules=['redhot',],
)
