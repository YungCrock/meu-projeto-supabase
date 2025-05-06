
#
import os
from dotenv import load_dotenv

load_dotenv('/content/drive/MyDrive/canil/.env')

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

#
from supabase import create_client
SUPABASE_URL = "https://nqiazalzcvwexuhrfayb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5xaWF6YWx6Y3Z3ZXh1aHJmYXliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE0MDA3MzYsImV4cCI6MjA1Njk3NjczNn0.2ah-aYI0Xt2PMMRaMb41toU0UrA6oC4nuKiT4Qb4EEo"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#
resposta = supabase.table("animais").select("*").execute()
print(resposta.data)

#
novo_animal = {
    "nome": "Rex",
    "especie": "Cachorro",
    "idade": 4
}
resposta = supabase.table("animais").insert(novo_animal).execute()
print(resposta.data)

#
resposta = supabase.table("animais").update({"cor": "Caramelo"}).eq("id", 1).execute()
print(resposta.data)

#
resposta = supabase.table("animais").delete().eq("id", 1).execute()
print(resposta.data)

#
def cadastrar_animal(nome, especie, raca, porte, sexo, idade, cor,adotado):
    return supabase.table("animais").insert({
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "porte": porte,
        "sexo": sexo,
        "idade": idade,
        "cor": cor,
        "adotado": False
    }).execute()
cadastrar_animal("Nina", "Cachorro", "shih tzu", "Pequeno", "F", 1, "Branco e Marrom")

#
response = supabase.table("animais").select("*").eq("adotado", False).execute()
for animal in response.data:
    print(animal)

#
especie = input("Digite a espécie: ")
response = supabase.table("animais").select("*").eq("especie", especie).execute()
for animal in response.data:
    print(animal)

#
response = supabase.table("animais").select("*").order("idade", desc=False).execute()
for animal in response.data:
    print(animal)

#
nome = input("Nome do animal: ")
especie = input("Espécie: ")
idade = int(input("Idade: "))
adotado = input("Adotado? (s/n): ").lower() == "s"

dados = {
    "nome": nome,
    "especie": especie,
    "idade": idade,
    "adotado": adotado
}

res = supabase.table("animais").insert(dados).execute()
print("Animal inserido com sucesso!", res.data)
