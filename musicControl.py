from pythonosc import dispatcher
from pythonosc import osc_server, udp_client
from pynput.keyboard import Key, Controller
import argparse

keyboard = Controller()

def osc_handler(address, *args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=8000, help="The port the OSC server is listening on")
    args2 = parser.parse_args()

    if address == "/avatar/parameters/musictoggle":
        print(address)
        if args[0]==True:
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause)

    elif address == "/avatar/parameters/musicskip":
        print(address)

        if args[0]==True:
            keyboard.press(Key.media_next)
            keyboard.release(Key.media_next)
    elif address == "/avatar/parameters/volume0":
        print(address)
        print(args[0]*-72+12)
        client = udp_client.SimpleUDPClient(args2.ip, args2.port)
        client.send_message("/vm/strip/7/gain", args[0]*-72+12)
         
           

if __name__ == "__main__":

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/avatar/parameters/*", osc_handler)

    ip = "127.0.0.1"  # Host. Change if you are recieving on a quest.
    port = 9001 
    server = osc_server.BlockingOSCUDPServer((ip, port), dispatcher)
    
    print(f"Listening for OSC messages on {ip}:{port}")

    server.serve_forever()
