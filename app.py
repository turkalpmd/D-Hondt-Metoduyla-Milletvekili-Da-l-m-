import streamlit as st

def dhondt(partiler, milletvekili_sayisi):
    bolumler = {}
    
    for parti in partiler:
        bolumler[parti] = [partiler[parti] / (i + 1) for i in range(milletvekili_sayisi)]
    
    milletvekili_dagilimi = {parti: 0 for parti in partiler}
    
    for _ in range(milletvekili_sayisi):
        en_yuksek_bolum = max(bolumler, key=lambda x: bolumler[x][0])
        milletvekili_dagilimi[en_yuksek_bolum] += 1
        bolumler[en_yuksek_bolum].pop(0)

    return milletvekili_dagilimi

st.title("D'Hondt Metoduyla Milletvekili Dağılımı")

parti_sayisi = st.number_input("Parti Sayısı:", min_value=1, value=4)

partiler = {}
for i in range(parti_sayisi):
    partiler[chr(ord("A") + i)] = st.number_input(f"{chr(ord('A') + i)} Partisinin Oyu:", min_value=0, value=0)

milletvekili_sayisi = st.number_input("Milletvekili Sayısı:", min_value=1, value=5)

if st.button("Hesapla"):
    sonuc = dhondt(partiler, milletvekili_sayisi)
    
    # Sonucu sırala ve güzel bir biçimde yazdır
    sonuc_sirali = sorted(sonuc.items(), key=lambda x: x[1], reverse=True)
    
    for parti, koltuk in sonuc_sirali:
        st.error(f"{parti} partisi koltuk sayısı: {koltuk}")
