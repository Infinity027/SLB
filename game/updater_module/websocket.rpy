
init python in websocket:


    import threading
    import socketio
    import store
    import time

    KEEP_RUNNING = False
    sio = socketio.Client(logger=True, engineio_logger=True)


    def run():
        global sio, KEEP_RUNNING
        print(f"Sio: Connect: {store.portal_url}")
        renpy.display.log.write(f"Sio: Stop: {store.portal_url}")
        sio.connect(store.portal_url)
        while KEEP_RUNNING:
            time.sleep(5)
            sio.emit("ping")
        else:
            stop()


    def stop():
        global KEEP_RUNNING
        KEEP_RUNNING = False
        print(f"Sio: Stop: {sio.sid}")
        renpy.display.log.write(f"Sio: Stop: {sio.sid}")
        sio.disconnect()


    @sio.event
    def after_connect(data):
        print(f"Sio: Connected to server: {sio.sid} {data.get('sid')}")
        renpy.display.log.write(f"Sio: Connected to server: {sio.sid} {data.get('sid')}")
        if data.get("sid"):
            store.persistent.sio_sid = data.get("sid")


    @sio.event
    def disconnect():
        global KEEP_RUNNING
        KEEP_RUNNING = False
        print(f"Disconnected from server: {sio.sid}")
        renpy.display.log.write(f"Sio: Disconnected from server")
        store.persistent.sio_sid = None


    @sio.on("authz_token")
    def get_authz_token(data):
        print(f"Client received data: {data}")
        renpy.display.log.write(f"Sio: Client received data {data}")
        store.persistent.authentication_token = data.get("authentication_token")
        store.persistent.authentication_provider = data.get("authentication_provider")
        store.persistent.portal_environment = data.get("portal_environment")


    @sio.on("*")
    def sio_catchall(data=None):
        print(f"Sio: Client catchall received data: {data}")
        renpy.display.log.write(f"Sio: Client catchall received data: {data}")


    def start():
        global KEEP_RUNNING
        if KEEP_RUNNING is False:
            KEEP_RUNNING = True
            thread = threading.Thread(target=run)
            thread.daemon = True
            thread.start()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
