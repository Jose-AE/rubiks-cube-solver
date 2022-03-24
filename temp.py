class GUI(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.start()

        def callback(self):
            self.root.quit()

        def run(self):
            #put all tk intern gui stuff in here so it can run at the same time as while loop

            window = Tk()

            window.geometry("420x420") #define size of window (not requiered)
            window.title("Mogliah") #name of the window (not requiered)
            window.iconphoto(True, PhotoImage(file="Images\\AppIcon.png"))

            

            window.mainloop()


GUI = GUI()