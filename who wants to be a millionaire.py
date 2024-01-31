"""
Name: Nevetha Magendran and Jahena Orthi
Class Assignment: ICS 4U1
Date: 01-30-2024
Description: Devi-themed Who Wants to Be a Millionaire
"""
# imports
from tkinter import Tk, Label, Button, PhotoImage, Frame, Entry
import random
from bankofquestions import bankofquestions
import pygame
import time
from tkinter import Label
import cv2
from PIL import Image, ImageTk
from tkVideoPlayer import TkinterVideo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



root = Tk()
root.title("Who Wants to Be")
root.geometry("1300x700")


class WhoWantsToBe_:

    def __init__(self, master):
        pygame.mixer.init()
        root.config(cursor="heart")

        self.master = master
        master.title("Who Wants to Be A Millionaire?")
        master.geometry("1300x600")

        #copying questions
        self.questions = bankofquestions.copy()
        random.shuffle(self.questions)

        #frames
        self.introScreen = Frame(master, width=1300, height=600)

            #rules frame
        self.RulesFrame = Frame(master, width=1300, height=600)

            #name & details frame
        self.PlayerInfoFrame = Frame(master, width=1300, height=600)

            # background
        self.BackgroundFrame = Frame(master, width=1300, height=600)
        self.BackgroundFrame = Frame(master, width=1300, height=600)

            #image on background
        self.background = PhotoImage(file="maingamescreen.png")
        self.b_image = Label(self.BackgroundFrame, image=self.background)
        self.b_image.pack()

            #image for rules screen
        self.rules = PhotoImage(file="rules.png")
        self.rules_img = Label(self.RulesFrame,image=self.rules)
        self.rules_img.place(x=0, y=0)

            #rules button
        self.RulesButton = Button(master, text="Got it, Next!", command=self.ShowInfoDetails,font=("Arial", 25,'bold'))
        self.RulesButton.place(x=500, y=525)

            #entry page
        self.questions_img = PhotoImage(file="questions.png")
        self.q_img = Label(self.PlayerInfoFrame, image=self.questions_img)
        self.q_img.pack()

            #age entry
        self.Intro_name = Entry(self.PlayerInfoFrame)
        self.Intro_name.place(x=352,y=265-55)

            #name entry
        self.Intro_age = Entry(self.PlayerInfoFrame)
        self.Intro_age.place(x=352,y=365-75)

            #place entry
        self.Intro_place = Entry(self.PlayerInfoFrame)
        self.Intro_place.place(x=352,y=465-85)


        #buttons for confidence
        #worried
        self.buttonworried = Button(self.PlayerInfoFrame,text='Worried',command=self.buttonworriedv)
        self.buttonworried.place(x=400,y=583-65)
        #medium
        self.buttongood = Button(self.PlayerInfoFrame, text='Good', command=self.buttongoodv,bg='yellow')
        self.buttongood.place(x=592, y=583 - 65)
        #very confident
        self.buttonamazing= Button(self.PlayerInfoFrame, text='Amazing', command=self.buttonamazingv,bg='yellow')
        self.buttonamazing.place(x=785, y=583 - 65)

        #button for gamescreen
        self.Start = Button(self.PlayerInfoFrame,text='Enter',command=self.ShowGameScreen,font=("Arial", 35,'bold'))
        self.Start.place(x=984,y=460)

        #labels
        self.balancelabel = Label(self.master, text="")
        self.balancelabel.place_forget()
        self.questionlabel = Label(self.master, text="",font=("Arial", 15))
        self.questionlabel.place_forget()
        self.winlosslabel = Label(self.master, text="",font=("Arial", 14,'bold'))
        self.winlosslabel.place_forget()

        #running intro screen
        self.introScreenPlace()

        # variables
        self.maxq = 15
        self.qn = 0
        self.balance = 0
        self.reward = 0
        self.removeoption = 1
        self.bankfive = False
        self.bankten = False

        #button image for no button
        self.walkaway = PhotoImage(file='walkaway.png')
        self.walkawayimg_label = Label(self.master, image=self.walkaway)

        #yes/no buttons
        self.nbutton = Button(self.master, image=self.walkaway, command=self.no, state="normal")
        self.nbutton.place_forget()
        self.ybutton = Button(self.master, text="Yes", font=("Arial", 35),command=self.GetQuestion, state="disabled")
        self.ybutton.place_forget()

        #buttons for choices
        self.option1 = Button(self.master, text=f"",font=("Arial", 35),command=self.choice1)
        self.option1.place_forget()
        self.option2 = Button(self.master, text=f"",font=("Arial", 35), command=self.choice2)
        self.option2.place_forget()
        self.option3 = Button(self.master, text=f"",font=("Arial", 35), command=self.choice3)
        self.option3.place_forget()
        self.option4 = Button(self.master, text=f"",font=("Arial", 35), command=self.choice4)
        self.option4.place_forget()
        self.callf = True

        #import image
        self.fiftyimg = PhotoImage(file='fiftyfifty.png')
        #label of image
        self.fiftyfiftyimg_label = Label(self.master, image=self.fiftyimg)
        # Create a button and pass the image
        self.fflabel = Button(self.master, bg='maroon1', image=self.fiftyimg, command=lambda:(self.fiftyfifty(),self.playfiftyfifty()))
        self.fflabel.place_forget()

        #audience image button
        self.audienceimg = PhotoImage(file='audience.png')
        self.audienceimg_label = Label(self.master, image=self.audienceimg)
        self.askaudience = Button(self.master, image=self.audienceimg, command=lambda:(self.askaudiencef(),self.playaudience()))
        self.askaudience.place_forget()
        self.callimg = PhotoImage(file='phone.png')

        # label of image
        self.callimg_label = Label(self.master, image=self.callimg)
        self.call = Button(self.master, image=self.callimg,command=self.callafriend)
        self.call.place_forget()
        self.audienceanswer = Label(self.master, text="")
        self.response = 0

        # placing score
        self.scoreimg = PhotoImage(file='scoreboard.png')
        self.scoreimg_label = Label(self.master, image=self.scoreimg)
        self.scoreimg_label.place_forget()

        #intro music
        self.master.after(1,pygame.mixer.music.load('intro.mp3'))
        pygame.mixer.music.play(0)
        self.audioloop = 1

        #settings image
        self.settingsimg = PhotoImage(file='settings2.png')

        # Create a label for the image
        self.settings_label = Label(self.master, image=self.settingsimg)

        #settings button
        self.settingsbutton = Button(self.master,image=self.settingsimg,command=lambda: self.settingson() if self.settingsstatus == 0 else self.settingsoff())
        self.settingsbutton.place(x=20,y=520)

        #MUTE
        self.muteimg = PhotoImage(file='mute.png')
        self.unmuteimg = PhotoImage(file='unmute.png')

        self.mutebutton = Button(self.master,text="Mute",command=lambda: self.mute() if self.mutestatus ==1 else self.unmute(),image=self.muteimg)
        self.mutestatus = 1

        #camera frame
        self.camera_frame = Frame(master, width=50, height=50)
        self.camera_frame.place_forget()  # Adjust the padding as needed

        #initializing camera
        self.video_capture = cv2.VideoCapture(0)  # Use 0 for default camera, adjust as needed

        #label for camera
        self.camera_label = Label(self.camera_frame)
        self.camera_label.pack()

        #tracking lifelines
        self.settingsstatus = 0
        self.mutestatus = 1
        self.lifelinefifty = True
        self.lifelinecallfriend = True
        self.lifelineaudience = True

        #30 sec timer
        self.timer_label = Label(self.master, text="")
        self.timer_label.place_forget()

        #video
        self.video_player = TkinterVideo(master=self.master)
        self.video_player.load("introvideo.mp4")
        self.video_player.pack(expand=True, fill="both")
        self.video_player.play()

    #functions
    def timer(self):
        self.timer_label.place(x=600, y=20)
        if self.time > 0:
            self.timer_label.config(text=f"Time Left: {self.time} seconds")
            self.time -= 1
            self.master.after(1000, self.timer)
        elif self.time == 0:
            #no time left
            self.timeimage = PhotoImage(file="timer.png")
            self.timerimg = Label(self.master, image=self.timeimage)
            self.timerimg.pack()
            pygame.mixer.music.load('timerdone.mp3')
            pygame.mixer.music.play(-1)
            self.audioloop = 1

    def stoptimer(self):
        self.time = -1

    def buttonworriedv(self):
        #???
        self.confidence = ["worried","worry","Worried"]
        self.buttonworried.config(state="disabled")
        self.buttongood.config(state="disabled")
        self.buttonamazing.config(state="disabled")

    def playfiftyfifty(self):
        #plays fifty fifty music
        pygame.mixer.music.load('fiftyfifty.mp3')
        pygame.mixer.music.play(0)
        self.audioloop = 1

    def playaudience(self):
        #plays ask the audience music
        pygame.mixer.music.load('asktheaudience.mp3')
        pygame.mixer.music.play(0)
        self.audioloop = 1

    def buttongoodv(self):
        #confidence level good
        self.confidence = ["good","Good"]
        self.buttonworried.config(state="disabled")
        self.buttongood.config(state="disabled")
        self.buttonamazing.config(state="disabled")
    def buttonamazingv(self):
        #confidence level amazing
        self.confidence = ["amazing","Amazing"]
        self.buttonworried.config(state="disabled")
        self.buttongood.config(state="disabled")
        self.buttonamazing.config(state="disabled")

    def update_camera(self):
        #frame information stores tupe from video capture
        frame_info = self.video_capture.read()

        if frame_info[0]:
            captured = True
            frame = frame_info[1]
            # Further processing of the frame...
        else:
            captured = False

        if captured:
            frame = cv2.resize(frame, (220, 150))
            if self.callf == False:
                self.camera_frame.place(x=780, y=65)
            elif self.callf == True:
                self.camera_frame.place(x=1000, y=65)
            elif self.callf == 3:
                self.camera_frame.place(x=853, y=362-65)
            elif self.callf == 4:
                self.camera_frame.place(x=962, y=267-65)

            #displaying image
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image = ImageTk.PhotoImage(image)

            # Update the label to display the camera feed
            self.camera_label.config(image=image)
            self.camera_label.image = image

        #updating camera
        self.BackgroundFrame.after(10, self.update_camera)

    def settingsoff(self):
        self.settingsstatus -= 1
        self.mutebutton.pack_forget()

    def settingsoff(self):
        self.settingsstatus -= 1
        self.mutebutton.place_forget()

    def settingson(self):
        self.mutebutton.place(x=27,y=470)
        self.settingsstatus = 1

    def mute(self):
        self.mutebutton.config(image=self.unmuteimg)
        self.mutebutton.place(x=27,y=470)
        pygame.mixer.music.pause()
        self.audioloop = 0
        self.mutestatus = 0

    def unmute(self):
        self.mutebutton.config(image=self.muteimg)
        self.mutebutton.place(x=27, y=470)
        pygame.mixer.music.unpause()
        self.audioloop = 1
        self.mutestatus = 1

    def ShowGameScreen(self):
        #start gamescreen
        self.age = self.Intro_age.get()
        self.name = self.Intro_name.get()
        self.place = self.Intro_place.get()
        self.GetQuestion()
        self.update_camera()
        self.PlayerInfoFrame.destroy()
        self.Start.destroy()
        self.BackgroundFrame.place(x=0, y=0)
        self.camera_frame.place(x=0, y=0)

    def introScreenPlace(self):
        self.age = str(self.Intro_age.get())
        self.name = str(self.Intro_name.get())
        self.place = str(self.Intro_place.get())
        self.introScreen.place(x=0, y=0)
        self.RulesFrame.place_forget()
        self.PlayerInfoFrame.place_forget()
        self.BackgroundFrame.place_forget()
        self.RulesButton.place_forget()
        self.introScreen.after(22000, self.RulesScreenPlace)

    def RulesScreenPlace(self):
        self.video_player.pack_forget()
        pygame.mixer.music.load('rules.mp3')
        pygame.mixer.music.play(0)
        self.audioloop = 1
        self.introScreen.destroy()
        self.RulesFrame.place(x=0,y=0)
        self.RulesButton.place(x=500, y=525)
        self.BackgroundFrame.place_forget()
        self.PlayerInfoFrame.place_forget()


    def ShowInfoDetails(self):
        #Starts music
        self.start_background_music()
        self.RulesFrame.destroy()
        self.RulesButton.destroy()
        self.PlayerInfoFrame.place(x=0, y=0)

    def askaudiencef(self):

        #ask the audience
        self.lifelineaudience = False
        self.fflabel.config(state="disabled")
        self.askaudience.config(state="disabled")
        self.call.config(state="disabled")
        self.askaudienceimg = PhotoImage(file="audiencegraph.png")
        self.askaudiencephoto = Label(self.master, image=self.askaudienceimg)
        self.askaudiencephoto.pack()

        # right answer is weight 70 and all wrong answers are weighted 10 percent.
        w1 = 70 if self.question["choices"][0] == self.question["answer"] else 10
        w2 = 70 if self.question["choices"][1] == self.question["answer"] else 10
        w3 = 70 if self.question["choices"][2] == self.question["answer"] else 10
        w4 = 70 if self.question["choices"][3] == self.question["answer"] else 10
        self.response = random.choices(self.question["choices"], weights=[w1,w2,w3,w4],k=1)
        self.audienceanswer.config(text=f"Audience Says: {self.response}")

        #creates a graph
        self.graph([w1, w2, w3, w4])

    def graph(self, weights):
        #creating graph
        fig, ax = plt.subplots(figsize=(6,4))
        ax.bar([f"{self.question['choices'][0]}", f"{self.question['choices'][1]}", f"{self.question['choices'][2]}", f"{self.question['choices'][3]}"], weights)
        ax.set_title("Audience Poll",fontsize=8)
        ax.set_ylabel("Audience Choice",fontsize=8)
        ax.set_xticks([0, 1, 2, 3])
        ax.set_xticklabels([f"{self.question['choices'][0]}", f"{self.question['choices'][1]}", f"{self.question['choices'][2]}", f"{self.question['choices'][3]}"],fontsize=8)

        #displaying the graph
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().place(x=350,y=200-65)
        self.master.after(10000,self.askaudiencephoto.destroy)
        self.master.after(10000, canvas.get_tk_widget().destroy)
    def changebackground(self):
        self.camera_frame.place(x=1000, y=65)
        self.b_image.config(image=self.background)
        self.callf = True
        self.b_image.pack()

    def millwin(self):
        self.stoptimer()
        #Commands for if the player gets to the end
        #forgetting buttons/labels
        self.balancelabel.place_forget()
        self.questionlabel.place_forget()
        self.ybutton.place_forget()
        self.fflabel.place_forget()
        self.call.place_forget()
        self.nbutton.place_forget()
        self.askaudience.place_forget()
        self.scoreimg_label.place_forget()
        self.option1.place_forget()
        self.option2.place_forget()
        self.option3.place_forget()
        self.option4.place_forget()

        #win image
        self.win = PhotoImage(file="bigwin.png")
        self.b_image.config(image=self.win)
        self.callf = 4
        self.b_image.pack()

        #winner music
        pygame.mixer.music.load('winnermusic.mp3')
        pygame.mixer.music.play(0)

    def lwin(self):
        #timer
        self.stoptimer()
        #photo
        self.win = PhotoImage(file="winloss.png")
        self.b_image.config(image=self.win)
        self.callf = 3
        self.b_image.pack()
        #forgetting buttons/labels
        self.scoreimg_label.place_forget()
        self.option1.place_forget()
        self.option2.place_forget()
        self.option3.place_forget()
        self.option4.place_forget()
        #music
        pygame.mixer.music.load('winnermusic.mp3')
        pygame.mixer.music.play(0)

    def callafriend(self):
        self.lifelinecallfriend = False
        self.fflabel.config(state="disabled")
        self.askaudience.config(state="disabled")
        self.call.config(state="disabled")
        self.callf = False
        self.callafriendimg = PhotoImage(file="callfriendscreen.png")
        self.b_image.config(image=self.callafriendimg)
        self.b_image.pack()
        self.winlosslabel.config(text="Say your question!")
        self.fflabel.config(state="disabled")
        pygame.mixer.Sound(f"{self.question["audio"]}")
        pygame.mixer.music.load(f"{self.question["audio"]}")
        pygame.mixer.music.play(loops=1)
        self.audioloop -=1
        root.after(15000, self.start_background_music)
        self.master.after(15000,self.changebackground)

    def start_background_music(self):
        # Load and start playing the background music
        pygame.mixer.music.load('wwtnm.mp3')
        pygame.mixer.music.play(-1)

    def fiftyfifty(self):
        self.lifelinefifty = False
        self.winlosslabel.config(text="Let's eliminate two choices!")
        self.fflabel.config(state="disabled")
        self.askaudience.config(state="disabled")
        self.call.config(state="disabled")

        self.master.after(3000, self.start_background_music)
        # variables
        correctans = self.question["answer"]
        choices = self.question["choices"]
        # list of options
        choiceslist = [0, 1, 2, 3]
        #bank
        self.bankfive = False
        self.bankten = False

        # Shuffles through choices
        random.shuffle(choiceslist)

        # loop through randomly
        for x in choiceslist:
            if choices[x] != correctans and self.removeoption >= 0:
                if x == 0:
                    self.option1.place_forget()
                    self.removeoption -= 1
                elif x == 1:
                    self.option2.place_forget()
                    self.removeoption -= 1
                elif x == 2:
                    self.option3.place_forget()
                    self.removeoption -= 1
                elif x == 3:
                    self.option4.place_forget()
                    self.removeoption -= 1

    def no(self):
        #if player decides to walk away
        self.option1.place_forget()
        self.option2.place_forget()
        self.option3.place_forget()
        self.option4.place_forget()
        self.fflabel.config(state="disabled")
        self.askaudience.config(state="disabled")
        self.call.config(state="disabled")
        self.nbutton.config(state="disabled")
        self.winlosslabel.config(text=f"Congratulations {self.name} from {self.place}! You won ${self.balance}",font=("Arial", 40,'bold'),fg="yellow",bg="black")
        self.winlosslabel.place(x=108, y=100)
        self.balancelabel.place_forget()
        self.questionlabel.place_forget()
        self.ybutton.place_forget()
        self.fflabel.place_forget()
        self.call.place_forget()
        self.nbutton.place_forget()
        self.askaudience.place_forget()
        self.lwin()


        # getting question

    def GetQuestion(self):
        self.time = 30
        self.timer()

        if self.lifelinefifty:
            self.fflabel.config(state="normal")
        if self.lifelinecallfriend:
            self.call.config(state="normal")
        if self.lifelineaudience:
            self.askaudience.config(state="normal")

        self.start_background_music()
        self.nbutton.config(state="disabled")
        self.ybutton.place_forget()
        self.ybutton.config(state="disabled")
        self.winlosslabel.place_forget()
        self.scoreimg_label.place(x=1110, y=320)
        self.askaudience.place(x=0,y=200)
        self.call.place(x=0,y=113)
        self.fflabel.place(x=0,y=23)
        self.nbutton.place(x=0,y=288)


        if self.maxq > 0:
            # track of how many questions left
            self.maxq -= 1
            self.qn += 1
            # Money reward for each question
            self.rewards = [1000000, 500000, 250000, 125000, 64000, 32000, 16000, 8000, 4000, 2000, 1000, 500, 300, 200,100]


            # getting question
            self.question = self.questions.pop(0)

            # displaying question
            self.questionlabel.config(text=f"{self.qn}. {self.question['question']}")
            self.questionlabel.place(x=265,y=310)
            self.balancelabel.config(text=f"Balance: ${self.balance}")
            self.balancelabel.place(x=1154,y=350-65)

            # displaying buttons
            self.option1.config(text=f"{self.question['choices'][0]}", state="normal")
            self.option1.place(x=245,y=477-65)
            self.option2.config(text=f"{self.question['choices'][1]}", state="normal")
            self.option2.place(x=716,y=477-65)
            self.option3.config(text=f"{self.question['choices'][2]}", state="normal")
            self.option3.place(x=245,y=577-65)
            self.option4.config(text=f"{self.question['choices'][3]}", state="normal")
            self.option4.place(x=716, y=577-65)
            if self.maxq == 10:
                self.bankten = False
                self.bankfive = True
            elif self.maxq == 5:
                self.bankten = True
                self.bankfive = False

        else:
            self.winloss.config(text="GAME OVER! HAHA")

    def choice1(self):
        self.stoptimer()

        #If player picks button 1
        self.option1.config(state="disabled")
        self.option2.config(state="disabled")
        self.option3.config(state="disabled")
        self.option4.config(state="disabled")
        self.nbutton.config(state="normal")
        c1 = self.question["choices"][0]

        # if answer is right
        self.winlosslabel.place(x=472, y=100)
        if c1 == self.question["answer"]:
            self.winlosslabel.place(x=472, y=100)
            self.balance = self.rewards[self.maxq]
            self.balancelabel.config(text=f"Balance: ${self.balance}")
            if self.maxq > 0:
                self.winlosslabel.config(text=f"Correct {self.name}! Would you like to continue?")
                self.questionlabel.place_forget()
                self.ybutton.config(state="normal")
                self.ybutton.place(x=600, y=260-65)
            elif self.maxq == 0:
                self.questionlabel.place_forget()
                self.winlosslabel.config(text=f"GAME OVER! {self.name} from {self.place} WON $1 000 000",font=("Arial", 40,'bold'),fg="yellow",bg="black")
                self.winlosslabel.place(x=108, y=100)
                self.millwin()

            # removing display of choice buttons
            self.option1.pack_forget()
            self.option2.pack_forget()
            self.option3.pack_forget()
            self.option4.pack_forget()

        #If button 1 was wrong
        elif c1 != self.question["answer"]:
            self.stoptimer()
            self.questionlabel.place_forget()
            self.questionlabel.place_forget()
            self.winlosslabel.config(text=f"YOU LOST {self.name}!")
            self.winlosslabel.place(x=472, y=100)

            if self.bankten == True:
                self.stoptimer()
                self.balance = 32000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

            elif self.bankfive == True:
                self.stoptimer()
                self.balance = 1000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

    def choice2(self):
        self.stoptimer()
        # If player picks button 2
        self.winlosslabel.place(x=472, y=100)
        self.option1.config(state="disabled")
        self.option2.config(state="disabled")
        self.option3.config(state="disabled")
        self.option4.config(state="disabled")
        self.nbutton.config(state="normal")

        c2 = self.question["choices"][1]        # if answer is right

        # If button 2 is the correct answer
        if c2 == self.question["answer"]:
            self.stoptimer()
            self.winlosslabel.place(x=472, y=100)
            self.questionlabel.place_forget()
            self.balance = self.rewards[self.maxq]
            self.balancelabel.config(text=f"Balance: ${self.balance}")
            if self.maxq > 0:
                self.stoptimer()
                self.winlosslabel.config(text=f"Good job {self.name}! You are correct! Would you like to continue?")
                self.ybutton.config(state="normal")
                self.ybutton.place(x=600, y=260-65)
            elif self.maxq == 0:
                self.stoptimer()
                self.winlosslabel.config(text=f"GAME OVER! {self.name} from {self.place} WON $1 000 000!!",font=("Arial", 40,'bold'),fg="yellow",bg="black")
                self.winlosslabel.place(x=108, y=100)
                self.millwin()

            self.option1.pack_forget()
            self.option2.pack_forget()
            self.option3.pack_forget()
            self.option4.pack_forget()
        #if button 2 is wrong
        elif c2 != self.question["answer"]:
            self.stoptimer()
            self.questionlabel.place_forget()
            self.questionlabel.place_forget()
            self.winlosslabel.config(text=f"YOU LOST {self.name}!")
            self.winlosslabel.place(x=472, y=100)
            if self.bankten == True:
                self.stoptimer()
                self.balance = 32000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

            elif self.bankfive == True:
                self.stoptimer()
                self.balance = 1000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

    def choice3(self):
        self.stoptimer()
        # If player picks button 3
        self.winlosslabel.place(x=472, y=100)
        self.option1.config(state="disabled")
        self.option2.config(state="disabled")
        self.option3.config(state="disabled")
        self.option4.config(state="disabled")
        self.nbutton.config(state="normal")
        c3 = self.question["choices"][2]
        # if answer is right
        if c3 == self.question["answer"]:
            self.stoptimer()
            self.questionlabel.place_forget()
            self.balance = self.rewards[self.maxq]
            self.balancelabel.config(text=f"Balance: ${self.balance}")
            if self.maxq > 0:
                self.stoptimer()
                self.winlosslabel.config(text=f"Good job {self.name}! You are correct! Would you like to continue?")
                self.winlosslabel.place(x=472, y=100)
                self.ybutton.config(state="normal")
                self.ybutton.place(x=600, y=260-65)
                self.stoptimer()
            elif self.maxq == 0:
                self.winlosslabel.config(text=f"GAME OVER! {self.name} from {self.place} WON $1 000 000",font=("Arial", 40,'bold'),fg="yellow",bg="black")
                self.millwin()
                self.winlosslabel.place(x=108, y=100)

            self.option1.pack_forget()
            self.option2.pack_forget()
            self.option3.pack_forget()
            self.option4.pack_forget()
        #if answer is wrong
        elif c3 != self.question["answer"]:
            self.stoptimer()
            self.questionlabel.place_forget()
            self.questionlabel.place_forget()
            self.questionlabel.place_forget()
            self.winlosslabel.config(text=f"YOU LOST {self.name}!")
            self.winlosslabel.place(x=472, y=100)
            if self.bankten == True:
                self.stoptimer()
                self.balance = 32000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

            elif self.bankfive == True:
                self.stoptimer()
                self.balance = 1000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

    def choice4(self):
        self.stoptimer()
        #if player picks button 4
        self.winlosslabel.place(x=472, y=100)
        self.option1.config(state="disabled")
        self.option2.config(state="disabled")
        self.option3.config(state="disabled")
        self.option4.config(state="disabled")
        self.nbutton.config(state="normal")
        c4 = self.question["choices"][3]

        # if answer is right
        if c4 == self.question["answer"]:
            self.stoptimer()
            self.questionlabel.place_forget()
            self.balance = self.rewards[self.maxq]
            self.balancelabel.config(text=f"Balance: ${self.balance}")
            self.winlosslabel.place(x=472, y=100)

            if self.maxq > 0:
                self.stoptimer()
                self.winlosslabel.config(text=f"Good job {self.name}! You are correct! Would you like to continue?")
                self.ybutton.config(state="normal")
                self.ybutton.place(x=600, y=260-65)
            elif self.maxq == 0:
                self.stoptimer()
                self.winlosslabel.config(text=f"GAME OVER! {self.name} from {self.place} WON $1 000 000",font=("Arial", 40,'bold'),fg="yellow",bg="black")
                self.winlosslabel.place(x=108, y=100)
                self.millwin()

            self.option1.pack_forget()
            self.option2.pack_forget()
            self.option3.pack_forget()
            self.option4.pack_forget()

        #if answer is wrong
        elif c4 != self.question["answer"]:
            self.questionlabel.place_forget()
            self.questionlabel.place_forget()
            self.winlosslabel.config(text="YOU LOST!")
            self.winlosslabel.place(x=472, y=100)
            
            if self.bankten == True:
                self.stoptimer()
                self.balance = 32000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

            elif self.bankfive == True:
                self.stoptimer()
                self.balance = 1000
                self.winlosslabel.config(text=f"YOU LOST {self.name}!! You still take ${self.balance} back to {self.place}!")
                self.winlosslabel.place(x=472, y=100)
                self.lwin()

root.geometry("1300x600")
my_gui = WhoWantsToBe_(root)
root.mainloop()