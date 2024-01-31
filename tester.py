import tkinter as tk
from tkVideoPlayer import TkinterVideo


# Create the main window
master = tk.Tk()
master.title("Video Player")

# Create and pack the video player
videoplayer = TkinterVideo(master=master)
videoplayer.set_scaled(1.0)
videoplayer.load("introvideo.mp4")
videoplayer.pack(expand=True, fill="both")

# Play the video
videoplayer.play()

# Run the Tkinter main loop
master.mainloop()