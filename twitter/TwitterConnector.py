#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File : twitter.TwitterConnector.py
# Description : Access to Twitter basic function.
# Auteur : Nils Schaetti <n.schaetti@gmail.com>
# Date : 09.08.2017 15:48:00
# Lieu : Nyon, Suisse
#
# This file is part of the TwitterAnalyzer.
# The TwitterAnalyzer is a set of free software:
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTweetBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with pyTweetBar.  If not, see <http://www.gnu.org/licenses/>.
#

import tweepy
import time
import logging
from patterns.singleton import singleton


# Twitter connector
@singleton
class TwitterConnector(object):
    """
    Twitter Connector
    """

    # Constructor
    def __init__(self, auth_token1, auth_token2, access_token1, access_token2):
        """
        Constructor
        :param auth_token1:
        :param auth_token2:
        :param access_token1:
        :param access_token2:
        """
        # Auth to Twitter
        auth = tweepy.OAuthHandler(auth_token1, auth_token2)
        auth.set_access_token(access_token1, access_token2)
        self._api = tweepy.API(auth)
        self._cursor = tweepy.Cursor(self._api.followers).pages()
    # end __init__

    ###########################################
    # Public
    ###########################################

    # Get time line
    def get_time_line(self, n_pages):
        """
        Get time line.
        :param n_pages:
        :return:
        """
        return tweepy.Cursor(self._api.home_timeline, screen_name='nschaetti').pages(limit=n_pages)
    # end get_time_line

    # Get user timeline
    def get_user_timeline(self, screen_name, n_pages=-1):
        """
        Get time line.
        :param n_pages:
        :return:
        """
        if n_pages == -1:
            return tweepy.Cursor(self._api.user_timeline, screen_name=screen_name).pages()
        else:
            return tweepy.Cursor(self._api.user_timeline, screen_name=screen_name).pages(limit=n_pages)
        # end if
    # end get_time_line

    # Get search cursor
    def search_tweets(self, search, n_pages=-1):
        """
        Get search cursor
        :param search:
        :param n_pages:
        :return:
        """
        if n_pages == -1:
            return tweepy.Cursor(self._api.search, q=search).pages()
        else:
            return tweepy.Cursor(self._api.search, q=search).pages(limit=n_pages)
        # end if
    # end search_tweets

    # Get tweets with hashtag
    def get_hashtag_tweets(self, hashtag, n_pages=-1):
        """
        Get tweets with hashtag
        :param hashtag:
        :param n_pages:
        :return:
        """
        return self.search_tweets(u"#" + hashtag, n_pages)
    # end get_hashtag_tweets

    # Get the user
    def get_user(self):
        """
        Get the user
        :return: The Twitter user object.
        """
        return self._api.get_user(self._config['user'])
    # end get_user

    # Get a tweet
    def get_tweet(self, tweet_id):
        """
        Get a tweet
        :param tweet_id:
        :return:
        """
        self._api.get_status(tweet_id)
    # end if

    ###########################################
    # Override
    ###########################################

    ###########################################
    # Private
    ###########################################

# end TwitterConnector
