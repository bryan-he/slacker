#!/usr/bin/env python

from __future__ import print_function
import slacker
import sys
import argparse
import sys
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spam some jokers.")
    parser.add_argument('token', help="Slack API Token (can be obtained from https://api.slack.com/docs/oauth-test-tokens)")
    args = parser.parse_args()
    token = args.token

    slack = slacker.Slacker(token)

    users = slack.users.list().body["members"]
    mpim_users = []
    for u in users:
        if u["name"] == "thodrek" or u["name"] == "cdesa":
            mpim_users.append(u["id"])

    channel = slack.mpim.open(mpim_users).body["group"]["id"]
    #slack.chat.post_message(channel, "any updates? :slightly_smiling_face:")
    oldest = time.time()
    while True:
        print(time.asctime())
        sys.stdout.flush()
        mpim = slack.mpim.history(channel, oldest=oldest).body
        messages = mpim["messages"]
        if messages != []:
            oldest = messages[0]["ts"]
        for m in messages:
            print(m["ts"])
            is_human = "user" in m.keys() # Bots have a "username" but no "user"
            if is_human:
                if "update" in m["text"].lower():
                    slack.chat.post_message(channel, "any updates? :slightly_smiling_face:")
