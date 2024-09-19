import nltk

from textblob import TextBlob
from newspaper import Article
import tkinter as tk  
def summarize():
    url = u_1.get("1.0",'end').strip()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    t_1.config(state='normal')
    a_1.config(state='normal')
    p_1.config(state='normal')
    s_1.config(state='normal')
    se_1.config(state='normal')

    t_1.delete("1.0","end")
    t_1.insert("1.0",article.title)
    
    a_1.delete("1.0","end")
    a_1.insert("1.0",article.authors)

    p_1.delete("1.0","end")
    p_1.insert("1.0",article.publish_date)

    s_1.delete("1.0","end")
    s_1.insert("1.0",article.summary)


    check = TextBlob(article.text)
    sentiment = check.polarity

    se_1.delete("1.0","end")
    se_1.insert("1.0",f"Sentiment: {"Positive" if sentiment > 0 else "Negative"}")

    
    t_1.config(state='disabled')
    a_1.config(state='disabled')
    p_1.config(state='disabled')
    s_1.config(state='disabled')
    se_1.config(state='disabled')
   

    





    



root = tk.Tk()
root.title("News Summary")
root.geometry("1200x600")


tlabel = tk.Label(root,text="Title")
t_1 = tk.Text(root,height=1,width=140)
t_1.config(state="disabled",bg="#dddddd")
tlabel.pack()
t_1.pack()

alabel = tk.Label(root,text="Authors")
a_1 = tk.Text(root,height=1,width=140)
a_1.config(state="disabled",bg="#dddddd")
alabel.pack()
a_1.pack()


plabel = tk.Label(root,text="Publication date")
p_1 = tk.Text(root,height=1,width=140)
p_1.config(state="disabled",bg="#dddddd")
plabel.pack()
p_1.pack()

slabel = tk.Label(root,text="Summary")
s_1 = tk.Text(root,height=10,width=140)
s_1.config(state="disabled",bg="#dddddd")
slabel.pack()
s_1.pack()

selabel = tk.Label(root,text="Sentiment Analysis")
se_1 = tk.Text(root,height=1,width=140)
se_1.config(state="disabled",bg="#dddddd")
selabel.pack()
se_1.pack()

ulabel = tk.Label(root,text="URL")
u_1 = tk.Text(root,height=1,width=140)
ulabel.pack()
u_1.pack()

button = tk.Button(root,text="Summarize",command=summarize)
button.pack()



root.mainloop()



