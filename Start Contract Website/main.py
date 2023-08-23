# -*- coding: utf-8 -*-
import tkinter as tk
#from tkinter import *
from PIL import ImageTk,Image
#import os

#class window(tk):
#    def __init__(self):
#        super(window,self).__init__()
window = tk.Tk()
window.title("StartContract")

#window2=tk.Tk()
#window2.title("DAOs")

frame = tk.Frame(window,bg="#DBCFC4")
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# frame.rowconfigure(0,weight=1)
# frame.rowconfigure(1,weight=1)
# frame.rowconfigure(2,weight=1)
# frame.rowconfigure(3,weight=1)
# frame.rowconfigure(4,weight=1)
# frame.rowconfigure(5,weight=1)

def community():
    window2=tk.Tk()
    window2.title("Community")
    communityDAO=tk.Label(window2,fg="#352314",font=('Gill Sans MT',11), text="We allow individuals to collectively own and govern assets, whether they're digital currencies, NFTs, or even physical assets tokenized on the blockchain.""\n"
                          " With web3, shared ownership becomes transparent, secure, and highly accessible, empowering communities to collaborate, make decisions,""\n"
                          " and benefit collectively from their shared resources,""\n"
                          " all while reducing the need for intermediaries and fostering a new era of democratized ownership.""\n"
                          "Explore different communities and build your own on Metis website:https://metis.io/")
    communityDAO.grid(column=0,row=7,pady=30,sticky="nsew")
    
    window2.mainloop()
    
def collaboration():
    window2=tk.Tk()
    window2.title("Collaboration")
    collaborationDAO=tk.Label(window2,fg="#352314",font=('Gill Sans MT',11), text="Smart contracts, a fundamental component of blockchain technology, empower users to trust each other and collaborate with unprecedented security and transparency.""\n"
                              " These self-executing contracts automatically enforce predefined rules and agreements without the need for intermediaries, ensuring that all parties involved in a ""\n"
                              "transaction or collaboration fulfill their obligations. Trust is established through code and cryptographic verification rather than relying on traditional intermediaries. ""\n"
                              "This eliminates the potential for fraud, reduces the risk of disputes, and enhances collaboration efficiency, ultimately fostering a new era of trust among individuals, businesses, ""\n"
                              "and organizations in the digital age.""\n"
                              "Create your own secure smart contracts using OpenZeppelin:https://www.openzeppelin.com/ and even automate it using Defender:https://www.openzeppelin.com/defender ")
    collaborationDAO.grid(column=0,row=7,pady=30,sticky="nsew")
    
    window2.mainloop()   
    
def decentralization():
    window2=tk.Tk()
    window2.title("Decentralization")
    decentralizationDAO=tk.Label(window2,fg="#352314",font=('Gill Sans MT',11),text="Web3 technology is transforming the way we conduct voting, introducing unprecedented transparency and inclusivity. ""\n"
                                 "Through the use of blockchain ledgers, the entire voting process becomes fully transparent and tamper-proof, with each vote recorded as an immutable transaction.""\n"
                                 " What's remarkable is that web3 enables users to vote anonymously, thanks to cryptographic techniques. ""\n"
                                 "This anonymity protects individual privacy while ensuring the integrity of the electoral process. With these innovations, web3 is paving the way for more secure, ""\n"
                                 "transparent, and democratic voting systems, promising to revolutionize governance, elections, and decision-making in a digital world. ""\n"
                                 "Explore Secret Society:https://scrt.network/ to see how to stay protected and anonymous on Web3. ")
    decentralizationDAO.grid(column=0,row=7,pady=30,sticky="nsew")
    
    window2.mainloop()
    
#logo=ImageTk.PhotoImage(Image.open("una"))
##logo =tk.ImageTK.PhotoImage(Image.open("C:\Users\Kylie\Downloads\Mrs.Goose.png"))
#logoLabel=tk.Label(frame,image=logo)
#logoLabel.place(x=0,y=0)    

greeting = tk.Label(frame, text="Welcome to Start Contract by UNA", font=(
    'Gill Sans Ultra Bold', 16), fg="#352314", bg="#C7BCB3", width=130, height=5)
greeting.grid(row=0, column=0)

description = tk.Label(frame,bg="#DBCFC4", font=('Gill Sans MT',11),
                       text="StartContract by UNA was created as a submission to the Ethwomen 2023 hackathon." "\n ""\n"
                       "Begin to explore by clicking one of the buttons below regarding what value you would like to pursue""\n"
                       "Web3 technology has made possible new forms of connecting. Explore your Values below to learn how they can encoded in future technology. ""\n""\n"
                       "Purpose: Guides users through an educational & applied journey of forming a DAO and employing Smart Contracts. ""\n"
                       "From pacts with your friends to your first shareholder's agreements, we guide you through a step-by-step process where you can learn first-hand how the future can be different.""\n"
                       "Details: An applied learning platform where we guide people through the process of creating a DAO and smart contracts. ""\n"
                       "The step-by-step process will explain each component and link to resources where users can create their own community with rules."
                       )
description.grid(row=1, column=0)

buttonOne = tk.Button(frame, font=('Candara',11),text="Community", width=15,
                      height=5, bg="#B3A497", fg="#352314", 
                      command=community
                      )
buttonOne.grid(row=2, column=0, padx=70, pady=30, sticky="w")

buttonTwo = tk.Button(frame, font=('Candara',11),text="Collaboration",
                      width=15, height=5, bg="#B3A497", fg="#352314", 
                      command=collaboration
                      )
buttonTwo.grid(row=2, column=0, padx=70, pady=30)

buttonThree = tk.Button(frame, font=('Candara',11),text="Decentralization",
                        width=15, height=5, bg="#B3A497", fg="#352314",
                        command=decentralization
                        )
buttonThree.grid(row=2, column=0, padx=70, pady=30, sticky="e")

enterName = tk.Label(frame, bg="#DBCFC4",fg="#494038", text="Enter the name of your new business!")
enterName.grid(row=4, column=0)
mybusiness = tk.Entry(frame, bg='#D8D0C9')
mybusiness.grid(row=5, column=0)
mybusiness.insert(0,"ex:Una")


def helloBusiness():
    hello="Hello " + mybusiness.get() + ", Welcome to Una"
    helloButton=tk.Label(text=hello,bg="#DBCFC4",fg="#352314")
    helloButton.place(x=550,y=140)
    
hellobutton=tk.Button(frame,fg="#352314",text="GO",command=helloBusiness)
hellobutton.grid(column=0,row=5,sticky="e",padx=545,pady=20)
 
#def show():
    #if clicked=CryptoChicks:
     #   links=tk.Label(frame,text="www.cc.com")
     #   links.place(x=50,y=50)
   
clicked = tk.StringVar()
clicked.set("Click Below to learn more about our bounty application companies")

drop = tk.OptionMenu(frame,clicked,"Click Below to Learn More", "Metis:https://metis.io/","OpenZepplin:https://www.openzeppelin.com/","Defender:https://www.openzeppelin.com/defender","Secret Society:https://scrt.network/")
drop.place(x=0,y=0)

#menuButton = tk.Button(frame, text= "Go", command=show)
#menuButton.place(x=20,y=20)

frame.pack(fill='x')
# frame.pack(fill='y')

# logo = tk.Image(file="Mrs.Goose")
# logoLabel=tk.Label(frame,logo=logo)
# logoLabel.grid(row=4,column=0)

# def handle_click(event):
#    window2=tk.Tk()
#    communityDAO.grid("nsew")
# buttonOne.bind("<Button-1>", handle_click)


window.mainloop()