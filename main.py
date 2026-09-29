import random
from tabulate import tabulate


class Player():
	def __init__(self):
		self.players = []
		self.turno_atual = 1
		self.loja = [
			{"nome": "cura", "preco": 10, "efeito": "vida", "valor": 15},
			{"nome": "escudo", "preco": 15, "efeito": "defesa", "valor": 10},
			{"nome": "colar da sorte", "preco": 10, "efeito": "sorte", "valor": 0.5},
		]

	def jogador_atual(self):
		for p in self.players:
			if p["id"] == self.turno_atual:
				return p
		return None

	def prox_turno(self):
		self.turno_atual += 1
		if self.turno_atual > len(self.players):
			self.turno_atual = 1

	def mostrar_tabela(self):
		if not self.players:
			print("nenhum player encontrado")
			return

		dados = []
		for p in self.players:
			marcador = "🫴" if p["id"] == self.turno_atual else " "
			dados.append({
				" ": marcador,
				"ID": p["id"],
				"Vida": p["vida"],
				"Defesa": p["defesa"],
				"Dinheiro": p["dinheiro"],
				"Sorte": p["sorte"]
			})

		print(tabulate(
			dados,
			headers="keys",
			tablefmt="fancy_grid",
			colalign=("center", "center", "center", "center", "center")
		))

	def add_player(self):
		num = int(input("quer quantos player: "))

		for i in range(1, num + 1):
			novo_player = {
				"id": i,
				"vida": 40,
				"defesa": 0,
				"sorte": 1,
				"dinheiro": 20
			}
			self.players.append(novo_player)

	def atacar(self):
		atacante = self.jogador_atual()
		if not atacante:
			print("nenhum jogador encontrado")
			return

		try:
			esc = int(input("quer atacar qual player: "))
		except ValueError:
			print("digite um número válido")
			return

		if esc == atacante["id"]:
			print("voce não pode atacar voce mesmo")
			return

		alvo = None
		for p in self.players:
			if p["id"] == esc:
				alvo = p
				break

		if not alvo:
			print("alvo não encontrado")
			return

		if alvo["vida"] <= 0:
			print(f"o jogador {alvo['id']} já está morto")
			return

		dano_total = self.dano() - alvo["defesa"]
		if dano_total < 0:
			dano_total = 0
		alvo["vida"] -= dano_total

		print(f"o jogador {alvo['id']} perdeu {dano_total} de dano, agora ele tem {alvo['vida']} de vida")

		if alvo["vida"] <= 0:
			print(f"💀 o jogador {alvo['id']} morreu!")

		self.prox_turno()

	def dano(self):
		dado = random.randint(1, 20)

		if dado <= 10:
			dano = random.randint(1, 10)
		elif dado <= 15:
			dano = random.randint(11, 15)
		else:
			dano = random.randint(16, 20)

		return dano

	def lojoja(self):
		jogador = self.jogador_atual()

		while True:
			print(tabulate(
				self.loja,
				headers="keys",
				tablefmt="fancy_grid",
				colalign=("center", "center", "center", "center")
			))
			
			self.mostrar_tabela()
			
			print("digite 0 para sair")
			
			esc = input("quer comprar qual item: ")
			
			for i in self.loja:
					if esc == i["nome"]:	
						if jogador["dinheiro"] >= i["preco"]:
							print("item comprado com sucesso")
							jogador["dinheiro"] -= i["preco"]
							jogador[i["efeito"]] += i["valor"]
			if esc == "0":
				break
def main():
	p = Player()

	while True:
		print("=" * 15)
		print("1 - começar")
		print("2 - sair")
		print("=" * 15)

		esc = input("qual voce vai escolher: ")

		if esc == "2":
			print("até mais!")
			break

		if esc == "1":
			p.players = []
			p.turno_atual = 1
			p.add_player()

			while True:
				p.mostrar_tabela()

				print("=" * 15)
				print("1 - atacar")
				print("2 - loja")
				print("4 - sair")
				print("=" * 15)

				esc = input("o que quer fazer: ")

				if esc == "1":
					p.atacar()
				elif esc == "2":
					p.lojoja()
				elif esc == "3":
					print("itens ainda não implementados")
				elif esc == "4":
					break
				else:
					print("opção inválida")


if __name__ == "__main__":
	main()