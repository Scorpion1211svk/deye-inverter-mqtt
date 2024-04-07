# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from deye_sensor import (
    SingleRegisterSensor,
    SignedMagnitudeSingleRegisterSensor,
    SignedMagnitudeDoubleRegisterSensor,
    SensorRegisterRange,
)

#
# IGEN DTSD-422-D3 support.
#
# Todo:
# * Daily Values for Positive and Negative energy are missing, can't find them.
# * Need to verify data is still read correctly when double reg values exceed one
#   register
#
# Total
total_active_power_sensor = SignedMagnitudeDoubleRegisterSensor(
    "Total Active Power",
    0x0D,
    1,
    mqtt_topic_suffix="total/active_power",
    unit="W",
    groups=["igen_dtsd422"],
)
total_active_power2_sensor = SignedMagnitudeDoubleRegisterSensor(
    "Total Active Power 2",
    0x100E,
    1,
    mqtt_topic_suffix="total/active_power2",
    unit="W",
    groups=["igen_dtsd422"],
)
total_positive_energy_sensor = SingleRegisterSensor(
    "Total Positive Energy",
    0x2A,
    0.01,
    mqtt_topic_suffix="total/positive_energy",
    unit="kWh",
    groups=["igen_dtsd422"],
)
total_positive_energy2_sensor = SingleRegisterSensor(
    "Total Positive Energy 2",
    0x102A,
    0.01,
    mqtt_topic_suffix="total/positive_energy2",
    unit="kWh",
    groups=["igen_dtsd422"],
)
total_negative_energy_sensor = SingleRegisterSensor(
    "Total Negative Energy",
    0x34,
    0.01,
    mqtt_topic_suffix="total/negative_energy",
    unit="kWh",
    groups=["igen_dtsd422"],
    print_format="{:0.2f}",
)
total_frequency_sensor = SingleRegisterSensor(
    "Frequency",
    0x29,
    0.01,
    mqtt_topic_suffix="total/frequency",
    unit="Hz",
    groups=["igen_dtsd422"],
    print_format="{:0.2f}",
)
total_frequency2_sensor = SingleRegisterSensor(
    "Frequency 2",
    0x1029,
    0.01,
    mqtt_topic_suffix="total/frequency2",
    unit="Hz",
    groups=["igen_dtsd422"],
    print_format="{:0.2f}",
)


igen_dtsd422_sensors = [
    total_active_power_sensor,
    total_active_power2_sensor,
    total_positive_energy_sensor,
    total_positive_energy2_sensor,
    total_negative_energy_sensor,
    total_frequency_sensor,
    total_frequency2_sensor,
]

igen_dtsd422_register_ranges = [
    SensorRegisterRange(group="igen_dtsd422", first_reg_address=0x01, last_reg_address=0x64),
    SensorRegisterRange(group="igen_dtsd422", first_reg_address=0x65, last_reg_address=0xA1),
    SensorRegisterRange(group="igen_dtsd422", first_reg_address=0x1001, last_reg_address=0x1064),
    SensorRegisterRange(group="igen_dtsd422", first_reg_address=0x1065, last_reg_address=0x10A1),
]
