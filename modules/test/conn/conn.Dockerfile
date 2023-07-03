# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Image name: test-run/conn-test
FROM test-run/base-test:latest

ARG MODULE_NAME=conn
ARG MODULE_DIR=modules/test/$MODULE_NAME

# Install all necessary packages
RUN apt-get install -y wget

#Update the oui.txt file from ieee
RUN wget http://standards-oui.ieee.org/oui.txt -P /usr/local/etc/

#Load the requirements file
COPY $MODULE_DIR/python/requirements.txt /testrun/python

#Install all python requirements for the module
RUN pip3 install -r /testrun/python/requirements.txt

# Copy over all configuration files
COPY $MODULE_DIR/conf /testrun/conf

# Copy over all binary files
COPY $MODULE_DIR/bin /testrun/bin

# Copy over all python files
COPY $MODULE_DIR/python /testrun/python
