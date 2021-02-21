#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Ogrenci Bilgi Listeleri

OgrenciAdSoyad=["Deniz Aydın","Ömer Cengiz","Mert Çobanov","Kutay Akalın","Ayşe Yılmaz"]
OgrenciNotlari=[[100,100,90],[60,70,80],[90,45,75],[25,50,100],[100,90,80]]

print(OgrenciAdSoyad)
print(OgrenciNotlari)


# In[27]:


#Ogrenci Bilgileri

OgrenciBilgileri=dict(zip(OgrenciAdSoyad,OgrenciNotlari))
print(OgrenciBilgileri)


# In[26]:


#Ortalama Hesaplama ve Sıralama

i=0
while i<len(OgrenciNotlari):
    ortalama=((OgrenciNotlari[i][0]+OgrenciNotlari[i][1]+OgrenciNotlari[i][2])/3)
    if len(OgrenciNotlari[i])<4:
        OgrenciNotlari[i].insert(4,ortalama) #kodu çalıştırdıkça ortalamayı tekrar eklememesi için
    i+=1
MaxOrtalama=0
for AdSoyad in OgrenciAdSoyad:
    if MaxOrtalama<OgrenciBilgileri[AdSoyad][3]:
        MaxOrtalama=OgrenciBilgileri[AdSoyad][3]
    else:
        MaxOrtalama=MaxOrtalama
        
print("En yüksek ortalama: "+str(MaxOrtalama))

Ortalamalar=[]
for AdSoyad in OgrenciAdSoyad:
    Ortalamalar.append(OgrenciBilgileri[AdSoyad][3])
OrtSiralama=sorted(Ortalamalar)

print(OrtSiralama)


# In[23]:


#Bilgilendirme Sistemi

AdSoyad=input("Öğrencinin adını ve soyadını giriniz: ")

if AdSoyad in OgrenciAdSoyad:
    print("Merhaba "+AdSoyad+"!\nNotlarınız:\n"+"Midterm: "+str(OgrenciBilgileri[AdSoyad][0])+
          "\nFinal: "+str(OgrenciBilgileri[AdSoyad][1])+"\nHomework: "+str(OgrenciBilgileri[AdSoyad][2])
            +"\nOrtalama: "+str(OgrenciBilgileri[AdSoyad][3]))
    if OgrenciBilgileri[AdSoyad][3]==OrtSiralama[-1]:
        print("Tebrikler, 1. sıradasınız! Top Learner olmaya hak kazandınız. :)")
    elif OgrenciBilgileri[AdSoyad][3]==OrtSiralama[-2]:
        print("Tebrikler, 2. sıradasınız!")
    elif OgrenciBilgileri[AdSoyad][3]==OrtSiralama[-3]:
        print("Tebrikler, 3. sıradasınız!")    
else:
    print("Hata!\nBilgileriniz sistemde mevcut deği. Yanlış kullanıcı adı girmiş olabilirsiniz.\nTekrar deneyiniz ya da öğrenci işlerine başvurunuz.")

