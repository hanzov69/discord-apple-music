from pypresence import Presence
import time
import os

client_id = '667394345279684626'  # This is mine, I think it's reusable by all?
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

current_song = os.popen('osascript getsong.scpt').read()
print(RPC.update(state=current_song)) # initial presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
    current_song = applescript.run('getsong.scpt')
    print(RPC.update(state=current_song.out)) # updated presence
