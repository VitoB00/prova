#vogliamo un module utile che faccia operazione con matrici nxn e poi nxm, n != m

def zeros(n):
   mm=[]
   for r in range(n):
       riga=[] 
       for c in range(n):
           riga.append(0)
       mm.append(riga)   
   return mm

def scalar(k,m):   
   n=len(m)
   mm=zeros(n,n)
   for r in range(n):
       for c in range(n):
           mm[r][c]=k*m[r][c] 
   return mm 

def somma(m1,m2):   
   n=len(m1) 
   mm=zeros(n)
   for r in range(n):
       for c in range(n):
           mm[r][c]=m1[r][c]+m2[r][c]
   return mm

def product(m1,m2):   
   n=len(m1) 
   mm=zeros(n,n)
   for r in range(n):
       for c in range(n):
           somma=0  
           for k in range(n):
               somma+=m1[r][k]*m2[k][c]
           mm[r][c]=somma   
   return mm
 
#iniziamo a caratterizzare funzioni che facciano prodotti di matrici n x m

def generalzeros(nr,nc):
   mm=[]
   for r in range(nr):
      riga=[] 
      for c in range(nc):
         riga.append(0)
      mm.append(riga)   
   return mm

def scalar(k,m):   
   nr=len(m) 
   nc=len(m[0]) 
 
   mm=generalzeros(nr,nc)
   for r in range(nr):
      for c in range(nc):
         mm[r][c]=k*m[r][c] 
   return mm

def somma(m1,m2):   
   r1=len(m1)
   c1=len(m1[0])
   r2=len(m2)
   c2=len(m2[0])
   if(r1 != r2)or(c1 != c2): 
       return   
 
   mm=generalzeros(r1,c1)
   for r in range(r1):
       for c in range(c1):
           mm[r][c]=m1[r][c]+m2[r][c]
   return mm

#qui è stato necessario prestare TANTA attenzione all'indentazione
def product(m1,m2):   
   r1=len(m1)
   c1=len(m1[0])
   r2=len(m2)
   c2=len(m2[0])
   if(c1 != r2): 
      return
 
   mm=generalzeros(r1,c2)
   for r in range(r1):
       for c in range(c2):
           somma=0  
           for k in range(c1):
               somma+=m1[r][k]*m2[k][c]
           mm[r][c]=somma   
   return mm

 #determinante che può sempre tornare utile
 
def submat(m, er,ec):      # Crea una sottomatrice di m (nxn) 
   mm=[]                      # Copia tutto tranne la riga er e la colonna ec
   n=len(m)
 
   for r in range(n):
       if(r != er): 
           riga=[]
           for c in range(n):
               if(c != ec):
                   riga.append(m[r][c])
           mm.append(riga)   
   return mm
 
def determinant(m):          # Calcola il determinante
   nr=len(m)                    
   nc=len(m[0])
   if(nr != nc):              # Se la matrice non è quadrata...
       return 0        
   if(nr == 1 ):              # Se è uno scalare...
       return m[0][0]
 
   somma=0
   segno=+1
   for r in range(nr):        # Sviluppa la 1° colonna...
       mm     = submat(m, r,0) 
       somma += segno*m[r][0]*determinant(mm)
       segno *= -1
   return somma