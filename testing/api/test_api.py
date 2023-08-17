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

""" Test assertions for CI network baseline test """
# Temporarily disabled because using Pytest fixtures
# TODO refactor fixtures to not trigger error
# pylint: disable=redefined-outer-name

import json
import pytest
import re
import os
import requests
from pathlib import Path

API = "http://127.0.0.1:8000"
LOG_PATH = "/tmp/testrun.log"
TEST_SITE_DIR = ".."



def get_network_interfaces():
  """ return list of network interfaces on machine """
  path = Path('/sys/class/net')
  return [i.stem for i in path.iterdir() if i.is_dir()]


def test_get_system_interfaces():
  """ Tests API system interfaces against actual local interfaces"""
  r = requests.get(f"{API}/system/interfaces")
  response = json.loads(r.text)
  local_interfaces = get_network_interfaces()
  assert set(response) == set(local_interfaces)

def test_create_and_get_device():
  pass

def test_create_device():
  
  payload = {
    "manufacturer": "Delta",
    "model": "O3-DIN-CPU",
    "mac_addr": "00:1e:42:35:73:c4",
  }

  r = requests.post(f"{API}/device", data=json.dumps(payload))
  print(r.text)
  assert r.status_code == 200
  

def test_get_devices():
  r = requests.get(f"{API}/devices")
  print(r.text)
  print(r.headers)
  assert False

def test_get_devices_when_none_exist():
  # Delete the devices
  r = requests.get(f"{API}/devices")
  print(r.text)
  print(r.headers)
  assert False

def test_get_system_config():
  r = requests.get(f"{API}/system/config")
  print(r.text)
  print(r.headers)
  assert False

def test_invalid_path_get():
  r = requests.get(f"{API}/blah/blah")
  print(r.status_code)
  print(r.text)
  print(r.headers)
  assert False

def test_trigger_run():
  payload={'device':{'mac_addr': "aa:bb:cc:dd:ee:ff"}}
  r = requests.post(f"{API}/system/start", data=json.dumps(payload))
  print(r.status_code)
  print(r.text)
  print(r.headers)
  assert False