#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : track_retweet.py
# Description : Track
# Auteur : Nils Schaetti <nils.schaetti@unine.ch>
# Date : 01.02.2017 17:59:05
# Lieu : Nyon, Suisse
#
# This file is part of the Reservoir Computing NLP Project.
# The Reservoir Computing Memory Project is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

# Imports
import logging
import argparse
from twitter.TwitterConnector import TwitterConnector


####################################################
# Main function
####################################################

if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser(description="TwitterAnalyzer - Track a retweet")

    # Argument
    parser.add_argument("--auth-token1", type=str, help="First authentification token", required=True)
    parser.add_argument("--auth-token2", type=str, help="Second authentification token", required=True)
    parser.add_argument("--access-token1", type=str, help="First access token", required=True)
    parser.add_argument("--access-token2", type=str, help="Second access token", required=True)
    parser.add_argument("--retweet-id", type=str, help="Retweet ID to track", required=True)
    parser.add_argument("--log-level", type=int, help="Log level", default=20)
    args = parser.parse_args()

    # Logging
    logging.basicConfig(level=args.log_level)
    logger = logging.getLogger(name="TwitterAnalyzer")

    # Connection to Twitter
    twitter_connector = TwitterConnector(args.auth_token1, args.auth_token2, args.access_token1, args.access_token2)

    # Get tweets from the hashtag


# end if