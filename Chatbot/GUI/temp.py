import requests
import tkinter
import ast

root=tkinter.Tk()
root.geometry("275x525")
root.title("Innovate - Assistant")
root.resizable(0, 0)
text = tkinter.StringVar()
conversation=["Welcome to Innovate Yourself\n"]
text.set("\n".join(conversation))
big_label = tkinter.Label(root, textvariable="Welcome to Innovate Yourself.",
                          height=2,width=30,justify=tkinter.LEFT,
                          anchor='nw',font={"family":"Arial Black", "size":20})

big_label.grid(row=0, column=0, columnspan = 2)

label = tkinter.Label(root, textvariable=text,
                      height=25,width=30,justify=tkinter.LEFT,
                     anchor='nw',font={"family":"Arial Black", "size":20})
                      # yscrollcommand = scrollbar.set)
label.grid(row=1, column=0, columnspan = 2)

# scrollbar = tkinter.Scrollbar(root)
# scrollbar.pack( side = tkinter.RIGHT, fill = tkinter.Y )



# display=tkinter.Label(root,height=40,width=50)
# display.grid(row=0,column=0)

def ReadText():
    message=entry.get()
    conversation.append("User: "+message)
    text.set("\n".join(conversation))
    label.update()

    url = 'http://innovate-yourself.herokuapp.com/webhooks/rest/webhook'  ##change rasablog with your app name
    myobj = {
        "message": message,
        "sender": "Ashish",
    }
    entry.delete(0, 'end')
    x = requests.post(url, json=myobj)
    ast.literal_eval([{"recipient_id":"Ashish","text":"Hey! How are you?"}])
    print(ast.literal_eval(x.text))
    # conversation.append("Innovate: "+"\n".join([ast.literal_eval(x.text)[0]["text"].split(" ")[3*(i-1):3*(i-1)+3] if len(ast.literal_eval(x.text)[0]["text"].split(" "))//10 >10 else ast.literal_eval(x.text)[0]["text"] for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//10)]))

    reply=""
    if len(ast.literal_eval(x.text)[0]["text"].split(" ")) >9:
        for i in range(len(ast.literal_eval(x.text)[0]["text"].split(" "))//9 +1):
            reply+=" ".join(ast.literal_eval(x.text)[0]["text"].split(" ")[9 * (i - 1):9 * (i - 1) + 9]) + "\n"
    else:
        reply=ast.literal_eval(x.text)[0]["text"]
    conversation.append("Innovate: " + reply)

    print([list(i.keys())[1] for i in ast.literal_eval(x.text)])
    if 'image' in [list(i.keys())[1] for i in ast.literal_eval(x.text)]:
        def OpenImage():
            import webbrowser
            webbrowser.open(ast.literal_eval(x.text)[1]["image"].replace("\\",""))
        conversation.append("Innovate: " + ast.literal_eval(x.text)[1]["image"].replace("\\",""))
        b = tkinter.Button(root, text="Open Image",command=OpenImage).pack(...)
    text.set("\n".join(conversation))


entry=tkinter.Entry(root, width=38)
entry.grid(row=2, column=0, rowspan=50)
button=tkinter.Button(root,text="Send",command=ReadText)
button.grid(row=2, column=1)

# button.pack(side='bottom')
root.configure(background='green')
label.configure(background='green')
big_label.configure(background='yellow')

root.mainloop()
