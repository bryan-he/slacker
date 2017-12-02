#!/usr/bin/env python

from __future__ import print_function
import slacker
import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spam some jokers.")
    parser.add_argument('token', help="Slack API Token (can be obtained from https://api.slack.com/docs/oauth-test-tokens)")
    args = parser.parse_args()
    token = args.token

    slack = slacker.Slacker(token)

    users = slack.users.list().body["members"]
    mpim_users = []
    for u in users:
        if u["name"] == "paroma":
            print("DEBUG")
            mpim_users.append(u["id"])
            channel = slack.im.open(u["id"])
            for i in range(1000000):
                try:
                    slack.chat.post_message(u["id"], "Submit the poster " + str(i))
                    print(i)
                except:
                    print("EXCEPTION")
