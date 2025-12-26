import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

massaEletron = 9.109e-31
massaProton = 1.672e-27
luz = 3e8
hJ = 6.626E-34
hEV = 4.136E-15
conversao = 1.602E-19

arrayPis = []#Array com arrays de tamanhos variados de Pis para simulacao da onda
nPis = 1
while nPis <30:
    arrayPis.append(np.arange(0, nPis*np.pi, 0.01))
    nPis+=1

def notacaoCientifica(valor):
  if (valor > 0):
    if (valor > 999 or valor < 0.001):
      return "{:.3E}".format(valor)
    else:
      return "{:.3f}".format(valor)
  elif (valor != 0):
    if (valor < -999 or valor > -0.001):
      return "{:.3E}".format(valor)
    else:
      return "{:.3f}".format(valor)
  else:
    return "{:.3f}".format(valor)

class SimularParticulas:
  def __init__(self,root):
    w8 = Toplevel(root)
    w8.lift()
    w8.title("Simular Particula")
    mainframe8 = ttk.Frame(w8,padding=10)
    mainframe8.grid(column=0, row=0, sticky=(N, W, E, S))
    w8.columnconfigure(0, weight=1)
    w8.rowconfigure(0, weight=1)

    self.Massa = StringVar()
    self.Largura = StringVar()
    self.Ni = StringVar()
    self.Nf = StringVar()

    ttk.Label(mainframe8, text="Particula(Eletron 1, Proton 2):").grid(column=1, row=1, sticky=E)
    Massa_entry = ttk.Entry(mainframe8, width=15, textvariable=self.Massa).grid(column=2, row=1, sticky=E)

    ttk.Label(mainframe8, text="Largura:").grid(column=3, row=1, sticky=E)
    Largura_entry = ttk.Entry(mainframe8, width=15, textvariable=self.Largura).grid(column=4, row=1, sticky=E)

    ttk.Label(mainframe8, text="Nivel Inicial:").grid(column=1, row=2, sticky=E)
    Ni_entry = ttk.Entry(mainframe8, width=15, textvariable=self.Ni).grid(column=2, row=2, sticky=E)
    ttk.Label(mainframe8, text="Nivel Final:").grid(column=3, row=2, sticky=E)
    Nf_entry = ttk.Entry(mainframe8, width=15, textvariable=self.Nf).grid(column=4, row=2, sticky=E)

    ttk.Label(mainframe8, text="Funções de onda:").grid(column=1, row=3, sticky=E)
    ttk.Button(mainframe8, text="Calcular", command=self.CalcularFO).grid(column=2, row=3, sticky=(W, E))

    ttk.Label(mainframe8, text="Parametros Particula:").grid(column=3, row=3, sticky=E)
    ttk.Button(mainframe8, text="Calcular", command=self.CalcularPP).grid(column=4, row=3, sticky=(W, E))

    ttk.Label(mainframe8, text="Pulos Quanticos:").grid(column=1, row=4, sticky=E)
    ttk.Button(mainframe8, text="Simular", command=self.SimularPQ).grid(column=2, row=4, sticky=(W, E))

    ttk.Label(mainframe8, text="Probabilidade de particula:").grid(column=3, row=4, sticky=E)
    ttk.Button(mainframe8, text="Calcular", command=self.CalcularPdP).grid(column=4, row=4, sticky=(W, E))    

    ttk.Label(mainframe8, text="Funções de onda:").grid(column=1, row=5, sticky=E)
    ttk.Button(mainframe8, text="Simular", command=self.SimularFO).grid(column=2, row=5, sticky=(W, E))

    ttk.Label(mainframe8, text="Distribuição de probabilidade:").grid(column=3, row=5, sticky=E)
    ttk.Button(mainframe8, text="Simular", command=self.SimularDP).grid(column=4, row=5, sticky=(W, E))


    for child in mainframe8.winfo_children(): 
      child.grid_configure(padx=5, pady=5)
      
  def testeCaixa(self, *args):
    if self.Massa.get() == "":
      messagebox.showerror("Erro", "Escolha de Particula invalido")
      return False
    elif self.Largura.get() == "":
      messagebox.showerror("Erro", "Escolha de Largura invalido")
      return False
    elif self.Ni.get() == "":
      messagebox.showerror("Erro", "Escolha de Nivel Inicial invalido")
      return False
    elif self.Nf.get() == "":
      messagebox.showerror("Erro", "Escolha de Nivel Final invalido")
      return False
    else:
      return True
      
  def CalcularFO(self, *args):
      try:
        if self.testeCaixa():
          CalcularFuncaoOnda(root,self.Largura, self.Ni.get(), self.Nf.get())
      except ValueError:
        messagebox.showerror("Erro", "Valor invalido")
        #pass
  def CalcularPP(self, *args):
    try:
      if self.testeCaixa():
        if (self.Massa.get() == "1" ):
          CalcularParametrosParticula(root,self.Largura, self.Ni.get(), self.Nf.get(),massaEletron)
        elif (self.Massa.get() == "2"):
          CalcularParametrosParticula(root,self.Largura, self.Ni.get(), self.Nf.get(),massaProton)
        else:
          messagebox.showinfo(message='Escolha de Particula Incorreta')
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass
  def SimularPQ(self, *args):
    try:
      if self.testeCaixa():
        if (self.Massa.get() == "1" ):
          SimularPulosQuanticos(root,self.Largura, self.Ni.get(), self.Nf.get(),massaEletron)
        elif (self.Massa.get() == "2"):
          SimularPulosQuanticos(root,self.Largura, self.Ni.get(), self.Nf.get(),massaProton)
        else:
          messagebox.showinfo(message='Escolha de Particula Incorreta')
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass
  def CalcularPdP(self, *args):
    try:
      if self.testeCaixa():
        if (self.Massa.get() == "1" ):
          CalcularProbabilidadeParticula(root,self.Largura, self.Ni.get(), self.Nf.get(),massaEletron)
        elif (self.Massa.get() == "2"):
          CalcularProbabilidadeParticula(root,self.Largura, self.Ni.get(), self.Nf.get(),massaProton)
        else:
          messagebox.showinfo(message='Escolha de Particula Incorreta')
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass
  def SimularFO(self, *args):
    try:
      if self.testeCaixa():
        if (self.Massa.get() == "1" ):
          SimularFuncaoOnda(root,self.Largura, self.Ni.get(), self.Nf.get(),massaEletron)
        elif (self.Massa.get() == "2"):
          SimularFuncaoOnda(root,self.Largura, self.Ni.get(), self.Nf.get(),massaProton)
        else:
          messagebox.showinfo(message='Escolha de Particula Incorreta')
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass
  def SimularDP(self, *args):
    try:
      if self.testeCaixa():
        if (self.Massa.get() == "1" ):
          SimularDistribuicaoParticula(root,self.Largura, self.Ni.get(), self.Nf.get(),massaEletron)
        elif (self.Massa.get() == "2"):
          SimularDistribuicaoParticula(root,self.Largura, self.Ni.get(), self.Nf.get(),massaProton)
        else:
          messagebox.showinfo(message='Escolha de Particula Incorreta')
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class CalcularFuncaoOnda:
  def __init__(self,root,largura,Ni,Nf):
    w1 = Toplevel(root)
    w1.lift()
    w1.title("Calcular Funcao de Onda")
    mainframe1 = ttk.Frame(w1,padding=10)
    mainframe1.grid(column=0, row=0, sticky=(N, W, E, S))
    w1.columnconfigure(0, weight=1)
    w1.rowconfigure(0, weight=1)

    self.largura = StringVar()
    self.Ni = StringVar()
    self.Nf = StringVar()
    self.N = StringVar()

    self.largura.set(largura.get())
    self.Ni.set(Ni)
    self.Nf.set(Nf)

    self.func = StringVar()

    self.func.set("Ψn(𝑥) = A * sin(Kni * x)")

    ttk.Label(mainframe1, text=f"Nivel para Calcular({self.Ni.get()} ≤ N ≤ {self.Nf.get()}):").grid(column=1, row=2, sticky=E)
    N_entry = ttk.Entry(mainframe1, width=20, textvariable=self.N).grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe1, text="Calcular", command=self.CalcularFO).grid(column=1, row=3, sticky=(W, E))
    ttk.Label(mainframe1, textvariable=self.func).grid(column=2, row=3, sticky=E)

  def CalcularFO(self, *args):
    try:
      N = int(self.N.get())
      Ni = int(self.Ni.get())
      Nf = int(self.Nf.get())
      if(Ni>N or N>Nf):
        messagebox.showerror("Erro", "N invalido ")
      else:
        largura = float(self.largura.get())
        self.func.set(f"Ψ{N}(𝑥) = {notacaoCientifica(np.sqrt(2/largura))} * sin({notacaoCientifica((N*np.pi)/largura)} * x)")
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class CalcularParametrosParticula:
  def __init__(self,root,largura,Ni,Nf,massa):
    w2 = Toplevel(root)
    w2.lift()
    w2.title("Calcular Parametros de Particula")
    mainframe2 = ttk.Frame(w2,padding=10)
    mainframe2.grid(column=0, row=0, sticky=(N, W, E, S))
    w2.columnconfigure(0, weight=1)
    w2.rowconfigure(0, weight=1)

    self.largura = StringVar()
    self.Ni = StringVar()
    self.Nf = StringVar()
    self.N = StringVar()

    self.largura.set(largura.get())
    self.massa = massa
    self.Ni.set(Ni)
    self.Nf.set(Nf)

    self.EnergiaParticulaEv = StringVar()
    self.EnergiaParticulaJ = StringVar()
    self.ComprimentoParticula = StringVar()
    self.VelocidadeParticula = StringVar()

    self.EnergiaParticulaEv.set("..")
    self.EnergiaParticulaJ.set("..")
    self.ComprimentoParticula.set("..")
    self.VelocidadeParticula.set("..")

    ttk.Label(mainframe2, text=f"Nivel para Calcular({self.Ni.get()} ≤ N ≤ {self.Nf.get()}):").grid(column=1, row=1, sticky=E)
    N_entry = ttk.Entry(mainframe2, width=12, textvariable=self.N).grid(column=2, row=1, sticky=(W, E))

    ttk.Button(mainframe2, text="Calcular", command=self.CalcularPP).grid(column=1, row=2, sticky=(W, E),columnspan = 2)

    ttk.Label(mainframe2, text="Energia: ").grid(column=1, row=3, sticky=E)
    ttk.Label(mainframe2, textvariable=self.EnergiaParticulaEv).grid(column=2, row=3, sticky=E)
    ttk.Label(mainframe2, text="Ev").grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe2, text="Energia: ").grid(column=1, row=4, sticky=E)
    ttk.Label(mainframe2, textvariable=self.EnergiaParticulaJ).grid(column=2, row=4, sticky=E)
    ttk.Label(mainframe2, text="J").grid(column=3, row=4, sticky=W)

    ttk.Label(mainframe2, text="Comprimento de Onda: ").grid(column=1, row=5, sticky=E)
    ttk.Label(mainframe2, textvariable=self.ComprimentoParticula).grid(column=2, row=5, sticky=E)
    ttk.Label(mainframe2, text="m ").grid(column=3, row=5, sticky=W)

    ttk.Label(mainframe2, text="Velocidade: ").grid(column=1, row=6, sticky=E)
    ttk.Label(mainframe2, textvariable=self.VelocidadeParticula).grid(column=2, row=6, sticky=E)
    ttk.Label(mainframe2, text="m/s ").grid(column=3, row=6, sticky=W)

  def CalcularPP(self, *args):
    try:
      N = int(self.N.get())
      Ni = int(self.Ni.get())
      Nf = int(self.Nf.get())
      if(Ni>N or N>Nf):
        messagebox.showerror("Erro", "N invalido ")
      else:
        massa = self.massa
        largura = float(self.largura.get())
        energiaN1 = hJ**2/(8*massa*largura**2)
        EnergiaFoton = energiaN1 * N ** 2
        velocidade = np.sqrt(2*EnergiaFoton/massa)
        ComprimentoFoton = hJ /(np.sqrt(2*massa*EnergiaFoton))
        self.VelocidadeParticula.set(f"{notacaoCientifica(velocidade)} ")
        self.ComprimentoParticula.set(f"{notacaoCientifica(ComprimentoFoton)} ")
        self.EnergiaParticulaEv.set(f"{notacaoCientifica(EnergiaFoton/conversao)} ")
        self.EnergiaParticulaJ.set(f"{notacaoCientifica(EnergiaFoton)} ")
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class SimularPulosQuanticos:
  def __init__(self,root,largura,Ni,Nf,massa):
    w3 = Toplevel(root)
    w3.lift()
    w3.title("Simular Pulos Quanticos")
    mainframe3 = ttk.Frame(w3,padding=10)
    mainframe3.grid(column=0, row=0, sticky=(N, W, E, S))
    w3.columnconfigure(0, weight=1)
    w3.rowconfigure(0, weight=1)

    self.printAtual = 8
    self.noteFrames = []

    self.largura = StringVar()
    self.N = StringVar()
    self.Nf = StringVar()
    self.emissoesSV = StringVar()
    self.NatualPrint1 = StringVar()
    self.NatualPrint2 = StringVar()
    
    self.Natual = int(Nf)
    self.emissoes = [int(Ni),int(Nf)]
    
    self.NatualPrint1.set(f"Particula em {self.Natual}:")
    self.NatualPrint2.set(f"Nivel disponivel para pulo Pulo(1 ≤ N ≤ {self.Natual-1}):")
    
    self.Nf.set(Nf)
    self.largura.set(largura.get())
    self.massa = massa
    self.emissoesSV.set(f"[{Ni},{Nf}]")

    self.EnergiaParticulaEv = StringVar()
    self.EnergiaParticulaJ = StringVar()
    self.ComprimentoParticula = StringVar()
    self.VelocidadeParticula = StringVar()

    self.EnergiaParticulaEv.set("..")
    self.EnergiaParticulaJ.set("..")
    self.ComprimentoParticula.set("..")
    self.VelocidadeParticula.set("..")

    ttk.Label(mainframe3, textvariable=self.NatualPrint1).grid(column=1, row=1, sticky=(W, E), columnspan=2)
    ttk.Label(mainframe3, textvariable=self.NatualPrint2).grid(column=1, row=2, sticky=(W, E), columnspan=2)

    ttk.Label(mainframe3, text=f"Nivel para pulo:").grid(column=1, row=3, sticky=E)
    N_entry = ttk.Entry(mainframe3, width=20, textvariable=self.N).grid(column=2, row=3, sticky=W)

    ttk.Button(mainframe3, text="Adicionar Pulo", command=self.AdicionaPulo).grid(column=1, row=4, sticky=(W, E),columnspan = 2)
    ttk.Button(mainframe3, text="Remover Ultimo Pulo", command=self.RemovePulo).grid(column=1, row=5, sticky=(W, E),columnspan = 2)

    ttk.Label(mainframe3, text="Ordem de Pulos: ").grid(column=1, row=6, sticky=E)
    ttk.Label(mainframe3, textvariable=self.emissoesSV).grid(column=2, row=6, sticky=W)

    ttk.Button(mainframe3, text="Simular Pulos", command=self.SimulaPulo).grid(column=1, row=7, sticky=(W, E),columnspan = 2)
    self.Notebook = ttk.Notebook(mainframe3)
    self.Notebook.grid(column=1, row=8, sticky=(W, E, S),columnspan = 2,rowspan=4)


  def AdicionaPulo(self, *args):
    try:
      N = int(self.N.get())
      if (self.Natual <= N or N < 1):
        messagebox.showinfo(message='Nivel de pulo invalido')
      else:
        self.Natual = N
        self.NatualPrint1.set(f"Particula em {self.Natual}:")
        self.NatualPrint2.set(f"Nivel disponivel para pulo Pulo(1 ≤ N ≤ {self.Natual-1}):")
        self.emissoes.append(N)
        SV = "["
        for i in range(len(self.emissoes)):
          SV = SV + f"{self.emissoes[i]}"
          if i != len(self.emissoes)-1:
            SV = SV + ","
        SV = SV + "]"
        self.emissoesSV.set(SV)
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

  def RemovePulo(self, *args):
    try:
      if (len(self.emissoes)<=2):
        messagebox.showinfo(message='Não foi possivel remover pulo')
      else:
        self.emissoes.pop()
        self.Natual = self.emissoes[len(self.emissoes)-1]
        SV = "["
        for i in range(len(self.emissoes)):
          SV = SV + f"{self.emissoes[i]}"
          if i != len(self.emissoes)-1:
            SV = SV + ","
        SV = SV + "]"
        self.emissoesSV.set(SV)
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass


  def SimulaPulo(self, *args):
    #try:
      if (self.emissoes[len(self.emissoes)-1]!=1):
        messagebox.showinfo(message='Ordem não termina no nivel 1')
      else:
        for item in self.Notebook.winfo_children():
            item.destroy()
        self.noteFrames = []
        self.emissoes.append(1)
        self.emissoes.append(1)
        self.emissoes.append(1)
        self.emissoes.append(1)
        self.emissoes.append(1)
        self.nAtualSimulacao = 0
        self.setGraficoPulos(self, *args)
        ani = animation.FuncAnimation(self.fig, self.animate, interval=20, blit=True, save_count=50)
        plt.show()
    #except ValueError:
      #messagebox.showerror("Erro", "Valor invalido")
      #pass

  def setGraficoPulos(self, *args):
    largura = float(self.largura.get())
    self.max = float(-1)
    self.min = float(1)
    self.fig, self.ax= plt.subplots()
    self.line, = self.ax.plot(0, 0)
    plt.xlabel("Largura(m)")
    plt.ylabel("Energia(eV)")
    plt.xticks(np.arange(0, np.pi+0.01, step=np.pi/5), labels=[str(0),"%.2e" % (2*largura/10),"%.2e" % (4*largura/10),"%.2e" % (6*largura/10),"%.2e" % (8*largura/10),"%.2e" % (largura)], fontsize=7)
    plt.yticks(np.arange(0, 12.01, step=2), labels=[str(0),str(0.005),str(0.020),str(0.046),str(0.082),str(0.128),"∞"], fontsize=7)
    self.ax.set(xlim=[0,np.pi],ylim=[0, 12],)
    self.annotation = self.ax.annotate('', xy=(1,0), xytext=(-1,0), arrowprops = {'arrowstyle': "->"})

  def calculoEmitido(self, ni, nf, *args):
    largura = float(self.largura.get())
    EnergiaNi = hJ**2/(8*self.massa*largura**2) * ni ** 2
    EnergiaNf = hJ**2/(8*self.massa*largura**2) * nf ** 2
    EnergiaFoton =  EnergiaNi - EnergiaNf 
    ComprimentoFoton = (hEV * luz) / (EnergiaFoton /conversao)
    FrequenciaFoton = (EnergiaFoton/conversao) / hEV

    self.noteFrames.append(ttk.Frame(self.Notebook))
    self.Notebook.add(self.noteFrames[len(self.noteFrames)-1],text=f"{ni}->{nf}")

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Energia:").grid(column=1, row=1, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(EnergiaFoton/conversao)} eV").grid(column=2, row=1, sticky=W)

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Energia:").grid(column=1, row=2, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(EnergiaFoton)} J").grid(column=2, row=2, sticky=W)

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Comprimento de onda:").grid(column=1, row=3, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(ComprimentoFoton)} m").grid(column=2, row=3, sticky=W)

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Frequencia:").grid(column=1, row=4, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(FrequenciaFoton)} Hz").grid(column=2, row=4, sticky=W)

  def calculoAbsorvido(self, ni, nf, *args):
    largura = float(self.largura.get())
    EnergiaNi = hJ**2/(8*self.massa*largura**2) * ni ** 2
    EnergiaNf = hJ**2/(8*self.massa*largura**2) * nf ** 2
    EnergiaFoton =  EnergiaNf - EnergiaNi
    ComprimentoFoton = (hEV * luz) / (EnergiaFoton /conversao)
    FrequenciaFoton = (EnergiaFoton/conversao) / hEV

    self.noteFrames.append(ttk.Frame(self.Notebook))
    self.Notebook.add(self.noteFrames[len(self.noteFrames)-1],text=f"{ni}->{nf}")

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Energia:").grid(column=1, row=1, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(EnergiaFoton/conversao)} eV").grid(column=2, row=1, sticky=W)

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Energia:").grid(column=1, row=2, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(EnergiaFoton)} J").grid(column=2, row=2, sticky=W)

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Comprimento de onda:").grid(column=1, row=3, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(ComprimentoFoton)} m").grid(column=2, row=3, sticky=W)

    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text="Frequencia:").grid(column=1, row=4, sticky=E)
    ttk.Label(self.noteFrames[len(self.noteFrames)-1], text=f"{notacaoCientifica(FrequenciaFoton)} Hz").grid(column=2, row=4, sticky=W)


  def animate(self, i):
    velocidadeMult = 3
    if (self.min!=self.max and self.min<1.01 and self.min>-1.01):
      self.min += (self.max/6)
    else:
      self.min = self.max
      self.max = (self.max*-1)


    if i%(30*velocidadeMult)==0 and self.nAtualSimulacao+1<len(self.emissoes) and i!=0 and self.emissoes[self.nAtualSimulacao]!=self.emissoes[self.nAtualSimulacao+1]:
      if(i!=30*velocidadeMult):
        self.calculoEmitido(self.emissoes[self.nAtualSimulacao],self.emissoes[self.nAtualSimulacao+1])
      self.nAtualSimulacao+=1
    if i<=30*velocidadeMult:
      tempo = i
      self.annotation.set_position((-0.5+tempo/(20*velocidadeMult), 4+(self.emissoes[0]*2-2)-tempo/(15*velocidadeMult)))
      self.annotation.xy = (tempo/(20*velocidadeMult), 3+(self.emissoes[0]*2-2)-tempo/(15*velocidadeMult))
      self.line.set_xdata(arrayPis[self.emissoes[0]-1])
      if(self.emissoes[0]>5):
        self.line.set_ydata(np.sin(arrayPis[self.emissoes[0]-1])*self.min+(self.emissoes[0]*20))
      else:
        self.line.set_ydata(np.sin(arrayPis[self.emissoes[0]-1])*self.min+(self.emissoes[0]*2))
    elif i>30*velocidadeMult and i<=60*velocidadeMult:
      tempo = i-30*velocidadeMult
      self.annotation.set_position((-1, -1))
      self.annotation.xy = (-1, -1)
      self.line.set_xdata(arrayPis[self.emissoes[1]-1]/self.emissoes[1])
      if(self.emissoes[1]>5):
        self.line.set_ydata(np.sin(arrayPis[self.emissoes[1]-1])*self.min+(self.emissoes[1]*20))
      else:
        self.line.set_ydata(np.sin(arrayPis[self.emissoes[1]-1])*self.min+(self.emissoes[1]*2))
    else:
      tempo = i-30*velocidadeMult*(self.nAtualSimulacao)
      self.annotation.set_position((1.5+tempo/(20*velocidadeMult),self.emissoes[self.nAtualSimulacao-1]*2-1))
      self.annotation.xy = (2+tempo/(20*velocidadeMult),self.emissoes[self.nAtualSimulacao-1]*2-1)
      self.line.set_xdata(arrayPis[self.emissoes[self.nAtualSimulacao]-1]/self.emissoes[self.nAtualSimulacao])
      if(self.emissoes[self.nAtualSimulacao]>5):
        self.line.set_ydata(np.sin(arrayPis[self.emissoes[self.nAtualSimulacao]-1])*self.min+(self.emissoes[self.nAtualSimulacao]*20))
      else:
        self.line.set_ydata(np.sin(arrayPis[self.emissoes[self.nAtualSimulacao]-1])*self.min+(self.emissoes[self.nAtualSimulacao]*2))

    if i==30*velocidadeMult:
      self.calculoAbsorvido(self.emissoes[0], self.emissoes[1])

    return [self.line, self.annotation]

class CalcularProbabilidadeParticula:
  def __init__(self,root,largura,Ni,Nf,massa):
    w4 = Toplevel(root)
    w4.lift()
    w4.title("Calcular Probabilida de Particula")
    mainframe4 = ttk.Frame(w4,padding=10)
    mainframe4.grid(column=0, row=0, sticky=(N, W, E, S))
    w4.columnconfigure(0, weight=1)
    w4.rowconfigure(0, weight=1)

    self.largura = StringVar()
    self.Ni = StringVar()
    self.Nf = StringVar()
    self.N = StringVar()
    self.pontoA = StringVar()
    self.pontoB = StringVar()

    self.largura.set(largura.get())
    self.massa = massa
    self.Ni.set(Ni)
    self.Nf.set(Nf)

    self.Probabilidade = StringVar()

    self.Probabilidade.set("..")

    ttk.Label(mainframe4, text=f"Nivel para Calcular({self.Ni.get()} ≤ N ≤ {self.Nf.get()}):").grid(column=1, row=1, sticky=E)
    N_entry = ttk.Entry(mainframe4, width=12, textvariable=self.N).grid(column=2, row=1, sticky=W)

    ttk.Label(mainframe4, text=f"(0 ≤ Ponto A < Ponto B  ≤ {self.largura.get()}").grid(column=1, row=2, sticky=E, columnspan=2)

    ttk.Label(mainframe4, text="Ponto A:").grid(column=1, row=3, sticky=E)
    pontoA_entry = ttk.Entry(mainframe4, width=12, textvariable=self.pontoA).grid(column=2, row=3, sticky=W)

    ttk.Label(mainframe4, text="Ponto B").grid(column=1, row=4, sticky=E)
    pontoB_entry = ttk.Entry(mainframe4, width=12, textvariable=self.pontoB).grid(column=2, row=4, sticky=W)

    ttk.Button(mainframe4, text="Calcular", command=self.CalcularPdP).grid(column=1, row=5, sticky=(W, E),columnspan = 2)

    ttk.Label(mainframe4, text="Probabilidade de particula: ").grid(column=1, row=6, sticky=E)
    ttk.Label(mainframe4, textvariable=self.Probabilidade).grid(column=2, row=6, sticky=W)

  def CalcularPdP(self, *args):
    try:
      N = int(self.N.get())
      Ni = int(self.Ni.get())
      Nf = int(self.Nf.get())
      if(Ni>N or N>Nf):
        messagebox.showerror("Erro", "N invalido ")
      else:
        massa = self.massa
        largura = float(self.largura.get())
        pontoA = float(self.pontoA.get())
        pontoB = float(self.pontoB.get())
        constA = np.sqrt(2/largura)
        constB = N*np.pi/largura
        if pontoA>=pontoB:
          messagebox.showerror("Erro", "Ponto A maior ou igual ao ponto B")
        else:
          self.Probabilidade.set(f"{notacaoCientifica(abs((constA**2)*((1/2)*pontoA-(1/(4*constB))*np.sin(2*constB*pontoA))-(constA**2)*((1/2)*pontoB-(1/(4*constB))*np.sin(2*constB*pontoB)))*100)} %")
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class SimularFuncaoOnda:
  def __init__(self,root,largura,Ni,Nf,massa):
    w5 = Toplevel(root)
    w5.lift()
    w5.title("Simular Funcao de Onda")
    mainframe5 = ttk.Frame(w5,padding=10)
    mainframe5.grid(column=0, row=0, sticky=(N, W, E, S))
    w5.columnconfigure(0, weight=1)
    w5.rowconfigure(0, weight=1)
    
    self.largura = StringVar()
    self.Ni = StringVar()
    self.Nf = StringVar()
    self.N = StringVar()

    self.largura.set(largura.get())
    self.massa = massa
    self.Ni.set(Ni)
    self.Nf.set(Nf)



    ttk.Label(mainframe5, text=f"Nivel para Calcular({self.Ni.get()} ≤ N ≤ {self.Nf.get()}):").grid(column=1, row=1, sticky=E)
    N_entry = ttk.Entry(mainframe5, width=12, textvariable=self.N).grid(column=2, row=1, sticky=W)

    ttk.Button(mainframe5, text="Simular", command=self.SimularFO).grid(column=1, row=5, sticky=(W, E),columnspan = 2)

  def SimularFO(self, *args):
    try:
      N = int(self.N.get())
      Ni = int(self.Ni.get())
      Nf = int(self.Nf.get())
      if(Ni>N or N>Nf):
        messagebox.showerror("Erro", "N invalido ")
      else:
        largura = float(self.largura.get())
        fig, ax= plt.subplots()
        plt.xlabel("Largura(m)")
        plt.ylabel("Ψ%d" % (N))
        plt.xticks(np.arange(0, np.pi+0.01, step=np.pi/5), labels=[str(0),"%.2e" % (2*largura/10),"%.2e" % (4*largura/10),"%.2e" % (6*largura/10),"%.2e" % (8*largura/10),"%.2e" % (largura)], fontsize=7)
        plt.yticks(np.arange(-2, 2.01, step=2), labels=["-∞",str(0),"∞"], fontsize=10)
        ax.set(xlim=[0,np.pi],ylim=[-2.5, 2.5])
        ax.plot(arrayPis[N]/N,np.sin(arrayPis[N]))
        ax.text(2.5, 2, f"N = {N}", fontsize=15)
        plt.show()
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class SimularDistribuicaoParticula:
  def __init__(self,root,largura,Ni,Nf,massa):
    w6 = Toplevel(root)
    w6.lift()
    w6.title("Simular Distribuicao de Particula")
    mainframe6 = ttk.Frame(w6,padding=10)
    mainframe6.grid(column=0, row=0, sticky=(N, W, E, S))
    w6.columnconfigure(0, weight=1)
    w6.rowconfigure(0, weight=1)

    self.largura = StringVar()
    self.Ni = StringVar()
    self.Nf = StringVar()
    self.N = StringVar()
    
    self.largura.set(largura.get())
    self.massa = massa
    self.Ni.set(Ni)
    self.Nf.set(Nf)
    
    
    
    ttk.Label(mainframe6, text=f"Nivel para Simular({self.Ni.get()} ≤ N ≤ {self.Nf.get()}):").grid(column=1, row=1, sticky=E)
    N_entry = ttk.Entry(mainframe6, width=12, textvariable=self.N).grid(column=2, row=1, sticky=W)
    
    ttk.Button(mainframe6, text="Simular", command=self.SimularDP).grid(column=1, row=5, sticky=(W, E),columnspan = 2)
    
  def SimularDP(self, *args):
    try:
      N = int(self.N.get())
      Ni = int(self.Ni.get())
      Nf = int(self.Nf.get())
      if(Ni>N or N>Nf):
        messagebox.showerror("Erro", "N invalido ")
      else:
        largura = float(self.largura.get())
        fig, ax= plt.subplots()
        plt.xlabel("Largura(m)")
        plt.ylabel("|Ψ%d|²" % (N))
        plt.xticks(np.arange(0, np.pi+0.01, step=np.pi/5), labels=[str(0),"%.2e" % (2*largura/10),"%.2e" % (4*largura/10),"%.2e" % (6*largura/10),"%.2e" % (8*largura/10),"%.2e" % (largura)], fontsize=7)
        plt.yticks(np.arange(0, 2.01, step=2), labels=[str(0),"∞"], fontsize=10)
        ax.set(xlim=[0,np.pi],ylim=[0, 2.5])
        ax.plot(arrayPis[N]/N,np.sin(arrayPis[N])**2)
        ax.text(2.5, 2, f"N = {N}", fontsize=15)
        plt.show()
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class CalcularParametros:
  def __init__(self,root):
    w7 = Toplevel(root)
    w7.lift()
    w7.title("Calcular Parametros")
    mainframe7 = ttk.Frame(w7,padding=10)
    mainframe7.grid(column=0, row=0, sticky=(N, W, E, S))
    w7.columnconfigure(0, weight=1)
    w7.rowconfigure(0, weight=1)

    self.A = StringVar()
    self.K = StringVar()
    self.Xp = StringVar()

    self.largura = StringVar()
    self.NQ = StringVar()
    self.Prob = StringVar()

    self.largura.set("___")
    self.NQ.set("___")
    self.Prob.set("___")

    ttk.Label(mainframe7, text="Preencha a Função de Onda:").grid(column=1, row=1, sticky=W)
    ttk.Label(mainframe7, text="Ψ(𝑥) = ").grid(column=1, row=1, sticky=E)
    A_entry = ttk.Entry(mainframe7, width=21, textvariable=self.A).grid(column=2, row=1, sticky=(W, E))
    ttk.Label(mainframe7, text=" . sin(").grid(column=3, row=1, sticky=(W, E))
    K_entry = ttk.Entry(mainframe7, width=21, textvariable=self.K).grid(column=4, row=1, sticky=(W, E))
    ttk.Label(mainframe7, text=" . x)").grid(column=5, row=1, sticky=E)

    ttk.Button(mainframe7, text="Calcular Parametros", command=self.calculoParametro).grid(column=1, row=2, sticky=(W, E))
    ttk.Label(mainframe7, textvariable= self.largura).grid(column=2, row=2, sticky=(W, E))
    ttk.Label(mainframe7, textvariable= self.NQ).grid(column=4, row=2, sticky=(W, E))

    ttk.Label(mainframe7, text="Calcular probabilidade da particula na posição: ").grid(column=1, row=3, sticky=(W, E))
    Xp_entry = ttk.Entry(mainframe7, width=21, textvariable=self.Xp).grid(column=2, row=3, sticky=E)
    ttk.Label(mainframe7, text="metros").grid(column=3, row=3, sticky=E)

    ttk.Button(mainframe7, text="Calcular Probabilidade", command=self.calculoProbabilidade).grid(column=1, row=4, sticky=(W, E))
    ttk.Label(mainframe7, textvariable= self.Prob).grid(column=2, row=4, sticky=(W, E))

    for child in mainframe7.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

  def calculoParametro(self, *args):
    try:
      A = float(self.A.get())
      K = float(self.K.get())
      if A == 0:
        self.largura.set("Largura Invalida")
        self.NQ.set("Largura Invalida")
      else:
        self.largura.set(f"Largura = {notacaoCientifica(2/A**2)} m")
        self.NQ.set(f"Numero Quantico = {notacaoCientifica(K*(2/A**2)/np.pi)}")
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

  def calculoProbabilidade(self, *args):
    try:
      A = float(self.A.get())
      K = float(self.K.get())
      Xp = float(self.Xp.get())
      self.Prob.set(f"Probabilidade = {notacaoCientifica((A**2)*(np.sin(K*Xp))**2)} dx")
    except ValueError:
      messagebox.showerror("Erro", "Valor invalido")
      #pass

class menu:
  def __init__(self,root):
    root.title("Particula na Caixa")
    mainframe = ttk.Frame(root,padding=10)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Particula de Schrödinger: contenção em  uma  caixa  unidimensional").grid(column=1, row=1, sticky=W, columnspan=2)
    ttk.Label(mainframe, text="Esse  progama  simula  os  comportamentos de uma particula ").grid(column=1, row=2, sticky=E, columnspan=2)
    ttk.Label(mainframe, text="contida em  uma  caixa unidimensional em um espaço limitado por").grid(column=1, row=3, sticky=W, columnspan=2)
    ttk.Label(mainframe, text="um potencial infinito.").grid(column=1, row=4, sticky=W, columnspan=2)
    ttk.Label(mainframe, text="").grid(column=1, row=5, sticky=W, columnspan=2)
    ttk.Label(mainframe, text="Determinação  da  função  de  onda  quântica  e  outros parâmetros:").grid(column=1, row=6, sticky=W, columnspan=2)
    ttk.Button(mainframe, text="Calcular Parametros", command=self.SimularParticula).grid(column=1, row=7, sticky=(W, E), columnspan=2)
    ttk.Label(mainframe, text="").grid(column=1, row=8, sticky=W, columnspan=2)
    ttk.Label(mainframe, text="Cálculo dos parâmetros da caixa e partícula, dada a função de onda:").grid(column=1, row=9, sticky=W, columnspan=2)
    ttk.Button(mainframe, text="Calcular Parametros", command=self.CalcularParametro).grid(column=1, row=10, sticky=(W, E), columnspan=2)

    for child in mainframe.winfo_children(): 
      child.grid_configure(padx=5, pady=5)

  def SimularParticula(self, *args):
    SimularParticulas(root)

  def CalcularParametro(self, *args):
    CalcularParametros(root)

root = Tk()
menu(root)
root.mainloop()