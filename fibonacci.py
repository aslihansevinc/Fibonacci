
def control(sinir):
    if(sinir>0):
        return fibonacci(sinir)
    else:
        
        sinir=int(input("lütfen pozitif bir sayi giriniz"))
        return fibonacci(sinir)
    

def fibonacci(sinir):
      sayi1=0
      sayi2=1
      print(sayi1)
      print(sayi2)
      for i in range(sinir-2):
        sayi3=sayi1+sayi2
        print(sayi3)
        sayi1=sayi2
        sayi2=sayi3

sinir=int(input("lütfen sayı giriniz"))
control(sinir)

    
    


