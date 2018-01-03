import os
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)

slack_client = SlackClient(SLACK_TOKEN)


def list_messages(message):
    channels_call = slack_client.api_call("search.messages", query = message)
    if channels_call['ok']:
        return channels_call['messages']
    return None


if __name__ == '__main__':
    
    message = raw_input('Enter message you want to search: ')
    messages = list_messages(message)
    
    if messages:
        matches = messages['matches']
        if matches: 
            print("Messages: ")
            for m in matches:
                channel = m['channel'];
                if ( channel['is_channel']  == True ):
                    print("User: " + m['username'] + " / Message: " + m['text'] + " / Channel Name: " + channel['name'])
                else:
                    print("User: " + m['username'] + " / Message: " + m['text'] + " / Not in channel ")
        else:
            print("None matches.")
                
    else:
        print("Unable to authenticate.")