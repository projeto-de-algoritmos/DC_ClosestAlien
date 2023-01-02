import random
import tkinter as tk
from PIL import ImageTk, Image
from algorithms import calculateInversions

def openMenu():
  class Drag_and_Drop_Listbox(tk.Listbox):
    def __init__(self, master, **kw):
      kw['selectmode'] = tk.MULTIPLE
      kw['activestyle'] = 'none'
      tk.Listbox.__init__(self, master, kw)
      self.bind('<Button-1>', self.getState, add='+')
      self.bind('<Button-1>', self.setCurrent, add='+')
      self.bind('<B1-Motion>', self.shiftSelection)
      self.curIndex = None
      self.curState = None
      self.currentOrder = None
    def showOrder(self):
      list = self.get(0, tk.END)
      self.currentOrder = list
      root.destroy()
    def setCurrent(self, event):
      self.curIndex = self.nearest(event.y)
    def getState(self, event):
      i = self.nearest(event.y)
      self.curState = self.selection_includes(i)
    def shiftSelection(self, event):
      i = self.nearest(event.y)
      if self.curState == 1:
        self.selection_set(self.curIndex)
      else:
        self.selection_clear(self.curIndex)
      if i < self.curIndex:
        x = self.get(i)
        selected = self.selection_includes(i)
        self.delete(i)
        self.insert(i+1, x)
        if selected:
          self.selection_set(i+1)
        self.curIndex = i
      elif i > self.curIndex:
        x = self.get(i)
        selected = self.selection_includes(i)
        self.delete(i)
        self.insert(i-1, x)
        if selected:
          self.selection_set(i-1)
        self.curIndex = i

  root = tk.Tk()
  root.geometry("800x950")
  root.title("Escolha Musical!")

  listbox = Drag_and_Drop_Listbox(root, font=('Script', 12))
  label = tk.Label(root, text="Antes de começarmos o jogo, classifique os doze instrumentos musicais abaixo do que mais gosta (no topo) para o que menos gosta (no final) para escolhermos uma trilha sonora para o seu jogo usando o cálculo de inversões!", font=('Arial', 14), wraplength=700, justify="center")

  img = ImageTk.PhotoImage(Image.open("./images/logo.png"))
  panel = tk.Label(root, image = img)
  panel.pack(side = "top")

  label.pack(pady=5)

  instructions = tk.Label(root, text="Clique e arraste cada instrumento para a ordem desejada.", font=('Arial', 10), wraplength=700, justify="center")
  instructions.pack(pady=5)

  bossanova = [
    'Violão'
    , 'Piano'
    , 'Flauta'
    , 'Trompete'
    , 'Vocal'
    , 'Baixo'
    , 'Saxofone'
    , 'Contrabaixo'
    , 'Guitarra'
    , 'Sintetizador'
    , 'Beatbox'
    , 'Bateria'
  ]

  dubstep = [
    'Sintetizador'
    , 'Baixo'
    , 'Beatbox'
    , 'Vocal'
    , 'Contrabaixo'
    , 'Bateria'
    , 'Piano'
    , 'Trompete'
    , 'Guitarra'
    , 'Saxofone'
    , 'Violão'
    , 'Flauta'
  ]

  hiphop = [
    'Sintetizador'
    , 'Beatbox'
    , 'Baixo'
    , 'Vocal'
    , 'Contrabaixo'
    , 'Saxofone'
    , 'Piano'
    , 'Violão'
    , 'Trompete'
    , 'Bateria'
    , 'Guitarra'
    , 'Flauta'
  ]

  jazz = [
    'Trompete'
    , 'Baixo'
    , 'Contrabaixo'
    , 'Piano'
    , 'Bateria'
    , 'Violão'
    , 'Vocal'
    , 'Flauta'
    , 'Saxofone'
    , 'Sintetizador'
    , 'Guitarra'
    , 'Beatbox'
  ]

  pop = [
    'Vocal'
    , 'Violão'
    , 'Piano'
    , 'Guitarra'
    , 'Saxofone'
    , 'Baixo'
    , 'Sintetizador'
    , 'Trompete'
    , 'Bateria'
    , 'Contrabaixo'
    , 'Flauta'
    , 'Beatbox'
  ]

  rock = [
    'Guitarra'
    , 'Bateria'
    , 'Contrabaixo'
    , 'Violão'
    , 'Vocal'
    , 'Piano'
    , 'Flauta'
    , 'Trompete'
    , 'Saxofone'
    , 'Sintetizador'
    , 'Baixo'
    , 'Beatbox'
  ]

  genres = [
    ('Bossa Nova', bossanova)
    , ('Dubstep', dubstep)
    , ('Hip Hop', hiphop)
    , ('Jazz', jazz)
    , ('Pop', pop)
    , ('Rock', rock)
  ]

  instruments = [
    'Violão'
    , 'Piano'
    , 'Flauta'
    , 'Trompete'
    , 'Saxofone'
    , 'Contrabaixo'
    , 'Sintetizador'
    , 'Baixo'
    , 'Beatbox'
    , 'Vocal'
    , 'Bateria'
    , 'Guitarra'
  ]

  shuffled = random.sample(instruments, len(instruments))

  i = 0
  for name in shuffled:
      listbox.insert(tk.END, name)
      if i % 2 == 0:
          listbox.selection_set(i)
      i +=1

  listbox.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

  btn=tk.Button(root, text="CONTINUAR", bg='#6dc62e', fg='#266116', command=listbox.showOrder, height=2, width=15)
  btn.pack(padx=20, pady=20)
  root.mainloop()

  choices = listbox.currentOrder
  instrumentsMap = {}

  for i in range(len(choices)):
    instrumentsMap[choices[i]] = i

  # print(instrumentsMap)
  # print(genres)

  inversions = {}

  for genre in genres:
    inversions[genre[0]] = calculateInversions(genre[1], instrumentsMap)

  new = sorted(inversions.items(), key=lambda x: x[1])
  print(new)
  return new
# print(listbox.currentOrder)

# choices = []
# for i in range(5):
#     print(f'O quanto você gosta de {instrumentos[i]}?')
#     choices.append(input())

# rock = [3,2,4,1,5]
# ri = inversions(rock, copy.copy(rock), 0, len(rock)-1)
# bossanova = [3,5,1,4,2]
# bi = inversions(bossanova, copy.copy(bossanova), 0, len(bossanova)-1)
# jazz = [2,4,5,3,1]
# ji = inversions(jazz, copy.copy(jazz), 0, len(jazz)-1)

# vi = sorted([(ri, 'rock'),(bi, 'bossa nova'),(ji, 'jazz')])
# print(vi)
# result = inversions(choices, copy.copy(choices), 0, len(choices)-1)

# print("Number of inversions are", result)