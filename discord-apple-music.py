from pypresence import Presence
import time
import applescript

client_id = '667394345279684626'  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

current_song = applescript.run('getsong.scpt')
#print(RPC.update(state="Playing", details=current_song.out))  # Set the presence
print(RPC.update(state=current_song.out))

while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
    current_song = applescript.run('getsong.scpt')
    #print(RPC.update(state="Playing", details=current_song.out))  # Set the presence
    print(RPC.update(state=current_song.out))
