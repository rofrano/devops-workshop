# Copyright 2016, 2019 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Package: service

Package for the application models and service routes
This module creates and configures the Flask app and sets up the logging

An SQL datavase
"""
import os
import sys
import logging
from flask import Flask

# Get configuration from environment
DATABASE_URI = os.getenv('DATABASE_URI', 'postgres://postgres:postgres@localhost:5432/postgres')
SECRET_KEY = os.getenv('SECRET_KEY', 'please, tell nobody... Shhhh')

# Create Flask application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

# Import the rutes After the Flask app is created
import service.routes

# Set up logging for production
routes.initialize_logging()

app.logger.info(70 * '*')
app.logger.info('  P E T   S E R V I C E   R U N N I N G  '.center(70, '*'))
app.logger.info(70 * '*')

try:
    routes.init_db()  # make our sqlalchemy tables
except Exception as error:
    app.logger.critical('%s: Cannot continue', error)
    # gunicorn requires exit code 4 to stop spawning workers when they die
    sys.exit(4)

app.logger.info('Service inititalized!')
