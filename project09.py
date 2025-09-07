import tkinter as tk
from tkinter import messagebox
import subprocess

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL.")
        return
    
    try:
        # Run yt-dlp command (downloads highest quality mp4+audio)
        subprocess.run(["yt-dlp", "-f", "best", url], check=True)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video.\n{e}")

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader - Day 9")
root.geometry("500x220")
root.resizable(False, False)
root.config(bg="#111")

title_label = tk.Label(root, text="YouTube Video Downloader", font=("Poppins", 16, "bold"), bg="#111", fg="#1DB954")
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#111")
frame.pack(pady=10)

url_label = tk.Label(frame, text="Enter YouTube URL:", font=("Poppins", 12), bg="#111", fg="white")
url_label.grid(row=0, column=0, padx=5)

url_entry = tk.Entry(frame, width=40, font=("Poppins", 12))
url_entry.grid(row=0, column=1, padx=5)

download_btn = tk.Button(root, text="Download", font=("Poppins", 12, "bold"),
                         bg="#1DB954", fg="black", relief="flat", padx=20, pady=10,
                         command=download_video)
download_btn.pack(pady=20)

footer = tk.Label(root, text="Day 9 of 30-Day Coding Challenge | Aryan Sunil", 
                  font=("Poppins", 9), bg="#111", fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
